---
title: "PRODUCTION_DEPLOYMENT_PLAN"
project: klm-migrate
original_path: PRODUCTION_DEPLOYMENT_PLAN.md
modified: 2025-12-28T17:44:38.144967
---

# KLM Insurance - Production Deployment Plan

**Date:** December 28, 2025
**Goal:** Deploy Hugo site to production and migrate DNS from current hosting

---

## Current State

### Staging (Complete)
- ✅ URL: https://www.klmcrm.com
- ✅ S3 Bucket: klmcrm.com
- ✅ CloudFront ID: E3HA8770RGET6T
- ✅ SSL Certificate: *.klmcrm.com (ISSUED)
- ✅ Route53 Hosted Zone: ZNUGG3NYBSQJ8
- ✅ Status: Working perfectly

### Production (In Progress)
- 🎯 URL: https://www.klminsurance.com
- ✅ S3 Bucket: klminsurance.com (exists, website hosting enabled)
- ❌ CloudFront: Not created yet
- ❌ SSL Certificate: None for klminsurance.com
- ❌ Route53 Hosted Zone: None (DNS hosted elsewhere)
- ❌ Current hosting: External provider (needs migration)

---

## Deployment Strategy: Phased Approach

### Phase 1: Deploy to S3 & Test (30 minutes)
**Goal:** Get site deployed and testable without affecting DNS

**Steps:**
1. Deploy site to S3 bucket (without CloudFront)
2. Test via S3 website URL
3. Verify all pages, forms, and links work
4. Get stakeholder approval

**Testing URL:** http://klminsurance.com.s3-website-us-east-1.amazonaws.com

**Advantages:**
- ✅ Safe - doesn't affect current live site
- ✅ Fast - no waiting for CloudFront/DNS propagation
- ✅ Reversible - easy to rollback
- ✅ Can test thoroughly before DNS change

---

### Phase 2: Setup CloudFront + SSL (1 hour)
**Goal:** Prepare CDN and HTTPS

**Steps:**

#### 2a. Request SSL Certificate
```bash
aws acm request-certificate \
  --domain-name klminsurance.com \
  --subject-alternative-names www.klminsurance.com \
  --validation-method DNS \
  --region us-east-1
```

**Important:** You'll need to add DNS validation records. If klminsurance.com DNS is with your current provider, you'll add records there temporarily.

#### 2b. Create CloudFront Distribution

Once SSL cert is validated:
```bash
# Create distribution with proper config
# Including:
# - Origin: S3 bucket (website endpoint)
# - Aliases: klminsurance.com, www.klminsurance.com
# - SSL Certificate: ACM cert from step 2a
# - HTTPS redirect
# - Custom error pages (404 → index.html for SPA routing)
```

#### 2c. Update Production Script

Update `publish_to_production.py` line 21 with new CloudFront ID:
```python
PRODUCTION_CLOUDFRONT_ID = "E_YOUR_NEW_CF_ID_HERE"
```

**Time:** SSL validation can take 5-30 minutes. CloudFront creation takes 15-20 minutes.

---

### Phase 3: DNS Migration (Variable time)
**Goal:** Point klminsurance.com to AWS

This is the critical step where you switch from old hosting to new.

#### Option A: Gradual Migration (RECOMMENDED)

**Day 1: Prepare**
1. Lower TTL on current DNS records to 300 seconds (5 minutes)
2. Wait 24-48 hours for old TTL to expire
3. Document all current DNS records

**Day 2: Create Route53 Zone**
```bash
# Create hosted zone
aws route53 create-hosted-zone --name klminsurance.com --caller-reference $(date +%s)

# Note the nameservers - you'll need these
```

**Day 3: Setup Records in Route53**
```bash
# A record for klminsurance.com → CloudFront
# CNAME for www.klminsurance.com → CloudFront
# MX records (if you have email)
# TXT records (SPF, DKIM, etc.)
# Any other records from current DNS
```

