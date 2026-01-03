---
title: "COMPLETE-SETUP-GUIDE"
project: klm-plan
original_path: COMPLETE-SETUP-GUIDE.md
modified: 2026-01-03T10:52:06.874376
---

# Complete Hugo Documentation Site Setup - Step-by-Step Guide

This document captures the **complete process** we followed to create a secure, production-ready Hugo documentation site with AWS hosting, HTTPS, password protection, and automated deployment.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Setup Process](#step-by-step-setup-process)
4. [Architecture](#architecture)
5. [Security Implementation](#security-implementation)
6. [Troubleshooting](#troubleshooting)
7. [What We Built](#what-we-built)

---

## Overview

### What We Built
- **Hugo static site** with hugo-book theme for documentation
- **AWS S3** for storage (completely private)
- **CloudFront** for CDN and HTTPS
- **Lambda@Edge** for password authentication + URL rewriting
- **GitHub Actions** for automated deployment
- **Secure architecture** with Origin Access Control (OAC)

### Key Features
- ✅ HTTPS encryption via CloudFront
- ✅ Password protection (basic auth)
- ✅ Private S3 bucket (no public access)
- ✅ Auto-deployment from GitHub
- ✅ Mobile editing via GitHub app
- ✅ Navigation that works correctly
- ✅ ~60-90 second deployment pipeline

---

## Prerequisites

### Local Tools
```bash
# Install Hugo (macOS)
brew install hugo

# Verify
hugo version  # Should show v0.1xx.x or higher (extended)

# Install AWS CLI
brew install awscli

# Configure AWS credentials
aws configure
# Enter: Access Key ID, Secret Access Key, Region (us-east-1), Output (json)

# Install GitHub CLI
brew install gh

# Authenticate with GitHub
gh auth login
```

### Required Access
- AWS account with programmatic access
- GitHub account
- Permissions to create: S3 buckets, CloudFront distributions, Lambda functions, IAM roles

---

## Step-by-Step Setup Process

### Phase 1: Create Hugo Site Locally

#### 1. Initialize Hugo Site
```bash
# Create new site
hugo new site project-name
cd project-name

# Initialize git
git init

# Add hugo-book theme as submodule
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book
```

#### 2. Configure Hugo (hugo.toml)
```toml
baseURL = 'http://localhost:1313/'  # Will update later with CloudFront URL
languageCode = 'en-us'
title = 'Project Name Documentation'
theme = 'hugo-book'

# Book theme configuration
[params]
  BookRepo = 'https://github.com/username/project-name'
  BookSearch = true
  BookToC = true
  BookComments = false

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
  [markup.tableOfContents]
    startLevel = 1
```

#### 3. Create Content Structure
```bash
# Create homepage
hugo new _index.md

# Create content sections
hugo new lines-of-business/_index.md
hugo new products/_index.md
hugo new marketing/_index.md
hugo new sales-operations/_index.md
```

Example `content/_index.md`:
```markdown
---
title: "Home"
type: docs
---

# Welcome to Project Documentation

Your content here...
```

#### 4. Test Locally
```bash
hugo server -D

# Visit http://localhost:1313
# Verify navigation, content, theme
```

---

### Phase 2: AWS S3 Setup (Initial - Public Website)

#### 1. Create S3 Bucket
```bash
# Create bucket (use unique name)
aws s3 mb s3://project-name --region us-east-1
```

#### 2. Enable Static Website Hosting (Initially)
```bash
aws s3 website s3://project-name \
  --index-document index.html \
  --error-document 404.html
```

#### 3. Make Bucket Public (Temporarily)
```bash
# Disable public access blocks (temporary)
aws s3api put-public-access-block \
  --bucket project-name \
  --public-access-block-configuration \
  "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

# Create public bucket policy
cat > bucket-policy-public.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::project-name/*"
  }]
}
EOF

aws s3api put-bucket-policy \
  --bucket project-name \
  --policy file://bucket-policy-public.json
```

#### 4. Build and Deploy Hugo Site
```bash
# Build site
hugo --minify

# Sync to S3
aws s3 sync public/ s3://project-name --delete
```

#### 5. Test Public Website
```bash
# Get website URL
aws s3api get-bucket-website --bucket project-name

# Visit: http://project-name.s3-website-us-east-1.amazonaws.com
```

---

### Phase 3: GitHub Repository Setup

#### 1. Create GitHub Repository
```bash
# Create repo
gh repo create project-name --public --source=. --remote=origin

# Add files
git add .
git commit -m "Initial commit: Hugo site with hugo-book theme"

# Push
git push -u origin main
```

#### 2. Configure GitHub Secrets for AWS
```bash
# Add AWS credentials as secrets
gh secret set AWS_ACCESS_KEY_ID
# Paste your AWS access key when prompted

gh secret set AWS_SECRET_ACCESS_KEY
# Paste your AWS secret key when prompted

gh secret set AWS_REGION
# Enter: us-east-1
```

---

### Phase 4: GitHub Actions Auto-Deployment

#### 1. Create Workflow File
```bash
mkdir -p .github/workflows
```

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy Hugo to S3 and Invalidate CloudFront

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          submodules: true
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build Hugo site
        run: hugo --minify

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ secrets.AWS_REGION }}

      - name: Sync to S3
        run: |
          aws s3 sync public/ s3://project-name \
            --delete \
            --cache-control "public, max-age=3600"

      - name: Invalidate CloudFront cache
        run: |
          aws cloudfront create-invalidation \
            --distribution-id YOUR_DISTRIBUTION_ID \
            --paths "/*"
```

#### 2. Test Deployment
```bash
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions deployment workflow"
git push

# Check deployment status
gh run list
gh run view
```

---

### Phase 5: CloudFront with HTTPS

#### 1. Create CloudFront Distribution
```bash
# Create distribution configuration
cat > cloudfront-config.json <<EOF
{
  "CallerReference": "project-name-$(date +%s)",
  "Comment": "Project Name Docs with HTTPS",
  "DefaultRootObject": "index.html",
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "S3-project-name",
      "DomainName": "project-name.s3-website-us-east-1.amazonaws.com",
      "CustomOriginConfig": {
        "HTTPPort": 80,
        "HTTPSPort": 443,
        "OriginProtocolPolicy": "http-only"
      }
    }]
  },
  "DefaultCacheBehavior": {
    "TargetOriginId": "S3-project-name",
    "ViewerProtocolPolicy": "redirect-to-https",
    "AllowedMethods": {
      "Quantity": 2,
      "Items": ["HEAD", "GET"],
      "CachedMethods": {
        "Quantity": 2,
        "Items": ["HEAD", "GET"]
      }
    },
    "Compress": true,
    "ForwardedValues": {
      "QueryString": false,
      "Cookies": {"Forward": "none"}
    },
    "MinTTL": 0,
    "DefaultTTL": 86400,
    "MaxTTL": 31536000
  },
  "Enabled": true
}
EOF

