---
title: "claude"
project: klm-migrate
original_path: klm-hugo-site/claude.md
modified: 2026-01-02T01:16:28.690236
---

# KLM Insurance Website Migration Project

**Complete Project Context & Technical Reference**

---

## 📋 Quick Reference

**Project Location:** `/Users/mark/PycharmProjects/klm-migrate`
**Hugo Site:** `/Users/mark/PycharmProjects/klm-migrate/klm-hugo-site`
**Repository:** https://github.com/emmalone/klm-migrate
**Developer:** Mark (mark@emm-associates.com)
**Company:** KLM Insurance Solutions, Inc.
**Last Updated:** January 2, 2026

---

## ⚙️ Claude Code Permission Configuration

### Settings File Location
**Project Settings:** `.claude/settings.json` (committed to git)
**Local Overrides:** `.claude/settings.local.json` (gitignored)

### Current Configuration
The project has pre-configured permissions in `.claude/settings.json` that allow:
- ✅ All git commands (status, add, commit, push, etc.)
- ✅ Hugo commands (server, build)
- ✅ AWS CLI commands (S3, CloudFront, Route53)
- ✅ GitHub CLI commands (gh run, gh secret, gh pr)
- ✅ Reading all project files
- ✅ Editing content files (md, html, css, js, py, yml)
- ✅ WebSearch and approved domain fetches

**Default Mode:** `acceptEdits` - Auto-accepts file edits without prompting

### Key Permission Rules
```json
"allow": [
  "Bash(git:*)",          // All git commands
  "Bash(hugo:*)",         // All hugo commands
  "Bash(aws s3:*)",       // AWS S3 operations
  "Bash(gh:*)",           // GitHub CLI
  "Read(/Users/mark/PycharmProjects/klm-migrate/**)", // Read all project files
  "Edit(**/*.md)",        // Edit markdown files
  "WebSearch"             // Web search enabled
],
"deny": [
  "Read(.env*)",          // Protect environment files
  "Bash(rm -rf:*)",       // Prevent destructive deletes
  "Bash(sudo:*)",         // No sudo commands
  "Bash(git push --force:*)" // No force pushes
]
```

### Modify Permissions
To add more allowed commands:
1. Edit `.claude/settings.json`
2. Add patterns to the `allow` array
3. Commit and push to share with team

**Example - Allow npm commands:**
```json
"allow": [
  "Bash(npm install:*)",
  "Bash(npm run:*)"
]
```

### View Active Permissions
In any Claude Code session, type:
```
/permissions
```

---

## 🔑 Credentials & API Keys

### JotForm
- **Primary Form ID:** 253585658329169 (Request Quote Form - with page tracking)
- **Secondary Form ID:** 253584401906155 (Quote Form - legacy)
- **API Key:** `d250db3b489a19b5b1ed8f7e68bb9e79`
- **Account URL:** https://www.jotform.com
- **Hidden Field Name:** `page_source` (tracks which page submissions come from)
- **API Endpoint:** `https://api.jotform.com/form/{FORM_ID}/submissions`

**API Usage Example:**
```bash
curl "https://api.jotform.com/form/253585658329169/submissions?apiKey=d250db3b489a19b5b1ed8f7e68bb9e79&limit=10"
```

### AWS Account
- **Account ID:** 837716495292
- **IAM User:** klm-hugo
- **Access Key ID:** AKIA4GC6LJO6OIIMIIRY
- **Region:** us-east-1
- **AWS CLI Profile:** default

**Verify AWS Access:**
```bash
aws sts get-caller-identity
# Should return Account: 837716495292, User: klm-hugo
```

