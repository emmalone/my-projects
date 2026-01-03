---
title: "DEPLOYMENT"
project: klm-migrate
original_path: klm-hugo-site/docs/DEPLOYMENT.md
modified: 2026-01-01T17:26:07.717618
---

# Deployment Guide - Three Environment Setup

## Overview

Your repository is configured with **three separate environments** for a professional development workflow:

| Environment | S3 Bucket | Deploys From | Purpose |
|-------------|-----------|--------------|---------|
| **DEV** | `S3_DEV_BUCKET` | `claude/*` branches | Your iteration & testing |
| **STAGING** | `S3_STAGING_BUCKET` | `staging` branch | Business review |
| **PRODUCTION** | `S3_PROD_BUCKET` | `main` branch | Live customer site |

## How It Works

### DEV Environment (Rapid Iteration)
1. **You make changes** via Claude Code on your iPhone
2. **Changes are pushed** to a `claude/*` branch (automatic)
3. **GitHub Actions triggers** and builds the Hugo site
4. **Site is deployed** to your S3 DEV bucket
5. **You preview** immediately on your iPhone at dev.klm-insurance.com

### STAGING Environment (Business Review)
1. **You create a PR** from your `claude/*` branch to `staging`
2. **You review and merge** the PR
3. **GitHub Actions deploys** to S3 STAGING bucket
4. **Business users review** at staging.klm-insurance.com

### PRODUCTION Environment (Live Site)
1. **Business approves** features on staging
2. **You create PR** from `staging` to `main`
3. **You merge** after final review
4. **GitHub Actions deploys** to S3 PRODUCTION bucket
5. **Site is live** at klm-insurance.com

**See DEVELOPMENT_WORKFLOW.md for complete workflow details.**

## Initial Setup (One-Time Only)

You need to configure AWS credentials in your GitHub repository:

### Step 1: Create AWS IAM User (if you don't have one)

1. Go to AWS Console → IAM → Users
2. Create new user: `github-actions-klm-deploy`
3. Attach policy: `AmazonS3FullAccess` (or create custom policy - see below)
4. Create access keys
5. **Save the Access Key ID and Secret Access Key**

### Step 2: Add Secrets to GitHub

1. Go to: https://github.com/emmalone/klm-migrate/settings/secrets/actions
2. Click "New repository secret"
3. Add these secrets:

   **Required Secrets:**
   - Name: `AWS_ACCESS_KEY_ID`
     Value: [Your AWS Access Key ID]

   - Name: `AWS_SECRET_ACCESS_KEY`
     Value: [Your AWS Secret Access Key]

   - Name: `AWS_REGION`
     Value: `us-east-1` (or your S3 bucket region)

   - Name: `S3_DEV_BUCKET`
     Value: [Your dev bucket name, e.g., `klm-dev`]

   - Name: `S3_STAGING_BUCKET`
     Value: [Your staging bucket name, e.g., `klm-staging`]

   - Name: `S3_PROD_BUCKET` (optional for now)
     Value: [Your production bucket name, e.g., `klm-production`]

### Step 3: Add Variables (Optional but Recommended)

1. Go to: https://github.com/emmalone/klm-migrate/settings/variables/actions
2. Click "New repository variable"
3. Add these variables:

   - Name: `DEV_URL`
     Value: [Your dev site URL, e.g., `https://dev.klm-insurance.com`]

   - Name: `STAGING_URL`
     Value: [Your staging site URL, e.g., `https://staging.klm-insurance.com`]

   - Name: `CLOUDFRONT_DEV_DISTRIBUTION_ID` (if using CloudFront for dev)
     Value: [Your dev CloudFront distribution ID, e.g., `E1234567890ABC`]

   - Name: `CLOUDFRONT_DISTRIBUTION_ID` (if using CloudFront for staging)
     Value: [Your staging CloudFront distribution ID, e.g., `E9876543210XYZ`]

## Custom IAM Policy (Recommended for Security)

