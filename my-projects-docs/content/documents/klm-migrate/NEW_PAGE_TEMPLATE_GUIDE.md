---
title: "NEW_PAGE_TEMPLATE_GUIDE"
project: klm-migrate
original_path: docs/NEW_PAGE_TEMPLATE_GUIDE.md
modified: 2025-12-22T10:23:51.820120
---

# KLM Insurance - New Page & Menu Template Guide

**Last Updated:** December 22, 2025

This guide explains how to create new pages and menu items in your KLM Insurance Hugo website.

---

## Table of Contents

1. [Creating a New Page](#creating-a-new-page)
2. [Adding to Navigation Menu](#adding-to-navigation-menu)
3. [Page Templates Available](#page-templates-available)
4. [Step-by-Step Examples](#step-by-step-examples)
5. [Troubleshooting](#troubleshooting)

---

## Creating a New Page

### Quick Start

1. **Create the content file** in `klm-hugo-site/content/`
2. **Add menu item** in `klm-hugo-site/hugo.toml`
3. **Run Hugo** to see your changes

### File Naming Convention

- Use lowercase
- Use hyphens (not spaces or underscores)
- End with `.md`
- Examples:
  - ✅ `boat-insurance.md`
  - ✅ `privacy-policy.md`
  - ✅ `claims-process.md`
  - ❌ `Boat Insurance.md`
  - ❌ `privacy_policy.md`

---

## Page Templates Available

### Template 1: Insurance Service Page
**Use for:** Auto, Home, Life, Commercial insurance pages

```markdown
---
title: "Page Title Here"
description: "SEO description for this page"
draft: false
---

## Main Heading

Introduction paragraph explaining the insurance type.

### Subheading 1

Content about this topic.

### Subheading 2

More content here.

#### Sub-subheading

Details and bullet points:

- Point one
- Point two
- Point three

### Get a Quote

Contact us today at **610-429-1330** for a free quote.
```

**Example File:** `content/auto-insurance.md`

---

### Template 2: Informational Page
**Use for:** About Us, Privacy Policy, Terms of Service

```markdown
---
title: "Page Title"
description: "Page description"
draft: false
---

## About Our Company

Introduction text here.

### Our Mission

Mission statement text.

### Our Values

List of values and explanations.

### Contact Information

**Address:** 1554 Paoli Pike, West Chester, PA 19380
**Phone:** 610-429-1330
**Email:** info@klminsurance.com
```

**Example File:** `content/about.md`

---

### Template 3: Contact/Form Page
**Use for:** Contact pages, quote request pages

```markdown
---
title: "Contact Us"
description: "Get in touch with KLM Insurance"
draft: false
---

## Get in Touch

We're here to help with all your insurance needs.

### Contact Information

**Phone:** [610-429-1330](tel:6104291330)
**Email:** [info@klminsurance.com](mailto:info@klminsurance.com)

### Office Location

KLM Insurance Solutions
1554 Paoli Pike
West Chester, PA 19380

### Office Hours

- Monday - Friday: 9:00 AM - 5:00 PM
- Saturday: By appointment
- Sunday: Closed

### Send Us a Message

<div class="contact-form-container">
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" class="contact-form">
  <div class="form-group">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" required>
  </div>

  <div class="form-group">
    <label for="email">Email</label>
    <input type="email" id="email" name="email" required>
  </div>

  <div class="form-group">
    <label for="message">Message</label>
    <textarea id="message" name="message" rows="5"></textarea>
  </div>

  <button type="submit" class="btn btn-primary">Send Message</button>
</form>
</div>
```

**Example File:** `content/contact.md`

---

## Adding to Navigation Menu

### Step 1: Edit hugo.toml

Open `klm-hugo-site/hugo.toml` and find the `[[menu.main]]` section.

### Step 2: Add Your Menu Item

```toml
[[menu.main]]
  name = "Display Name"    # What users see
  url = "/page-url/"       # URL path (must match filename)
  weight = 10              # Lower numbers appear first
```

### Example: Adding "Boat Insurance"

```toml
[[menu.main]]
  name = "Boat Insurance"
  url = "/boat-insurance/"
  weight = 8
```

### Menu Weight Guide

Current menu weights:
- Home: 1
- Auto Insurance: 2
- Home Insurance: 3
- Commercial: 4
- Life Insurance: 5
- About Us: 6
- Contact: 7

**Add new items between existing items by using decimals:**
- 3.5 would appear between "Home Insurance" and "Commercial"
- 7.5 would appear after "Contact"

---

## Step-by-Step Examples

### Example 1: Create "Boat Insurance" Page

**Step 1:** Create the content file

```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
```

Create `content/boat-insurance.md`:

```markdown
---
title: "Boat and Watercraft Insurance"
description: "Protect your boat or watercraft with comprehensive insurance coverage"
draft: false
---

## Boat and Watercraft Insurance in Pennsylvania

Protect your investment on the water with comprehensive boat and watercraft insurance from KLM Insurance Solutions.

### What We Cover

- Boats and yachts
- Personal watercraft (jet skis)
- Fishing boats
- Sailboats

### Coverage Options

#### Physical Damage
Covers damage to your boat from collisions, weather, theft, and vandalism.

#### Liability Protection
Protects you if you're responsible for injury or property damage while operating your watercraft.

#### Medical Payments
Covers medical expenses for you and your passengers.

### Get a Quote

Call us at **610-429-1330** for a free boat insurance quote.
```

**Step 2:** Add to menu in `hugo.toml`:

```toml
[[menu.main]]
  name = "Boat Insurance"
  url = "/boat-insurance/"
  weight = 4.5
```

**Step 3:** View your changes

```bash
hugo server -D
```

Open http://localhost:1313/boat-insurance/

---

### Example 2: Create "FAQ" Page

**Step 1:** Create `content/faq.md`:

```markdown
---
title: "Frequently Asked Questions"
description: "Common questions about KLM Insurance Services"
draft: false
---

## Frequently Asked Questions

### General Questions

#### What types of insurance do you offer?

We offer auto, home, commercial, life, umbrella, and boat/watercraft insurance.

#### Do you offer free quotes?

Yes! All quotes are free and come with no obligation.

#### How quickly can I get coverage?

Coverage can often start the same day you apply.

### About Our Agency

#### Are you an independent agent?

Yes, we're an independent insurance agency working with multiple carriers.

#### What areas do you serve?

We serve all of Pennsylvania, with our office in West Chester.

### Contact Us

**Can't find your answer?** Call us at 610-429-1330 or [contact us online](/contact/).
```

**Step 2:** Add to menu (in footer or as dropdown):

```toml
[[menu.main]]
  name = "FAQ"
  url = "/faq/"
  weight = 6.5
```

---

## Advanced: Creating Dropdown Menus

To create a dropdown menu (like "Insurance Services"):

### Step 1: Create Parent Menu Item

```toml
[[menu.main]]
  name = "Insurance Services"
  url = "/services/"
  weight = 2
```

### Step 2: Add Child Items

```toml
[[menu.main]]
  name = "Auto Insurance"
  url = "/auto-insurance/"
  parent = "Insurance Services"
  weight = 1

[[menu.main]]
  name = "Home Insurance"
  url = "/home-insurance/"
  parent = "Insurance Services"
  weight = 2
```

**Note:** Current theme uses simple navigation. For dropdowns, you may need to customize the header template.

---

## Page Front Matter Reference

Every page starts with "front matter" between `---` markers:

```markdown
---
title: "Page Title"          # Required - Appears in browser tab
description: "SEO description" # Recommended - For search engines
draft: false                  # Required - false = published, true = hidden
date: 2025-12-22             # Optional - Publication date
author: "KLM Insurance"       # Optional - Author name
tags: ["insurance", "pa"]     # Optional - For categorization
---
```

### Front Matter Fields

| Field | Required | Purpose | Example |
|-------|----------|---------|---------|
| `title` | Yes | Page title | "Auto Insurance" |
| `description` | Recommended | SEO meta description | "Get affordable auto insurance in PA" |
| `draft` | Yes | Publication status | `false` |
| `date` | No | Publication date | `2025-12-22` |
| `author` | No | Content author | "KLM Insurance" |
| `tags` | No | Content tags | `["auto", "insurance"]` |
| `categories` | No | Content categories | `["Services"]` |

---

## Content Formatting Guide

### Headings

```markdown
# H1 - Page Title (use once per page)
## H2 - Major sections
### H3 - Subsections
#### H4 - Minor subsections
```

### Text Formatting

```markdown
**Bold text**
*Italic text*
***Bold and italic***
`Code or technical term`
```

### Links

```markdown
[Link text](https://example.com)
[Internal link](/about/)
[Phone link](tel:6104291330)
[Email link](mailto:info@klminsurance.com)
```

### Lists

```markdown
Unordered list:
- Item one
- Item two
  - Nested item
  - Another nested item
- Item three

Ordered list:
1. First item
2. Second item
3. Third item
```

### Quotes

```markdown
> This is a blockquote
> It can span multiple lines
```

### Images

```markdown
![Alt text](/images/my-image.jpg)
```

**Note:** Images go in `static/images/` folder

---

## File Structure Summary

```
klm-hugo-site/
├── content/                  # Your pages go here
│   ├── _index.md            # Homepage
│   ├── auto-insurance.md    # Auto insurance page
│   ├── boat-insurance.md    # Boat insurance page
│   └── new-page.md          # Your new page
├── static/
│   └── images/              # Images for your pages
│       └── new-image.jpg
└── hugo.toml                # Site config & menus
```

---

## Quick Reference Commands

### Start Development Server
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo server -D
```

### Build for Production
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo --minify
```

### Create New Page (Alternative Method)
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo new content/page-name.md
```

---

## Troubleshooting

### Page Not Showing Up

**Check:**
1. Is `draft: false` in front matter?
2. Is the file in `content/` folder?
3. Does filename match URL in menu?
4. Did you restart Hugo server?

### Menu Item Not Appearing

**Check:**
1. Correct syntax in `hugo.toml`?
2. URL matches page filename?
3. Did you save `hugo.toml`?
4. Did Hugo rebuild (check terminal)?

### Broken Links

**Check:**
1. URLs start with `/` for internal links
2. URLs end with `/` for pages
3. File exists in `content/` folder
4. Filename matches exactly (case-sensitive)

### Images Not Loading

**Check:**
1. Image is in `static/images/` folder
2. Path in markdown: `/images/filename.jpg`
3. Filename is lowercase
4. File extension is correct (.jpg, .png, .gif)

---

## Best Practices

### ✅ DO

- Use descriptive, SEO-friendly filenames
- Include meta descriptions
- Keep URLs simple and clean
- Use heading hierarchy (H2, then H3, not H4 first)
- Add alt text to images
- Test pages before deploying

### ❌ DON'T

- Use spaces in filenames
- Skip the description field
- Create overly long URLs
- Use H1 tags in content (title is H1)
- Forget to set `draft: false`
- Leave broken links

---

## Getting Help

### Resources

- **Hugo Documentation:** https://gohugo.io/documentation/
- **Markdown Guide:** https://www.markdownguide.org/
- **Project README:** `/Users/mark/PycharmProjects/klm-migrate/README.md`

### Common Questions

**Q: How do I change the homepage?**
A: Edit `content/_index.md` or `layouts/index.html`

**Q: Can I use HTML in markdown files?**
A: Yes! Hugo's config has `unsafe = true` which allows HTML

**Q: How do I add a blog?**
A: Create `content/blog/` directory and add posts there

**Q: How do I change colors?**
A: Edit `static/css/style.css`

---

## Template Quick Copy

### New Insurance Service Page

```bash
# Copy this template and customize it

---
title: "Service Name Insurance"
description: "Description for SEO"
draft: false
---

## Service Name Insurance

Introduction paragraph.

### Why You Need This Coverage

Explanation of benefits.

### What We Cover

- Coverage point 1
- Coverage point 2
- Coverage point 3

### Get Your Free Quote

Contact KLM Insurance at **610-429-1330** today.
```

---

**Happy page creating! 🎉**

For questions or issues, refer to the main project README.md or Hugo documentation.
