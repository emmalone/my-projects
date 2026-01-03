---
title: "FIX_APEX_DOMAIN"
project: klm-migrate
original_path: docs/FIX_APEX_DOMAIN.md
modified: 2025-12-23T16:02:23.590929
---

# Fix Apex Domain (klmcrm.com without www)

**Issue:** The apex domain `klmcrm.com` (without www) is not resolving to the staging site.

**Status:**
- ✅ **www.klmcrm.com** - Works correctly
- ❌ **klmcrm.com** - Not resolving (DNS issue)

---

## Problem

Your domain registrar is currently using **GoDaddy nameservers** instead of **AWS Route 53 nameservers**.

**Current nameservers (WRONG):**
```
dns1.name-services.com
dns2.name-services.com
dns3.name-services.com
dns4.name-services.com
dns5.name-services.com
```

**Required nameservers (CORRECT - AWS Route 53):**
```
ns-570.awsdns-07.net
ns-1027.awsdns-00.org
ns-1567.awsdns-03.co.uk
ns-17.awsdns-02.com
```

---

## Solution: Update Nameservers at Domain Registrar

### Step 1: Find Your Domain Registrar

First, determine where you purchased `klmcrm.com`:
- GoDaddy
- Namecheap
- Google Domains
- Network Solutions
- Other registrar

You can check with:
```bash
whois klmcrm.com | grep -i registrar
```

### Step 2: Log Into Your Domain Registrar

Go to your registrar's website and log in to your account.

### Step 3: Update Nameservers

The exact steps vary by registrar, but generally:

#### For GoDaddy:
1. Go to **My Products** → **Domains**
2. Click on **klmcrm.com**
3. Scroll down to **Additional Settings**
4. Click **Manage DNS**
5. Under **Nameservers**, click **Change**
6. Select **Custom** nameservers
7. Enter the AWS nameservers:
   ```
   ns-570.awsdns-07.net
   ns-1027.awsdns-00.org
   ns-1567.awsdns-03.co.uk
   ns-17.awsdns-02.com
   ```
8. Click **Save**

#### For Namecheap:
1. Go to **Domain List**
2. Click **Manage** next to klmcrm.com
3. Find **Nameservers** section
4. Select **Custom DNS**
5. Enter the AWS nameservers:
   ```
   ns-570.awsdns-07.net
   ns-1027.awsdns-00.org
   ns-1567.awsdns-03.co.uk
   ns-17.awsdns-02.com
   ```
6. Click the green checkmark to save

#### For Other Registrars:
Look for:
- "DNS Settings"
- "Nameservers"
- "Name Server Settings"
- "DNS Management"

Then change from default/custom to the AWS nameservers listed above.

---

## Step 4: Verify the Change

After updating, wait 5-10 minutes and check:

```bash
dig klmcrm.com NS +short
```

You should see the AWS nameservers:
```
ns-570.awsdns-07.net.
ns-1027.awsdns-00.org.
ns-1567.awsdns-03.co.uk.
ns-17.awsdns-02.com.
```

**Note:** Changes can take up to 24-48 hours to fully propagate globally, but often work within 1-2 hours.

---

## Step 5: Test Both URLs

Once DNS propagates, both URLs should work:

```bash
# Test www version
curl -I https://www.klmcrm.com

# Test apex domain (no www)
curl -I https://klmcrm.com
```

Both should return `HTTP/2 200` status.

You can also test in your browser:
- https://www.klmcrm.com ✅
- https://klmcrm.com ✅

---

## Why This Happens

When you created the Route 53 hosted zone for `klmcrm.com`, AWS assigned nameservers. However, your domain registrar still has the old nameservers configured. The registrar is the authoritative source for which nameservers to use, so you must update it there.

---

## Verification Commands

```bash
# Check current public nameservers
dig klmcrm.com NS +short

# Check if apex domain resolves
dig klmcrm.com A +short

# Check if www subdomain resolves
dig www.klmcrm.com A +short

# Test HTTP response for apex
curl -I https://klmcrm.com

# Test HTTP response for www
curl -I https://www.klmcrm.com
```

---

## AWS Route 53 Configuration (Already Complete)

The following is already configured correctly in AWS:

**Hosted Zone ID:** `ZNUGG3NYBSQJ8`

**DNS Records:**
- `klmcrm.com` A record → CloudFront (d1c9gkvd5eio3l.cloudfront.net)
- `www.klmcrm.com` A record → CloudFront (d1c9gkvd5eio3l.cloudfront.net)

**CloudFront Distribution:** `E3HA8770RGET6T`
- Aliases: www.klmcrm.com, klmcrm.com
- HTTPS redirect enabled

Everything on AWS is configured correctly. You only need to update the nameservers at your registrar.

---

## Timeline

- **Immediate:** Nameserver update submitted at registrar
- **5-15 minutes:** Some DNS servers start using new nameservers
- **1-2 hours:** Most DNS servers worldwide updated
- **24-48 hours:** Full global propagation guaranteed

---

## Need Help?

If you need assistance identifying your registrar or updating nameservers, contact your domain registrar's support with this information:

**Domain:** klmcrm.com
**Action needed:** Update nameservers to AWS Route 53
**New nameservers:**
```
ns-570.awsdns-07.net
ns-1027.awsdns-00.org
ns-1567.awsdns-03.co.uk
ns-17.awsdns-02.com
```

---

**Created:** 2025-12-23
**Status:** Waiting for nameserver update at domain registrar