Instead of `AmazonS3FullAccess`, create a custom policy with minimal permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::YOUR-DEV-BUCKET-NAME",
        "arn:aws:s3:::YOUR-DEV-BUCKET-NAME/*",
        "arn:aws:s3:::YOUR-STAGING-BUCKET-NAME",
        "arn:aws:s3:::YOUR-STAGING-BUCKET-NAME/*",
        "arn:aws:s3:::YOUR-PROD-BUCKET-NAME",
        "arn:aws:s3:::YOUR-PROD-BUCKET-NAME/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudfront:CreateInvalidation"
      ],
      "Resource": [
        "arn:aws:cloudfront::YOUR-ACCOUNT-ID:distribution/YOUR-DEV-DISTRIBUTION-ID",
        "arn:aws:cloudfront::YOUR-ACCOUNT-ID:distribution/YOUR-STAGING-DISTRIBUTION-ID",
        "arn:aws:cloudfront::YOUR-ACCOUNT-ID:distribution/YOUR-PROD-DISTRIBUTION-ID"
      ]
    }
  ]
}
```

Replace:
- `YOUR-DEV-BUCKET-NAME` with your dev S3 bucket name (e.g., `klm-dev`)
- `YOUR-STAGING-BUCKET-NAME` with your staging S3 bucket name (e.g., `klm-staging`)
- `YOUR-PROD-BUCKET-NAME` with your production S3 bucket name (e.g., `klm-production`)
- `YOUR-ACCOUNT-ID` with your AWS account ID
- Distribution IDs for each environment (if using CloudFront)

## Usage

### Automatic Deployment to DEV

Every time you push to a branch starting with `claude/`, it automatically deploys to DEV:

```
You (on iPhone): "Create a new landing page with video"
Claude Code: [Creates files, commits, pushes to claude/create-landing-page-xyz]
GitHub Actions: [Builds and deploys to DEV]
You: Visit your DEV URL to see the new page!
```

### Automatic Deployment to STAGING

When you merge a PR to the `staging` branch, it automatically deploys to STAGING:

```
You: [Merge PR from claude/* to staging branch]
GitHub Actions: [Builds and deploys to STAGING]
Business Users: Review at your STAGING URL
```

### Manual Deployment

You can manually trigger any workflow:

1. Go to: https://github.com/emmalone/klm-migrate/actions
2. Click on the workflow you want (Dev, Staging, or Production)
3. Click "Run workflow"
4. Select the branch you want to deploy
5. Click "Run workflow"

## Viewing Your Changes

### On DEV (After pushing to claude/* branch)
After deployment completes (usually 2-3 minutes):

1. Open your DEV URL in Safari on your iPhone
2. View the landing page at: `https://dev.klm-insurance.com/landing`
3. Iterate on changes and push again - it auto-deploys to DEV!

### On STAGING (After merging PR to staging)
After deployment completes (usually 2-3 minutes):

1. Share STAGING URL with business users
2. View at: `https://staging.klm-insurance.com/landing`
3. Gather feedback and iterate as needed

## Workflow Status

Check deployment status:
- Go to: https://github.com/emmalone/klm-migrate/actions
- You'll see a list of all deployments
- Green checkmark = successful deployment
- Red X = failed (click for details)

## Troubleshooting

### Deployment Failed

1. Check the Actions tab for error messages
2. Common issues:
   - AWS credentials not set or expired
   - S3 bucket name incorrect
   - AWS region mismatch
   - Insufficient IAM permissions

### Site Not Updating

1. Check if deployment succeeded in Actions tab
2. If using CloudFront:
   - Make sure `CLOUDFRONT_DISTRIBUTION_ID` is set
   - Cache invalidation can take 5-10 minutes
3. Try hard refresh in browser (Cmd+Shift+R on desktop, or clear Safari cache on iPhone)

### Hugo Build Errors

1. Check the Actions logs for Hugo build errors
2. Test locally with `hugo --minify` to reproduce
3. Fix the issue and push again

## S3 Bucket Configuration

Your S3 bucket should be configured for static website hosting:

1. Go to S3 Console → Your Bucket → Properties
2. Scroll to "Static website hosting"
3. Enable it
4. Set:
   - Index document: `index.html`
   - Error document: `404.html`

### Bucket Policy (for public access)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::YOUR-STAGING-BUCKET-NAME/*"
    }
  ]
}
```

**Note:** If using CloudFront, you may want to restrict direct S3 access and only allow CloudFront.

## Cost Considerations

- S3 storage: Very cheap (~$0.023/GB/month)
- S3 requests: Minimal cost for low traffic
- CloudFront (if used): Free tier covers most staging use
- GitHub Actions: Free for public repos, 2000 min/month for private

## Security Best Practices

1. ✅ Use dedicated IAM user for deployments
2. ✅ Apply least-privilege IAM policy
3. ✅ Store credentials as GitHub Secrets (never in code)
4. ✅ Rotate access keys periodically
5. ✅ Use CloudFront with custom domain for production
6. ✅ Consider password-protecting staging site (CloudFront Functions or Lambda@Edge)

## Next Steps

Once this is working for staging:

1. Create a separate workflow for production deployments
2. Only trigger production on merges to `main` branch
3. Use different S3 bucket for production
4. Add approval gates for production deployments

---

**Questions?**
- Check GitHub Actions logs for detailed error messages
- Review AWS CloudWatch logs
- Refer to Hugo documentation: https://gohugo.io/hosting-and-deployment/

**Last Updated:** December 29, 2025