**Day 4: Switch Nameservers at Domain Registrar**
1. Log into domain registrar (GoDaddy, Namecheap, etc.)
2. Update nameservers to Route53 nameservers
3. Monitor propagation (use `dig klminsurance.com`)

**Day 5: Monitor**
- Watch for DNS propagation (can take 24-48 hours)
- Test from multiple locations
- Monitor CloudFront metrics

#### Option B: Quick Migration (RISKY)

Switch nameservers immediately. Downtime possible if records aren't set up correctly.

**NOT RECOMMENDED** unless you're confident in DNS setup.

---

## Detailed Step-by-Step: Phase 1 (Deploy to S3)

### Step 1: Deploy Without CloudFront

Since the script requires CloudFront ID, let's deploy directly first:

```bash
# In klm-hugo-site directory
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site

# Build for production
hugo --baseURL="http://klminsurance.com.s3-website-us-east-1.amazonaws.com" \
     --environment production \
     --destination public \
     --cleanDestinationDir

# Deploy to S3
aws s3 sync public/ s3://klminsurance.com --delete

# Test the site
curl -I http://klminsurance.com.s3-website-us-east-1.amazonaws.com
```

### Step 2: Test Thoroughly

Visit: http://klminsurance.com.s3-website-us-east-1.amazonaws.com

**Test checklist:**
- [ ] Homepage loads
- [ ] All menu items work
- [ ] Insurance Services dropdown works
- [ ] Customer Service dropdown works
- [ ] All insurance product pages load
- [ ] Contact form displays (JotForm embed)
- [ ] Compare quotes form displays
- [ ] Client center page works
- [ ] Images load correctly
- [ ] CSS styling is correct
- [ ] Mobile menu works
- [ ] All links are correct

### Step 3: Get Approval

Share S3 URL with stakeholders for approval before proceeding to CloudFront/DNS.

---

## DNS Migration Checklist

### Before Migration

- [ ] **Document current DNS records**
  - A records
  - CNAME records
  - MX records (email!)
  - TXT records (SPF, DKIM, verification)
  - Any subdomains

- [ ] **Lower TTL to 300 seconds**
  - Wait 24-48 hours after lowering

- [ ] **Backup current DNS config**
  - Take screenshots
  - Export if possible

- [ ] **Verify email setup**
  - Will MX records work after migration?
  - Do you use email with klminsurance.com?

### During Migration

- [ ] **Create Route53 hosted zone**
- [ ] **Copy ALL DNS records to Route53**
- [ ] **Add CloudFront records**
  - A record: klminsurance.com → CloudFront (Alias)
  - CNAME: www.klminsurance.com → CloudFront

- [ ] **Test Route53 records**
  ```bash
  # Query Route53 nameservers directly
  dig @ns-xxxx.awsdns-xx.com klminsurance.com
  ```

- [ ] **Update nameservers at registrar**
- [ ] **Monitor propagation**
  ```bash
  # Check propagation
  dig klminsurance.com
  dig www.klminsurance.com

  # Check from multiple DNS servers
  dig @8.8.8.8 klminsurance.com
  dig @1.1.1.1 klminsurance.com
  ```

### After Migration

- [ ] **Verify site is live**
  - https://www.klminsurance.com
  - https://klminsurance.com

- [ ] **Test email** (if applicable)
- [ ] **Monitor CloudFront metrics**
- [ ] **Check for broken links**
- [ ] **Test forms submission**
- [ ] **Raise TTL back to normal** (3600 or 86400)

---

## Important Questions to Answer First

### DNS & Domain

1. **Where is klminsurance.com registered?**
   - GoDaddy? Namecheap? Network Solutions?
   - You'll need login credentials

2. **What DNS records currently exist?**
   - Run: `dig klminsurance.com ANY` from current setup
   - Document all records

3. **Do you use email with @klminsurance.com?**
   - If yes, you MUST preserve MX records
   - Test email after migration

4. **Any subdomains in use?**
   - mail.klminsurance.com?
   - ftp.klminsurance.com?
   - All must be migrated

### Current Hosting

1. **What's your current hosting provider?**
   - When does the contract end?
   - Will you keep it temporarily?

