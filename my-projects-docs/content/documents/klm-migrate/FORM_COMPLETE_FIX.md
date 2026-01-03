---
title: "FORM_COMPLETE_FIX"
project: klm-migrate
original_path: docs/FORM_COMPLETE_FIX.md
modified: 2025-12-25T22:19:33.933212
---

# Complete Form Fix - Double Borders & Missing Fields

## Problems Identified

1. ❌ Two blue borders (different shades)
2. ❌ Top of form not visible (First Name field cut off)
3. ❌ Submit button missing

## Root Causes

- **Default JotForm theme** conflicting with custom CSS
- **iFrame height too short** (550px - needs 700-800px)
- **Multiple containers** creating nested borders

---

## ✅ COMPLETE FIX (Step-by-Step)

### Part 1: Reset JotForm Styling FIRST

Before applying any CSS, we need to reset the form to defaults:

1. Go to: https://www.jotform.com/build/253585658329169
2. Click **"Form Designer"** (paint palette icon)
3. Click **"Themes"** tab
4. Select **"Default"** or **"Blank"** theme (removes all styling)
5. Click **"Styles"** tab
6. Click **"Reset to Default"** if available
7. Go to **"Advanced Designer"**
8. **Delete ALL existing CSS** (clear the text box completely)
9. Click **"Save"**

Now the form is clean and ready for proper styling.

---

### Part 2: Apply This CLEAN CSS

After resetting, paste ONLY this CSS:

```css
/* Main form container - single blue background */
.form-all {
  background-color: #00A6CE !important;
  padding: 25px !important;
  border: none !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  margin: 0 !important;
}

/* Remove any extra containers that create double borders */
.form-section,
.form-header-group,
li.form-line {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

/* Hide form title/header if present */
.form-header {
  display: none !important;
}

/* Form body - no extra styling */
.form-body {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
}

/* Labels - white, uppercase, small */
.form-label,
.form-label-top {
  color: #FFFFFF !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  font-size: 11px !important;
  letter-spacing: 0.5px !important;
  margin-bottom: 6px !important;
}

/* Field spacing */
li.form-line {
  margin-bottom: 15px !important;
  padding: 0 !important;
}

/* All input fields - white */
.form-textbox,
.form-textarea,
.form-dropdown,
input[type="text"],
input[type="email"],
input[type="tel"] {
  background-color: #FFFFFF !important;
  border: 1px solid #DDDDDD !important;
  border-radius: 3px !important;
  padding: 10px !important;
  font-size: 14px !important;
  color: #333333 !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

/* Phone field special handling */
.form-sub-label-container {
  background: transparent !important;
}

/* Textarea */
.form-textarea {
  min-height: 90px !important;
  font-family: inherit !important;
}

/* Input focus */
input:focus,
textarea:focus,
select:focus {
  outline: none !important;
  border-color: #0088AA !important;
}

/* Submit button - orange, full width */
.form-submit-button {
  background-color: #FF6B35 !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 3px !important;
  padding: 14px 30px !important;
  font-size: 14px !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 1px !important;
  cursor: pointer !important;
  width: 100% !important;
  margin-top: 10px !important;
}

.form-submit-button:hover {
  background-color: #E55A2B !important;
}

/* Button container */
.form-submit-container {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  margin: 15px 0 0 0 !important;
}

/* Required asterisk - white */
.form-required {
  color: #FFFFFF !important;
}

/* Remove JotForm branding */
.form-pagebreak,
.poweredby {
  display: none !important;
}

/* Ensure everything is visible */
.form-line,
.form-input,
.form-input-wide {
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
}
```

**Save the form!**

---

### Part 3: Test in JotForm First

1. In Form Designer, click **"Preview"**
2. You should see:
   - ✅ Single blue background (no double borders)
   - ✅ All 5 fields visible (First Name at top)
   - ✅ White labels in uppercase
   - ✅ White input boxes
   - ✅ Orange SUBMIT button at bottom

If it doesn't look right in JotForm preview, the CSS isn't applied correctly.

---

## Part 4: Fix iFrame Heights on Website

The iframe is too short - that's why you can't see the top and bottom. I need to increase the heights:

