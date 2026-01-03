---
title: "PUBLISHING_WORKFLOW"
project: klm-migrate
original_path: docs/PUBLISHING_WORKFLOW.md
modified: 2025-12-23T12:46:16.710126
---

# KLM Insurance Website - Complete Publishing Workflow

**Complete Lifecycle Documentation: Development → Staging → Production**

---

## Table of Contents

1. [Overview](#overview)
2. [Environment Architecture](#environment-architecture)
3. [Prerequisites](#prerequisites)
4. [Development Workflow](#development-workflow)
5. [Creating a New Page](#creating-a-new-page)
6. [Local Testing (Localhost)](#local-testing-localhost)
7. [Publishing to Staging](#publishing-to-staging)
8. [Publishing to Production](#publishing-to-production)
9. [Troubleshooting](#troubleshooting)
10. [Quick Reference](#quick-reference)

---

## Overview

The KLM Insurance website follows a three-tier publishing workflow:

```
Development (Localhost) → Staging (klmcrm.com) → Production (klminsurance.com)
```

**Key Principles:**
- All changes are developed and tested locally first
- Staging is used for validation and client review
- Production deployments happen only after staging approval
- Each environment is isolated and independent

---

## Environment Architecture

| Environment | URL | S3 Bucket | CloudFront ID | Purpose |
|-------------|-----|-----------|---------------|---------|
| **Development** | http://localhost:1313 | N/A | N/A | Local development and testing |
| **Staging** | https://www.klmcrm.com<br>https://klmcrm.com | s3://klmcrm.com | E3HA8770RGET6T | Client review and validation |
| **Production** | https://www.klminsurance.com<br>https://klminsurance.com | s3://klminsurance.com | *To be configured* | Live customer-facing site |

**AWS Account:** 837716495292
**Region:** us-east-1
**IAM User:** klm-hugo

---

## Prerequisites

### Required Software

Verify all tools are installed:

```bash
# Check Hugo
hugo version
# Required: v0.153.1+extended or newer

# Check AWS CLI
aws --version
# Required: aws-cli/2.x.x or newer

# Check Python
python3 --version
# Required: Python 3.9+

# Check Git
git --version
```

### AWS Configuration

Verify AWS CLI is configured:

```bash
aws sts get-caller-identity
```

Expected output:
```json
{
    "UserId": "AIDA4GC6LJO6C5CPI73CD",
    "Account": "837716495292",
    "Arn": "arn:aws:iam::837716495292:user/klm-hugo"
}
```

If not configured, run:
```bash
aws configure
```

And provide your credentials.

---

## Development Workflow

### Daily Development Process

1. **Start Local Server**
   ```bash
   cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
   hugo server -D --bind 0.0.0.0
   ```

2. **Make Changes**
   - Edit files in real-time
   - Changes auto-reload in browser
   - View at http://localhost:1313

3. **Test Changes**
   - Check all pages work
   - Test on multiple viewports (mobile, tablet, desktop)
   - Verify forms and navigation

4. **Stop Server**
   - Press `Ctrl+C` in terminal

---

## Creating a New Page

### Step 1: Create Content File

Navigate to the content directory:
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content
```

Create a new Markdown file (e.g., `renters-insurance.md`):

```markdown
---
title: "Renters Insurance"
description: "Renters Insurance - KLM Insurance Solutions"
draft: false
hero_image: "/images/featured-banner.png"
sidebar_image: "/images/content-banner.png"
form_type: "full"
---

## Protect Your Belongings with Renters Insurance

Your content goes here...

### What's Covered

- Personal property
- Liability protection
- Additional living expenses

Contact us today for a quote!
```

### Step 2: Choose Form Type

**form_type: "simple"** - Zip code + insurance type only
```yaml
form_type: "simple"
```

**form_type: "full"** - Complete contact form (name, email, phone, comments)
```yaml
form_type: "full"
```

### Step 3: Add to Navigation (Optional)

If the page should appear in the main navigation, edit:
```bash
/Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/layouts/_default/baseof.html
```

Find the navigation section and add your link:
```html
<li><a href="/renters-insurance/">Renters Insurance</a></li>
```

For dropdown menu items, add within a dropdown:
```html
<li class="dropdown">
    <a href="#" class="dropdown-toggle">INSURANCE SERVICES</a>
    <ul class="dropdown-menu">
        <li><a href="/auto-insurance/">Auto Insurance</a></li>
        <li><a href="/home-insurance/">Home Insurance</a></li>
        <!-- Add your new page here -->
        <li><a href="/renters-insurance/">Renters Insurance</a></li>
    </ul>
</li>
```

### Step 4: Add Images (if needed)

Place images in:
```bash
/Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/static/images/
```

Reference in your content:
```markdown
![Alt text](/images/your-image.png)
```

---

## Local Testing (Localhost)

### Start the Hugo Development Server

```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo server -D --bind 0.0.0.0
```

The site will be available at: **http://localhost:1313**

### Testing Checklist

Before publishing to staging, verify:

- [ ] New page displays correctly
- [ ] All images load properly
- [ ] Navigation links work
- [ ] Forms are functional
- [ ] Content is spell-checked
- [ ] Mobile layout looks good (resize browser or use dev tools)
- [ ] No console errors (check browser developer tools)

### UI/UX Testing (Optional)

Run automated tests:
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 test_ui_ux.py
```

This generates screenshots for all devices and pages.

---

## Publishing to Staging

### When to Publish to Staging

- After local testing is complete
- Before client review
- Before production deployment
- When you want to share changes with others

### Run the Staging Deployment Script

```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py
```

### What the Script Does

1. ✅ Verifies Hugo and AWS CLI are installed
2. ✅ Confirms AWS credentials are valid
3. 🧹 Cleans the build directory
4. 🔨 Builds Hugo site with baseURL: https://www.klmcrm.com
5. 📤 Syncs files to S3 bucket (s3://klmcrm.com)
6. 🗑️ Deletes old files from S3 (--delete flag)
7. 🔄 Invalidates CloudFront cache
8. ✅ Verifies site is accessible

### Expected Output

```
================================================================================
  KLM Insurance - Staging Deployment
================================================================================

🕐 Started at: 2025-12-23 10:30:00
🎯 Target: https://www.klmcrm.com
📦 Bucket: s3://klmcrm.com

[Step 1] Verifying Prerequisites
--------------------------------------------------------------------------------
✅ hugo v0.153.1+extended+withdeploy darwin/arm64
✅ AWS Account: 837716495292
✅ IAM User: klm-hugo

[Step 2] Cleaning Build Directory
--------------------------------------------------------------------------------
✅ Cleaning old build directory completed successfully

[Step 3] Building Hugo Site
--------------------------------------------------------------------------------
✅ Building Hugo site for staging completed successfully
📦 Built 42 files

[Step 4] Deploying to S3
--------------------------------------------------------------------------------
✅ Syncing to s3://klmcrm.com completed successfully
📤 Uploaded: 15 files
🗑️  Deleted: 3 old files

[Step 5] Invalidating CloudFront Cache
--------------------------------------------------------------------------------
✅ Invalidating CloudFront cache completed successfully
🔄 Invalidation ID: ICLIAL866EJI2C3USU5R6TONS7
⏱️  Status: InProgress

[Step 6] Verifying Deployment
--------------------------------------------------------------------------------
✅ Site is accessible (HTTP 200)

================================================================================
✅ DEPLOYMENT SUCCESSFUL!
================================================================================
⏱️  Total time: 15.42 seconds
🌐 Visit: https://www.klmcrm.com
📝 Note: CloudFront invalidation takes 1-3 minutes to complete
```

### Post-Deployment Verification

1. **Wait 1-3 minutes** for CloudFront cache invalidation
2. **Visit the site:** https://www.klmcrm.com
3. **Test your changes:**
   - Navigate to your new page
   - Test all forms
   - Check on mobile devices
   - Verify images load
4. **Hard refresh** (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows) if changes don't appear

---

## Publishing to Production

### ⚠️ IMPORTANT: Production Deployment Checklist

Before deploying to production, ensure:

- [ ] Changes have been tested in staging
- [ ] Client/stakeholder has approved the changes
- [ ] All forms work correctly (test submissions)
- [ ] All links work
- [ ] Spelling and grammar have been reviewed
- [ ] No broken images
- [ ] Mobile experience tested
- [ ] You have permission to deploy

### Run the Production Deployment Script

```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_production.py
```

### Safety Confirmation

The script will ask you to confirm:

```
================================================================================
  ⚠️  PRODUCTION DEPLOYMENT WARNING ⚠️
================================================================================

You are about to deploy to PRODUCTION: www.klminsurance.com
This will update the LIVE website that customers see.

Before proceeding, ensure:
  ✓ Changes have been tested in staging (www.klmcrm.com)
  ✓ All forms and links work correctly
  ✓ Content has been reviewed and approved
  ✓ You have permission to deploy to production

================================================================================

Type 'DEPLOY TO PRODUCTION' to continue (or anything else to cancel):
```

**You must type exactly:** `DEPLOY TO PRODUCTION`

### What the Script Does

Same as staging, but:
- Builds with baseURL: https://www.klminsurance.com
- Deploys to s3://klminsurance.com
- Invalidates production CloudFront cache
- Creates a deployment log in `deployment-logs/`

### Post-Production Deployment

1. **Wait 1-3 minutes** for CloudFront invalidation
2. **Visit:** https://www.klminsurance.com
3. **Spot-check critical pages:**
   - Homepage
   - Your newly added/changed pages
   - Contact form
   - Compare Quotes
4. **Monitor for issues** over the next hour
5. **Keep staging in sync** - any fixes should go through staging first

---

## Troubleshooting

### Hugo Build Errors

**Error:** `command not found: hugo`
```bash
# Install Hugo
brew install hugo
```

**Error:** `failed to render pages`
- Check for syntax errors in your Markdown files
- Verify front matter (YAML between `---`) is correctly formatted
- Look for unclosed HTML tags

### AWS Deployment Errors

**Error:** `Unable to locate credentials`
```bash
# Reconfigure AWS CLI
aws configure
```

**Error:** `Access Denied` when syncing to S3
- Verify IAM permissions (user: klm-hugo should have S3 access)
- Check AWS account ID matches: 837716495292

**Error:** `Distribution not found` (CloudFront)
- Verify CloudFront distribution ID in script
- For production: Update `PRODUCTION_CLOUDFRONT_ID` in `publish_to_production.py`

### Site Not Updating

**Issue:** Changes don't appear on staging/production

1. **Check CloudFront cache:**
   - Invalidation takes 1-3 minutes
   - Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+R)
   - Try incognito/private browsing mode

2. **Verify files were uploaded:**
   ```bash
   aws s3 ls s3://klmcrm.com/ --recursive | grep your-page
   ```

3. **Check build output:**
   - Look for errors in deployment script output
   - Verify file count matches expectations

### Hugo Server Issues

**Issue:** `port 1313 already in use`
```bash
# Kill existing Hugo server
lsof -ti:1313 | xargs kill -9

# Or use a different port
hugo server -D --bind 0.0.0.0 --port 1314
```

**Issue:** Changes not showing locally
- Stop and restart Hugo server
- Clear browser cache
- Check for errors in terminal

---

## Quick Reference

### Common Commands

```bash
# Start local development server
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo server -D --bind 0.0.0.0

# Publish to staging
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py

# Publish to production
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_production.py

# Run UI/UX tests
cd /Users/mark/PycharmProjects/klm-migrate
python3 test_ui_ux.py

# Check AWS identity
aws sts get-caller-identity

# List S3 buckets
aws s3 ls

# Manually sync to staging (if needed)
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo --baseURL="https://www.klmcrm.com" --environment staging
aws s3 sync public/ s3://klmcrm.com --delete
aws cloudfront create-invalidation --distribution-id E3HA8770RGET6T --paths "/*"
```

### File Locations

```
Project Root: /Users/mark/PycharmProjects/klm-migrate/

Hugo Site:    klm-hugo-site/
Content:      klm-hugo-site/content/
Layouts:      klm-hugo-site/layouts/
Static:       klm-hugo-site/static/
Images:       klm-hugo-site/static/images/
CSS:          klm-hugo-site/static/css/style.css

Scripts:
  publish_to_staging.py      - Deploy to staging
  publish_to_production.py   - Deploy to production
  test_ui_ux.py             - UI/UX testing

Documentation:
  PUBLISHING_WORKFLOW.md     - This file
  NEW_PAGE_TEMPLATE_GUIDE.md - Page creation guide
  docs/klm_crm_publishing_process.md - AWS/Hugo publishing process
```

### Environment URLs

```
Local:      http://localhost:1313
Staging:    https://www.klmcrm.com
            https://klmcrm.com
Production: https://www.klminsurance.com
            https://klminsurance.com
```

### Front Matter Templates

**Simple Page (zip + insurance type form):**
```yaml
---
title: "Page Title"
description: "Page description for SEO"
draft: false
hero_image: "/images/featured-banner.png"
sidebar_image: "/images/content-banner.png"
form_type: "simple"
---
```

**Full Form Page (name, email, phone, comments):**
```yaml
---
title: "Page Title"
description: "Page description for SEO"
draft: false
hero_image: "/images/featured-banner.png"
sidebar_image: "/images/content-banner.png"
form_type: "full"
---
```

**Contact Page:**
```yaml
---
title: "Contact Us"
description: "Contact information"
draft: false
hero_image: "/images/featured-banner.png"
form_title: "GET A QUOTE"
form_type: "simple"
layout: "contact"
---
```

---

## Complete Lifecycle Example

### Scenario: Adding a "Motorcycle Insurance" Page

1. **Create the page locally:**
   ```bash
   cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content
   nano motorcycle-insurance.md
   ```

   ```markdown
   ---
   title: "Motorcycle Insurance"
   description: "Motorcycle Insurance - KLM Insurance Solutions"
   draft: false
   hero_image: "/images/featured-banner.png"
   sidebar_image: "/images/content-banner.png"
   form_type: "full"
   ---

   ## Protect Your Ride with Motorcycle Insurance

   Content here...
   ```

2. **Test locally:**
   ```bash
   cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
   hugo server -D --bind 0.0.0.0
   ```
   Visit: http://localhost:1313/motorcycle-insurance/

3. **Add to navigation** (edit `layouts/_default/baseof.html`):
   ```html
   <li><a href="/motorcycle-insurance/">Motorcycle Insurance</a></li>
   ```

4. **Test again locally** - verify navigation works

5. **Publish to staging:**
   ```bash
   cd /Users/mark/PycharmProjects/klm-migrate
   python3 publish_to_staging.py
   ```

6. **Review on staging:**
   - Visit: https://www.klmcrm.com/motorcycle-insurance/
   - Test all functionality
   - Share with client for approval

7. **Get approval** from stakeholder

8. **Publish to production:**
   ```bash
   python3 publish_to_production.py
   # Type: DEPLOY TO PRODUCTION
   ```

9. **Verify on production:**
   - Visit: https://www.klminsurance.com/motorcycle-insurance/
   - Confirm everything works

**✅ Done!** The new page is now live.

---

## Best Practices

### Development
- ✅ Always test locally first
- ✅ Use descriptive commit messages (if using git)
- ✅ Keep content and code separate
- ✅ Test on multiple browsers and devices

### Staging
- ✅ Deploy to staging for every change
- ✅ Get client approval before production
- ✅ Use staging URL for sharing previews
- ✅ Staging should mirror production as closely as possible

### Production
- ✅ Only deploy during low-traffic hours (if possible)
- ✅ Always test in staging first
- ✅ Keep deployment logs
- ✅ Monitor site after deployment
- ⚠️ Never deploy untested changes directly to production

### General
- ✅ Document all changes
- ✅ Keep backups of important content
- ✅ Regularly update dependencies (Hugo, etc.)
- ✅ Monitor site performance and uptime

---

## Support & Resources

### Documentation
- Hugo Documentation: https://gohugo.io/documentation/
- AWS S3 Documentation: https://docs.aws.amazon.com/s3/
- AWS CloudFront Documentation: https://docs.aws.amazon.com/cloudfront/

### Project Files
- Main workflow: `PUBLISHING_WORKFLOW.md` (this file)
- Page templates: `NEW_PAGE_TEMPLATE_GUIDE.md`
- AWS config: `docs/klm_crm_publishing_process.md`

### Getting Help
- Check the troubleshooting section above
- Review deployment script output for error messages
- Verify AWS permissions and credentials
- Test with a simple page first before complex changes

---

## Maintenance

### Regular Tasks

**Weekly:**
- Review staging site for any issues
- Check for broken links
- Monitor form submissions

**Monthly:**
- Update Hugo if new version available
- Review and clean up old deployment logs
- Backup important content

**As Needed:**
- Update SSL certificates (handled by AWS)
- Review and update IAM permissions
- Optimize images for faster loading

---

## Appendix: Script Details

### publish_to_staging.py

- **Purpose:** Deploy to staging environment
- **Target:** https://www.klmcrm.com
- **S3 Bucket:** s3://klmcrm.com
- **CloudFront:** E3HA8770RGET6T
- **Safety:** No confirmation required (staging is safe)

### publish_to_production.py

- **Purpose:** Deploy to production environment
- **Target:** https://www.klminsurance.com
- **S3 Bucket:** s3://klminsurance.com
- **CloudFront:** *Needs configuration*
- **Safety:** Requires typing "DEPLOY TO PRODUCTION"
- **Logging:** Creates deployment log in `deployment-logs/`

### test_ui_ux.py

- **Purpose:** Automated UI/UX testing
- **Devices:** iPhone 14 Pro, iPad Pro, Desktop (2 sizes)
- **Tests:** Load time, navigation, forms, images, layout
- **Output:** Screenshots in `screenshots-testing/`

---

**Last Updated:** December 23, 2025
**Document Version:** 1.0
**Maintained by:** KLM Insurance Development Team
