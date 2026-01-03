---
title: "LANDING_PAGES_GUIDE"
project: klm-migrate
original_path: klm-hugo-site/docs/LANDING_PAGES_GUIDE.md
modified: 2026-01-01T22:37:14.639053
---

# Landing Pages & Form Tracking Guide

This guide explains how to create landing pages and track which page users submitted forms from.

## 📋 Table of Contents

1. [Overview](#overview)
2. [Setting Up JotForm Hidden Field](#setting-up-jotform-hidden-field)
3. [Creating New Landing Pages](#creating-new-landing-pages)
4. [How Form Tracking Works](#how-form-tracking-works)
5. [Viewing Submission Data](#viewing-submission-data)
6. [Examples](#examples)

---

## Overview

### The Strategy

We use **ONE JotForm** for all pages with a **hidden field** that captures which page the user came from.

**Benefits:**
- ✅ All submissions in one place
- ✅ Easy to filter by landing page
- ✅ No need to create multiple forms
- ✅ Automatically tracks page source

---

## Setting Up JotForm Hidden Field

**You only need to do this ONCE for your main quote form.**

### Step 1: Log into JotForm

1. Go to https://www.jotform.com
2. Log in to your account
3. Find form ID: `253585658329169` (Request Quote Form)
4. Click **"Edit Form"**

### Step 2: Add Hidden Field

**Note:** JotForm doesn't have a dedicated "Hidden Field" element in recent versions.

1. In the form builder, click **"Add Form Element"**
2. Find and add a **"Short Text Entry"** field
3. Drag it anywhere in your form (position doesn't matter since it will be hidden)

### Step 3: Configure and Hide the Field

1. Click on the newly added Short Text field
2. In the **Properties** panel on the right:
   - **Field Label**: `Page Source` (for your reference)
   - **Default Value**: Leave blank (or set to "unknown")

3. Click **"Advanced"** tab at the top
4. Scroll down and toggle **"Hide Field"** to ON (this makes it invisible to users)
5. Scroll to the bottom and expand **"Field Details"**
6. Note the **Unique Name** - it should be `page_source` (or similar like `pageSource3`)

**IMPORTANT:** The **Unique Name** is what you'll use in the URL parameter!

### Step 4: Save Form

Click **"Save"** or **"Publish"** in the top-right corner.

**That's it!** Your form is now ready to track page sources.

---

## How Form Tracking Works

### Automatic Tracking

The landing page template automatically adds the source parameter to the form URL:

```html
<!-- The template does this automatically -->
<iframe src="https://form.jotform.com/253585658329169?source=landing-page-example"></iframe>
```

### What Gets Captured

When a user on `/guides/landing/` fills out the form:
- JotForm receives the URL parameter `?source=landing-page-example`
- The hidden field captures the value: `landing-page-example`
- This value is saved with the submission

### Customizing the Source Name

In your landing page content file (e.g., `content/landing.md`):

```yaml
---
title: "Special Promotion Landing Page"
layout: "landing"
form_source: "summer-2026-promo"  # ← Custom source identifier
---
```

**If you don't specify `form_source`:**
- It defaults to the filename (e.g., `landing`, `auto-special-offer`)

---

## Creating New Landing Pages

### Method 1: Duplicate Existing Landing Page

```bash
# Navigate to content directory
cd content/

# Copy the landing page
cp landing.md my-new-landing.md

# Edit the new file
nano my-new-landing.md
```

### Method 2: Create from Scratch

Create `content/my-landing-page.md`:

```yaml
---
title: "My Special Offer"
description: "Exclusive insurance offer for new customers"
draft: false
layout: "landing"
hero_image: "/images/featured-banner.png"
video_url: ""  # Optional: Add MP4 URL here
form_source: "special-offer-2026"  # ← Unique identifier
---

## Welcome to Our Special Offer!

This is the content that appears below the video.

You can use **markdown** formatting:
- Bullet points
- **Bold text**
- [Links](https://example.com)

### Add Headings

And paragraphs of text to explain your offer.
```

### The Page Will Have:

1. ✅ **Hero section** (800px tall, matches other pages)
2. ✅ **Contact form overlay** (same as interior pages)
3. ✅ **Video section** (optional - shows placeholder if no video)
4. ✅ **Description content** (your markdown content)
5. ✅ **Form tracking** (automatic source parameter)

---

## Viewing Submission Data

### In JotForm

1. Log into JotForm
2. Go to form `253585658329169`
3. Click **"Submissions"**
4. You'll see a column called **"Page Source"** with values like:
   - `landing-page-example`
   - `summer-2026-promo`
   - `auto-insurance` (from regular pages)

### Filtering by Landing Page

1. In Submissions view, click **"Filter"**
2. Select **"Page Source"**
3. Choose specific landing page (e.g., `summer-2026-promo`)
4. See only submissions from that page

### Exporting Data

1. Click **"Export"** in Submissions
2. Choose **Excel** or **CSV**
3. The exported file includes the `page_source` column
4. Use Excel/Google Sheets to analyze by landing page

---

## Examples

### Example 1: Summer Promotion Landing Page

**File:** `content/summer-promo.md`

```yaml
---
title: "Summer Insurance Savings"
description: "Special summer rates on auto insurance"
layout: "landing"
hero_image: "/images/featured-auto-insurance.jpg"
video_url: "/videos/summer-promo.mp4"
form_source: "summer-2026-auto-promo"
---

## Save Big This Summer! ☀️

Get exclusive summer rates on auto insurance.

**Limited Time Offer:**
- Up to 20% savings
- No down payment
- Free roadside assistance

Watch the video above to learn more, then request your free quote!
```

**URL:** `https://www.klminsurance.com/summer-promo/`

**Form tracking:** Submissions tagged as `summer-2026-auto-promo`

---

### Example 2: Home Insurance Guide Landing Page

**File:** `content/home-insurance-guide.md`

```yaml
---
title: "Home Insurance Buying Guide"
description: "Everything you need to know about home insurance"
layout: "landing"
hero_image: "/images/featured-home-insurance.jpg"
video_url: "/videos/home-insurance-explained.mp4"
form_source: "home-insurance-guide-2026"
---

## Understanding Home Insurance

Watch our comprehensive guide to home insurance coverage.

### What's Covered:
- Dwelling coverage
- Personal property
- Liability protection
- Additional living expenses

Request a personalized quote using the form above!
```

**URL:** `https://www.klminsurance.com/home-insurance-guide/`

**Form tracking:** Submissions tagged as `home-insurance-guide-2026`

---

### Example 3: PPC Campaign Landing Page

**File:** `content/ppc-auto-offer.md`

```yaml
---
title: "Click Here for Auto Insurance Quote"
description: "Fast, easy auto insurance quotes"
layout: "landing"
hero_image: "/images/featured-auto-insurance.jpg"
video_url: ""
form_source: "google-ads-auto-2026-q1"
---

## Get Your Auto Insurance Quote in Minutes

You found us through our ad - great choice!

We offer:
- **Fast quotes** - Get your rate in under 2 minutes
- **Top carriers** - Compare rates from 10+ insurers
- **Expert service** - Local agents who care

Fill out the form above to get started!
```

**URL:** Use in Google Ads or Facebook Ads
**Form tracking:** Submissions tagged as `google-ads-auto-2026-q1`

---

## Form Source Naming Conventions

### Recommended Format

```
[channel]-[product]-[campaign]-[year]-[period]
```

**Examples:**
- `google-ads-auto-2026-q1` (Google Ads, Auto, Q1 2026)
- `facebook-home-spring-2026` (Facebook, Home, Spring 2026)
- `email-life-newsletter-feb-2026` (Email, Life, February 2026)
- `landing-boat-summer-promo` (Organic landing page, Boat, Summer)

### Keep It Simple

For simple campaigns, shorter names work too:
- `auto-promo-2026`
- `home-special`
- `life-insurance-info`

---

## Testing Form Tracking

### Before Going Live

1. **Create test landing page** in `content/test-landing.md`
2. **Set form_source:** `test-page-do-not-use`
3. **View locally:** http://localhost:1313/test-landing/
4. **Submit test form** with fake data
5. **Check JotForm submissions** for the `test-page-do-not-use` value
6. **Delete test submission** and test page when done

---

## Troubleshooting

### Hidden Field Not Capturing Source

**Problem:** Submissions show empty `page_source`

**Solution:**
1. Verify hidden field is configured for URL parameter `source`
2. Check the iframe URL includes `?source=something`
3. Make sure the field name matches in JotForm

### Source Shows Filename Instead of Custom Value

**Problem:** Getting `landing` instead of `summer-promo`

**Solution:** Add `form_source: "summer-promo"` to the page's front matter

### Form Not Displaying

**Problem:** Landing page shows but no form

**Solution:**
1. Check that `layout: "landing"` is set
2. Verify form ID `253585658329169` is correct
3. Clear browser cache and reload

---

## Summary

### Quick Checklist

- [x] JotForm has hidden field configured (do once)
- [ ] Create landing page with unique `form_source`
- [ ] Add video URL (optional)
- [ ] Write compelling content
- [ ] Test form submission
- [ ] Check JotForm for correct source tracking
- [ ] Deploy to staging
- [ ] Deploy to production

### Key Benefits

✅ **One form** to rule them all
✅ **Automatic tracking** - no manual work
✅ **Easy reporting** - filter by landing page
✅ **Scalable** - add unlimited landing pages

---

**Last Updated:** January 1, 2026
**Form ID:** 253585658329169
**Template:** `layouts/_default/landing.html`
