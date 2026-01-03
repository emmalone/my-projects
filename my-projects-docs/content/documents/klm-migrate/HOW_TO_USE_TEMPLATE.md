---
title: "HOW_TO_USE_TEMPLATE"
project: klm-migrate
original_path: templates/HOW_TO_USE_TEMPLATE.md
modified: 2025-12-23T13:03:31.174727
---

# How to Create a New Product/Service Page

**Complete guide for using the KLM Insurance product/service template**

---

## Quick Start

1. **Copy the template:**
   ```bash
   cp /Users/mark/PycharmProjects/klm-migrate/templates/product-service-template.md \
      /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content/your-product-name.md
   ```

2. **Edit the file** - Replace all `[placeholders]` with your content

3. **Test locally:**
   ```bash
   cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
   hugo server -D --bind 0.0.0.0
   ```

4. **View at:** http://localhost:1313/your-product-name/

5. **Publish when ready:**
   ```bash
   cd /Users/mark/PycharmProjects/klm-migrate
   python3 publish_to_staging.py
   ```

---

## Template Sections Explained

### Front Matter (YAML Header)

```yaml
---
title: "[Product/Service Name]"
description: "[Product/Service Name] - KLM Insurance Solutions"
draft: false
hero_image: "/images/featured-banner.png"
sidebar_image: "/images/featured-[product-name]-thumbnail.png"
form_type: "full"
---
```

**What to change:**

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Page title, appears in browser tab and as H1 | `"Motorcycle Insurance"` |
| `description` | SEO meta description | `"Motorcycle Insurance - KLM Insurance Solutions"` |
| `draft` | Set to `false` to publish, `true` to hide | `false` |
| `hero_image` | Main hero background image | Usually keep: `"/images/featured-banner.png"` |
| `sidebar_image` | Small thumbnail in sidebar | `"/images/featured-motorcycle-thumbnail.png"` |
| `form_type` | Type of contact form | `"simple"` or `"full"` (see below) |

**Choosing Form Type:**

- **`form_type: "simple"`** - Quick quote form with just:
  - Zip code
  - Insurance type dropdown
  - Best for: Auto, Home, General insurance pages

- **`form_type: "full"`** - Complete contact form with:
  - First name / Last name
  - Email
  - Phone
  - Comments field
  - Best for: Life, Commercial, Complex products

---

## Content Structure

### 1. Opening Paragraph (Hook)

**Purpose:** Grab attention and establish relevance

**Formula:**
- Start with a question or statement about customer needs
- Explain why they might need this product/service
- Mention KLM Insurance Solutions
- Keep it 2-3 sentences

**Examples:**

**Good:**
```markdown
Owning a motorcycle offers freedom and excitement, but it also comes with
unique risks. Whether you ride a cruiser, sport bike, or touring motorcycle,
having the right insurance coverage is essential. KLM Insurance Solutions Inc.
specializes in motorcycle insurance that protects both you and your bike.
```

**Bad (too generic):**
```markdown
We offer insurance. Call us today.
```

---

### 2. Main Heading (##)

**Purpose:** Introduce the primary benefit or topic

**Formula:**
- Focus on customer benefit, not just product name
- Use action-oriented language
- Keep it clear and specific

**Examples:**
- `## Find the Right Auto Insurance Protection`
- `## Protect Your Business with Commercial Coverage`
- `## Understanding Your Motorcycle Insurance Options`
- `## Get Comprehensive Coverage for Your Home`

**Not:**
- `## About This Product`
- `## Information`

---

### 3. Main Content Section

**Purpose:** Explain the value proposition in detail

**Formula:**
- 2-4 paragraphs
- Explain what problems this solves
- Mention coverage options or features
- Address common customer concerns
- Reference Pennsylvania/Greater Philadelphia region

**Example:**
```markdown
## Find the Right Auto Insurance Protection

We are proudly serving the insurance needs of customers just like you
in the Greater Philadelphia region and across the state of Pennsylvania.
We can help potential clients discover what their individual needs are
currently and even help them make any changes to the policy as their
needs change along the way.

Additionally, we can help you get the right coverage to meet financing
requirements so you can drive away from the dealership or car lot with
confidence knowing you're fully protected.
```

---

### 4. Secondary Heading (##)

**Purpose:** Provide additional important information

**Formula:**
- Address another key benefit or consideration
- Explain types/options available
- Provide helpful details

**Examples:**
- `## Types of Life Insurance`
- `## What's Covered Under Homeowners Insurance`
- `## A Commitment to Service`
- `## How to Find the Right Policy`

---

