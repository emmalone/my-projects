---
title: "QUICK_START"
project: klm-migrate
original_path: QUICK_START.md
modified: 2025-12-26T10:05:04.657393
---

# KLM Insurance Website - Quick Start Guide

**Fast reference for common tasks**

---

## Publishing Commands

### Work Locally (Development)
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo server -D --bind 0.0.0.0
```
**View at:** http://localhost:1313
**Stop:** Press `Ctrl+C`

### Publish to Staging
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py
```
**View at:** https://www.klmcrm.com

### Publish to Production
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_production.py
```
**Type:** `DEPLOY TO PRODUCTION`
**View at:** https://www.klminsurance.com

---

## Create a New Page

1. **Create content file:**
   ```bash
   cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content
   nano my-new-page.md
   ```

2. **Add content:**
   ```markdown
   ---
   title: "My New Page"
   description: "Description for SEO"
   draft: false
   hero_image: "/images/featured-banner.png"
   sidebar_image: "/images/content-banner.png"
   form_type: "full"
   ---

   ## Heading

   Your content here...
   ```

3. **Test locally:** `hugo server -D`
4. **Publish to staging:** `python3 publish_to_staging.py`
5. **Publish to production:** `python3 publish_to_production.py`

---

## Workflow Summary

```
1. Develop Locally (localhost:1313)
   ↓
2. Test Changes
   ↓
3. Publish to Staging (klmcrm.com)
   ↓
4. Client Review & Approval
   ↓
5. Publish to Production (klminsurance.com)
   ↓
6. Verify Live Site
```

---

## Important Files

```
Content:     klm-hugo-site/content/
Layouts:     klm-hugo-site/layouts/
Images:      klm-hugo-site/static/images/
CSS:         klm-hugo-site/static/css/style.css

Scripts:
  publish_to_staging.py       - Deploy to staging
  publish_to_production.py    - Deploy to production

Documentation:
  PUBLISHING_WORKFLOW.md      - Complete workflow guide
  QUICK_START.md              - This file
```

---

## Troubleshooting

**Hugo server already running:**
```bash
lsof -ti:1313 | xargs kill -9
```

**AWS credentials issue:**
```bash
aws sts get-caller-identity
# If error, run: aws configure
```

**Changes not appearing:**
- Wait 1-3 minutes for CloudFront cache
- Hard refresh: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
- Try incognito/private browsing

**Build errors:**
- Check Markdown syntax
- Verify front matter (YAML between `---`)
- Look for unclosed HTML tags

---

## Need More Help?

Read the complete guide: `PUBLISHING_WORKFLOW.md`

**Shows:**
- Detailed step-by-step instructions
- Complete lifecycle examples
- Troubleshooting guide
- Best practices
