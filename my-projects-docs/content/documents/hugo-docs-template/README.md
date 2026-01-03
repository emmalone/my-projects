---
title: "README"
project: hugo-docs-template
original_path: README.md
modified: 2026-01-03T10:55:17.026840
---

# Hugo Documentation Site Deployment Automation

**One-command deployment of secure Hugo documentation sites to AWS**

This automation system creates a complete, production-ready documentation site with:
- ✅ Hugo static site with hugo-book theme
- ✅ AWS S3 storage (completely private)
- ✅ CloudFront CDN with HTTPS
- ✅ Lambda@Edge password protection + URL rewriting
- ✅ GitHub repository with auto-deployment
- ✅ ~60-90 second deployment pipeline

## Quick Start

### 1. Prerequisites

```bash
# Install tools (macOS)
brew install hugo awscli gh python3

# Configure AWS
aws configure
# Enter: Access Key ID, Secret Key, Region, Output format

# Authenticate with GitHub
gh auth login

# Install Python dependencies
pip3 install boto3
```

### 2. Deploy a New Docs Site

```bash
# Clone or download this template
cd /path/to/hugo-docs-template

# Run deployment script
python3 deploy-hugo-docs.py \
  --project-name my-awesome-project \
  --username admin \
  --password SuperSecret123!
```

That's it! The script will:
1. Create Hugo site locally
2. Set up S3 bucket (initially public for testing)
3. Deploy site to S3
4. Create GitHub repository
5. Create CloudFront distribution with HTTPS
6. Create Lambda@Edge authentication function
7. Secure S3 bucket (make private)
8. Set up GitHub Actions auto-deployment
9. Commit and push everything

**Total time**: ~15-20 minutes (mostly waiting for CloudFront propagation)

### 3. Access Your Site

After deployment completes:

```
🌐 URL: https://d1abc123xyz.cloudfront.net
🔐 Username: admin
🔐 Password: SuperSecret123!
```

Visit the URL, enter credentials, and you're in!

## What Gets Created

### Local Files
```
my-awesome-project/
├── .github/workflows/deploy.yml    # Auto-deployment workflow
├── content/
│   ├── _index.md                   # Homepage
│   ├── about/
│   ├── docs/
│   ├── guides/
│   └── reference/
├── themes/hugo-book/               # Git submodule
├── hugo.toml                        # Hugo config with CloudFront URL
├── lambda-auth.js                   # Auth function (committed for reference)
└── lambda-auth.zip                  # Lambda deployment package
```

### AWS Resources
- **S3 Bucket**: `my-awesome-project-docs` (private, no public access)
- **CloudFront Distribution**: E1ABC123XYZ (HTTPS, global CDN)
- **Lambda@Edge Function**: `my-awesome-project-basic-auth:1`
- **IAM Role**: `my-awesome-project-lambda-edge-role`
- **Origin Access Control**: `my-awesome-project-oac`

### GitHub Resources
- **Repository**: `github.com/your-username/my-awesome-project`
- **GitHub Secrets**: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
- **Workflow**: Auto-deploy on push to main branch

## Usage

### Editing Content

#### Option 1: Desktop (Recommended for Bulk Edits)
```bash
cd my-awesome-project

# Edit content
vim content/docs/getting-started.md

# Test locally
hugo server -D
# Visit http://localhost:1313

# Commit and push (triggers auto-deployment)
git add .
git commit -m "Add getting started guide"
git push
```

#### Option 2: Mobile (Quick Edits)
1. Open GitHub mobile app
2. Navigate to your repository
3. Edit any markdown file
4. Commit directly to main branch
5. Wait ~60-90 seconds for auto-deployment

### Adding New Pages

```bash
# Create new page
hugo new docs/advanced-topics.md

# Edit the file
# ---
# title: "Advanced Topics"
# ---
#
# # Advanced Topics
# Content here...

# Commit and push
git add .
git commit -m "Add advanced topics"
git push
```

### Changing Password

Edit `lambda-auth.js`:
```javascript
const authUser = 'new-username';
const authPass = 'new-password';
```

