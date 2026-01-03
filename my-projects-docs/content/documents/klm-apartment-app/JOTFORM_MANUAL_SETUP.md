---
title: "JOTFORM_MANUAL_SETUP"
project: klm-apartment-app
original_path: output/jotform/JOTFORM_MANUAL_SETUP.md
modified: 2026-01-02T23:55:25.429608
---

# JotForm Manual Setup Guide

## Overview

Due to API limitations with programmatically creating JotForm forms with many questions, we've provided multiple alternatives for collecting the missing insurance application data.

## Option 1: Use the Standalone HTML Form (Recommended)

**File:** `output/jotform/missing_fields_form.html`

### Features:
- ✅ 88 missing fields organized by category
- ✅ Auto-saves progress to browser localStorage
- ✅ Downloads data as JSON on submit
- ✅ Responsive design (works on desktop and mobile)
- ✅ Shows which forms require each field
- ✅ Professional styling matching KLM branding

### How to Use:

1. **Live Form (DEPLOYED):**

   **🔗 https://dev-kaa.s3.us-east-1.amazonaws.com/forms/missing-fields.html**

   The form is live and ready to use! Access it from any device.

   *Note: Use HTTPS for secure access. HTTP-only alternative: http://dev-kaa.s3-website-us-east-1.amazonaws.com/forms/missing-fields.html*

2. **Local Testing:**
   ```bash
   open output/jotform/missing_fields_form.html
   ```

3. **Redeploy Updates:**
   ```bash
   aws s3 cp output/jotform/missing_fields_form.html s3://dev-kaa/forms/missing-fields.html --content-type "text/html"
   ```

3. **Customize Submission:**
   - Edit the JavaScript `submit` handler to send data to your backend
   - Current version downloads data as JSON file
   - Can easily integrate with FastAPI backend when ready

## Option 2: Manually Create JotForm

If you prefer to use JotForm's platform directly:

### Step 1: Start from Clone

We've already cloned a working form:
- **Form ID:** 260019147305045
- **Edit URL:** https://www.jotform.com/build/260019147305045
- **Public URL:** https://form.jotform.com/260019147305045

### Step 2: Add Fields Using JotForm Builder

Use the checklist: `missing_fields_checklist.md`

**Categories to Add (88 fields total):**

1. **Fire Safety** (11 fields)
   - Are fire extinguishers in all units and common areas
   - CO Detectors in all units
   - Emergency Lighting
   - Enclosed 2 Hour Fire Rated Stairways
   - Fire Alarm
   - Illuminated Exit Signs with Battery Backup
   - Means of Egress: Two Means of Egress from all units
   - Self-Closing Doors in Stairways
   - Smoke Detectors: Location
   - Sprinkler System
   - Type

2. **Applicant Info** (7 fields)
   - Applicant's Name
   - BUSINESS PHONE #
   - Entity Type
   - FEIN OR SOC SEC #
   - Mailing Address
   - NAME (First Named Insured) AND MAILING ADDRESS
   - Phone #

3. **Property Type** (7 fields)
   - Affordable/Subsidized Housing
   - Assisted Living
   - Boarding House
   - Seasonal Property
   - Senior Independent Living
   - Short Term Occupancies
   - Student Housing

4. **Building Info** (6 fields)
   - # Stories
   - # Units
   - Construction Type
   - Is the building listed on the National Register of Historic Places
   - Square Footage
   - Year Built

... and 25 more categories (see checklist for complete list)

### Step 3: Configure Form Settings

1. **Title:** "KAA Insurance Application - Missing Information"
2. **Thank You Message:** "Thank you! Your information has been received. We will use this data to complete your insurance applications."
3. **Notifications:** Send to mmalone@klminsurance.com
4. **Styling:** Apply KLM brand colors (#00A6CE, #FF6B35)

### Step 4: Test Submission

1. Fill out a test submission
2. Verify email notification works
3. Check submission appears in JotForm tables

## Option 3: Import to JotForm via CSV

### Step 1: Create CSV Template

We can generate a CSV file that JotForm might support for bulk import:

```bash
python3 scripts/export_fields_to_csv.py
```

### Step 2: Import in JotForm

1. Go to https://www.jotform.com/build/260019147305045
2. Look for "Import" or "Add Multiple Questions" option
3. Upload the CSV file

*Note: JotForm's import functionality may be limited depending on account type*

## Reference Files

- **`missing_fields_jotform.json`** - Complete field definitions in JotForm API format
- **`missing_fields_checklist.md`** - Human-readable checklist of all fields
- **`missing_fields_form.html`** - Standalone HTML form (ready to use)
- **`jotform_info.json`** - Form IDs and URLs

## Next Steps After Data Collection

Once you've collected the missing data (via HTML form or JotForm):

1. **Extract the data** from submissions
2. **Populate the database:**
   ```bash
   python3 scripts/populate_data_points.py submission_data.json
   ```
3. **Generate completed PDFs:**
   ```bash
   python3 scripts/generate_completed_forms.py
   ```

## Troubleshooting

### JotForm API Errors
- The JotForm API returns 500 errors when trying to add questions programmatically
- This appears to be a limitation of how forms can be created via API
- **Solution:** Use the standalone HTML form or manually create the form

### Form Too Long
- 88 fields is quite long for a single form
- **Solution:** Consider breaking into multiple shorter forms by category
- **Alternative:** Use the HTML form which organizes fields by collapsible categories

### Mobile Experience
- The HTML form is fully responsive
- JotForm's mobile app can be used for JotForm-based submissions
- Both work well on iPhone/iPad

## Support

For questions or issues:
- **Developer:** mark@emm-associates.com
- **Company:** KLM Insurance Solutions, Inc.
- **Phone:** 610-429-1330

---

**Last Updated:** January 2, 2026
