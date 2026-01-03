---
title: "JOTFORM_EMAIL_SETUP_GUIDE"
project: klm-migrate
original_path: docs/JOTFORM_EMAIL_SETUP_GUIDE.md
modified: 2025-12-25T21:46:47.576737
---

# JotForm Email Notifications Setup Guide

## Overview

You need to configure email notifications for **2 forms** so you receive submissions at sales@klminsurance.com.

**Forms requiring setup:**
1. KLM Contact Form - Full (ID: 253585658329169) - Used on most pages
2. Detailed Insurance Quote Form (ID: 253584401906155) - Used on Compare Quotes page

**Estimated Time:** 10-15 minutes per form (20-30 minutes total)

---

## Form 1: KLM Contact Form - Full

### Step 1: Open Form Settings

1. Log in to JotForm: https://www.jotform.com
2. Click **"My Forms"** in the top menu
3. Find **"KLM Contact Form - Full"**
   - Or go directly to: https://www.jotform.com/build/253585658329169
4. Click the **"Settings"** button (gear icon at top right)

### Step 2: Configure Email Notifications

1. In the left sidebar, click **"Emails"**
2. You should see a section called **"Notification Emails"**

#### Add Notification Email:

3. Look for existing notification emails or click **"Add Email"** button
4. If there's an existing notification, click **"Edit"** (pencil icon)
5. Configure the following settings:

**Recipient Email:**
- Click the dropdown and select **"Type Custom Email"**
- Enter: `sales@klminsurance.com`
- Click **"Add"** or confirm

**Email Subject:**
- Clear the default subject line
- Enter: `New Contact Form Submission from Website`

**Reply To:**
- Select **"Email Address"** (field 3 from your form)
- This allows you to reply directly to the customer

**Sender Name:**
- Enter: `KLM Website Contact Form`
- Or: `KLM Insurance Website`

**Email Content:**
- JotForm will automatically include all form fields
- You can customize the email template if desired
- Default template shows all fields clearly

6. Click **"Save"** or **"Done"**

#### Optional - Add Multiple Recipients:

If you want submissions to go to multiple email addresses:

1. In the Recipient Email field, click **"Add"** again
2. Enter additional emails (e.g., info@klminsurance.com)
3. Repeat for each recipient

### Step 3: Configure Auto-Responder (Optional but Recommended)

This sends a confirmation email to the customer who submitted the form.

1. Still in the **Emails** section, scroll down to **"Autoresponder Email"**
2. Click **"Add Email"** or enable the autoresponder
3. Configure:

