---
title: "HUGO-AUTOMATION-SYSTEM"
project: klm-plan
original_path: HUGO-AUTOMATION-SYSTEM.md
modified: 2026-01-03T10:57:24.932900
---

# Hugo Documentation Site Automation System

## Overview

We've created a **complete automation system** for deploying secure Hugo documentation sites to AWS with a single command. This system was built based on the klm-plan setup process and can be used for all future documentation projects.

## Location

**Template Directory**: `/Users/mark/PycharmProjects/hugo-docs-template/`

**Contents**:
- `deploy-hugo-docs.py` - Complete automation script
- `README.md` - Full documentation and usage guide
- `USAGE-EXAMPLES.md` - Real-world examples
- `COMPLETE-SETUP-GUIDE.md` - Step-by-step manual process (reference)

## Quick Start

### Deploy a New Documentation Site

```bash
cd /Users/mark/PycharmProjects/hugo-docs-template

python3 deploy-hugo-docs.py \
  --project-name my-new-project \
  --username admin \
  --password SecurePass123!
```

**That's it!** In 15-20 minutes you'll have:
- ✅ Hugo site with hugo-book theme
- ✅ Secure HTTPS hosting via CloudFront
- ✅ Password-protected access
- ✅ Private S3 bucket (no public access)
- ✅ GitHub repository with auto-deployment
- ✅ ~60-second deployment pipeline

## What It Does

The automation script executes the **complete 8-phase deployment** we followed for klm-plan:

### Phase 1: Local Hugo Site
- Creates Hugo site structure
- Installs hugo-book theme as submodule
- Configures hugo.toml
- Creates initial content structure

### Phase 2: S3 Bucket Setup
- Creates S3 bucket (project-name-docs)
- Enables static website hosting (initially)
- Makes bucket public (temporarily for testing)
- Builds and deploys Hugo site

### Phase 3: GitHub Repository
- Creates GitHub repository
- Configures AWS secrets (credentials, region)
- Initial commit and push

### Phase 4: CloudFront with HTTPS
- Creates CloudFront distribution
- Configures HTTPS redirect
- Enables compression and caching
- Waits for deployment (5-10 minutes)
- Updates Hugo baseURL with CloudFront domain

### Phase 5: Lambda@Edge Authentication
- Creates IAM role for Lambda@Edge
- Creates Lambda function with:
  - Password authentication (basic HTTP auth)
  - URL rewriting (appends index.html for navigation)
- Publishes Lambda version
- Attaches to CloudFront distribution

### Phase 6: Secure S3 Bucket
- Creates Origin Access Control (OAC)
- Updates CloudFront to use S3 bucket origin (not website)
- Disables S3 website hosting
- Removes public bucket policy
- Enables all public access blocks
- Creates CloudFront-only bucket policy

### Phase 7: GitHub Actions Workflow
- Creates `.github/workflows/deploy.yml`
- Configures auto-deployment on push to main
- Sets up CloudFront cache invalidation

### Phase 8: Final Commit
- Commits all files to repository
- Pushes to GitHub
- Prints deployment summary

## Command Reference

### Basic Deployment
```bash
python3 deploy-hugo-docs.py \
  --project-name PROJECT_NAME \
  --username USERNAME \
  --password PASSWORD
```

### With Custom Region
```bash
python3 deploy-hugo-docs.py \
  --project-name PROJECT_NAME \
  --username USERNAME \
  --password PASSWORD \
  --region eu-west-1
```

### With GitHub Organization
```bash
python3 deploy-hugo-docs.py \
  --project-name PROJECT_NAME \
  --username USERNAME \
  --password PASSWORD \
  --github-org your-organization
```

## Examples

### Example 1: Deploy Product Documentation
```bash
python3 deploy-hugo-docs.py \
  --project-name life-legacy-platform \
  --username product \
  --password ProductDocs2026!
```

**Result**:
- URL: https://d1abc123xyz.cloudfront.net
- S3: life-legacy-platform-docs
- GitHub: github.com/your-username/life-legacy-platform

### Example 2: Deploy API Documentation
```bash
python3 deploy-hugo-docs.py \
  --project-name api-documentation \
  --username developer \
  --password DevApiDocs2026!
```

### Example 3: Deploy Marketing Wiki
```bash
python3 deploy-hugo-docs.py \
  --project-name marketing-wiki \
  --username marketing \
  --password MarketingWiki2026!
```

## Comparison: Manual vs Automated

### Manual Process (What We Did for klm-plan)
- **Time**: 2-3 hours
- **Steps**: 50+ commands across 8 phases
- **Files**: 10+ configuration files to create/edit
- **Complexity**: High (AWS, Lambda, CloudFront, IAM)
- **Error-prone**: Easy to miss steps or misconfigure

### Automated Process (Using deploy-hugo-docs.py)
- **Time**: 15-20 minutes (mostly CloudFront propagation)
- **Steps**: 1 command
- **Files**: Automatically created
- **Complexity**: Low (hidden in script)
- **Error-prone**: Minimal (script handles all details)

## Architecture Created

```
User Browser
    ↓ HTTPS
CloudFront Edge (Global CDN)
    ↓
Lambda@Edge (viewer-request)
    ├─ Rewrite URL (append /index.html)
    └─ Check Password (Basic Auth)
        ↓ (authenticated)
CloudFront Cache
    ↓ (via OAC)
S3 Bucket (Private)
    └─ Hugo Static Site
```

**Security Layers**:
1. HTTPS encryption (CloudFront SSL)
2. Password authentication (Lambda@Edge)
3. Private S3 bucket (OAC only)
4. Public access blocks (all 4 enabled)

## What Gets Created