# Create distribution
aws cloudfront create-distribution \
  --distribution-config file://cloudfront-config.json
```

#### 2. Get Distribution Details
```bash
# List distributions
aws cloudfront list-distributions

# Get specific distribution
aws cloudfront get-distribution --id YOUR_DIST_ID

# Note the Domain Name (e.g., d1abc123xyz.cloudfront.net)
```

#### 3. Update Hugo Config with CloudFront URL
Edit `hugo.toml`:
```toml
baseURL = 'https://d1abc123xyz.cloudfront.net/'
```

#### 4. Update GitHub Actions with Distribution ID
Edit `.github/workflows/deploy.yml` and replace `YOUR_DISTRIBUTION_ID`

---

### Phase 6: Password Protection with Lambda@Edge

#### 1. Create IAM Role for Lambda@Edge
```bash
# Create trust policy
cat > lambda-trust-policy.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": [
        "lambda.amazonaws.com",
        "edgelambda.amazonaws.com"
      ]
    },
    "Action": "sts:AssumeRole"
  }]
}
EOF

# Create role
aws iam create-role \
  --role-name project-name-lambda-edge-role \
  --assume-role-policy-document file://lambda-trust-policy.json

# Attach execution policy
aws iam attach-role-policy \
  --role-name project-name-lambda-edge-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

