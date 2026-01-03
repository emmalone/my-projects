---
title: "JOTFORM_SETUP_GUIDE"
project: klm-migrate
original_path: docs/JOTFORM_SETUP_GUIDE.md
modified: 2025-12-25T10:07:38.040214
---

# JotForm Setup Guide for KLM Insurance Website

This guide provides detailed instructions for creating and integrating JotForm forms for the KLM Insurance website.

## Overview

You need to create **3 forms** in JotForm to replace the existing form placeholders:

1. **Quick Quote Form** - Simple quote request (homepage + contact page hero)
2. **Quick Contact Form** - Contact inquiry (contact page sidebar)
3. **Detailed Insurance Quote Form** - Comprehensive quote (compare-quotes page)

---

## Form 1: Quick Quote Form

**Purpose:** Fast lead capture on homepage and contact page hero section
**Current Location:** Homepage hero section, Contact page hero section

### Fields Required:

1. **Zip Code**
   - Field Type: Short Text Input
   - Label: "What zip code?"
   - Placeholder: "Zip Code"
   - Validation: Number only, exactly 5 digits
   - Required: Yes

2. **Type of Insurance**
   - Field Type: Dropdown
   - Label: "Type Of Insurance?"
   - Options:
     - "Select..." (default, non-selectable)
     - Auto Insurance
     - Home Insurance
     - Auto & Home
     - Commercial Insurance
     - Life Insurance
     - Umbrella Insurance
     - Boat/Watercraft
   - Required: Yes

3. **Submit Button**
   - Text: "QUOTE ME" (for homepage) or "QUOTE IT!" (for contact page)
   - Style: Primary button, blue/brand color

### JotForm Creation Steps:

1. Log in to your JotForm account at https://www.jotform.com
2. Click "Create Form" button
3. Select "Start From Scratch" or use "Classic Form" template
4. **Add Fields:**
   - Drag "Short Text" field onto form
     - Click field to edit
     - Set Label: "What zip code?"
     - Set Placeholder: "Zip Code"
     - Click "Properties" → "Validation" → Select "Number" → Set Min Length: 5, Max Length: 5
     - Check "Required"

   - Drag "Dropdown" field onto form
     - Click field to edit
     - Set Label: "Type Of Insurance?"
     - Add options (one per line):
       ```
       Select...
       Auto Insurance
       Home Insurance
       Auto & Home
       Commercial Insurance
       Life Insurance
       Umbrella Insurance
       Boat/Watercraft
       ```
     - Make "Select..." the default
     - Check "Required"

5. **Customize Form Settings:**
   - Click "Settings" tab (top right)
   - Under "Emails" → Add your email: sales@klminsurance.com
   - Set email subject: "New Quote Request from Website"
   - Under "Thank You Page" → Set custom message: "Thank you! We'll contact you shortly with your quote."

6. **Style the Form:**
   - Click "Form Designer" (paint palette icon)
   - Choose a style that matches your website colors
   - Adjust button text to "QUOTE ME"
   - Consider using transparent background for seamless integration