### 5. Secondary Content Section

**Purpose:** Give detailed information and specifics

**Formula:**
- 2-3 paragraphs OR
- Bullet list with explanation

**Using Bullet Lists:**

**When to use:**
- Listing coverage items
- Showing types of policies
- Explaining factors to consider
- Highlighting key benefits

**Example:**
```markdown
Knowing how much coverage is usually dependent on a few different
things, including:

- Funeral expenses
- Income source
- Tuition for school-age children
- Debts
- Living standards

When you are in your life can help to determine what kind of coverage
you need. This is especially true if you have children.
```

**Keep lists:**
- Between 3-7 items
- Concise (1-2 lines each)
- Parallel structure
- Relevant to the topic

---

### 6. Closing Paragraph (Call-to-Action)

**Purpose:** Encourage readers to contact you

**Formula:**
- Invite them to take action
- Reference KLM Insurance Solutions Inc.
- Mention Pennsylvania if applicable
- Keep it friendly and helpful

**Examples:**

**Good:**
```markdown
Find out more about shopping for life insurance in Pennsylvania by
contacting us at KLM Insurance Solutions Inc. today.
```

```markdown
Pennsylvania residents can count on our agency to match them with top
insurance products from reputable, reliable providers. Call or stop
by our office today to schedule a consultation with an agent, or to
ask any questions you may have about motorcycle insurance.
```

**Bad:**
```markdown
Contact us.
```

---

## Content Writing Tips

### Tone & Style

✅ **DO:**
- Write conversationally (like talking to a friend)
- Use "you" and "your" to address the reader
- Use "we" and "our" when talking about KLM
- Be helpful and educational
- Show empathy for customer concerns
- Use short paragraphs (3-5 sentences)
- Break up long text with headings

❌ **DON'T:**
- Use overly technical jargon
- Write in passive voice
- Make it all about you/the company
- Use salesy or pushy language
- Write huge blocks of text
- Forget to proofread

### Length Guidelines

- **Total page:** 300-600 words
- **Opening paragraph:** 50-75 words
- **Each section:** 100-150 words
- **Bullet lists:** 3-7 items
- **Closing paragraph:** 40-60 words

### SEO Best Practices

1. **Use your product/service name:**
   - In the title
   - In first paragraph
   - In at least one heading
   - In closing paragraph

2. **Include location keywords:**
   - Pennsylvania
   - Greater Philadelphia region
   - West Chester (if relevant)

3. **Use related terms naturally:**
   - Coverage, protection, policy
   - Quote, premium, deductible
   - Agent, agency, insurance solutions

4. **Keep it natural:**
   - Don't stuff keywords
   - Write for humans first
   - Search engines prefer quality content

---

## Adding Images

### Hero Image

**Standard:** Use the default for consistency
```yaml
hero_image: "/images/featured-banner.png"
```

This is the large background image behind the quote form.

**Custom:** If you have a product-specific hero image:
```yaml
hero_image: "/images/hero-motorcycle.png"
```

### Sidebar Image

**Required:** Create or use a product-specific thumbnail

**Size:** Approximately 300×200 pixels

**Format:** PNG or JPG

**Naming:** `featured-[product-name]-thumbnail.png`

**Location:** `/Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/static/images/`

**Example:**
```yaml
sidebar_image: "/images/featured-motorcycle-thumbnail.png"
```

**If you don't have a custom image yet:**
```yaml
sidebar_image: "/images/content-banner.png"
```

---

## Adding to Navigation

If you want your new page in the main navigation menu:

1. **Open the layout file:**
   ```bash
   nano /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/layouts/_default/baseof.html
   ```

2. **Find the dropdown menu section** (around line 25)

3. **Add your link inside the INSURANCE SERVICES dropdown:**
   ```html
   <li class="dropdown">
       <a href="#" class="dropdown-toggle">INSURANCE SERVICES</a>
       <ul class="dropdown-menu">
           <li><a href="/auto-insurance/">Auto Insurance</a></li>
           <li><a href="/home-insurance/">Home Insurance</a></li>
           <li><a href="/commercial-insurance/">Commercial Insurance</a></li>
           <li><a href="/boat-insurance/">Boat/Watercraft Insurance</a></li>
           <li><a href="/life-insurance/">Life Insurance</a></li>
           <li><a href="/umbrella-insurance/">Umbrella Insurance</a></li>
           <!-- ADD YOUR NEW PAGE HERE -->
           <li><a href="/motorcycle-insurance/">Motorcycle Insurance</a></li>
       </ul>
   </li>
   ```

4. **Save and test locally**

---