#### 2. Create Lambda Function Code
Create `lambda-auth.js`:
```javascript
'use strict';

// Basic Authentication for CloudFront
// Username: your-username
// Password: your-password

exports.handler = (event, context, callback) => {
    const request = event.Records[0].cf.request;
    const headers = request.headers;

    // Step 1: Handle index.html for directory requests
    // This fixes navigation links when using S3 bucket origin
    let uri = request.uri;

    // If URI ends with '/', append 'index.html'
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    }
    // If URI has no file extension, append '/index.html'
    else if (!uri.includes('.') && !uri.endsWith('/')) {
        request.uri += '/index.html';
    }

    // Step 2: Require Basic Authentication
    const authUser = 'your-username';
    const authPass = 'your-password';
    const authString = 'Basic ' + Buffer.from(authUser + ':' + authPass).toString('base64');

    if (typeof headers.authorization == 'undefined' || headers.authorization[0].value != authString) {
        const response = {
            status: '401',
            statusDescription: 'Unauthorized',
            body: 'Unauthorized',
            headers: {
                'www-authenticate': [{key: 'WWW-Authenticate', value:'Basic realm="Project Docs"'}]
            },
        };
        callback(null, response);
    }

    // Continue request processing if authenticated
    callback(null, request);
};
```

#### 3. Deploy Lambda Function
```bash
# Package function
zip lambda-auth.zip lambda-auth.js

# Create function (MUST be in us-east-1 for Lambda@Edge)
aws lambda create-function \
  --region us-east-1 \
  --function-name project-name-basic-auth \
  --runtime nodejs20.x \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/project-name-lambda-edge-role \
  --handler lambda-auth.handler \
  --zip-file fileb://lambda-auth.zip \
  --timeout 5 \
  --memory-size 128

# Publish version
aws lambda publish-version \
  --function-name project-name-basic-auth
```

#### 4. Attach Lambda to CloudFront
Create Python script `attach-lambda.py`:
```python
#!/usr/bin/env python3
import boto3
import sys

try:
    cloudfront = boto3.client('cloudfront', region_name='us-east-1')

    dist_id = 'YOUR_DISTRIBUTION_ID'
    lambda_arn = 'arn:aws:lambda:us-east-1:YOUR_ACCOUNT_ID:function:project-name-basic-auth:1'

    print(f"📡 Fetching CloudFront distribution {dist_id}...")
    response = cloudfront.get_distribution_config(Id=dist_id)
    config = response['DistributionConfig']
    etag = response['ETag']

    print("🔧 Adding Lambda@Edge function association...")
    config['DefaultCacheBehavior']['LambdaFunctionAssociations'] = {
        'Quantity': 1,
        'Items': [{
            'LambdaFunctionARN': lambda_arn,
            'EventType': 'viewer-request',
            'IncludeBody': False
        }]
    }

    print("☁️  Updating CloudFront distribution...")
    cloudfront.update_distribution(
        Id=dist_id,
        DistributionConfig=config,
        IfMatch=etag
    )

    print("\n✅ Lambda@Edge attached successfully!")
    print("⏳ Deployment in progress (takes 5-10 minutes)")

except Exception as e:
    print(f"\n❌ Error: {e}")
    sys.exit(1)
```

Run it:
```bash
python3 attach-lambda.py
```

Wait 5-10 minutes for CloudFront to deploy the Lambda function globally.

---

### Phase 7: Secure the S3 Bucket (Make Private)

#### 1. Create Origin Access Control (OAC)
```bash
# Create OAC configuration
cat > oac-config.json <<EOF
{
  "Name": "project-name-oac",
  "Description": "OAC for project-name S3 bucket",
  "SigningProtocol": "sigv4",
  "SigningBehavior": "always",
  "OriginAccessControlOriginType": "s3"
}
EOF

# Create OAC
aws cloudfront create-origin-access-control \
  --origin-access-control-config file://oac-config.json

# Note the OAC ID from output
```

