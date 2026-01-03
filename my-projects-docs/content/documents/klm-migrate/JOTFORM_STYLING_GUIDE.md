---
title: "JOTFORM_STYLING_GUIDE"
project: klm-migrate
original_path: docs/JOTFORM_STYLING_GUIDE.md
modified: 2025-12-25T21:44:06.658436
---

# JotForm Styling Guide - Match Screenshot

## ✅ Basic Styling Applied via API

I've already applied these colors to your form (253585658329169):
- **Form Background:** #00A6CE (Blue/Cyan)
- **Label Text:** #FFFFFF (White)
- **Input Fields:** #FFFFFF (White background)
- **Submit Button:** #FF6B35 (Orange/Coral)
- **Button Text:** #FFFFFF (White)

---

## Manual Fine-Tuning Required

Some styling options require manual configuration in the JotForm Form Designer. Follow these steps:

### Step 1: Open Form Designer

1. Log in to JotForm: https://www.jotform.com
2. Go to "My Forms"
3. Find "KLM Contact Form - Full" (ID: 253585658329169)
4. Click the **"Form Designer"** button (paint palette icon)

---

### Step 2: Apply Form Styling

#### Form Background & Container

1. In Form Designer, select **"Styles"** tab
2. Under **"Form Background"**:
   - Color: `#00A6CE` (blue/cyan) - Already set ✓
   - Or use color picker to match screenshot exactly

3. Under **"Form Padding"**:
   - Set to `20px` or `30px` for proper spacing

#### Font Settings

1. Under **"Font Family"**:
   - Select a clean sans-serif font (Arial, Helvetica, or Roboto)

2. Under **"Question Text"** (Labels):
   - Color: `#FFFFFF` (white) - Already set ✓
   - Font Size: `12px` or `14px`
   - Font Weight: **Bold**
   - Text Transform: **UPPERCASE** (important!)

#### Input Fields

1. Under **"Text Fields"**:
   - Background Color: `#FFFFFF` (white) - Already set ✓
   - Border: `1px solid #CCCCCC` (light gray)
   - Border Radius: `3px` or `4px` (slightly rounded)
   - Padding: `10px` (inside spacing)
   - Font Color: `#333333` (dark gray for typed text)

2. Under **"Textarea"** (Comments field):
   - Same settings as text fields above

#### Submit Button

1. Under **"Submit Button"**:
   - Background Color: `#FF6B35` (orange/coral) - Already set ✓
   - Text Color: `#FFFFFF` (white) - Already set ✓
   - Text: `SUBMIT` (uppercase) - Already set ✓
   - Font Size: `16px` or `18px` (large, readable)
   - Font Weight: **Bold**
   - Padding: `12px 30px` (vertical horizontal)
   - Border Radius: `3px` or `4px`
   - Border: None or `1px solid #FF6B35`

2. **Hover State** (optional):
   - Hover Background: `#E55A2B` (darker orange)

---

### Step 3: Advanced Customization (Optional)

If you want pixel-perfect matching to the screenshot:

#### Using Custom CSS

1. In Form Designer, click **"Advanced Designer"**
2. Find the **"Inject Custom CSS"** section
3. Add this CSS:

```css
/* Form container */
.form-all {
  background-color: #00A6CE !important;
  padding: 30px !important;
  border-radius: 5px;
}

/* Labels - uppercase and white */
.form-label {
  color: #FFFFFF !important;
  font-weight: bold !important;
  text-transform: uppercase !important;
  font-size: 12px !important;
  margin-bottom: 8px !important;
}

/* Input fields - white with subtle border */
.form-textbox,
.form-textarea,
.form-dropdown {
  background-color: #FFFFFF !important;
  border: 1px solid #DDDDDD !important;
  border-radius: 4px !important;
  padding: 10px !important;
  font-size: 14px !important;
  color: #333333 !important;
  width: 100% !important;
}

/* Remove focus outline, add custom */
.form-textbox:focus,
.form-textarea:focus {
  outline: none !important;
  border-color: #0088AA !important;
}

/* Submit button - orange/coral */
.form-submit-button {
  background-color: #FF6B35 !important;
  color: #FFFFFF !important;
  border: none !important;
  border-radius: 4px !important;
  padding: 12px 40px !important;
  font-size: 16px !important;
  font-weight: bold !important;
  text-transform: uppercase !important;
  cursor: pointer !important;
  width: 100% !important;
}

/* Submit button hover */
.form-submit-button:hover {
  background-color: #E55A2B !important;
}

/* Required asterisk */
.form-required {
  color: #FFFFFF !important;
}

/* Spacing between fields */
.form-line {
  margin-bottom: 15px !important;
}
```

