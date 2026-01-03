---
title: "JOTFORM_STYLING_STEPS"
project: klm-migrate
original_path: docs/JOTFORM_STYLING_STEPS.md
modified: 2025-12-25T22:06:57.832264
---

# JotForm Styling - Correct Steps

## ⚠️ IMPORTANT: Where to Apply the CSS

**DO NOT** add CSS to your website or use the JavaScript embed code!

The CSS needs to be applied **INSIDE JotForm** using their Form Designer tool.

Your website already has the correct iframe embeds - you just need to style the form in JotForm.

---

## ✅ Correct Process (Step-by-Step)

### Step 1: Open JotForm Form Designer

1. Go to: https://www.jotform.com
2. Log in with your account
3. Click **"My Forms"** at the top
4. Find **"KLM Contact Form - Full"** (ID: 253585658329169)
5. Hover over the form
6. Click the **"Form Designer"** button (it's a paint palette icon)
   - NOT the "Edit" button
   - NOT the "Settings" button
   - The **"Form Designer"** button specifically

### Step 2: Access Custom CSS Section

1. Once in Form Designer, look at the top toolbar
2. Click the **"<> Advanced Designer"** button
   - Or look for **"Inject Custom CSS"** in the designer menu
3. You should see a text box for entering custom CSS

### Step 3: Paste the CSS Code

Copy and paste this CSS into the Custom CSS box:

```css
/* Form container - blue/cyan background */
.form-all {
  background-color: #00A6CE !important;
  padding: 30px !important;
  border-radius: 5px;
}

/* Labels - white, uppercase, bold */
.form-label {
  color: #FFFFFF !important;
  font-weight: bold !important;
  text-transform: uppercase !important;
  font-size: 12px !important;
  margin-bottom: 8px !important;
}

/* Input fields - white background */
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

/* Input focus state */
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

/* Submit button hover effect */
.form-submit-button:hover {
  background-color: #E55A2B !important;
}

/* Required asterisk - white */
.form-required {
  color: #FFFFFF !important;
}

/* Spacing between fields */
.form-line {
  margin-bottom: 15px !important;
}

/* Form header (if you have one) */
.form-header {
  color: #FFFFFF !important;
}

/* Remove default JotForm branding space */
.form-pagebreak {
  display: none !important;
}
```

### Step 4: Save the Styling

1. Click **"Update"** or **"Apply"** button in the Form Designer
2. Close the Custom CSS window
3. Click **"Save"** or **"Publish"** at the top of Form Designer

### Step 5: Preview Your Styled Form

1. In Form Designer, click the **"Preview"** button (eye icon)
2. Or click **"Open Form"** to see it in a new tab
3. Check that the form now has:
   - ✓ Blue/cyan background
   - ✓ White labels in uppercase
   - ✓ White input fields
   - ✓ Orange submit button

### Step 6: Check on Your Website

1. Go to your website: http://localhost:1313/
2. The form should automatically show the new styling
3. **If it doesn't update:**
   - Clear your browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
   - Hard refresh the page (Ctrl+Shift+R or Cmd+Shift+R)
   - Wait 1-2 minutes for JotForm's CDN to update

---

## 🚫 What NOT to Do

### ❌ Don't Use JavaScript Embed Code

This code you mentioned:
```html
<script type="text/javascript" src="https://form.jotform.com/jsform/253585658329169"></script>
```

**Don't add this to your website!**

Your website already has the correct iframe embeds in place. We configured them earlier.

### ❌ Don't Add CSS to Your Website

The CSS should NOT go in your Hugo templates or website files. It goes INSIDE JotForm's Form Designer.

### ✅ Keep the Existing iFrame Embeds

Your website already has this (which is correct):
```html
<iframe
  id="JotFormIFrame-253585658329169-home"
  title="Request Quote Form"
  src="https://form.jotform.com/253585658329169"
  ...>
</iframe>
```

This is perfect - don't change it!

---

## 📸 Visual Guide to Finding Form Designer

1. **Login Screen:** https://www.jotform.com
2. **My Forms:** Shows list of all your forms
3. **Form Actions:** When you hover over a form, you'll see buttons
4. **Form Designer Button:** Looks like a paint palette 🎨
5. **Advanced Designer:** Inside Form Designer, click this for CSS

---

## 🔧 Alternative: Use Form Designer Visual Tools

If you don't want to use custom CSS, you can style visually:

### Method 1: Use the Visual Designer

1. Open Form Designer
2. Click **"Themes"** tab
3. Browse available themes
4. Find one close to the screenshot colors
5. Apply it
6. Then click **"Styles"** tab to fine-tune:
   - Form Background Color → `#00A6CE`
   - Question Text Color → `#FFFFFF`
   - Button Background → `#FF6B35`

### Method 2: Manual Color Picker

1. In Form Designer, click **"Styles"** tab
2. You'll see color pickers for:
   - Form Background
   - Question (label) Color
   - Text Color
   - Button Background
   - Button Text
3. Click each color picker and enter hex codes:
   - Form Background: `#00A6CE`
   - Question Color: `#FFFFFF`
   - Button Background: `#FF6B35`
   - Button Text: `#FFFFFF`

---

## ✅ Verification Checklist

After applying CSS in JotForm:

- [ ] Logged into JotForm.com
- [ ] Opened "KLM Contact Form - Full"
- [ ] Clicked "Form Designer" (paint palette icon)
- [ ] Clicked "Advanced Designer" or "Inject Custom CSS"
- [ ] Pasted the CSS code from Step 3
- [ ] Clicked "Update" and "Save"
- [ ] Previewed form in JotForm (looks correct)
- [ ] Checked form on website: http://localhost:1313/
- [ ] Cleared browser cache if needed
- [ ] Form shows blue background, white labels, orange button

---

## 🆘 Troubleshooting

### "I don't see the Form Designer button"

- Make sure you're logged into JotForm
- Hover over the form name in "My Forms"
- Look for a paint palette icon 🎨
- Or click the three dots menu → "Design Form"

### "I can't find the Custom CSS option"

- In Form Designer, look for "Advanced Designer"
- Or look in the left sidebar for "Inject Custom CSS"
- Some accounts may say "Add CSS" or "Custom CSS"

### "The styling isn't showing on my website"

1. **Clear browser cache:**
   - Chrome: Ctrl+Shift+Delete (Windows) or Cmd+Shift+Delete (Mac)
   - Check "Cached images and files"
   - Clear

2. **Hard refresh:**
   - Windows: Ctrl+Shift+R
   - Mac: Cmd+Shift+R

3. **Wait a moment:**
   - JotForm's CDN may take 1-2 minutes to update

4. **Check in incognito/private mode:**
   - This bypasses cache completely

### "The form looks different in JotForm preview vs. website"

- This is normal - the iframe may have different dimensions
- The colors and styling should still match
- Adjust iframe height in your templates if needed

---

## 📱 Next Steps

1. ✅ Apply CSS in JotForm Form Designer (follow Step 1-6 above)
2. ✅ Preview in JotForm to verify
3. ✅ Check on website: http://localhost:1313/
4. ✅ Clear cache if needed
5. ✅ Test form submission to ensure it still works

---

## 🔗 Quick Links

**Form Designer Direct Link:**
https://www.jotform.com/build/253585658329169

**After logging in:**
1. Click "My Forms"
2. Find "KLM Contact Form - Full"
3. Click Form Designer (paint palette icon)
4. Click Advanced Designer
5. Paste CSS
6. Save

---

## 💡 Remember

- ✅ CSS goes **INSIDE JotForm** (Form Designer → Advanced Designer)
- ✅ Keep iframe embed on your website (already configured)
- ❌ Don't use JavaScript embed code
- ❌ Don't add CSS to your Hugo website files

The iframe will automatically display whatever styling you apply in JotForm!
