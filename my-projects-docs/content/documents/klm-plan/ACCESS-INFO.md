---
title: "ACCESS-INFO"
project: klm-plan
original_path: ACCESS-INFO.md
modified: 2026-01-02T23:49:52.833898
---

# KLM Business Plan - Quick Access Guide

## 🔒 Your Secure Business Plan Site

**URL**: https://d1jrr6wppi7k7d.cloudfront.net

**Login Credentials:**
- Username: `klm`
- Password: `KLM2026Plan!`

## ✅ What's Protected

✅ **HTTPS Enabled** - All traffic is encrypted
✅ **Password Protected** - Requires login to view
✅ **Mobile Friendly** - Works on iPhone, iPad, desktop
✅ **Auto-Deployment** - Edit on GitHub, auto-publishes

## 📱 How to Edit from Your iPhone

### Quick Steps:

1. **Open GitHub app** (or github.com in Safari)
2. **Go to your repo**: emmalone/klm-plan
3. **Navigate** to any file in `content/` folder
4. **Tap the pencil icon** ✏️ to edit
5. **Make your changes** in markdown
6. **Scroll down** and tap "Commit changes"
7. **Wait 60-90 seconds** - your changes are live!

### Example: Update Product Ideas

```
github.com/emmalone/klm-plan
  └── content/
      └── products/
          └── new-ideas/
              └── _index.md  ← Tap this, then ✏️ to edit
```

## 🌐 URL Differences

| URL | Security | Status |
|-----|----------|--------|
| https://d1jrr6wppi7k7d.cloudfront.net | ✅ HTTPS + Password + Private S3 | **ONLY way to access** |
| http://klm-plan.s3-website-us-east-1.amazonaws.com | 🚫 Disabled | No longer works - returns 404 |

**Note**: S3 bucket is now completely private. Only CloudFront can access it. See [S3-SECURITY-COMPLETE.md](./S3-SECURITY-COMPLETE.md) for details.

## 🔐 Changing the Password

If you want to change the login credentials:

1. Edit `lambda-auth.js` file
2. Change `authUser` and `authPass` variables
3. Run `python3 attach-lambda.py` to update

Or see [SECURITY-SETUP.md](./SECURITY-SETUP.md) for detailed instructions.

## 📂 Site Structure

```
Lines of Business
├── Personal Lines (Auto, Home, Boat, Liability)
├── Commercial Lines (Apartments, BOP)
└── Life Insurance

Products & Innovation
├── New Product Ideas (10 concepts)
├── Digital Life Vault
└── Worst Case Scenario Planner

Marketing
├── Facebook Strategy
└── Marketing Plan

Sales Operations
├── Sales Process
└── Compensation
```

## 💡 Common Tasks

### Add a New Product Idea

1. Go to `content/products/new-ideas/`
2. Tap "Add file" → "Create new file"
3. Name it: `my-idea.md`
4. Add content:
   ```markdown
   ---
   title: "My Product Idea"
   weight: 10
   ---

   ## Overview
   Description here...
   ```
5. Commit the file
6. Auto-publishes in 60 seconds

### Update Marketing Plans

1. Navigate to `content/marketing/plan.md`
2. Tap ✏️ to edit
3. Make changes
4. Commit
5. Live in 60 seconds

### Add a New Business Line

1. Create folder in `content/lines-of-business/`
2. Add `_index.md` with frontmatter
3. Add individual pages as .md files
4. Commit all files
5. Auto-publishes

## ⚡ Tips

- **Small commits**: Make one change at a time for easier tracking
- **Descriptive messages**: Use clear commit messages like "Added Q2 revenue goals"
- **Preview first**: GitHub shows a preview tab when editing
- **Test locally**: For major changes, test with `hugo server` first
- **Check Actions**: If something doesn't update, check github.com/emmalone/klm-plan/actions

## 🆘 Troubleshooting

**Q: I don't see a login prompt**
- CloudFront can take 5-15 minutes for first deployment
- Try hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows/Android)
- Check if status says "Deployed": `aws cloudfront get-distribution --id E1Z0GEJNAKEO42`

**Q: Login doesn't work**
- Double-check: username is `klm` (lowercase)
- Password is `KLM2026Plan!` (case-sensitive, with !)
- Try clearing browser cache

**Q: My changes don't appear**
- Wait 60-90 seconds for deployment
- Check Actions tab for workflow status
- CloudFront cache can take a minute to invalidate
- Try hard refresh in browser

**Q: I want to add a custom domain**
- See [SECURITY-SETUP.md](./SECURITY-SETUP.md) section on custom domains
- Requires owning a domain (like klminsurance.com)
- Can be added without rebuilding anything

## 📞 Support Files

- **Complete Documentation**: [claude.md](./claude.md)
- **Security Details**: [SECURITY-SETUP.md](./SECURITY-SETUP.md)
- **GitHub Repository**: https://github.com/emmalone/klm-plan

---

**🎉 Your business plan is now secure, mobile-friendly, and auto-updating!**

Last Updated: 2026-01-02