### AWS Resources
- **S3 Bucket**: `{project-name}-docs` (private, us-east-1 or specified region)
- **CloudFront Distribution**: Global CDN with HTTPS
- **Lambda@Edge Function**: `{project-name}-basic-auth:1`
- **IAM Role**: `{project-name}-lambda-edge-role`
- **Origin Access Control**: `{project-name}-oac`

### GitHub Resources
- **Repository**: `github.com/{user}/{project-name}`
- **Secrets**: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
- **Workflow**: `.github/workflows/deploy.yml`

### Local Files
```
{project-name}/
├── .github/workflows/deploy.yml
├── content/
│   ├── _index.md
│   ├── about/_index.md
│   ├── docs/_index.md
│   ├── guides/_index.md
│   └── reference/_index.md
├── themes/hugo-book/
├── hugo.toml
├── lambda-auth.js
└── lambda-auth.zip
```

## Cost per Site

### Typical Usage (Small Documentation Site)
- S3 Storage (5 GB): $0.12/month
- S3 Requests: $0.05/month
- CloudFront Transfer (20 GB): $1.70/month
- CloudFront Requests (100k): $0.10/month
- Lambda@Edge (100k invocations): $0.20/month
- **Total**: ~$2.17/month per site

### Free Tier Benefits (First 12 Months)
- S3: 5 GB storage free
- CloudFront: 1 TB transfer free
- Lambda: 1M requests free
- **Potential**: $0-0.50/month with free tier

## Prerequisites

### Required Tools
```bash
# Install (macOS)
brew install hugo awscli gh python3

# Verify
hugo version        # v0.1xx.x or higher
aws --version       # aws-cli/2.x
gh --version        # gh version 2.x
python3 --version   # Python 3.7+
```

### Configuration
```bash
# AWS credentials
aws configure
# Enter: Access Key, Secret Key, Region (us-east-1), Output (json)

# GitHub authentication
gh auth login
# Follow prompts

# Python dependencies
pip3 install boto3
```

### AWS Permissions Required
- S3: CreateBucket, PutBucketPolicy, PutBucketWebsite, PutPublicAccessBlock
- CloudFront: CreateDistribution, UpdateDistribution, CreateInvalidation
- Lambda: CreateFunction, PublishVersion, UpdateFunctionCode
- IAM: CreateRole, AttachRolePolicy
- CloudFront: CreateOriginAccessControl

## Maintenance

### Update Hugo Site Content
```bash
cd project-name

# Edit content
vim content/docs/new-page.md

# Test locally
hugo server -D

# Deploy
git add .
git commit -m "Add new page"
git push  # Auto-deploys in ~60 seconds
```

### Change Password
```bash
cd project-name

# Edit Lambda function
vim lambda-auth.js
# Change authUser and authPass

# Update Lambda
zip lambda-auth.zip lambda-auth.js
aws lambda update-function-code \
  --function-name project-name-basic-auth \
  --zip-file fileb://lambda-auth.zip

# Publish new version
aws lambda publish-version \
  --function-name project-name-basic-auth

# Update CloudFront with new version ARN
# (See COMPLETE-SETUP-GUIDE.md for details)
```

### Update Hugo Theme
```bash
cd project-name/themes/hugo-book
git pull origin main
cd ../..
git add themes/hugo-book
git commit -m "Update theme"
git push
```

## Use Cases

### 1. Product Documentation
- Document product features and functionality
- Customer-facing help center
- Internal product specs

### 2. API Documentation
- REST API endpoints
- Code examples
- Authentication guides

### 3. Business Planning
- Strategic plans (like klm-plan)
- Process documentation
- Team wikis

### 4. Engineering Wikis
- Technical architecture
- Development guides
- Runbooks and procedures

### 5. Marketing Content
- Campaign planning
- Brand guidelines
- Content strategy

## Extending the Automation

The Python script can be extended to:
- Support custom Hugo themes
- Add custom domains automatically
- Configure custom Lambda functions
- Integrate with other services (Slack notifications, etc.)
- Add monitoring and alerting

Edit `/Users/mark/PycharmProjects/hugo-docs-template/deploy-hugo-docs.py` to customize.

## Reference Documentation

**In Template Directory**:
- `README.md` - Complete usage guide
- `USAGE-EXAMPLES.md` - Real-world examples
- `COMPLETE-SETUP-GUIDE.md` - Manual step-by-step process

**In klm-plan**:
- `CLAUDE.md` - Project documentation
- `SECURITY-SETUP.md` - Security implementation
- `NAVIGATION-FIX.md` - Navigation fix details
- `PERMISSIONS-SETUP.md` - Claude Code permissions

**External**:
- Hugo: https://gohugo.io/documentation/
- Hugo Book Theme: https://github.com/alex-shpak/hugo-book
- AWS CloudFront: https://docs.aws.amazon.com/cloudfront/
- Lambda@Edge: https://docs.aws.amazon.com/lambda/latest/dg/lambda-edge.html

## Summary

This automation system:
- ✅ Reduces 2-3 hours of manual work to 1 command
- ✅ Eliminates configuration errors
- ✅ Creates production-ready, secure documentation sites
- ✅ Follows AWS security best practices
- ✅ Sets up complete CI/CD pipeline
- ✅ Costs ~$2/month per site (or $0 with free tier)
- ✅ Can deploy unlimited documentation sites
- ✅ Each site is completely independent

**Perfect for**: Any project that needs secure, professional documentation hosting with minimal operational overhead.

---

**Created**: 2026-01-03
**Based on**: klm-plan setup process
**Location**: `/Users/mark/PycharmProjects/hugo-docs-template/`
**Purpose**: Reusable automation for all future documentation sites