### GitHub
- **Repository:** emmalone/klm-migrate
- **GitHub User:** emmalone
- **GitHub CLI:** Authenticated with workflow scope
- **Actions Secrets:**
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION` = us-east-1
  - `S3_DEV_BUCKET` = dev-klmhugoweb

---

## 🌐 Deployment Environments

The project supports **3 development scenarios** with 4 deployment environments:

### Development Scenarios

#### Scenario 1: Laptop/Desktop Development (Mac/PC)
- **Branch:** `main`
- **Testing:** Local Hugo server + auto-deploy to dev
- **Local URL:** http://localhost:1313
- **Dev URL:** http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com
- **Deploy to Staging:** Manual via `python3 publish_to_staging.py`
- **Auto-deploy to Dev:** ✅ YES - Every push to main
- **Auto-deploy to Staging:** ❌ NO - Manual control only

#### Scenario 2: iPhone Development (Claude Code + GitHub)
- **Branch:** `claude/**` (auto-created by Claude Code)
- **Testing:** Auto-deploy to dev environment
- **URL:** http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com
- **Deploy:** ✅ AUTOMATIC on push to any `claude/**` branch
- **Target Bucket:** `dev-klmhugoweb`

#### Scenario 3: Staging Deployment
- **Target:** klmcrm.com bucket (https://www.klmcrm.com)
- **Deploy Method:** Manual control ONLY via `python3 publish_to_staging.py`
- **Auto-deploy:** ❌ DISABLED - You control when staging updates

---

### Environment Details

### 1. Local Development
- **URL:** http://localhost:1313
- **Purpose:** Local development and testing on laptop/desktop
- **Start Server:** `cd klm-hugo-site && hugo server -D --bind 0.0.0.0`
- **Deploy:** Not applicable (local only)

### 2. Dev Environment (Auto-Deploy Always)
- **URL:** http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com
- **S3 Bucket:** dev-klmhugoweb
- **Region:** us-east-1
- **Purpose:** Always-current development preview for both laptop and iPhone work
- **Trigger:** ✅ Auto-deploys on push to `main` OR `claude/**` branches
- **Workflow:** `.github/workflows/deploy-dev.yml`
- **Cache:** 5 minutes (max-age=300)
- **BaseURL:** http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com/

**When It Deploys:**
- ✅ Automatically when you push to `main` (laptop/desktop work)
- ✅ Automatically when you push to any `claude/**` branch (iPhone work)
- Preview ready in ~30 seconds after push
- CSS and assets load correctly with proper baseURL
- **Always ready for iPhone preview** - Dev reflects latest committed code

### 3. Staging (Manual Deployment Only)
- **URL:** https://www.klmcrm.com
- **S3 Bucket:** klmcrm.com
- **CloudFront ID:** E3HA8770RGET6T
- **Route53 Zone ID:** ZNUGG3NYBSQJ8
- **SSL Certificate:** *.klmcrm.com (ISSUED)
- **Status:** ✅ Working perfectly
- **Purpose:** Business review and stakeholder approval
- **Deploy Method:** ⚠️ MANUAL ONLY - Python script
- **Cache:** 1 hour (max-age=3600)

**Deployment Command (From Laptop/Desktop ONLY):**
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py
```

**Important:** Staging does NOT auto-deploy. You have full control over when changes go to staging.

### 4. Production (Live Site)
- **URL:** https://www.klminsurance.com
- **S3 Bucket:** klminsurance.com
- **CloudFront ID:** Not yet configured
- **SSL Certificate:** None yet
- **Route53:** None (DNS hosted elsewhere)
- **Status:** 🔄 Ready for Phase 1 deployment
- **Purpose:** Customer-facing live website
- **Deploy Script:** `publish_to_production.py`

**Deployment Command:**
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_production.py
# Type: DEPLOY TO PRODUCTION
```

---

## 🔄 Git Branch Strategy

### Branches
- **`main`** - Primary development branch (laptop/desktop work)
- **`claude/**`** - Auto-created by Claude Code on iPhone (e.g., `claude/add-landing-page-xyz`)

### Workflow

#### Working on Laptop/Desktop:
```bash
# Work directly on main branch
git checkout main
git pull origin main

# Make changes locally
# ... edit files ...

# Test locally
hugo server -D

# When satisfied, commit to main
git add .
git commit -m "Your changes"
git push origin main

# Deploy to staging when ready (manual control)
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py
```

#### Working on iPhone with Claude Code:
```
Claude Code automatically:
1. Creates branch: claude/feature-name-xyz
2. Makes changes
3. Commits changes
4. Pushes to GitHub
5. Auto-deploys to dev-klmhugoweb S3 bucket

Preview at: http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com

When ready:
- Create PR to merge claude/* branch into main
- Or ask Claude to merge directly to main
- Then manually deploy to staging from laptop when ready
```

### Important Notes
- **No staging branch** - Staging deployment is controlled manually via Python script
- **No auto-deploy to staging** - You decide when staging updates
- **iPhone work previews on dev** - All `claude/**` branches auto-deploy to dev-klmhugoweb
- **Laptop work stays local** - Test with `hugo server`, deploy to staging when ready

---

## 📂 Project Structure

```
/Users/mark/PycharmProjects/klm-migrate/
├── claude.md                           # ⭐ This file - project context
├── PRODUCTION_DEPLOYMENT_PLAN.md       # Production deployment guide
├── QUICK_START.md                      # Quick reference
├── WORKFLOW.md                         # Git workflow guide
├── SECURITY_REVIEW.md                  # Security audit results
├── requirements.txt                    # Python dependencies
├── todo.txt                            # Outstanding tasks
│
├── klm-hugo-site/                      # Main Hugo website
│   ├── hugo.toml                       # Hugo configuration
│   ├── content/                        # 14 Markdown pages
│   ├── layouts/                        # Custom HTML templates
│   ├── static/                         # CSS, images, assets
│   ├── themes/                         # klm-theme + megakit
│   ├── docs/                           # Reference documentation
│   └── .github/workflows/              # GitHub Actions
│       ├── deploy-dev.yml              # Auto-deploy dev branch
│       └── (deploy-staging.yml removed - staging uses Python scripts)
│
├── docs/                               # 20 documentation files
│   ├── JOTFORM_SETUP_GUIDE.md
│   ├── PUBLISHING_WORKFLOW.md
│   ├── PROJECT_COMPLETE.md
│   └── ... (17 more)
│
├── screenshots-manual/                 # Manual screenshots for debugging
│
└── Python Scripts (8 files):
    ├── build_klm_site.py               # Master orchestration
    ├── create_hugo_site.py             # Site builder
    ├── create_all_pages.py             # Page generator
    ├── scraper.py                      # Content scraper
    ├── download_images.py              # Image downloader
    ├── screenshot_pages.py             # Screenshot capture
    ├── publish_to_staging.py           # Staging deployment
    ├── publish_to_production.py        # Production deployment
    └── test_ui_ux.py                   # UI/UX testing
```

---

## 📝 Hugo Site Structure

### Content Pages (14 files in `content/`)
1. `_index.md` - Homepage with hero and services grid
2. `about.md` - Company information
3. `contact.md` - Contact form page
4. `auto-insurance.md` - Auto coverage
5. `home-insurance.md` - Homeowners coverage
6. `commercial-insurance.md` - Business insurance
7. `boat-insurance.md` - Boat/watercraft insurance
8. `life-insurance.md` - Life insurance
9. `umbrella-insurance.md` - Umbrella coverage
10. `term-whole-permanent-insurance.md` - Specific life products
11. `insurance-insights.md` - Blog/insights
12. `landing.md` - Landing page template example
13. `client-center.md` - Client resources
14. `compare-quotes.md` - Quote comparison

### Layouts (7 files in `layouts/`)
- `index.html` - Homepage layout
- `_default/baseof.html` - Base template (header/footer)
- `_default/single.html` - Default page layout (most pages)
- `_default/contact.html` - Contact page with form
- `_default/compare-quotes.html` - Quote comparison page
- `_default/client-center.html` - Client resources page
- `_default/landing.html` - Landing page with video support

### Static Assets (`static/`)
- **CSS:** `css/style.css` - Custom styles
- **Images:** 30+ images including:
  - Logos: klm-insurance-logo.png, klm-logo-short-white.png
  - Featured banners: featured-auto-insurance.jpg, featured-home-insurance.jpg, etc.
  - Partner logos: travelers-slide.png, progressive-slide.png, nationwide-slide.png
  - Content banners: content-banner.png
- **Favicon:** favicon.ico

---

## 🎯 Form Tracking System

### Strategy
**ONE JotForm for all pages** with hidden `page_source` field that tracks which page submissions come from.

### Benefits
- ✅ All submissions in one place
- ✅ Easy to filter by landing page in JotForm
- ✅ No need to create multiple forms
- ✅ Automatically tracks page source

### Implementation

**JotForm Hidden Field Setup:**
1. Form ID: 253585658329169
2. Field Type: Short Text Entry (hidden)
3. Field Label: "Page Source"
4. Unique Name: `page_source` ⭐ (this is what matters!)
5. Hide Field: ON (in Advanced settings)

**Template Implementation:**
- **Homepage:** `?page_source=homepage`
- **Contact:** `?page_source=contact`
- **Interior Pages:** `?page_source={{.File.BaseFileName}}` (e.g., auto-insurance)
- **Landing Pages:** `?page_source={{.Params.form_source}}` (customizable in front matter)

**Example URL Parameters:**
```html
<!-- Homepage -->
<iframe src="https://form.jotform.com/253585658329169?page_source=homepage"></iframe>

<!-- Auto Insurance page -->
<iframe src="https://form.jotform.com/253585658329169?page_source=auto-insurance"></iframe>

<!-- Landing page (customizable) -->
<iframe src="https://form.jotform.com/253585658329169?page_source=summer-2026-promo"></iframe>
```

**Viewing Submissions:**
1. Log into JotForm
2. Go to form 253585658329169
3. Click "Submissions"
4. See `page_source` column with values
5. Filter by specific landing page
6. Export to Excel/CSV for analysis

**API Check:**
```bash
curl "https://api.jotform.com/form/253585658329169/submissions?apiKey=d250db3b489a19b5b1ed8f7e68bb9e79&limit=5"
```

---

## 📄 Creating Landing Pages

Landing pages use a special template with:
- ✅ Hero section (800px tall, matches other pages)
- ✅ Contact form overlay (same as interior pages)
- ✅ Video section (optional - shows placeholder if no video)
- ✅ Description content (markdown)
- ✅ Form tracking (automatic source parameter)

### Create New Landing Page

**Step 1: Create Content File**
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content
cp landing.md my-new-landing.md
```

**Step 2: Edit Front Matter**
```yaml
---
title: "Summer Auto Insurance Promo"
description: "Special summer rates on auto insurance"
draft: false
layout: "landing"
hero_image: "/images/featured-auto-insurance.jpg"
video_url: "/videos/summer-promo.mp4"  # Optional
form_source: "summer-2026-auto-promo"  # ⭐ Custom tracking identifier
---

## Welcome to Our Summer Promo!

Your markdown content here...
```

**Step 3: Test Locally**
```bash
hugo server -D
# Visit: http://localhost:1313/my-new-landing/
```

**Step 4: Deploy**
```bash
git add content/my-new-landing.md
git commit -m "Add summer auto insurance landing page"
git push
```

**Result:**
- URL: `https://www.klminsurance.com/my-new-landing/`
- Form tracking: Submissions tagged as `summer-2026-auto-promo`

---

## 🚀 Deployment Workflows

### Scenario 1: Laptop/Desktop Development
```bash
# Step 1: Local development and testing
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo server -D --bind 0.0.0.0
# View at: http://localhost:1313
# Test all changes locally
# Press Ctrl+C to stop

# Step 2: Commit to main
git add .
git commit -m "Descriptive message"
git push origin main

# Step 3: Deploy to staging (when ready for review)
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py

# Script automatically:
# 1. Builds Hugo with baseURL: https://www.klmcrm.com
# 2. Syncs to S3: s3://klmcrm.com
# 3. Invalidates CloudFront: E3HA8770RGET6T
# 4. Verifies deployment with HTTP check
# 5. Preview at: https://www.klmcrm.com
```

### Scenario 2: iPhone Development (Auto-Deploy to Dev)
```
Step 1: Work with Claude Code on iPhone
- Tell Claude what you want to change
- Claude creates claude/* branch automatically
- Claude makes changes and commits
- Claude pushes to GitHub

Step 2: Automatic deployment to dev
- GitHub Actions detects push to claude/* branch
- Builds with: hugo --minify --baseURL "http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com/"
- Syncs to S3: aws s3 sync public/ s3://dev-klmhugoweb/ --delete
- Preview ready in ~30 seconds at: http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com

Step 3: Merge to main when satisfied
- Ask Claude to create PR to main
- Review and merge on GitHub or via Claude
- Changes now in main branch

Step 4: Deploy to staging from laptop (when ready)
- From laptop: python3 publish_to_staging.py
```

### Scenario 3: Deploy to Staging (Manual Control)
```bash
# Always done from laptop/desktop - NEVER auto-deploys
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py

# What it does:
# 1. Builds Hugo site with staging baseURL
# 2. Syncs to klmcrm.com S3 bucket
# 3. Invalidates CloudFront cache
# 4. Verifies deployment
# 5. Live at: https://www.klmcrm.com

# You control WHEN this happens - no automation
```

### Deploy to Production
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_production.py

# Prompts for confirmation:
# Type: DEPLOY TO PRODUCTION

# Script:
# 1. Shows production warning
# 2. Builds with baseURL: https://www.klminsurance.com
# 3. Syncs to S3: s3://klminsurance.com
# 4. Creates deployment log
# 5. Verifies deployment

# ⚠️ Note: CloudFront and DNS not yet configured for production
```

### Workflow Summary

| Scenario | Branch | Testing | Auto-Deploy to Dev | Deploy to Staging |
|----------|--------|---------|-------------------|-------------------|
| **Laptop/Desktop** | `main` | Local (hugo server) | ✅ Yes | Manual (Python script) |
| **iPhone** | `claude/**` | Dev environment | ✅ Yes | Manual (Python script) |
| **Staging** | N/A | N/A | N/A | Manual (Python script) |

**Key Point:** Dev environment auto-deploys from BOTH `main` and `claude/**` branches, ensuring it's always current for iPhone preview.

---

## ⚙️ Hugo Configuration

**File:** `klm-hugo-site/hugo.toml`

```toml
baseURL = "https://www.klminsurance.com/"
languageCode = "en-us"
title = "KLM Insurance Solutions"
theme = "klm-theme"

[params]
  description = "High-quality, reliable insurance coverage options in Pennsylvania"
  author = "KLM Insurance Solutions"

[params.contact_info]
  address = "1554 Paoli Pike, West Chester, PA 19380"
  phone = "610-429-1330"
  email = "info@klminsurance.com"

[markup.goldmark.renderer]
  unsafe = true  # Allows HTML in markdown
```

**Menu Configuration:**
- HOME
- INSURANCE SERVICES (dropdown with 6 products)
- INSURANCE INSIGHTS
- CUSTOMER SERVICE (dropdown with Client Center)
- COMPARE QUOTES
- CONTACT US
- ABOUT US

---

## 🔒 Security & Git

### Files Excluded from Git (`.gitignore`)
- ✅ Hugo build outputs: `public/`, `resources/_gen/`
- ✅ Python: `__pycache__/`, `.venv/`, `*.pyc`
- ✅ Secrets: `.env*`, `secrets.json`, `*.key`, `*.pem`
- ✅ OS: `.DS_Store`, `Thumbs.db`
- ✅ IDE: `.vscode/`, `.idea/`
- ✅ Dangerous scripts with API keys (excluded but kept locally)

### API Key Locations
API keys are in Python utility scripts:
- `apply_form_settings.py` - Apply CSS styling to form
- `add_submit_button.py` - Add submit button
- `remove_theme.py` - Remove form theme
- `compress_form.py` - Reduce comment box height
- `fix_form_fields.py` - Fix field labels and requirements
- `check_form_structure.py` - Inspect form structure
- `fix_form_width.py` - Fix comment field width to match other fields

**Run Locally:** These scripts require local execution (JotForm API not accessible from cloud environments).

---

## 🐛 Troubleshooting

### CSS Not Loading on Dev Site
**Problem:** Pages load but appear unstyled (all default HTML)
**Cause:** Hugo built with wrong baseURL, assets pointing to production
**Solution:** Deploy workflow uses `--baseURL` flag
```bash
# In .github/workflows/deploy-dev.yml:
hugo --minify --baseURL "http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com/"
```

### Form Not Tracking Page Source
**Problem:** Submissions show empty `page_source` field
**Solution:** Check these:
1. JotForm field unique name is `page_source` (not "source")
2. Template includes `?page_source=value` in iframe src
3. Field is not disabled in JotForm
```bash
# Verify in HTML:
curl http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com/ | grep "page_source"
```

### GitHub Actions Deploy Failing
**Problem:** Workflow fails with AWS credential errors
**Solution:** Check GitHub secrets
```bash
gh secret list
# Should show:
# - AWS_ACCESS_KEY_ID
# - AWS_SECRET_ACCESS_KEY
# - AWS_REGION
# - S3_DEV_BUCKET
```

### Hugo Server Port Already in Use
**Problem:** `hugo server` fails - port 1313 busy
**Solution:** Kill existing Hugo process or use different port
```bash
# Option 1: Kill existing
lsof -ti:1313 | xargs kill -9

# Option 2: Use different port
hugo server -p 1314
```

### S3 Deployment Permission Denied
**Problem:** `aws s3 sync` fails with AccessDenied
**Solution:** Verify AWS credentials and IAM permissions
```bash
aws sts get-caller-identity
# Should return: klm-hugo user, account 837716495292
```

### Form Fields Have Inconsistent Widths
**Problem:** Comment field is wider than other form fields on landing pages
**Solution:** Run the fix_form_width.py script locally
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 fix_form_width.py
```
This script:
1. Sets the Comments textarea `cols` property to match text input width
2. Updates form CSS for consistent max-width on all fields

---

## 📚 Important Documentation Files

### Landing Pages & Forms
- **`klm-hugo-site/docs/LANDING_PAGES_GUIDE.md`** - Complete landing page guide with form tracking
- **`docs/JOTFORM_SETUP_GUIDE.md`** - JotForm configuration and integration
- **`docs/JOTFORM_INTEGRATION_SUMMARY.md`** - Form integration overview

### Deployment
- **`PRODUCTION_DEPLOYMENT_PLAN.md`** - Phased production deployment plan (S3 → CloudFront → DNS)
- **`docs/PUBLISHING_WORKFLOW.md`** - Complete lifecycle: Dev → Staging → Production
- **`publish_to_staging.py`** - Staging deployment script
- **`publish_to_production.py`** - Production deployment script

### Development
- **`QUICK_START.md`** - Quick reference for common tasks
- **`WORKFLOW.md`** - Git workflow and branching strategy
- **`docs/NEW_PAGE_TEMPLATE_GUIDE.md`** - Creating new pages

### Security & Process
- **`SECURITY_REVIEW.md`** - Security audit results (API keys, .gitignore)
- **`docs/FIX_APEX_DOMAIN.md`** - DNS apex domain configuration
- **`todo.txt`** - Outstanding tasks

---

## 📋 Common Tasks

### Add New Insurance Product Page
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content
nano motorcycle-insurance.md
```
```yaml
---
title: "Motorcycle Insurance"
description: "Motorcycle Insurance - KLM Insurance Solutions"
draft: false
hero_image: "/images/featured-banner.png"
sidebar_image: "/images/content-banner.png"
---

## Motorcycle Insurance Content
Your content here...
```
```bash
# Test locally
hugo server -D

# Deploy to staging
cd ..
python3 publish_to_staging.py
```

### Check Recent Form Submissions
```bash
curl "https://api.jotform.com/form/253585658329169/submissions?apiKey=d250db3b489a19b5b1ed8f7e68bb9e79&limit=5" | python3 -m json.tool
```

### Verify S3 Bucket Contents
```bash
# Dev
aws s3 ls s3://dev-klmhugoweb/ --recursive | head -20

# Staging
aws s3 ls s3://klmcrm.com/ --recursive | head -20

# Production
aws s3 ls s3://klminsurance.com/ --recursive | head -20
```

### Invalidate CloudFront Cache
```bash
# Staging only (production CloudFront not yet configured)
aws cloudfront create-invalidation \
  --distribution-id E3HA8770RGET6T \
  --paths "/*"
```

### Check GitHub Actions Status
```bash
gh run list --limit 5
gh run view <RUN_ID>
```

### Update Menu Navigation
Edit `klm-hugo-site/hugo.toml`:
```toml
[[menu.main]]
  name = "Motorcycle Insurance"
  url = "/motorcycle-insurance/"
  weight = 8
```

---

## 🎯 Recent Work History

### January 2, 2026 (Latest Session - Form Width Fix)
- ✅ Successfully completed iPhone → Laptop workflow for JotForm fixes
  - Pulled `claude/fix-form-field-width-9NPVL` branch from iPhone work
  - Ran `fix_form_width.py` script locally (JotForm API requires local execution)
  - Merged fix branch to main and cleaned up old branches
- ✅ Fixed landingv2 form container width issue
  - Root cause: Container was 600px wide (too wide), causing submit button to appear next to comments field
  - Solution: Changed container from 600px → 350px to match other page templates
  - Updated background from white to #0099CC blue (matches form styling)
- ✅ JotForm field consistency achieved across all pages
  - Comments field: cols changed from 648 → 40 (matches text input width)
  - All form fields now have consistent widths via CSS
  - Form looks identical on homepage, interior pages, and landing pages
- ✅ Deployed fixes to staging (https://www.klmcrm.com)
  - 21 files updated including landingv2 template
  - CloudFront cache invalidated successfully
  - Forms verified working correctly across all page types

### January 2, 2026 (Continued)
- ✅ Configured dev to auto-deploy from BOTH `main` and `claude/**` branches
  - Ensures dev environment always reflects latest committed code
  - Dev always ready for iPhone preview
- ✅ Configured 3-scenario deployment workflow
  - Laptop/Desktop: Local dev + auto-deploy to dev + manual staging
  - iPhone: Auto-deploy to dev-klmhugoweb on `claude/**` branches
  - Staging: Manual control only via Python script
- ✅ Disabled staging auto-deploy workflow (renamed to .disabled)
- ✅ Added --baseURL flag to dev workflow for proper CSS loading
- ✅ Updated claude.md with comprehensive deployment documentation
- ✅ Updated WORKFLOW.md and DEVELOPMENT_WORKFLOW.md with new process
- ✅ Moved landing pages to /guides/ subfolder
- ✅ Created landingv2 template with trust-focused design

### January 2, 2026 (Earlier)
- ✅ Fixed dev site CSS loading issue (added --baseURL flag to deploy-dev.yml)
- ✅ Verified form tracking working with API (test submission confirmed)
- ✅ Created comprehensive claude.md file for project context
- ✅ Installed and configured GitHub CLI with workflow scope

### January 1, 2026
- ✅ Fixed JotForm form tracking with correct `page_source` parameter
- ✅ Updated all templates (homepage, contact, single, landing) with page_source
- ✅ Renamed `staging` branch to `dev-klmhugoweb`
- ✅ Created S3 bucket `dev-klmhugoweb` for auto-deployment
- ✅ Configured GitHub Actions workflow for dev auto-deploy
- ✅ Set up GitHub secrets (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_DEV_BUCKET)
- ✅ Updated LANDING_PAGES_GUIDE.md with correct JotForm setup instructions

### December 30, 2025 (Previous Session)
- ✅ Merged iPhone work (landing page, workflows, docs) into main branch
- ✅ Created landing page template matching interior page design
- ✅ Implemented form source tracking with URL parameters
- ✅ Fixed thumbnail image issues from MacBook work
- ✅ Resolved branch divergence (main vs claude/create-landing-page-dEu1p)

### December 28-29, 2025
- ✅ Completed staging deployment to klmcrm.com
- ✅ Configured CloudFront with SSL certificate
- ✅ Set up Route53 DNS for staging
- ✅ Verified staging site fully functional
- ✅ Created PRODUCTION_DEPLOYMENT_PLAN.md

---

## 📝 Outstanding Tasks

### Priority 1 - DNS (Staging)
- [ ] Update klmcrm.com nameservers to AWS Route 53
  - Apex domain (without www) needs nameserver update
  - Reference: `docs/FIX_APEX_DOMAIN.md`

### Priority 2 - Email (Staging)
- [ ] Configure JotForm email notifications
  - Set up notifications to sales@klminsurance.com
  - Enable auto-responders
  - Estimated: 20-30 minutes

### Priority 3 - Production Deployment
- [ ] Phase 1: Deploy to S3 (ready to execute)
- [ ] Phase 2: Setup CloudFront + SSL
- [ ] Phase 3: DNS migration planning
  - Document current DNS records
  - Coordinate with domain registrar
  - Plan migration timing

### Priority 4 - Content
- [ ] Add motorcycle insurance page (if needed)
- [ ] Review and update insurance insights blog content

---

## 🔗 Useful Links

**Production Sites:**
- Dev Preview: http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com
- Staging: https://www.klmcrm.com
- Production: https://www.klminsurance.com (when deployed)

**External Services:**
- JotForm Dashboard: https://www.jotform.com/myforms
- JotForm API Docs: https://api.jotform.com/docs
- AWS Console: https://console.aws.amazon.com (Account: 837716495292)
- GitHub Repository: https://github.com/emmalone/klm-migrate
- GitHub Actions: https://github.com/emmalone/klm-migrate/actions

**Hugo Resources:**
- Hugo Documentation: https://gohugo.io/documentation
- Hugo Themes: https://themes.gohugo.io

---

## 💡 Pro Tips

### Working Remotely (iPhone/iPad)
1. Make changes on GitHub web interface
2. Commit to `main` branch
3. Switch to `dev-klmhugoweb` branch on GitHub
4. Create Pull Request from `main` to `dev-klmhugoweb`
5. Merge PR → triggers auto-deploy
6. Preview at dev URL within 30 seconds

### Faster Local Development
```bash
# Use --disableFastRender for accurate previews
hugo server -D --disableFastRender

# Bind to all interfaces for mobile testing
hugo server -D --bind 0.0.0.0
# Access from phone: http://YOUR_LOCAL_IP:1313
```

### JotForm Form Testing
1. Use test submissions with obvious data (e.g., "TEST DO NOT USE")
2. Check page_source field immediately after submitting
3. Delete test submissions to keep data clean

### Before Major Deployments
```bash
# Always test build first
cd klm-hugo-site
hugo --minify
# Check public/ folder for issues

# Verify AWS access
aws sts get-caller-identity

# Check current S3 contents
aws s3 ls s3://TARGET_BUCKET/
```

---

## 🎓 Technology Stack

- **Static Site Generator:** Hugo (Extended) v0.154.0+
- **Hosting:** AWS S3 + CloudFront
- **CDN:** CloudFront with SSL/TLS
- **DNS:** Route 53 (staging), External (production)
- **Forms:** JotForm (iframe embeds)
- **Version Control:** Git + GitHub
- **CI/CD:** GitHub Actions
- **Languages:** HTML, CSS, JavaScript, Markdown, Python
- **Python Libs:** requests, beautifulsoup4, playwright, lxml
- **Markup:** Markdown (Goldmark renderer)
- **Theme:** Custom klm-theme + Megakit base

---

## 🏢 Company Information

**KLM Insurance Solutions, Inc.**
- **Address:** 1554 Paoli Pike, West Chester, PA 19380
- **Phone:** 610-429-1330
- **Email:** info@klminsurance.com
- **Website:** www.klminsurance.com

**Social Media:**
- Facebook: https://facebook.com/klminsurance
- LinkedIn: https://linkedin.com/company/klm-insurance
- Twitter: https://twitter.com/klminsurance

**Insurance Carriers/Partners:**
- Travelers
- Progressive
- Nationwide
- Foremost
- MetLife
- PURE Insurance
- The Philadelphia

---

## 📞 Support & Contact

**Developer Contact:**
- Mark
- Email: mark@emm-associates.com
- GitHub: emmalone

**For Claude Code Sessions:**
- This file (`claude.md`) contains all project context
- Reference specific sections as needed
- Update this file after major milestones
- Commit changes to keep it in sync across devices

---

**Project Status:** Active Development
**Current Phase:** Dev environment operational, staging live, production ready for Phase 1
**Next Milestone:** Production DNS migration planning

---

*Last session work: Fixed JotForm form field widths across all templates, deployed to staging for review*
