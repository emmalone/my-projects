---
title: "DEVELOPMENT_WORKFLOW"
project: klm-migrate
original_path: klm-hugo-site/docs/DEVELOPMENT_WORKFLOW.md
modified: 2026-01-01T23:45:19.140365
---

# Development Workflow - From Iteration to Production

## Overview: Three Development Scenarios

**Updated:** The workflow has been reconfigured for 3 distinct development scenarios:

| Scenario | Branch | Testing | Deploy to Dev | Deploy to Staging |
|----------|--------|---------|--------------|-------------------|
| **Laptop/Desktop** | `main` | Local (hugo server) | ✅ Auto (on push to main) | Manual (Python script) |
| **iPhone/Claude Code** | `claude/**` | Dev environment | ✅ Auto (on push to claude/**) | Manual (Python script) |
| **Staging** | N/A | N/A | N/A | Manual (Python script) |

### Environment Details

| Environment | Purpose | Deployed How | Who Uses It |
|-------------|---------|--------------|-------------|
| **Local** | Laptop/desktop development | `hugo server` | You (developer) on laptop/desktop |
| **Dev** | Remote preview (iPhone work) | `claude/*` branches (auto) | You (developer) on iPhone |
| **Staging** | Business review | Manual Python script ONLY | Business users for final review |
| **Production** | Live site | Manual Python script ONLY | Public customers |

### Key Changes from Previous Workflow

- ❌ **No staging branch** - Removed auto-deploy to staging
- ✅ **Manual staging control** - You decide when staging updates via Python script
- ✅ **Dev auto-deploys from main AND claude/** - Dev reflects all committed code
- ✅ **Always-current dev environment** - Whether working on laptop or iPhone, dev stays in sync
- ✅ **Laptop work auto-deploys to dev** - Push to main triggers dev deployment
- ✅ **iPhone work auto-deploys to dev** - Push to `claude/**` triggers dev deployment

---

## The Complete Workflow

### Scenario 1: Laptop/Desktop Development

**Goal:** Develop and test locally, auto-deploy to dev, manual control over staging

```bash
# Step 1: Local development
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
git pull origin main

# Step 2: Make changes
# ... edit files ...

# Step 3: Test locally
hugo server -D --bind 0.0.0.0
# Visit: http://localhost:1313
# Test thoroughly

# Step 4: Commit to main
git add .
git commit -m "Update homepage hero section"
git push origin main

# Step 5: Automatic deployment to dev (30 seconds)
# GitHub Actions deploys to: http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com
# Dev environment now has your latest changes

# Step 6: Deploy to staging (when ready for review)
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py

# Staging live at: https://www.klmcrm.com
```

**Key Points:**
- ✅ Test everything locally before committing
- ✅ Every push to main auto-deploys to dev environment
- ✅ Dev environment always current for iPhone preview
- ✅ No auto-deploy to staging - you control when staging updates
- ✅ Full control over staging deployment timing
- ✅ Perfect for focused development work

---

### Scenario 2: iPhone Development with Auto-Preview

**Goal:** Try ideas quickly, iterate on iPhone, preview instantly

#### On Your iPhone with Claude Code:

```
You: "Create a new landing page with video placeholder"
     ↓
Claude: Creates files, commits to claude/create-landing-page-xyz
     ↓
Auto-deployed to DEV bucket (30 seconds)
     ↓
You: View at dev-klmhugoweb.s3-website-us-east-1.amazonaws.com on your iPhone
     ↓
You: "The video placeholder is too small, make it bigger"
     ↓
Claude: Updates files, commits to same branch
     ↓
Auto-deployed to DEV again (30 seconds)
     ↓
You: Review again, iterate until satisfied
```

**Key Points:**
- ✅ Commits happen automatically as you work with Claude
- ✅ Each push auto-deploys to DEV
- ✅ Iterate as many times as needed
- ✅ Preview on your iPhone instantly
- ✅ Code is on `claude/*` branch, NOT in main yet

**When to Move Forward:**
- Feature works as expected
- You've tested it on DEV
- Ready to merge to main

#### Merging iPhone Work to Main:

**From iPhone (Claude Code):**
```
You: "This landing page looks good. Merge to main"
     ↓
Claude: Creates PR from claude/create-landing-page-xyz → main
     ↓
PR created on GitHub with description of changes
     ↓
You: Review and approve PR
     ↓
Claude: Merges to main (or you merge on GitHub)
     ↓
GitHub Actions detects push to main
     ↓
Auto-deploys to DEV environment again (30 seconds)
     ↓
Dev now reflects merged code from main branch
```

**From Desktop:**
```bash
# Pull the merged changes
git pull origin main

# Dev environment already has latest code (auto-deployed from main)

# Deploy to staging when ready for business review
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py
```

---

### Scenario 3: Deploying to Staging (Manual Control)

**Goal:** Deploy approved changes for business review

**Always from Laptop/Desktop - Never Auto-Deploys**

```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py

# Script does:
# 1. Builds Hugo with staging baseURL (https://www.klmcrm.com)
# 2. Syncs to klmcrm.com S3 bucket
# 3. Invalidates CloudFront cache
# 4. Verifies deployment
# 5. Live at: https://www.klmcrm.com
```

**When to Deploy:**
- ✅ Feature is complete and tested
- ✅ Code is merged to main
- ✅ Ready for business stakeholders to review
- ✅ You have time to support if issues arise

**Key Points:**
- ❌ NO auto-deploy to staging
- ✅ YOU control when staging updates
- ✅ Deploy only when ready for review
- ✅ Prevents accidental staging deployments

---

### Phase 3: Business Review (STAGING Environment)

**Goal:** Let business users review before going live

**Who Reviews:**
- Business stakeholders
- Content team
- Marketing team
- Anyone who needs to approve changes

**What They Review:**
- Content accuracy
- Visual design
- User experience
- Brand consistency

**How Staging Gets Updated:**

```
YOU deploy to staging manually from laptop:
     ↓
Business User: Reviews at https://www.klmcrm.com
     ↓
Business User: "The landing page looks great, but can we change
                the headline to 'Protecting What Matters Most'?"
     ↓
You (on iPhone): Tell Claude to update the headline
     ↓
Claude: Makes change on NEW claude/update-headline-abc branch
     ↓
Auto-deploys to DEV for you to review (30 seconds)
     ↓
You: Review on DEV at dev-klmhugoweb URL, approve
     ↓
Claude: Merges to main
     ↓
You (on laptop): python3 publish_to_staging.py
     ↓
Business user reviews updated staging site
     ↓
Business user: "Approved! Ready for production"
```

**Key Points:**
- ✅ YOU control when staging updates
- ✅ Business users never see incomplete work
- ✅ Preview changes on dev first
- ✅ Deploy to staging only when ready

---

### Phase 4: Production Deployment (PROD Environment)

**Goal:** Deploy approved changes to live site

**When to Deploy:**
- ✅ All business stakeholders approved
- ✅ Thoroughly tested on staging
- ✅ No known bugs or issues
- ✅ Ready for public

#### Option 1: Manual PR to Main (Recommended)

```bash
# Create PR from staging to main
1. Go to GitHub
2. Create new PR: staging → main
3. Add description: "Deploy landing page to production"
4. Review changes one final time
5. Merge PR
```

**What Happens:**
- Code merges to `main` branch
- GitHub Actions deploys to PRODUCTION bucket
- Live site updates for customers

#### Option 2: Fast-Forward Merge (for simple changes)

```bash
git checkout main
git merge staging --ff-only
git push origin main
```

---

## Quick Reference: When to Do What

### When to Commit & Push
- **Automatically:** Every time Claude makes changes for you
- **Manually:** After every logical unit of work
- **Frequency:** Often! Commit early, commit often

### When to Create a PR
- ✅ Feature is working on DEV
- ✅ You've tested it yourself
- ✅ Ready for others to review
- ✅ Ready to move to staging for business review

### When to Merge
- ✅ Code review passed (you reviewed your own code)
- ✅ All checks green (GitHub Actions build succeeded)
- ✅ Tested on DEV environment
- **Merge to staging:** When ready for business review
- **Merge to main:** When business approves for production

### When to Review Code
- **Before merging to staging:** Review your own changes
- **Before merging to main:** Final review (can be quick if already reviewed)
- **During development:** Continuous review as you work

---

## Branching Strategy

```
main (primary development branch)
  ↑
  ├── claude/create-landing-page-xyz (iPhone dev, auto-deploys to dev)
  ├── claude/update-headline-abc (iPhone dev, auto-deploys to dev)
  └── claude/fix-contact-form-def (iPhone dev, auto-deploys to dev)
```

**Branch Naming:**
- `main` - Primary development branch (laptop/desktop work + merged iPhone work)
- `claude/*` - iPhone development branches (auto-created by Claude Code)

**Branch Lifetime:**
- `main` - Permanent branch
- `claude/*` - Temporary, deleted after merging to main

**Deployment Strategy:**
- `main` branch → Auto-deploy to dev-klmhugoweb S3 bucket (GitHub Actions)
- `claude/*` branches → Auto-deploy to dev-klmhugoweb S3 bucket (GitHub Actions)
- `main` branch → Manual deploy to staging (klmcrm.com) via Python script
- Staging → Manual deploy to production (klminsurance.com) via Python script

**Key Changes:**
- ❌ **No staging branch** - Removed from git workflow
- ✅ **Staging is deployment target** - Not a git branch
- ✅ **Dev auto-deploys from main AND claude/** - Always current
- ✅ **Manual control over staging/production** - YOU decide when they update

---

## Environment Configuration

### AWS Secrets Needed (GitHub Repo Secrets)

**For DEV Environment (Auto-Deploy):**
- `AWS_ACCESS_KEY_ID` - AWS credentials for deployment
- `AWS_SECRET_ACCESS_KEY` - AWS credentials for deployment
- `AWS_REGION` - us-east-1
- `S3_DEV_BUCKET` - dev-klmhugoweb

**For STAGING Environment:**
- ❌ **No GitHub secrets needed** - Staging deploys manually via Python script on laptop

**For PRODUCTION:**
- ❌ **No GitHub secrets needed** - Production deploys manually via Python script on laptop

### Current GitHub Secrets

```bash
gh secret list

# Output:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
S3_DEV_BUCKET
```

### Why No Staging/Production Secrets?

Staging and production deployments are **intentionally manual** and run from your laptop using the Python scripts:
- `publish_to_staging.py` - Uses local AWS credentials
- `publish_to_production.py` - Uses local AWS credentials

This gives you complete control over when these environments update.

---

## Example: Complete Feature Development

### Scenario: Add New Landing Page

#### Day 1: Development (Monday morning, on iPhone)

```
9:00 AM - You: "Create a new landing page with video placeholder"
9:01 AM - Claude: Creates files, commits to claude/create-landing-page-xyz
9:04 AM - Auto-deployed to DEV
9:05 AM - You: Review on iPhone at dev.klm-insurance.com/landing

9:10 AM - You: "Make the video placeholder bigger and add a border"
9:11 AM - Claude: Updates files, commits to same branch
9:14 AM - Auto-deployed to DEV
9:15 AM - You: Review changes, looks better

9:20 AM - You: "Add some example text in the description"
9:21 AM - Claude: Updates content, commits
9:24 AM - Auto-deployed to DEV
9:25 AM - You: Perfect! Feature is done.

9:30 AM - You: "Create a PR to merge this into staging"
9:31 AM - Claude: Creates PR on GitHub
```

#### Day 1: Code Review (Monday afternoon)

```
2:00 PM - You: Open GitHub PR on desktop (or iPhone)
2:05 PM - Review code changes, everything looks good
2:10 PM - Check GitHub Actions - build passed ✅
2:15 PM - Merge PR to main
2:18 PM - Auto-deployed to DEV (from main branch)
2:20 PM - Dev environment updated with merged code
2:25 PM - Send email: "New landing page ready for review. Testing on dev before staging."
```

#### Day 2: Business Review (Tuesday)

```
10:00 AM - Deploy to staging for business review
10:01 AM - Run: python3 publish_to_staging.py
10:03 AM - Staging deployed: https://www.klmcrm.com
10:05 AM - Marketing team reviews staging site
11:30 AM - Feedback: "Can we change the headline and add our tagline?"

12:00 PM - You (on iPhone): "Update landing page headline to 'Protecting What Matters Most' and add tagline"
12:01 PM - Claude: Makes changes on claude/update-landing-page-headlines
12:04 PM - Auto-deployed to DEV
12:05 PM - You: Review on DEV, looks good
12:10 PM - Merge to main
12:13 PM - Auto-deployed to DEV again (from main)
12:15 PM - Run: python3 publish_to_staging.py
12:17 PM - Staging updated
12:18 PM - Email marketing team: "Updated version ready"

2:00 PM - Marketing approves: "Looks great! Ready to go live"
```

#### Day 2: Production Deploy (Tuesday afternoon)

```
3:00 PM - Run: python3 publish_to_production.py
3:01 PM - Type: DEPLOY TO PRODUCTION (confirmation)
3:05 PM - Production deployed
3:10 PM - Landing page is LIVE at klm-insurance.com/landing
```

---

## Best Practices

### For Development (DEV)
- ✅ Commit often, even if not perfect
- ✅ Test thoroughly before creating PR
- ✅ Keep DEV environment "messy" - it's for experimentation
- ✅ Use descriptive commit messages
- ✅ Don't worry about breaking DEV - that's what it's for!

### For Staging
- ✅ Only merge reviewed code
- ✅ Keep staging stable - business users rely on it
- ✅ Test everything before merging from staging to main
- ✅ Staging should always be "demo-ready"
- ✅ Don't merge experimental features here

### For Production (Main)
- ✅ Only merge from staging (never from claude/* branches directly)
- ✅ Require business approval before deploying
- ✅ Tag releases (e.g., `v1.0.0`, `v1.1.0`)
- ✅ Have rollback plan ready
- ✅ Deploy during low-traffic times when possible

### For Code Review
- ✅ Review your own code before creating PR
- ✅ Check for sensitive data (API keys, passwords)
- ✅ Verify build passes
- ✅ Test on DEV environment first
- ✅ Write clear PR descriptions

---

## Comparison: Your Workflow vs Traditional

### Traditional Workflow (Manual)
```
1. Write code on desktop
2. Manually test locally with Hugo server
3. Manually commit and push
4. Manually create PR
5. Wait for review
6. Manually merge
7. Manually deploy via CLI or scripts
8. Repeat for every environment
```

### Your Workflow (Automated)
```
1. Tell Claude what you want (from iPhone!)
2. Auto-deployed to DEV - test on your phone
3. Iterate quickly with Claude
4. Create PR (one command to Claude)
5. Review code (on phone or desktop)
6. Merge PR
7. Auto-deployed to staging
8. Business approves
9. Merge to main
10. Auto-deployed to production
```

**Time Saved:** 80%+ of deployment overhead eliminated!

---

## Troubleshooting

### "I want to see my changes but they're not on staging"

**Cause:** You pushed to a `claude/*` branch
**Solution:** That's correct! Changes deploy to DEV first. Create PR to staging when ready.

### "Business users say staging is broken"

**Cause:** Incomplete feature was merged to staging
**Solution:**
1. Test thoroughly on DEV first
2. Only merge complete features to staging
3. If needed, revert the PR or hotfix

### "I made changes but don't see them on any environment"

**Cause:** GitHub Actions might have failed
**Solution:**
1. Check: https://github.com/emmalone/klm-migrate/actions
2. Look for red X marks
3. Click to see error details
4. Fix the issue and push again

### "How do I undo a merge to staging?"

**Option 1: Revert the merge**
```bash
git checkout staging
git revert -m 1 <merge-commit-sha>
git push origin staging
```

**Option 2: Use Claude Code (easier)**
```
You: "Revert the last merge to staging - the landing page change needs more work"
Claude: Reverts the merge for you
```

---

## Summary: The Three Questions

### 1. "Should I commit and push this code?"

**YES if:**
- You made any changes (even small ones)
- You want to see it on DEV
- You want to save your work

**Commits are automatic** when using Claude Code - just keep working!

### 2. "Should I create a PR?"

**YES if:**
- ✅ Feature works on DEV
- ✅ You've tested it yourself
- ✅ Ready for business users to review
- ✅ Code is clean and reviewed

**NO if:**
- ❌ Still experimenting
- ❌ Feature incomplete
- ❌ Haven't tested on DEV yet
- ❌ Known bugs exist

### 3. "Should I merge this PR?"

**To STAGING - YES if:**
- ✅ Code reviewed
- ✅ Build passes (green check)
- ✅ Tested on DEV
- ✅ Ready for business review

**To MAIN - YES if:**
- ✅ Business stakeholders approved
- ✅ Thoroughly tested on staging
- ✅ No known issues
- ✅ Ready for customers

---

## Quick Start Checklist

### Initial Setup (One-Time)

- [ ] Create S3 bucket for DEV: `klm-dev`
- [ ] Create S3 bucket for STAGING: `klm-staging`
- [ ] Configure S3 buckets for static website hosting
- [ ] Add AWS secrets to GitHub repository
- [ ] Add GitHub variables (DEV_URL, STAGING_URL)
- [ ] Create `staging` branch: `git checkout -b staging && git push origin staging`
- [ ] Test deployment workflows

### Daily Workflow

- [ ] Make changes via Claude Code (auto-commits to `claude/*` branch)
- [ ] Review auto-deployed changes on DEV environment
- [ ] Iterate until feature is complete
- [ ] Create PR to merge into `staging` branch
- [ ] Review code and merge PR
- [ ] Business users review on STAGING environment
- [ ] When approved, create PR from `staging` to `main`
- [ ] Merge to `main` for production deployment

---

**Last Updated:** December 29, 2025

**Need Help?**
- See: `docs/DEPLOYMENT.md` for AWS setup details
- See: `WORKFLOW.md` for git basics
- Check: GitHub Actions logs for deployment issues