#### 2. Update CloudFront to Use S3 Bucket Origin (Not Website)
```bash
# Get current config
aws cloudfront get-distribution-config \
  --id YOUR_DIST_ID > dist-config.json

# Edit dist-config.json:
# Change Origin DomainName from:
#   "project-name.s3-website-us-east-1.amazonaws.com"
# To:
#   "project-name.s3.us-east-1.amazonaws.com"
#
# Change from CustomOriginConfig to S3OriginConfig:
# {
#   "S3OriginConfig": {
#     "OriginAccessIdentity": ""
#   },
#   "OriginAccessControlId": "YOUR_OAC_ID"
# }

# Update distribution (use Python script or AWS CLI)
```

#### 3. Disable S3 Public Access
```bash
# Disable website hosting
aws s3api delete-bucket-website --bucket project-name

# Remove public policy
aws s3api delete-bucket-policy --bucket project-name

# Enable all public access blocks
aws s3api put-public-access-block \
  --bucket project-name \
  --public-access-block-configuration \
  "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

#### 4. Create CloudFront-Only Bucket Policy
```bash
cat > bucket-policy-cloudfront.json <<EOF
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "AllowCloudFrontServicePrincipal",
    "Effect": "Allow",
    "Principal": {
      "Service": "cloudfront.amazonaws.com"
    },
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::project-name/*",
    "Condition": {
      "StringEquals": {
        "AWS:SourceArn": "arn:aws:cloudfront::YOUR_ACCOUNT_ID:distribution/YOUR_DIST_ID"
      }
    }
  }]
}
EOF

aws s3api put-bucket-policy \
  --bucket project-name \
  --policy file://bucket-policy-cloudfront.json
```

---

### Phase 8: Verification and Testing

#### 1. Test S3 Direct Access (Should Fail)
```bash
curl -I http://project-name.s3-website-us-east-1.amazonaws.com
# Expected: 404 or AccessDenied (website disabled)
```

#### 2. Test CloudFront Without Auth (Should Require Password)
```bash
curl -I https://d1abc123xyz.cloudfront.net/
# Expected: HTTP 401 Unauthorized
```

#### 3. Test CloudFront With Auth (Should Work)
```bash
curl -u "username:password" https://d1abc123xyz.cloudfront.net/
# Expected: HTTP 200 OK with content
```

#### 4. Test Navigation Links
Visit in browser:
- https://d1abc123xyz.cloudfront.net/
- https://d1abc123xyz.cloudfront.net/products/
- https://d1abc123xyz.cloudfront.net/lines-of-business/

All should work correctly and require authentication.

---

## Architecture

### Data Flow
```
User Request
    ↓
CloudFront Edge Location
    ↓
Lambda@Edge (viewer-request)
    ├─ Rewrite URI (append index.html)
    └─ Check Authentication
        ↓
CloudFront Cache (if authenticated)
    ↓
S3 Bucket (via OAC - private)
    ↓
Response to User (HTTPS)
```

### Security Layers
1. **HTTPS**: All traffic encrypted via CloudFront SSL
2. **Authentication**: Lambda@Edge basic auth
3. **Private S3**: No public access, only CloudFront via OAC
4. **Public Access Blocks**: All 4 S3 protections enabled

---

## Security Implementation

### What Makes It Secure?

#### 1. S3 Bucket Security
- ✅ All public access blocks enabled
- ✅ Static website hosting disabled
- ✅ Bucket policy only allows CloudFront service principal
- ✅ Condition checks specific CloudFront distribution ARN
- ❌ No public read permissions
- ❌ No website endpoint exposed

#### 2. CloudFront Security
- ✅ HTTPS enforced (redirect-to-https)
- ✅ Lambda@Edge authentication on viewer-request
- ✅ Origin Access Control (OAC) for S3 access
- ✅ Cache compression enabled
- ❌ No direct S3 access possible

#### 3. Lambda@Edge Security
- ✅ Basic HTTP authentication
- ✅ Runs at edge locations (low latency)
- ✅ Blocks unauthenticated requests before S3 fetch
- ✅ Also handles URL rewriting for navigation

---

## Troubleshooting

### Navigation Links Return 403
**Problem**: S3 bucket endpoint doesn't auto-append index.html

**Solution**: Lambda@Edge function must handle URL rewriting:
```javascript
if (uri.endsWith('/')) {
    request.uri += 'index.html';
}
else if (!uri.includes('.') && !uri.endsWith('/')) {
    request.uri += '/index.html';
}
```

### CloudFront Deployment Taking Forever
**Normal**: Lambda@Edge deployment takes 5-15 minutes to propagate to all edge locations globally.

**Check Status**:
```bash
aws cloudfront get-distribution --id YOUR_DIST_ID --query 'Distribution.Status'
```

### S3 Sync Not Working in GitHub Actions
**Check**:
1. AWS credentials in GitHub Secrets
2. Bucket name matches in workflow
3. Distribution ID is correct for invalidation

### Lambda Function Can't Be Attached to CloudFront
**Error**: "InvalidLambdaFunctionAssociation"

**Cause**: Multiple functions on same event type (viewer-request)

**Solution**: Combine both functions (auth + URL rewrite) into one Lambda function

---

## What We Built

### File Structure
```
project-name/
├── .github/
│   └── workflows/
│       └── deploy.yml              # Auto-deployment
├── content/
│   ├── _index.md                   # Homepage
│   ├── lines-of-business/
│   ├── products/
│   ├── marketing/
│   └── sales-operations/
├── static/                          # Images, PDFs
├── themes/
│   └── hugo-book/                  # Git submodule
├── hugo.toml                        # Hugo config
├── lambda-auth.js                   # Auth + URL rewrite function
├── attach-lambda.py                 # CloudFront Lambda attachment
├── bucket-policy-cloudfront.json    # S3 security policy
├── CLAUDE.md                        # Project documentation
├── SECURITY-SETUP.md                # Security documentation
├── NAVIGATION-FIX.md                # Navigation fix documentation
└── README.md
```

### AWS Resources Created
- **S3 Bucket**: project-name (private)
- **CloudFront Distribution**: YOUR_DIST_ID
- **Lambda@Edge Function**: project-name-basic-auth:1
- **IAM Role**: project-name-lambda-edge-role
- **Origin Access Control**: project-name-oac

### Credentials & Access
- **CloudFront URL**: https://d1abc123xyz.cloudfront.net
- **Username**: (configured in lambda-auth.js)
- **Password**: (configured in lambda-auth.js)
- **S3 Direct Access**: Blocked (returns 404)

---

## Cost Estimate (Monthly)

### Typical Usage
- S3 Storage: $0.50 (20GB)
- S3 Requests: $0.10 (10k requests)
- CloudFront Data Transfer: $2.00 (20GB out)
- CloudFront Requests: $0.20 (200k requests)
- Lambda@Edge: $0.50 (200k invocations)
- **Total**: ~$3.30/month

### Free Tier Benefits (First 12 Months)
- S3: 5GB storage, 20k GET, 2k PUT
- CloudFront: 1TB transfer, 10M requests
- Lambda: 1M requests, 400k GB-seconds
- **Potential Cost**: $0-1/month with free tier

---

## Next Steps

1. **Custom Domain** (Optional)
   - Register domain in Route 53
   - Request ACM certificate
   - Update CloudFront with custom domain and certificate

2. **Enhanced Security**
   - Implement OAuth instead of basic auth
   - Add IP allowlisting
   - Enable WAF for additional protection

3. **Monitoring**
   - Set up CloudWatch alarms for errors
   - Enable CloudFront access logs
   - Monitor costs with AWS Budgets

4. **Content Management**
   - Create content templates
   - Document content structure
   - Set up review process

---

**Created**: 2026-01-03
**Project**: klm-plan
**Purpose**: Complete reference for recreating secure Hugo documentation sites

This guide documents every step, every command, and every decision made during the setup process.