Update Lambda function:
```bash
# Package
zip lambda-auth.zip lambda-auth.js

# Update
aws lambda update-function-code \
  --function-name my-awesome-project-basic-auth \
  --zip-file fileb://lambda-auth.zip

# Publish new version
aws lambda publish-version \
  --function-name my-awesome-project-basic-auth

# Update CloudFront (use new version ARN)
# See COMPLETE-SETUP-GUIDE.md for details
```

## Command Reference

### Full Deployment
```bash
python3 deploy-hugo-docs.py \
  --project-name PROJECT_NAME \
  --username USERNAME \
  --password PASSWORD \
  [--region REGION] \
  [--github-org ORGANIZATION]
```

**Parameters**:
- `--project-name`: Project name (e.g., `my-docs`). Creates bucket `my-docs-docs`
- `--username`: Basic auth username
- `--password`: Basic auth password
- `--region`: AWS region (default: `us-east-1`)
- `--github-org`: GitHub organization (default: current user)

**Example**:
```bash
python3 deploy-hugo-docs.py \
  --project-name klm-business-plan \
  --username klm \
  --password KLM2026Plan! \
  --region us-east-1
```

### Manual Steps (If Automation Fails)

See `COMPLETE-SETUP-GUIDE.md` for step-by-step manual instructions.

## Architecture

### Security Model

```
User Request
    ↓ HTTPS
CloudFront Edge Location
    ↓
Lambda@Edge (viewer-request)
    ├─ Step 1: Rewrite URI (append index.html)
    └─ Step 2: Check Authentication (Basic Auth)
        ↓ (if authenticated)
CloudFront Cache
    ↓
S3 Bucket (via OAC - private)
    ↓
Response to User (HTTPS encrypted)
```

**Security Features**:
- ✅ HTTPS encryption via CloudFront SSL certificate
- ✅ Password protection (basic HTTP auth)
- ✅ Private S3 bucket (no direct access)
- ✅ Origin Access Control (OAC) - only CloudFront can access S3
- ✅ All S3 public access blocks enabled
- ✅ Condition checks CloudFront distribution ARN

### Auto-Deployment Pipeline

```
Git Push to Main
    ↓
GitHub Actions Triggered
    ↓
1. Checkout code + submodules
2. Install Hugo (extended)
3. Build site (hugo --minify)
4. Configure AWS credentials
5. Sync to S3 (aws s3 sync)
6. Invalidate CloudFront cache
    ↓
Site Updated (~60-90 seconds)
```

## Customization

### Changing Hugo Theme

Edit `hugo.toml`:
```toml
theme = 'your-theme-name'
```

Add theme as submodule:
```bash
git submodule add https://github.com/user/theme themes/your-theme-name
```

### Custom Domain (Optional)

1. Register domain in Route 53
2. Request ACM certificate for domain
3. Update CloudFront distribution with custom domain and certificate
4. Update Route 53 with CloudFront alias record

See AWS documentation for details.

### Enhanced Authentication

Replace basic auth with OAuth, SAML, or Cognito:
- Update Lambda@Edge function
- Integrate with identity provider
- Update CloudFront configuration

## Cost Estimate

### Typical Usage (20 GB storage, 100 GB/month transfer)
- S3 Storage: $0.50
- S3 Requests: $0.10
- CloudFront Transfer: $8.50
- CloudFront Requests: $0.10
- Lambda@Edge: $0.50
- **Total**: ~$9.70/month

### Free Tier (First 12 Months)
- S3: 5 GB storage, 20k GET, 2k PUT
- CloudFront: 1 TB transfer, 10M requests
- Lambda: 1M requests, 400k GB-seconds
- **Potential Cost**: $0-2/month with free tier

### Cost Optimization
- Enable CloudFront caching (already configured)
- Use S3 Intelligent-Tiering for large archives
- Set up lifecycle policies for old content
- Monitor with AWS Cost Explorer

## Troubleshooting

### Deployment Script Fails