## Complete Example Walkthrough

### Scenario: Creating a Renters Insurance Page

#### Step 1: Copy Template
```bash
cp /Users/mark/PycharmProjects/klm-migrate/templates/product-service-template.md \
   /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/content/renters-insurance.md
```

#### Step 2: Edit Front Matter
```yaml
---
title: "Renters Insurance"
description: "Renters Insurance - KLM Insurance Solutions"
draft: false
hero_image: "/images/featured-banner.png"
sidebar_image: "/images/featured-renters-thumbnail.png"
form_type: "full"
---
```

#### Step 3: Write Opening Paragraph
```markdown
Renting an apartment or home doesn't mean you should go without insurance
protection for your belongings. Many renters mistakenly believe their
landlord's insurance covers their personal property, but that's not the
case. KLM Insurance Solutions Inc. offers affordable renters insurance
to protect what matters most to you.
```

#### Step 4: Add Main Section
```markdown
## Protect Your Personal Belongings

Renters insurance provides coverage for your personal property in the
event of theft, fire, water damage, or other covered perils. This
includes furniture, electronics, clothing, jewelry, and other valuables.

We work with you to determine the right amount of coverage based on
the value of your possessions. Our experienced agents can help you
understand what's covered and ensure you have adequate protection
without overpaying.
```

#### Step 5: Add Secondary Section
```markdown
## What Renters Insurance Covers

A comprehensive renters insurance policy typically includes:

- Personal property coverage for your belongings
- Liability protection if someone is injured in your rental
- Additional living expenses if you're displaced from your home
- Medical payments to others
- Loss of use coverage

These protections give you peace of mind knowing that unexpected
events won't leave you financially vulnerable.
```

#### Step 6: Add Closing
```markdown
Contact KLM Insurance Solutions Inc. today to get a free quote on
renters insurance. Our knowledgeable agents serve renters throughout
Pennsylvania and can help you find affordable coverage that fits
your needs and budget.
```

#### Step 7: Test Locally
```bash
cd /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site
hugo server -D --bind 0.0.0.0
```

Visit: http://localhost:1313/renters-insurance/

#### Step 8: Publish to Staging
```bash
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py
```

---

## Checklist Before Publishing

- [ ] All `[placeholders]` replaced with actual content
- [ ] Title and description are accurate
- [ ] Form type chosen (simple or full)
- [ ] Sidebar image exists in `/static/images/`
- [ ] Spelling and grammar checked
- [ ] 2-3 main sections with clear headings
- [ ] Opening paragraph hooks the reader
- [ ] Closing has call-to-action
- [ ] Mentions Pennsylvania/Greater Philadelphia region
- [ ] Tested locally and looks good
- [ ] Mobile layout checked (resize browser)
- [ ] No broken links or images

---

## Common Mistakes to Avoid

❌ **Leaving placeholders**
```markdown
title: "[Product/Service Name]"  ← Still has brackets!
```

❌ **Wrong image path**
```yaml
sidebar_image: "images/my-image.png"  ← Missing leading slash!
# Should be:
sidebar_image: "/images/my-image.png"
```

❌ **No headings**
```markdown
Long paragraph of text without any ## headings to break it up.
```

❌ **Too generic**
```markdown
We offer this insurance. It's good. Call us.
```

❌ **Too salesy**
```markdown
BUY NOW!!! BEST PRICES!!! LIMITED TIME!!!
```

❌ **Forgetting geography**
```markdown
# No mention of Pennsylvania or Greater Philadelphia region
```

---

## Need Help?

**For content questions:**
- Look at existing pages for examples: `content/auto-insurance.md`, `content/life-insurance.md`
- Check this guide's examples section

**For technical issues:**
- See: `PUBLISHING_WORKFLOW.md`
- See: `QUICK_START.md`

**Testing:**
- Always test locally first: `hugo server -D`
- Then test on staging: `python3 publish_to_staging.py`
- Finally production: `python3 publish_to_production.py`

---

## Quick Reference

```bash
# Copy template
cp templates/product-service-template.md content/your-page.md

# Edit file
nano content/your-page.md

# Test locally
cd klm-hugo-site
hugo server -D --bind 0.0.0.0

# Publish to staging
cd ..
python3 publish_to_staging.py

# Publish to production (after approval)
python3 publish_to_production.py
```

**File locations:**
- Template: `templates/product-service-template.md`
- Your pages: `klm-hugo-site/content/`
- Images: `klm-hugo-site/static/images/`
- Navigation: `klm-hugo-site/layouts/_default/baseof.html`

---

**Happy page creating!** 🎉
