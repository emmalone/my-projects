---
title: "COMPACT_FORM_CSS"
project: klm-migrate
original_path: docs/COMPACT_FORM_CSS.md
modified: 2025-12-25T23:23:55.595050
---

# Compact Form CSS - Reduced Height

## Apply This Compact CSS in JotForm Designer

Go to: https://www.jotform.com/build/253585658329169

Click **"Advanced Designer"** → Delete all existing CSS → Paste this:

```css
/* Main form container - minimal padding */
.form-all {
  background-color: #00A6CE !important;
  padding: 10px 15px !important;
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
  margin-bottom: 8px !important;
  padding: 0 !important;
}

/* Hide form header */
.form-header {
  display: none !important;
}

/* Form body - transparent, no borders, no spacing */
.form-body {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* Labels - white, uppercase, bold, minimal spacing */
.form-label,
.form-label-top {
  color: #FFFFFF !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  font-size: 10px !important;
  letter-spacing: 0.3px !important;
  margin: 0 0 3px 0 !important;
  padding: 0 !important;
  line-height: 1 !important;
}

/* Input fields - white background, compact padding */
.form-textbox,
.form-textarea,
.form-dropdown,
input[type="text"],
input[type="email"],
input[type="tel"] {
  background-color: #FFFFFF !important;
  border: 1px solid #DDDDDD !important;
  border-radius: 3px !important;
  padding: 8px !important;
  font-size: 13px !important;
  color: #333333 !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

/* Textarea - smaller height */
.form-textarea {
  min-height: 50px !important;
  max-height: 50px !important;
  font-family: inherit !important;
  resize: none !important;
}

/* Submit button - orange, compact */
.form-submit-button {
  background-color: #FF6B35 !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 3px !important;
  padding: 10px 20px !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  cursor: pointer !important;
  width: 100% !important;
  margin-top: 5px !important;
}

.form-submit-button:hover {
  background-color: #E55A2B !important;
}

/* Button container - minimal spacing */
.form-button-wrapper,
.form-submit-container {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  margin: 8px 0 0 0 !important;
}

/* Hide JotForm branding */
.poweredby {
  display: none !important;
}

/* Required asterisk - RED */
.form-required {
  color: #FF0000 !important;
}

/* Phone field sublabels - minimal spacing */
.form-sub-label {
  font-size: 9px !important;
  margin-top: 2px !important;
}

/* Remove extra spacing from sublabel containers */
.form-sub-label-container {
  background: transparent !important;
  margin: 0 !important;
  padding: 0 !important;
}
```

**Click "Save"!**

---

## Key Reductions

| Element | Before | After |
|---------|--------|-------|
| Form padding | 20px | 10px 15px |
| Field spacing | 15px | 8px |
| Label font size | 11px | 10px |
| Label margin | 6px | 3px |
| Input padding | 10px | 8px |
| Input font size | 14px | 13px |
| Textarea height | 90px | 50px |
| Button padding | 14px 30px | 10px 20px |
| Button margin | 10px | 5px |

---

## Result

The form should now be significantly shorter and fit comfortably within the hero section without exceeding the hero image height.
