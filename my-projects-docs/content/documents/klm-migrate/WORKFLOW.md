---
title: "WORKFLOW"
project: klm-migrate
original_path: klm-hugo-site/WORKFLOW.md
modified: 2026-01-01T23:43:57.858567
---

# KLM Hugo Site - Development Workflow

Complete guide for working with the KLM Insurance Hugo site across multiple devices.

**Repository:** https://github.com/emmalone/klm-migrate

---

## Table of Contents

1. [Working on Another Computer](#working-on-another-computer)
2. [Working from iPhone with Claude Code](#working-from-iphone-with-claude-code)
3. [Syncing Between Devices](#syncing-between-devices)
4. [Daily Workflow](#daily-workflow)
5. [Hugo-Specific Setup](#hugo-specific-setup)
6. [Quick Reference](#quick-reference)

---

## Working on Another Computer

### Step-by-Step Setup Guide

**Important: Always create a NEW, CLEAN folder** - this is the best practice!

#### Step 1: Choose a Location
```bash
# Navigate to where you want the project
cd ~/Documents/Projects
# or
cd ~/Desktop
# or wherever you prefer
```

#### Step 2: Clone the Repository
```bash
# This creates a new folder called 'klm-migrate' and downloads everything
git clone https://github.com/emmalone/klm-migrate.git

# Navigate into it
cd klm-migrate
```

#### Step 3: Verify What You Got
```bash
# Check the files
ls -la

# You should see:
# - content/
# - layouts/
# - static/
# - themes/
# - hugo.toml
# - .gitignore
# etc.

# The API key files WON'T be there (they were excluded)
```

#### Step 4: Configure Git (First Time Only)
```bash
# Set your identity
git config user.name "emmalone"
git config user.email "mark@emm-associates.com"

# Verify
git config user.name
git config user.email
```

#### Step 5: Start Working!
```bash
# Make sure you're up to date
git pull origin main

# Create a branch for changes
git checkout -b update-homepage

# Edit files, make changes...

# When done:
git add .
git commit -m "Update homepage content"
git push -u origin update-homepage

# Create PR on GitHub, review, merge
```

---

## About the API Key Files

### What Happened to the API Key Files?

When you clone on a new computer, you'll notice these files are missing:
- ❌ `create_form3_fields.py` - NOT there
- ❌ `setup_form3_conditions.py` - NOT there

**This is CORRECT!** They were excluded by .gitignore for security.

### If You Need Them on the New Computer:

**Option 1: Copy Manually (if needed)**
```bash
# On your ORIGINAL computer, copy to USB/cloud:
cp create_form3_fields.py ~/Dropbox/
cp setup_form3_conditions.py ~/Dropbox/

# On NEW computer, copy them back:
cp ~/Dropbox/create_form3_fields.py .
cp ~/Dropbox/setup_form3_conditions.py .

# They'll remain local-only (protected by .gitignore)
```

**Option 2: Don't Copy Them (recommended)**
- If they were one-time setup scripts, just leave them out
- Your website works without them
- They contain JotForm API keys and should stay on original computer

---

## Working from iPhone with Claude Code

### YES! You can work remotely using your iPhone!

**NEW:** Dev environment auto-deploys from ALL commits (laptop AND iPhone)!

### Steps to Work from iPhone:

#### 1. Open Claude Code on iPhone
```
Go to: https://claude.ai/code
```

#### 2. Connect to Your Repository
- Tap the repository selector
- Choose: **emmalone/klm-migrate**
- Claude Code will have access to your files

#### 3. Make Changes
Just talk to Claude naturally:

**Example requests:**
```
"Update the homepage title to 'Your Trusted Insurance Partner'"

"Add a new insurance product page for pet insurance"

"Fix the contact form styling - make the submit button blue"

"Update the about page with new company information"

"Add a testimonials section to the homepage"
```

#### 4. Claude Will:
- ✅ Read the current files
- ✅ Make the changes
- ✅ Create a `claude/*` branch automatically
- ✅ Commit the changes
- ✅ Push to GitHub
- ✅ **Auto-deploy to dev environment within 30 seconds**

#### 5. Preview Your Changes
- **Dev URL:** http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com
- Changes appear automatically after push
- No manual deployment needed!
- Test on your iPhone immediately

#### 6. Iterate Quickly
```
You: "The button looks too small"
Claude: Updates files, commits, pushes
Auto-deployed to dev again (30 seconds)
You: Review on iPhone, looks better!
You: "Perfect! Merge this to main"
Claude: Creates PR or merges directly to main
After merge: Auto-deployed to dev again (from main branch)
```

#### 7. Deploy to Staging (When Ready)
```
From your laptop/desktop (not iPhone):
cd /Users/mark/PycharmProjects/klm-migrate
python3 publish_to_staging.py

Preview at: https://www.klmcrm.com
```

### Key Benefits
- ✅ Instant preview on dev environment
- ✅ Work from anywhere
- ✅ No laptop needed for development
- ✅ Dev always in sync with latest code (from both laptop and iPhone)
- ✅ Manual control over staging deployment

---

## Complete Workflow Example

### Scenario: Update Homepage from iPhone

**You say to Claude Code (on iPhone):**
```
"I want to update the homepage hero section. Change the main heading
to 'Protecting What Matters Most' and update the subtitle to mention
our 25 years of experience."
```

**Claude Code will:**
1. Read `content/_index.md`
2. Make the changes
3. Create branch: `claude/update-homepage-hero-xyz`
4. Commit: "Update homepage hero section with new messaging"
5. Push to GitHub

**Automatic Deployment (30 seconds later):**
- GitHub Actions detects push to `claude/*` branch
- Builds Hugo site with dev baseURL
- Deploys to dev-klmhugoweb S3 bucket
- ✅ Live at: http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com

**You:**
- Open dev URL on your iPhone
- Review the changes live
- Test the page

**If changes look good:**
```
You: "This looks perfect! Merge to main"
Claude: Creates PR (or merges directly if you prefer)
```

**After merge to main (automatic):**
- GitHub Actions detects push to `main` branch
- Builds and deploys to dev again (30 seconds)
- Dev now reflects merged code from main
- ✅ Dev environment stays current

**Deploy to staging (from laptop later):**
```bash
cd ~/PycharmProjects/klm-migrate
python3 publish_to_staging.py
# Live at: https://www.klmcrm.com
```

### Then On Your Desktop (Later):
```bash
cd ~/PycharmProjects/klm-migrate/klm-hugo-site
git pull origin main
# Your iPhone changes are now on your desktop!
# Dev environment already has latest code (auto-deployed from main)
```

---

## Working from Laptop/Desktop

### Development Workflow

```bash
# Step 1: Pull latest changes
cd ~/PycharmProjects/klm-migrate/klm-hugo-site
git pull origin main

# Step 2: Make changes locally
# ... edit files ...

# Step 3: Test locally (optional but recommended)
hugo server -D --bind 0.0.0.0
# Visit: http://localhost:1313
# Press Ctrl+C to stop

# Step 4: Commit and push to main
git add .
git commit -m "Update pricing page with new rates"
git push origin main

# Step 5: Automatic deployment to dev (30 seconds)
# GitHub Actions deploys to: http://dev-klmhugoweb.s3-website-us-east-1.amazonaws.com

# Step 6: Deploy to staging when ready for business review
cd ~/PycharmProjects/klm-migrate
python3 publish_to_staging.py
# Live at: https://www.klmcrm.com
```

### Key Points
- ✅ Test locally with `hugo server` for instant feedback
- ✅ Every push to main auto-deploys to dev environment
- ✅ Dev environment ready for iPhone preview immediately
- ✅ Deploy to staging manually when ready for review

---

## Syncing Between Devices

### The Golden Rule:
**Always pull before you start working**

### From Desktop:
```bash
git pull origin main
# Make changes
git add .
git commit -m "Updated pricing page"
git push origin main
# Auto-deploys to dev environment (30 seconds)
```

### From iPhone (via Claude Code):
```
"Pull the latest changes from GitHub first, then update the contact page"
# Changes auto-deploy to dev after commit
```

### Back to Desktop:
```bash
git pull origin main
# You now have the iPhone changes!
# Dev environment already updated (auto-deployed when iPhone work merged to main)
```

---

## Daily Workflow

### On Desktop/Laptop

#### Starting Work:
```bash
# 1. Navigate to project
cd ~/PycharmProjects/klm-migrate/klm-hugo-site

# 2. Get latest changes
git pull origin main

# 3. Create feature branch
git checkout -b update-about-page

# 4. Make your changes (edit files)

# 5. Preview locally (optional)
hugo server -D
# Visit: http://localhost:1313
```

#### Saving Work:
```bash
# 1. Check what changed
git status

# 2. Review changes
git diff

# 3. Stage files
git add .

# 4. Commit with descriptive message
git commit -m "Update about page with new team members"

# 5. Push to GitHub
git push -u origin update-about-page
```

#### After Pushing:
```bash
# Option A: Merge directly (for small changes)
git checkout main
git merge update-about-page
git push origin main
git branch -d update-about-page

# Option B: Create PR on GitHub (for review)
# 1. Go to https://github.com/emmalone/klm-migrate
# 2. Click "Compare & pull request"
# 3. Review changes
# 4. Merge PR
# 5. Sync locally:
git checkout main
git pull origin main
git branch -d update-about-page
```

### On iPhone (Claude Code)

#### Quick Updates:
```
1. Open https://claude.ai/code
2. Select emmalone/klm-migrate
3. Say: "Update the contact page phone number to 610-429-1330"
4. Review changes
5. Approve commit and push
```

#### Content Changes:
```
"Add a new blog post about winter insurance tips to the insurance-insights page"

"Update the auto insurance page to mention our new safe driver discount"

"Fix typos on the home insurance page"
```

#### Styling Updates:
```
"Make the navigation menu sticky so it stays at the top when scrolling"

"Change the primary button color to match our brand blue (#0066cc)"

"Add more spacing between the insurance product cards"
```

---

## Hugo-Specific Setup

### Installing Hugo on New Computer

If you want to **preview the website** on your new computer, you'll need Hugo installed:

#### macOS:
```bash
brew install hugo

# Verify installation
hugo version
```

#### Windows:
```bash
# Using Chocolatey
choco install hugo-extended

# Or download from: https://gohugo.io/installation/
```

#### Linux:
```bash
# Ubuntu/Debian
sudo apt-get install hugo

# Or download from: https://gohugo.io/installation/
```

### Running the Site Locally

```bash
# Navigate to project
cd klm-migrate

# Start Hugo development server
hugo server -D

# Open browser to: http://localhost:1313

# Press Ctrl+C to stop the server
```

### Building for Production

```bash
# Build the site
hugo

# Generated files will be in public/ directory
# (This directory is excluded from git via .gitignore)
```

### From iPhone:

You can't run Hugo locally on iPhone, but you can:
- Make content changes via Claude Code
- Deploy to hosting (Netlify, Vercel, GitHub Pages)
- View the deployed site

---

## Quick Reference

### On New Computer (First Time):
```bash
# 1. Clone
git clone https://github.com/emmalone/klm-migrate.git
cd klm-migrate

# 2. Configure
git config user.name "emmalone"
git config user.email "mark@emm-associates.com"

# 3. Install Hugo (optional, for local preview)
brew install hugo

# 4. Start working!
git pull origin main
```

### Daily Workflow (Desktop):
```bash
# Start
git pull origin main
git checkout -b feature-name

# Work
# make changes, test locally with: hugo server -D

# Save
git add .
git commit -m "Description"
git push -u origin feature-name

# Merge (via PR on GitHub or locally)
```

### Daily Workflow (iPhone):
```
1. Open claude.ai/code
2. Select emmalone/klm-migrate
3. Tell Claude what to change
4. Review and approve
5. Merge PR (if created)
```

### Essential Git Commands:
```bash
# Check status
git status

# See what changed
git diff

# See commit history
git log --oneline

# Switch branches
git checkout main
git checkout -b new-feature

# Update from GitHub
git pull origin main

# Push to GitHub
git push origin branch-name

# Delete branch (after merging)
git branch -d branch-name
```

---

## File Structure Overview

### What Gets Committed to GitHub:
```
klm-migrate/
├── content/              ✅ Markdown content files
├── layouts/              ✅ HTML templates
├── static/               ✅ CSS, images, favicon
│   ├── css/
│   ├── images/
│   └── favicon.ico
├── themes/               ✅ Hugo theme
├── docs/                 ✅ Reference documentation
├── hugo.toml             ✅ Site configuration
├── .gitignore            ✅ Protects secrets
├── WORKFLOW.md           ✅ This file
├── SECURITY_REVIEW.md    ✅ Security audit
├── README.md             ✅ Project overview
└── Utility scripts       ✅ (8 Python files - no secrets)
```

### What Stays Local Only:
```
├── public/               ❌ Generated HTML (built by Hugo)
├── resources/            ❌ Hugo cache
├── .hugo_build.lock      ❌ Build artifact
├── .DS_Store             ❌ macOS metadata
├── create_form3_fields.py    ❌ Has API key
└── setup_form3_conditions.py ❌ Has API key
```

---

## Recommended Setup by Device

### Desktop/Laptop (Full Development):
**Best for:**
- Major changes and refactoring
- Testing with Hugo local server
- Complex updates requiring IDE

**Setup:**
```bash
# Clone repository
# Install Hugo
# Use code editor (VS Code, etc.)
# Full git workflow
```

### iPhone (Quick Updates):
**Best for:**
- Content changes
- Typo fixes
- Quick updates from anywhere
- Simple page additions

**Setup:**
```
# Just open claude.ai/code
# No installation needed
# Natural language commands
```

### Best of Both Worlds:
- Start features on iPhone when inspired
- Test and refine on desktop with Hugo server
- Review PRs on either device
- Merge from anywhere

---

## Your Complete Setup

### Original Computer:
```
Location: /Users/mark/PycharmProjects/klm-migrate/klm-hugo-site/

Contains:
├── Full website ✅
├── API key files (local only) ✅
└── Git configured ✅
```

### New Computer (After Clone):
```
Location: ~/Projects/klm-migrate/ (or your choice)

Contains:
├── Full website (cloned from GitHub) ✅
├── NO API key files (excluded by .gitignore) ✅
└── Git needs configuration (one-time setup) ⚙️
```

### iPhone (Claude Code):
```
Access: https://claude.ai/code

Can:
├── Read all files ✅
├── Make changes ✅
├── Commit and push ✅
└── Create PRs ✅
```

---

## Common Workflows

### Adding a New Page

**Desktop:**
```bash
# Create new content file
hugo new content/rv-insurance.md

# Edit the file with your content

# Test locally
hugo server -D

# Commit and push
git add content/rv-insurance.md
git commit -m "Add RV insurance page"
git push origin main
```

**iPhone:**
```
"Create a new insurance product page for RV insurance. Include sections for
coverage types, benefits, and a call-to-action button to get a quote."
```

### Updating Existing Content

**Desktop:**
```bash
# Edit the file in your editor
nano content/about.md

# Test changes
hugo server -D

# Commit
git add content/about.md
git commit -m "Update about page team bios"
git push origin main
```

**iPhone:**
```
"Update the about page to add Sarah Johnson as our new Commercial Insurance
Specialist. Mention her 15 years of experience."
```

### Styling Changes

**Desktop:**
```bash
# Edit CSS
nano static/css/style.css

# Test in browser
hugo server -D

# Commit
git add static/css/style.css
git commit -m "Improve button styling and spacing"
git push origin main
```

**iPhone:**
```
"Update the CSS to make the quote buttons more prominent - increase font size
to 18px and add more padding"
```

### Emergency Fix from Phone

**Scenario:** You notice a typo on the live site while away from computer

**iPhone:**
```
1. Open claude.ai/code
2. Select emmalone/klm-migrate
3. Say: "Fix the typo on the contact page - change 'West Chesster' to 'West Chester'"
4. Review the change
5. Approve and push
6. Fixed in seconds!
```

---

## Troubleshooting

### "Permission denied" when pushing

**Problem:** GitHub credentials not set up

**Solution:**
```bash
# Use Personal Access Token (from your previous session)
# macOS stores it in Keychain
# You may need to re-authenticate
```

### "Your branch has diverged"

**Problem:** Local and remote have different commits

**Solution:**
```bash
# Pull and merge
git pull origin main

# Or rebase (advanced)
git pull --rebase origin main
```

### "Merge conflicts"

**Problem:** Same file edited on different devices

**Solution:**
```bash
# Pull the changes
git pull origin main

# Git will mark conflicts in the file
# Edit the file to resolve conflicts
# Look for: <<<<<<<, =======, >>>>>>>

# After fixing:
git add <file>
git commit -m "Resolve merge conflicts"
git push origin main
```

### Hugo not found

**Problem:** Hugo not installed on new computer

**Solution:**
```bash
# macOS
brew install hugo

# Verify
hugo version
```

### Can't see changes locally

**Problem:** Hugo server needs restart

**Solution:**
```bash
# Stop server: Ctrl+C
# Restart:
hugo server -D
# Refresh browser
```

---

## Best Practices

### Commit Messages:
✅ Good:
- "Update homepage hero section with new messaging"
- "Add pet insurance product page"
- "Fix contact form validation"

❌ Bad:
- "updates"
- "fix stuff"
- "changes"

### Branching:
- Use branches for features: `git checkout -b add-testimonials`
- Keep main branch stable
- Merge after testing

### Syncing:
- Always `git pull` before starting work
- Commit often with clear messages
- Push regularly to back up work

### Security:
- Never commit API keys or passwords
- Keep .gitignore updated
- Review changes before pushing

---

## Summary

### On Another Computer:
1. ✅ Create NEW folder
2. ✅ `git clone https://github.com/emmalone/klm-migrate.git`
3. ✅ Configure git identity
4. ✅ Optionally install Hugo
5. ✅ Start working!

### On iPhone:
1. ✅ Go to claude.ai/code
2. ✅ Select emmalone/klm-migrate
3. ✅ Tell Claude what to change
4. ✅ Review and merge!

### Remember:
- Always pull before you start working
- Commit often with clear messages
- API key files stay local only
- Test locally when possible
- You can work from anywhere!

---

## Additional Resources

**Official Documentation:**
- Hugo Docs: https://gohugo.io/documentation/
- Git Docs: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com

**Your Reference Docs:**
- GITOVERVIEW.md - Complete git workflow guide
- MIGRATE_TO_GITHUB_CHECKLIST.md - Migration checklist
- SECURITY_REVIEW.md - Security audit report
- SESSION_HANDOFF.md - Session transfer guide

**Repository:**
- GitHub: https://github.com/emmalone/klm-migrate

---

**Last Updated:** December 28, 2025
**Maintained by:** emmalone

**Questions or Issues?**
- Check the docs/ folder for detailed guides
- Review SECURITY_REVIEW.md for security best practices
- Refer to GITOVERVIEW.md for git commands reference

---

**You're all set to work from anywhere! 🎉**