7. **Get Embed Code:**
   - Click "Publish" button (top right)
   - Select "Embed" option
   - Choose "iFrame" embed type
   - Copy the embed code (you'll need this later)
   - Save form and name it: "KLM Quick Quote Form"

---

## Form 2: Quick Contact Form

**Purpose:** Contact inquiry form on contact page sidebar
**Current Location:** Contact page sidebar

### Fields Required:

1. **Name**
   - Field Type: Full Name or Short Text
   - Label: "Name:*"
   - Required: Yes

2. **Zip Code**
   - Field Type: Short Text Input
   - Label: "Zip Code:*"
   - Validation: Number only, exactly 5 digits
   - Required: Yes

3. **Phone**
   - Field Type: Phone Number
   - Label: "Phone:*"
   - Validation: Phone number format
   - Required: Yes

4. **E-mail**
   - Field Type: Email
   - Label: "E-mail:*"
   - Validation: Email format
   - Required: Yes

5. **Submit Button**
   - Text: "SUBMIT"
   - Style: Primary button, blue/brand color

### JotForm Creation Steps:

1. In JotForm dashboard, click "Create Form"
2. Select "Start From Scratch"
3. **Add Fields:**
   - Drag "Full Name" field (or "Short Text")
     - Label: "Name:*"
     - Check "Required"

   - Drag "Short Text" field
     - Label: "Zip Code:*"
     - Properties → Validation → Number, Min: 5, Max: 5
     - Check "Required"

   - Drag "Phone Number" field
     - Label: "Phone:*"
     - Select US phone format
     - Check "Required"

   - Drag "Email" field
     - Label: "E-mail:*"
     - Email validation enabled by default
     - Check "Required"

4. **Configure Settings:**
   - Settings → Emails → Notification Email: sales@klminsurance.com
   - Subject: "New Contact Form Submission"
   - Thank You Page: "Thank you for contacting us! We'll respond within 24 hours."

5. **Style Form:**
   - Match website design
   - Button text: "SUBMIT"
   - Consider compact layout for sidebar

6. **Get Embed Code:**
   - Publish → Embed → iFrame
   - Copy embed code
   - Name form: "KLM Quick Contact Form"

---

## Form 3: Detailed Insurance Quote Form

**Purpose:** Comprehensive quote request to replace EZLynx integration
**Current Location:** Compare Quotes page (/compare-quotes/)

### Fields Required:

This is a more comprehensive form for detailed quote requests.

#### Section 1: Personal Information

1. **First Name**
   - Field Type: Short Text
   - Required: Yes

2. **Last Name**
   - Field Type: Short Text
   - Required: Yes

3. **Email Address**
   - Field Type: Email
   - Required: Yes

4. **Phone Number**
   - Field Type: Phone Number
   - Required: Yes

5. **Date of Birth**
   - Field Type: Date Picker
   - Required: Yes

#### Section 2: Address Information

6. **Street Address**
   - Field Type: Address (Full Address field)
   - OR use separate fields:
     - Street Address (Short Text)
     - City (Short Text)
     - State (Dropdown - US states)
     - Zip Code (Short Text with validation)
   - Required: Yes

#### Section 3: Insurance Type & Current Coverage

7. **Insurance Type Needed** (Multiple Select)
   - Field Type: Checkboxes
   - Label: "What type of insurance are you interested in?"
   - Options:
     - Auto Insurance
     - Home Insurance
     - Commercial Insurance
     - Life Insurance
     - Umbrella Insurance
     - Boat/Watercraft Insurance
   - Required: Yes (at least one)

8. **Currently Insured?**
   - Field Type: Yes/No (Radio buttons)
   - Label: "Do you currently have insurance?"
   - Required: Yes

9. **Current Insurance Company** (Conditional - shows if "Yes" above)
   - Field Type: Short Text
   - Label: "Current insurance company name"
   - Required: No

10. **Current Policy Expiration Date** (Conditional)
    - Field Type: Date Picker
    - Label: "When does your current policy expire?"
    - Required: No

#### Section 4: Auto Insurance Specific (Conditional)

Shows only if "Auto Insurance" is selected in question 7.

11. **Number of Vehicles**
    - Field Type: Number or Dropdown (1-10)
    - Required: Yes (if auto selected)

12. **Primary Vehicle Year**
    - Field Type: Dropdown (current year back 30 years)
    - Required: Yes (if auto selected)

13. **Primary Vehicle Make**
    - Field Type: Short Text or Dropdown (major makes)
    - Required: Yes (if auto selected)

14. **Primary Vehicle Model**
    - Field Type: Short Text
    - Required: Yes (if auto selected)

15. **Number of Drivers**
    - Field Type: Number or Dropdown (1-10)
    - Required: Yes (if auto selected)

#### Section 5: Home Insurance Specific (Conditional)

Shows only if "Home Insurance" is selected in question 7.

16. **Property Type**
    - Field Type: Dropdown
    - Options:
      - Single Family Home
      - Condo
      - Townhouse
      - Multi-Family
      - Mobile Home
    - Required: Yes (if home selected)

17. **Year Built**
    - Field Type: Number (4 digits)
    - Range: 1800-current year
    - Required: Yes (if home selected)

18. **Approximate Square Footage**
    - Field Type: Number
    - Required: No

19. **Estimated Home Value**
    - Field Type: Number or Currency
    - Label: "Estimated home value ($)"
    - Required: Yes (if home selected)

#### Section 6: Commercial Insurance Specific (Conditional)

Shows only if "Commercial Insurance" is selected.

20. **Business Name**
    - Field Type: Short Text
    - Required: Yes (if commercial selected)

21. **Business Type**
    - Field Type: Dropdown
    - Options:
      - Retail
      - Restaurant/Food Service
      - Professional Services
      - Construction
      - Manufacturing
      - Healthcare
      - Technology
      - Other
    - Required: Yes (if commercial selected)

22. **Number of Employees**
    - Field Type: Number or Dropdown
    - Options: 1-5, 6-10, 11-25, 26-50, 51-100, 100+
    - Required: Yes (if commercial selected)

23. **Annual Revenue**
    - Field Type: Dropdown
    - Options:
      - Under $100,000
      - $100,000 - $500,000
      - $500,000 - $1,000,000
      - $1,000,000 - $5,000,000
      - Over $5,000,000
    - Required: No

#### Section 7: Life Insurance Specific (Conditional)

Shows only if "Life Insurance" is selected.

24. **Coverage Amount Desired**
    - Field Type: Dropdown
    - Options:
      - $50,000 - $100,000
      - $100,000 - $250,000
      - $250,000 - $500,000
      - $500,000 - $1,000,000
      - Over $1,000,000
    - Required: Yes (if life selected)

25. **Health Status**
    - Field Type: Dropdown
    - Options:
      - Excellent
      - Good
      - Fair
      - Poor
    - Required: No

26. **Tobacco User?**
    - Field Type: Yes/No
    - Required: Yes (if life selected)

#### Section 8: Additional Information

27. **Additional Details**
    - Field Type: Long Text (Textarea)
    - Label: "Is there anything else you'd like us to know?"
    - Required: No
    - Placeholder: "Please provide any additional information..."

28. **Preferred Contact Method**
    - Field Type: Radio Buttons
    - Options:
      - Phone
      - Email
      - Text Message
    - Required: Yes

29. **Best Time to Contact**
    - Field Type: Dropdown
    - Options:
      - Morning (8am-12pm)
      - Afternoon (12pm-5pm)
      - Evening (5pm-8pm)
      - Anytime
    - Required: No

30. **Submit Button**
    - Text: "Get My Quote"
    - Style: Large, prominent button

### JotForm Creation Steps:

1. Create new form: "KLM Detailed Insurance Quote Form"
2. **Add all fields above in order**
3. **Use Form Sections** to organize (Personal Info, Address, Insurance Type, etc.)
4. **Set up Conditional Logic:**
   - Go to Settings → Conditions
   - Create "Show/Hide Field" conditions:
     - IF "Insurance Type Needed" contains "Auto Insurance" → SHOW auto-specific fields (11-15)
     - IF "Insurance Type Needed" contains "Home Insurance" → SHOW home-specific fields (16-19)
     - IF "Insurance Type Needed" contains "Commercial Insurance" → SHOW commercial fields (20-23)
     - IF "Insurance Type Needed" contains "Life Insurance" → SHOW life fields (24-26)
     - IF "Currently Insured?" = "Yes" → SHOW fields 9-10

5. **Configure Email Notifications:**
   - To: sales@klminsurance.com
   - Subject: "New Detailed Quote Request - {insurance_type}"
   - Include all form data in email

6. **Auto-responder Email:**
   - Enable auto-responder to customer's email
   - Subject: "Your KLM Insurance Quote Request"
   - Message: "Thank you for requesting a quote from KLM Insurance Solutions! We've received your information and one of our agents will contact you within 1 business day via your preferred contact method. If you need immediate assistance, please call us at 610-429-1330."

7. **Thank You Page:**
   - Custom message: "Thank you! Your quote request has been submitted. We'll contact you within 1 business day."
   - Consider adding redirect to thank-you page on your site

8. **Style the Form:**
   - Use professional, clean design
   - Match KLM brand colors
   - Ensure mobile-responsive
   - Use multi-page form (recommended) or single long form

9. **Get Embed Code:**
   - Publish → Embed → iFrame (or use direct link)
   - Copy embed code

---

## Getting Your JotForm Embed Codes

After creating each form, you'll need to get the embed code:

1. Open the form in JotForm editor
2. Click "Publish" button (top right corner)
3. Click "Embed" option
4. Select **"iFrame Embed"** (recommended for Hugo/static sites)
5. **Optional: Customize iframe settings:**
   - Adjust width/height as needed
   - Enable "Make the form transparent"
   - Enable "Add a border"

6. Copy the entire iframe code (looks like this):
   ```html
   <iframe
     id="JotFormIFrame-XXXXXXXXX"
     title="Form Title"
     src="https://form.jotform.com/XXXXXXXXX"
     frameborder="0"
     style="min-width:100%;max-width:100%;height:539px;border:none;"
     scrolling="no">
   </iframe>
   ```

7. **Save the embed code** - you'll need to provide these to integrate into the website

**Alternative Embed Methods:**
- **Direct Link:** Simple link that opens form in new page
- **Lightbox Popup:** Opens form in modal overlay
- **Full Page:** Form takes entire page

---

## Integration Instructions

Once you've created all 3 forms and have the embed codes, provide them in the following format:

```
Form 1 - Quick Quote Form:
[paste iframe code here]

Form 2 - Quick Contact Form:
[paste iframe code here]

Form 3 - Detailed Insurance Quote Form:
[paste iframe code here]
```

I will then update the Hugo template files to integrate these forms into your website.

---

## Files That Will Be Updated

After you provide the embed codes, I'll update these files:

1. **layouts/index.html** - Homepage quick quote form
2. **layouts/_default/contact.html** - Contact page forms (both quick quote and quick contact)
3. **layouts/_default/compare-quotes.html** - Detailed quote form (replaces EZLynx)

---

## JotForm Tips & Best Practices

### Security & GDPR Compliance
- Enable SSL/HTTPS (should be default)
- Add privacy policy link in form
- Consider adding GDPR consent checkbox if needed
- Enable CAPTCHA to prevent spam (Settings → Form Options → CAPTCHA)

### Form Settings to Configure
- **Limit Submissions:** Settings → Form Options → Limit (optional)
- **Email Notifications:** Configure multiple recipient emails if needed
- **Integrations:** Connect to CRM (if you use one) - JotForm integrates with many CRMs
- **Payment Processing:** Not needed for these forms, but available if needed later

### Testing Your Forms
Before going live:
1. Submit test entries for each form
2. Verify emails are received at sales@klminsurance.com
3. Check form data in JotForm dashboard
4. Test on mobile devices
5. Test conditional logic (detailed form)

### Form Management
- View submissions: JotForm Dashboard → Select Form → "Submissions"
- Export data: Submissions → Export (Excel, CSV, PDF)
- Set up email alerts for new submissions
- Review form analytics: Form → Analytics tab

---

## Next Steps

1. **Create the 3 forms** in JotForm following the instructions above
2. **Test each form** by submitting test data
3. **Copy the iframe embed codes** for each form
4. **Provide the embed codes** so I can update the website templates
5. **Review and test** the integrated forms on the Hugo development server

---

## Questions or Issues?

Common issues and solutions:

**Problem:** Form doesn't match website styling
**Solution:** Use JotForm Designer to customize colors, fonts, and spacing

**Problem:** Form too tall/short in iframe
**Solution:** Adjust height in iframe code or enable JotForm's auto-resize script

**Problem:** Conditional logic not working
**Solution:** Check Settings → Conditions, ensure field names match exactly

**Problem:** Not receiving notification emails
**Solution:** Check spam folder, verify email in Settings → Emails → Notification Email

**Problem:** Form not mobile-responsive
**Solution:** JotForm forms are responsive by default - ensure iframe width is 100%

---

## Estimated Time

- **Form 1 (Quick Quote):** 10-15 minutes
- **Form 2 (Quick Contact):** 10-15 minutes
- **Form 3 (Detailed Quote):** 30-45 minutes (due to conditional logic)
- **Total:** Approximately 1 hour for all 3 forms

---

**Ready to proceed?** Create the forms in JotForm and share the embed codes when ready!