2. **Is there a rollback plan?**
   - Can you switch DNS back if needed?

3. **When is the best time to migrate?**
   - Low traffic period?
   - Weekend vs weekday?

---

## Risk Mitigation

### Low-Risk Approach (Recommended)

1. ✅ Deploy to S3 first, test via S3 URL
2. ✅ Create CloudFront, wait for deployment
3. ✅ Test via CloudFront URL (before DNS change)
4. ✅ Lower DNS TTL, wait 48 hours
5. ✅ Migrate DNS records to Route53
6. ✅ Test Route53 directly before nameserver change
7. ✅ Switch nameservers
8. ✅ Monitor for 24-48 hours
9. ✅ Only then cancel old hosting

### What Could Go Wrong?

**DNS Issues:**
- Missing MX records → Email breaks
- Missing subdomains → Subdomains offline
- Typo in records → Site unreachable
- **Mitigation:** Document everything, test before switching

**CloudFront Issues:**
- SSL cert not validated → HTTPS doesn't work
- Wrong origin config → 502/503 errors
- Cache issues → Old content showing
- **Mitigation:** Test with CloudFront URL before DNS change

**S3 Issues:**
- Bucket permissions wrong → 403 errors
- Missing files → 404 errors
- Wrong base URL → Broken links
- **Mitigation:** Test via S3 URL in Phase 1

---

## Emergency Rollback Plan

If something goes wrong:

### If using Route53 (nameservers changed)

1. **Quick fix: Update Route53 records**
   - Point A record back to old hosting IP
   - Usually takes 5-60 minutes

2. **Full rollback: Change nameservers back**
   - Log into registrar
   - Switch nameservers back to old DNS
   - Takes 1-48 hours to propagate

### If only changed specific records

- Update records back to old values
- Takes TTL time to propagate (5 min if you lowered it)

---

## Timeline Estimates

### Conservative (Recommended for First Time)

- Phase 1 (S3 Deploy & Test): 2-4 hours
- Phase 2 (CloudFront + SSL): 1-2 days
  - Waiting for SSL validation: 5-30 minutes
  - Waiting for CloudFront deployment: 15-20 minutes
  - Testing and verification: 2-4 hours
- Phase 3 (DNS Migration): 3-7 days
  - Lower TTL + wait: 2-3 days
  - Route53 setup + test: 1 day
  - Nameserver change + propagation: 1-3 days

**Total: 1-2 weeks for safe migration**

### Aggressive (If Experienced)

- Phase 1: 1 hour
- Phase 2: 4 hours
- Phase 3: 1-2 days

**Total: 2-3 days**

---

## Next Steps - What Do You Want to Do?

### Option 1: Deploy to S3 Now (Recommended)
- Safe, fast, testable
- Doesn't affect current site
- Can show stakeholders before DNS change

**Command:**
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo --baseURL="http://klminsurance.com.s3-website-us-east-1.amazonaws.com" \
     --environment production \
     --destination public \
     --cleanDestinationDir
aws s3 sync public/ s3://klminsurance.com --delete
```

### Option 2: Full Setup First (CloudFront + SSL)
- Takes longer
- More complete
- Still need DNS migration later

### Option 3: Get DNS Info First
- Document current DNS setup
- Plan migration timing
- Then deploy

---

## Recommended Order

1. **TODAY:** Deploy to S3, test, get approval
2. **NEXT:** Setup CloudFront + SSL
3. **THEN:** Plan DNS migration carefully
4. **FINALLY:** Execute DNS migration during low-traffic period

---

## Questions?

Before proceeding, we should discuss:

1. Do you have access to your domain registrar?
2. Do you use email with @klminsurance.com?
3. What's your risk tolerance (fast vs safe)?
4. When is the best time for DNS migration?
5. Is there a rollback window if needed?

---

**Status:** Ready for Phase 1 (S3 Deployment)
**Risk Level:** Low (no DNS changes yet)
**Reversible:** Yes (just delete S3 files)

Let me know when you're ready to proceed!