**Check Prerequisites**:
```bash
# Verify tools installed
hugo version
aws --version
gh --version
python3 --version

# Verify AWS credentials
aws sts get-caller-identity

# Verify GitHub authentication
gh auth status
```

**Common Issues**:
- **AWS credentials**: Run `aws configure`
- **GitHub not authenticated**: Run `gh auth login`
- **Bucket name taken**: Use a more unique project name
- **IAM permissions**: Ensure AWS user has permissions for S3, CloudFront, Lambda, IAM

### Site Not Accessible

**Wait**: CloudFront takes 5-15 minutes to deploy globally

**Verify**:
```bash
# Check distribution status
aws cloudfront get-distribution --id YOUR_DIST_ID --query 'Distribution.Status'

# Should return: "Deployed"
```

### Navigation Links Don't Work

**Cause**: Lambda@Edge function not handling URL rewriting

**Check**: Verify `lambda-auth.js` includes URL rewriting logic (Step 1 in the function)

### Password Not Working

**Verify**:
- Correct username/password
- Lambda function has latest code
- CloudFront is using latest Lambda version

**Update**:
```bash
# Check Lambda version in CloudFront
aws cloudfront get-distribution-config --id YOUR_DIST_ID \
  --query 'DistributionConfig.DefaultCacheBehavior.LambdaFunctionAssociations'
```

### GitHub Actions Failing

**Check Secrets**:
```bash
gh secret list
# Should show: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
```

**Check Workflow Logs**:
```bash
gh run list
gh run view
```

## Maintenance

### Update Hugo
```bash
brew upgrade hugo
```

### Update Theme
```bash
cd themes/hugo-book
git pull origin main
cd ../..
git add themes/hugo-book
git commit -m "Update hugo-book theme"
git push
```

### Monitor Costs
```bash
# View current month costs
aws ce get-cost-and-usage \
  --time-period Start=2026-01-01,End=2026-01-31 \
  --granularity MONTHLY \
  --metrics BlendedCost
```

### Backup Content
```bash
# Content is in git, but also backup S3
aws s3 sync s3://my-awesome-project-docs backups/
```

## Reference Documentation

- **Complete Setup Guide**: `COMPLETE-SETUP-GUIDE.md` - Step-by-step manual process
- **Hugo Documentation**: https://gohugo.io/documentation/
- **Hugo Book Theme**: https://github.com/alex-shpak/hugo-book
- **AWS S3**: https://docs.aws.amazon.com/s3/
- **CloudFront**: https://docs.aws.amazon.com/cloudfront/
- **Lambda@Edge**: https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html

## Examples

### Deploy KLM Business Plan Docs
```bash
python3 deploy-hugo-docs.py \
  --project-name klm-business-plan \
  --username klm \
  --password KLM2026Secure!
```

### Deploy Technical Documentation
```bash
python3 deploy-hugo-docs.py \
  --project-name api-docs \
  --username developer \
  --password DevPass123!
```

### Deploy to Specific AWS Region
```bash
python3 deploy-hugo-docs.py \
  --project-name eu-docs \
  --username admin \
  --password SecureEU2026! \
  --region eu-west-1
```

## Support

For issues, questions, or improvements:
1. Check `COMPLETE-SETUP-GUIDE.md` for detailed manual steps
2. Review troubleshooting section above
3. Check AWS CloudWatch logs for Lambda errors
4. Verify CloudFront distribution status

## License

This automation system is provided as-is for creating secure Hugo documentation sites.

---

**Created**: 2026-01-03
**Purpose**: One-command deployment of secure Hugo docs sites to AWS
**Automation**: Python script + AWS SDK (boto3) + GitHub CLI

**Features**:
- ✅ Complete automation (Hugo → S3 → CloudFront → Lambda@Edge → GitHub)
- ✅ Secure by default (HTTPS, auth, private S3)
- ✅ Auto-deployment pipeline (GitHub Actions)
- ✅ Mobile-friendly editing (GitHub mobile app)
- ✅ Production-ready architecture