**Recipient:**
- Select **"Email Address"** (field 3 - the customer's email from the form)

**Email Subject:**
- Enter: `Thank you for contacting KLM Insurance Solutions`

**Sender Email:**
- Enter: `sales@klminsurance.com`

**Sender Name:**
- Enter: `KLM Insurance Solutions`

**Email Message:**
- Click **"Edit Email"** to customize the message
- Example message:

```
Thank you for contacting KLM Insurance Solutions!

We've received your message and one of our insurance specialists will respond to you within 24 hours.

If you need immediate assistance, please call us at:
Phone: 610-429-1330

Your submission details:
{all_fields}

Best regards,
KLM Insurance Solutions Team

1554 Paoli Pike
West Chester, PA 19380
www.klminsurance.com
```

4. Click **"Save"**

### Step 4: Test the Notification

1. Go back to **"My Forms"**
2. Click **"Preview"** on your form
3. Fill out and submit a test entry
4. Check your email at sales@klminsurance.com
5. You should receive:
   - Notification email (to sales@klminsurance.com)
   - Auto-responder (to the email you entered in the test)

**Important:** Check your spam/junk folder if you don't see the email!

---

## Form 2: Detailed Insurance Quote Form

### Step 1: Open Form Settings

1. In JotForm, go to **"My Forms"**
2. Find **"KLM Detailed Insurance Quote Form"**
   - Or go directly to: https://www.jotform.com/build/253584401906155
3. Click the **"Settings"** button (gear icon)

### Step 2: Configure Email Notifications

1. In the left sidebar, click **"Emails"**
2. Click **"Add Email"** in the Notification Emails section

**Recipient Email:**
- Select **"Type Custom Email"**
- Enter: `sales@klminsurance.com`

**Email Subject:**
- Enter: `New Detailed Insurance Quote Request`
- Or: `New Quote Request - {insuranceType}`
  - (This includes the insurance type from the form)

**Reply To:**
- Select **"Email Address"** (field 3 - email from the form)

**Sender Name:**
- Enter: `KLM Quote Request Form`

**Email Content:**
- Keep default (shows all 29 fields)
- Or customize to highlight important fields first

3. Click **"Save"**

### Step 3: Configure Auto-Responder (Recommended)

1. In **"Emails"** section, scroll to **"Autoresponder Email"**
2. Click **"Add Email"** or enable

**Recipient:**
- Select **"Email Address"** (field 3)

**Email Subject:**
- Enter: `Your KLM Insurance Quote Request`

**Sender Email:**
- Enter: `sales@klminsurance.com`

**Sender Name:**
- Enter: `KLM Insurance Solutions`

**Email Message:**
```
Thank you for requesting an insurance quote from KLM Insurance Solutions!

We've received your detailed quote request and one of our licensed insurance agents will review your information and contact you within 1 business day via your preferred contact method.

If you have immediate questions or need to speak with an agent right away, please call us:
Phone: 610-429-1330
Hours: Monday-Friday, 8:00 AM - 5:00 PM EST

Your quote request details:
{all_fields}

We look forward to helping you find the right insurance coverage!

Best regards,
KLM Insurance Solutions Team

1554 Paoli Pike
West Chester, PA 19380
Phone: 610-429-1330
Email: sales@klminsurance.com
www.klminsurance.com
```

3. Click **"Save"**

### Step 4: Test the Notification

1. Preview the form
2. Fill out with test data (you may want to select multiple insurance types to test conditional fields)
3. Submit
4. Check sales@klminsurance.com for notification
5. Check spam folder if needed

---

## Advanced Email Settings (Optional)

### Email Templates

You can customize how the email looks:

1. In **Emails** section, click **"Edit"** on your notification
2. Click **"Edit Email"** button
3. Choose from:
   - **Default Template** - Simple, clean list of fields
   - **Professional Template** - Formatted with your logo
   - **Custom HTML** - Full control over design

### Email Conditions

Send different emails based on form responses:

1. Go to **Settings** → **Conditions**
2. Click **"Add Condition"**
3. Example: Send to different people based on insurance type
   - IF insurance type = "Commercial"
   - THEN send email to commercial@klminsurance.com

### Email Attachments

If users upload files in your form:
- Attachments are automatically included in notification emails
- Or you can configure to send links instead of attachments

---

## Troubleshooting

### Not Receiving Emails?

**Check Spam/Junk Folder:**
- JotForm emails might be flagged as spam
- Add notifications@jotform.com to your contacts
- Whitelist JotForm's sending domain

**Verify Email Address:**
1. Go to form Settings → Emails
2. Confirm sales@klminsurance.com is entered correctly
3. Check for typos

**Check Email Limits:**
- JotForm Silver plan allows plenty of emails
- View your usage: Account → Usage

**Test with Different Email:**
- Try sending a test to your personal Gmail/Yahoo
- If that works, the issue is with klminsurance.com email server

### Emails Going to Spam?

**Add SPF Record (IT/Domain Admin):**
- Add JotForm to your domain's SPF record
- This tells email servers that JotForm is authorized to send on your behalf

**Use Your Own Email Server (Premium):**
- JotForm allows custom SMTP settings
- Send emails from your own mail server
- Settings → Emails → SMTP Settings

### Wrong Fields in Email?

**Customize Email Content:**
1. Edit notification email
2. Click "Edit Email"
3. Remove unwanted fields
4. Rearrange field order
5. Add custom text

---

## Email Notification Checklist

Use this to verify setup:

### Form 1: KLM Contact Form - Full (253585658329169)

- [ ] Notification email to sales@klminsurance.com configured
- [ ] Email subject: "New Contact Form Submission from Website"
- [ ] Reply-To set to customer's email field
- [ ] Auto-responder enabled (optional)
- [ ] Auto-responder message customized
- [ ] Test submission completed
- [ ] Received notification email
- [ ] Checked spam folder
- [ ] Auto-responder received (if configured)

### Form 2: Detailed Insurance Quote Form (253584401906155)

- [ ] Notification email to sales@klminsurance.com configured
- [ ] Email subject: "New Detailed Insurance Quote Request"
- [ ] Reply-To set to customer's email field
- [ ] Auto-responder enabled (optional)
- [ ] Auto-responder message customized
- [ ] Test submission completed
- [ ] Received notification email
- [ ] All 29 fields included in email
- [ ] Auto-responder received (if configured)

---

## Quick Links

**Form 1 - KLM Contact Form - Full:**
- Form Builder: https://www.jotform.com/build/253585658329169
- Settings: https://www.jotform.com/build/253585658329169 (click Settings gear)
- Submissions: https://www.jotform.com/submissions/253585658329169

**Form 2 - Detailed Insurance Quote Form:**
- Form Builder: https://www.jotform.com/build/253584401906155
- Settings: https://www.jotform.com/build/253584401906155 (click Settings gear)
- Submissions: https://www.jotform.com/submissions/253584401906155

**JotForm Resources:**
- Help: https://www.jotform.com/help/
- Email Settings Guide: https://www.jotform.com/help/14-how-to-setup-notification-emails
- Support: https://www.jotform.com/contact/

---

## Email Notification Example

Here's what the notification email will look like:

**Subject:** New Contact Form Submission from Website

**From:** KLM Website Contact Form (via JotForm)

**To:** sales@klminsurance.com

**Body:**
```
You have a new submission from KLM Contact Form - Full

First Name: John
Last Name: Smith
Email: john.smith@example.com
Phone: 610-555-1234
Comments: I'm interested in getting a quote for auto and home insurance bundle.

Submission Date: December 25, 2025 11:30 AM
IP Address: 192.168.1.1

View submission details: [View in JotForm]
```

---

## Next Steps After Email Setup

Once email notifications are configured:

1. ✅ Test both forms thoroughly
2. ✅ Verify emails arrive promptly
3. ✅ Check auto-responders work
4. ✅ Delete test submissions from JotForm
5. ✅ Set up conditional logic for Detailed Quote Form (if not done yet)
6. ✅ Train staff on how to view submissions in JotForm
7. ✅ Set up email filters/folders in Outlook/Gmail for organization

---

## Managing Email Notifications Long-Term

**View All Submissions:**
- Log in to JotForm
- My Forms → Select form → Submissions tab
- Export to Excel/CSV if needed

**Email Digest (Instead of Individual Emails):**
- Settings → Emails → Digest Emails
- Receive one summary email per day instead of individual notifications
- Good if you receive many submissions

**Email Forwarding:**
- Forward JotForm notification emails to other team members
- Set up rules in your email client

**Integration with CRM:**
- Connect JotForm to your CRM (if you use one)
- Salesforce, HubSpot, Zoho, etc.
- Settings → Integrations

---

**Total Setup Time:** 20-30 minutes for both forms
**Difficulty:** Easy - Just follow the steps above!

🎯 **Start here:** https://www.jotform.com (Log in → My Forms → Settings → Emails)