4. Click **"Update"** or **"Save"**

---

### Step 4: Preview and Test

1. Click **"Preview"** button in Form Designer
2. Check that form matches screenshot:
   - ✓ Blue/cyan background
   - ✓ White labels in uppercase
   - ✓ White input fields
   - ✓ Orange submit button
   - ✓ Proper spacing

3. Test form submission to ensure it still works

---

## Color Reference from Screenshot

Use these exact colors for perfect matching:

| Element | Color Code | Description |
|---------|------------|-------------|
| Form Background | `#00A6CE` | Blue/Cyan |
| Label Text | `#FFFFFF` | White |
| Input Background | `#FFFFFF` | White |
| Input Border | `#DDDDDD` | Light Gray |
| Input Text | `#333333` | Dark Gray |
| Submit Button | `#FF6B35` | Orange/Coral |
| Button Text | `#FFFFFF` | White |
| Button Hover | `#E55A2B` | Darker Orange |

---

## Screenshot Comparison

### Current Form (Before Custom CSS):
- Basic colors applied ✓
- May need spacing adjustments
- Labels may not be uppercase
- Button may need sizing

### Target (Screenshot):
- Blue/cyan container ✓
- White uppercase labels ✓
- White input boxes ✓
- Orange submit button (full width) ✓
- Clean, professional appearance ✓

---

## Alternative: Use JotForm Themes

If custom CSS is complex, try using a JotForm theme:

1. In Form Designer, click **"Themes"**
2. Browse available themes
3. Look for themes with:
   - Dark or colored backgrounds
   - Light input fields
   - Prominent buttons
4. Apply theme and customize colors to match

---

## Testing Checklist

After styling, verify:

- [ ] Form background is blue/cyan (#00A6CE)
- [ ] All labels are white and uppercase
- [ ] Input fields have white background
- [ ] Input fields have subtle gray border
- [ ] Textarea (Comments) matches input styling
- [ ] Submit button is orange/coral (#FF6B35)
- [ ] Submit button text is white and uppercase
- [ ] Submit button is full width or properly sized
- [ ] Spacing between fields looks good
- [ ] Form works on mobile devices
- [ ] Form submission still works

---

## Quick Link

**Direct link to Form Designer:**
https://www.jotform.com/build/253585658329169

Click "Form Designer" (paint palette icon) to start styling.

---

## Troubleshooting

### Form doesn't look right on website
- **Solution:** Clear browser cache or hard refresh (Ctrl+Shift+R / Cmd+Shift+R)
- **Cause:** JotForm may cache old styling

### Colors don't match exactly
- **Solution:** Use Custom CSS (see Step 3 above)
- **Cause:** JotForm default styles may override

### Labels not uppercase
- **Solution:** Add CSS: `text-transform: uppercase !important;`
- **Or:** Manually edit each label to be uppercase in form builder

### Button too small/large
- **Solution:** Adjust padding in Custom CSS or Form Designer
- **Recommended:** `padding: 12px 40px;` or full width: `width: 100%;`

---

## Notes

- Basic colors have been applied via API ✓
- Fine-tuning requires Form Designer access
- Custom CSS provides pixel-perfect control
- Changes reflect immediately on your website
- No need to rebuild Hugo site (JotForm updates live)

---

**Next Steps:**
1. Open Form Designer: https://www.jotform.com/build/253585658329169
2. Apply Custom CSS from Step 3
3. Preview form
4. Check form on website: http://localhost:1313/
5. Adjust as needed

The form will automatically update on all pages where it's embedded!
