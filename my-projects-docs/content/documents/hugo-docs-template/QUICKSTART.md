---
title: "QUICKSTART"
project: hugo-docs-template
original_path: QUICKSTART.md
modified: 2026-01-03T10:57:53.641682
---

# Hugo Docs Automation - Quick Start

Deploy a secure Hugo documentation site in 3 steps.

## 1. Prerequisites (One-Time Setup)

```bash
# Install tools
brew install hugo awscli gh python3

# Configure AWS
aws configure
# Enter your AWS access key, secret key, region (us-east-1)

# Authenticate GitHub
gh auth login

# Install Python dependency
pip3 install boto3
```

## 2. Deploy Your Site

```bash
cd /Users/mark/PycharmProjects/hugo-docs-template

python3 deploy-hugo-docs.py \
  --project-name my-awesome-project \
  --username admin \
  --password SuperSecret123!
```

**Wait 15-20 minutes** while the script:
- Creates Hugo site
- Sets up S3 bucket
- Configures CloudFront with HTTPS
- Adds password protection
- Creates GitHub repository
- Sets up auto-deployment

## 3. Access Your Site

After deployment completes, you'll see:

```
🎉 DEPLOYMENT COMPLETE!
============================================================
📦 Project: my-awesome-project
🪣 S3 Bucket: my-awesome-project-docs (private)
☁️  CloudFront: E1ABC123XYZ
🌐 URL: https://d1abc123xyz.cloudfront.net
🔐 Username: admin
🔐 Password: SuperSecret123!
📚 GitHub: https://github.com/your-username/my-awesome-project
============================================================
```

Visit the URL, enter your credentials, and you're in!

## What You Get

✅ **Secure HTTPS Site**: CloudFront with SSL certificate
✅ **Password Protection**: Basic HTTP authentication
✅ **Private S3 Bucket**: No public access, only via CloudFront
✅ **Auto-Deployment**: Push to GitHub = site updates in 60 seconds
✅ **Mobile Editing**: Edit via GitHub mobile app
✅ **Production Ready**: Follows AWS security best practices

## Next Steps

### Edit Content

```bash
cd my-awesome-project

# Create new page
hugo new docs/getting-started.md

# Edit it
vim content/docs/getting-started.md

# Test locally
hugo server -D

# Deploy
git add .
git commit -m "Add getting started guide"
git push
```

Site updates automatically in ~60 seconds!

### Common Customizations

**Change password**: Edit `lambda-auth.js` and redeploy Lambda function
**Add custom domain**: Configure Route 53 and ACM certificate
**Customize theme**: Edit `hugo.toml` configuration
**Add images**: Place in `static/` folder

## Cost

**~$2-3/month** per site (or $0-1 with AWS free tier)

- S3 storage and requests
- CloudFront data transfer
- Lambda@Edge invocations

## Help

- **Full Documentation**: See `README.md`
- **Examples**: See `USAGE-EXAMPLES.md`
- **Manual Process**: See `COMPLETE-SETUP-GUIDE.md`

## Troubleshooting

**Script fails?**
- Check AWS credentials: `aws sts get-caller-identity`
- Check GitHub auth: `gh auth status`
- Verify tools installed: `hugo version`, `python3 --version`

**Site not loading?**
- Wait 5-15 minutes for CloudFront deployment
- Check status: `aws cloudfront get-distribution --id YOUR_DIST_ID`

**Password not working?**
- Verify username/password are correct
- Clear browser cache and try again

---

That's it! You now have a production-ready documentation site.

**Created**: 2026-01-03
