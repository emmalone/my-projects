---
title: "APPLY_CSS_MANUALLY"
project: klm-migrate
original_path: docs/APPLY_CSS_MANUALLY.md
modified: 2025-12-25T23:03:47.615280
---

# Apply CSS to JotForm Manually - FINAL FIX

## What I've Fixed

✅ **Submit button added** - Form now has all 6 elements (5 fields + submit button)
✅ **Website CSS fixed** - No more white padding around iframe
✅ **iframe height increased** - 750px to show all fields

## What YOU Need to Do

The JotForm API won't let me set custom CSS, so you must apply it manually in JotForm Designer.

---

## Step-by-Step Instructions

### 1. Open JotForm Form Designer

Go directly to this URL (you must be logged in):
```
https://www.jotform.com/build/253585658329169
```

### 2. Access Custom CSS Section

1. In Form Designer, look for the **"Design"** or **"Paint Palette"** icon in the top toolbar
2. Click **"Advanced Designer"** or **"Inject Custom CSS"**
3. You'll see a text box for entering CSS

### 3. Paste This CSS

**IMPORTANT:** Delete any existing CSS first, then paste ONLY this:

```css
/* Main form container - blue background, no borders, full width */
.form-all {
  background-color: #00A6CE !important;
  padding: 20px !important;
  border: none !important;
  box-shadow: none !important;
  margin: 0 !important;
  width: 100% !important;
  max-width: 100% !important;
}

/* Remove borders from all nested containers */
.form-section,
.form-header-group,
.formFooter,
li.form-line {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  margin-bottom: 15px !important;
  padding: 0 !important;
}

/* Hide form header */
.form-header {
  display: none !important;
}

/* Form body - transparent, no borders */
.form-body {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* Labels - white, uppercase, bold */
.form-label,
.form-label-top {
  color: #FFFFFF !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  font-size: 11px !important;
  letter-spacing: 0.5px !important;
  margin: 0 0 6px 0 !important;
  padding: 0 !important;
}

/* Input fields - white background */
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

/* Submit button - orange */
.form-submit-button {
  background-color: #FF6B35 !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 3px !important;
  padding: 14px 30px !important;
  font-size: 14px !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  cursor: pointer !important;
  width: 100% !important;
  margin-top: 10px !important;
}

.form-submit-button:hover {
  background-color: #E55A2B !important;
}

/* Button container - no extra styling */
.form-button-wrapper,
.form-submit-container {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  margin: 15px 0 0 0 !important;
}

/* Hide JotForm branding */
.poweredby {
  display: none !important;
}

/* Required asterisk - red */
.form-required {
  color: #FF0000 !important;
}
```

### 4. Save the Form

1. Click **"Update"** or **"Apply"**
2. Click **"Save"** at the top of Form Designer
3. Wait for "Saved" confirmation

### 5. Preview in JotForm

1. Click **"Preview"** button (eye icon)
2. You should see:
   - ✅ Blue background (#00A6CE)
   - ✅ NO white borders
   - ✅ All 5 fields visible (First Name at top)
   - ✅ White labels in UPPERCASE
   - ✅ White input boxes
   - ✅ Orange SUBMIT button at bottom

### 6. Check Your Website

1. Wait 30-60 seconds for JotForm CDN to update
2. **Hard refresh** your browser: `Cmd + Shift + R` (Mac) or `Ctrl + Shift + R` (Windows)
3. Check: http://localhost:1313/
4. Form should now display correctly with NO white borders and submit button visible

---

## Troubleshooting

### "I don't see the CSS text box"

- Make sure you clicked **"Advanced Designer"** or **"Inject Custom CSS"**
- Look for **"<> CSS"** icon in the designer toolbar
- Some accounts show it under **"Designer"** → **"Advanced"**

### "The CSS didn't work"

1. Make sure you **deleted all existing CSS** before pasting
2. Make sure you pasted the **entire CSS** block above
3. Make sure you clicked **"Save"** after applying
4. Wait 1-2 minutes for JotForm's CDN to update
5. **Hard refresh** your browser (Cmd+Shift+R or Ctrl+Shift+R)

### "Still seeing white borders"

- The white borders come from default JotForm theme
- The CSS above overrides all borders with `border: none !important`
- If still visible, you may need to reset the theme first:
  1. In Form Designer, click **"Themes"**
  2. Select **"Default"** or **"Blank"** theme
  3. Then apply the CSS above

---

## What Will Be Fixed

Once you apply this CSS:

✅ No white borders anywhere
✅ Single blue background (#00A6CE)
✅ All 5 input fields visible
✅ First Name field at the very top
✅ Orange submit button at the bottom
✅ Clean, professional appearance matching your screenshot

---

## Quick Reference

**Form ID:** 253585658329169
**Direct Link:** https://www.jotform.com/build/253585658329169
**What to do:** Paste CSS in Advanced Designer → Save → Hard refresh browser
**Time needed:** 2-3 minutes

---

Let me know once you've applied the CSS and I'll help verify everything looks correct!
