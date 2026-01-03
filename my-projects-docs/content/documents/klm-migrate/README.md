---
title: "README"
project: klm-migrate
original_path: templates/README.md
modified: 2025-12-23T13:05:00.146473
---

# KLM Insurance Page Templates

**Professional templates for creating consistent product and service pages**

---

## 📁 Files in This Directory

| File | Purpose |
|------|---------|
| `product-service-template.md` | **Main template** - Copy this to create new pages |
| `HOW_TO_USE_TEMPLATE.md` | **Complete guide** - Step-by-step instructions |
| `example-motorcycle-insurance.md` | **Example 1** - Completed motorcycle insurance page |
| `example-renters-insurance.md` | **Example 2** - Completed renters insurance page |
| `README.md` | This file - Overview of templates |

---

## 🚀 Quick Start

**To create a new page:**

```bash
# 1. Copy the template
cp /Users/mark/PycharmProjects/klm-migrate/templates/product-service-template.md \
   /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content/your-product.md

# 2. Edit the file
nano /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content/your-product.md

# 3. Test locally
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo server -D --bind 0.0.0.0

# 4. View at http://localhost:1313/your-product/

# 5. Publish to staging
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py
```

---

## 📖 Using the Templates

### For First-Time Users

1. **Read:** `HOW_TO_USE_TEMPLATE.md` - Complete guide with everything you need
2. **Look at:** Example files to see completed pages
3. **Copy:** `product-service-template.md` to your content folder
4. **Edit:** Replace all `[placeholders]` with your content
5. **Test:** Run Hugo server locally to preview
6. **Publish:** Deploy to staging for review

### For Experienced Users

1. **Copy:** `product-service-template.md`
2. **Edit:** Update front matter and content
3. **Publish:** Deploy when ready

---

## 🎨 Template Features

✅ **Consistent Design**
- Matches existing auto, home, and life insurance pages
- Same layout and styling
- Professional appearance

✅ **SEO Optimized**
- Proper title and description tags
- Content structure for search engines
- Pennsylvania/location keywords included

✅ **Two Form Types**
- Simple form (zip + insurance type)
- Full form (name, email, phone, comments)

✅ **Flexible Structure**
- 2-3 main content sections
- Support for bullet lists
- Clear call-to-action

✅ **Easy to Customize**
- Clear placeholders to replace
- Examples to follow
- Instructions for each section

---

## 📝 What to Customize

### Required Changes

1. **Front Matter (YAML):**
   - Page title
   - Meta description
   - Sidebar image filename
   - Form type (simple or full)

2. **Content:**
   - Opening paragraph (hook)
   - Main section headings
   - Body paragraphs
   - Bullet lists (if applicable)
   - Closing call-to-action

### Optional Changes

3. **Hero Image:**
   - Default is fine for most pages
   - Can use custom hero if available

4. **Navigation:**
   - Add link in dropdown menu
   - See guide for instructions

---

## 💡 Content Guidelines

### Length
- **Total:** 300-600 words
- **Opening:** 50-75 words
- **Each section:** 100-150 words
- **Closing:** 40-60 words

### Style
- Conversational tone
- Customer-focused (use "you" and "your")
- Educational and helpful
- Include Pennsylvania/Greater Philadelphia

### Structure
- 2-3 main sections with ## headings
- Short paragraphs (3-5 sentences)
- Bullet lists where helpful (3-7 items)
- Strong opening hook
- Clear call-to-action at end

---

## 🔍 Examples Included

### Motorcycle Insurance (`example-motorcycle-insurance.md`)
- **Form type:** Simple (zip + insurance type)
- **Style:** Focused on unique motorcycle risks
- **Sections:** 3 main sections
- **Features:** Bullet list of coverage types
- **Good for:** Specialty vehicle insurance, niche products

### Renters Insurance (`example-renters-insurance.md`)
- **Form type:** Full (complete contact form)
- **Style:** Educational about common misconception
- **Sections:** 4 main sections
- **Features:** Benefits list, detailed explanations
- **Good for:** Products needing more explanation, complex offerings

---

## ✅ Pre-Publishing Checklist

Use this before deploying your new page:

- [ ] All `[placeholders]` replaced
- [ ] Title is descriptive and accurate
- [ ] Description includes "- KLM Insurance Solutions"
- [ ] Sidebar image exists in `/static/images/`
- [ ] Form type chosen (simple or full)
- [ ] Opening paragraph hooks the reader
- [ ] 2-3 clear section headings (##)
- [ ] Mentions Pennsylvania/Greater Philadelphia
- [ ] Includes bullet list if helpful
- [ ] Strong call-to-action at end
- [ ] Spelling and grammar checked
- [ ] Tested locally (http://localhost:1313)
- [ ] Mobile view checked (resize browser)
- [ ] No console errors in browser dev tools

---

## 🛠️ Common Tasks

### Add to Navigation Menu

Edit: `/Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/layouts/_default/baseof.html`

Find the INSURANCE SERVICES dropdown (around line 25) and add:

```html
<li><a href="/your-product/">Your Product Name</a></li>
```

### Create Sidebar Image

**Size:** 300×200 pixels
**Format:** PNG or JPG
**Naming:** `featured-[product-name]-thumbnail.png`
**Location:** `/Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/static/images/`

**Temporary:** Use `/images/content-banner.png` until you have custom image

### Change Form Type

In front matter:
```yaml
form_type: "simple"   # Zip + insurance type
# OR
form_type: "full"     # Name, email, phone, comments
```

---

## 📚 Additional Resources

- **Complete workflow:** `../PUBLISHING_WORKFLOW.md`
- **Quick commands:** `../QUICK_START.md`
- **Hugo docs:** https://gohugo.io/documentation/

---

## 🆘 Need Help?

1. **Check the guide:** `HOW_TO_USE_TEMPLATE.md` has detailed instructions
2. **Look at examples:** See how completed pages look
3. **Test locally first:** Always preview before publishing
4. **Ask questions:** Better to ask than to break something!

---

## 📦 Template Directory Structure

```
/Users/mark/PycharmProjects/klm-migrate/templates/
│
├── README.md                           # This file
├── HOW_TO_USE_TEMPLATE.md             # Complete guide
├── product-service-template.md         # Main template (copy this!)
├── example-motorcycle-insurance.md     # Example 1
└── example-renters-insurance.md        # Example 2
```

---

**Created:** December 23, 2025
**Version:** 1.0
**Maintained by:** KLM Insurance Development Team

**Happy page creating!** 🎉
