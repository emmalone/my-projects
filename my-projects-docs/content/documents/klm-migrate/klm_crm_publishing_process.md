---
title: "klm_crm_publishing_process"
project: klm-migrate
original_path: docs/klm_crm_publishing_process.md
modified: 2025-12-22T14:00:56.117637
---

# KLM CRM – Hugo Publishing Process (Staging & Production)

## Purpose
This document defines the **end‑to‑end publishing workflow** for deploying a Hugo static site to **KLM staging (klmcrm)** and **production (klminsurance)** using AWS S3 and CloudFront. It is designed to:

- Support a **new MacBook** and fresh Hugo install
- Assume **AWS CLI credentials are already configured** (but provide verification steps)
- Clearly identify **what credentials are required vs. not required**
- Provide **safe, repeatable steps** to fully replace (delete + upload) S3 site content
- Align with the established **script‑driven KLM workflow**

All credentials are documented with **placeholders** where sensitive data is not available or should not be stored.

---

## High‑Level Architecture

```
Local MacBook
  └─ Hugo site (source)
      └─ hugo build
          └─ public/ (static output)
              └─ aws s3 sync --delete
                  └─ S3 bucket (private)
                      └─ CloudFront distribution
```

Key principle: **S3 is private**, CloudFront is the public entry point.

---

## Environments

| Environment | Domain | S3 Bucket | Base URL |
|------------|-------|-----------|---------|
| Staging | www.klmcrm.com | s3://klmcrm.com | https://www.klmcrm.com |
| Production | www.klminsurance.com | s3://klminsurance.com | https://www.klminsurance.com |

---

## Required Software (Mac)

Verify the following are installed:

```bash
hugo version
aws --version
python3 --version
git --version
```

Expected:
- Hugo ≥ extended version
- AWS CLI v2
- Python 3.9+ (Anaconda acceptable)

---

## AWS Credentials (Placeholders)

### AWS Account

```
AWS Account ID: <AWS_ACCOUNT_ID>
AWS Region: us-east-1
```

### IAM Identity (CLI)

The AWS CLI **must already be authenticated**.

```
IAM User or Role Name: <IAM_PRINCIPAL_NAME>
Access Type: programmatic (CLI)
```

**No access keys are required in this document.**

---

## Required IAM Permissions

The publishing principal must have at minimum:

```json
{
  "Effect": "Allow",
  "Action": [
    "s3:ListBucket",
    "s3:GetObject",
    "s3:PutObject",
    "s3:DeleteObject"
  ],
  "Resource": [
    "arn:aws:s3:::klmcrm.com",
    "arn:aws:s3:::klmcrm.com/*",
    "arn:aws:s3:::klminsurance.com",
    "arn:aws:s3:::klminsurance.com/*"
  ]
}
```

Optional but recommended:

```json
{
  "Effect": "Allow",
  "Action": "cloudfront:CreateInvalidation",
  "Resource": "*"
}
```

---

## Verification – AWS CLI Setup

Run **before publishing**:

```bash
aws sts get-caller-identity
```

Expected output:

```
Account: <AWS_ACCOUNT_ID>
Arn: arn:aws:iam::<AWS_ACCOUNT_ID>:user/<IAM_PRINCIPAL_NAME>
```

If this fails, publishing **will not work**.

---

## Hugo Site Verification

From the Hugo project root:

```bash
hugo env
hugo config
```

Confirm:
- Correct theme loaded
- No hard‑coded baseURL (or overridden via flags)

---

## Build Commands

### Staging Build

```bash
hugo \
  --baseURL="https://www.klmcrm.com" \
  --environment staging \
  --destination public
```

### Production Build

```bash
hugo \
  --baseURL="https://www.klminsurance.com" \
  --environment production \
  --destination public
```

---

## Pre‑Publish Safety Check (Optional)

List existing objects:

```bash
aws s3 ls s3://klmcrm.com --recursive | head
```

---

## Publish to Staging (FULL REPLACE)

This **deletes all existing content** and replaces it.

```bash
aws s3 sync public/ s3://klmcrm.com \
  --delete
```

Notes:
- `--delete` removes stale files
- Bucket must be private

---

## Publish to Production (FULL REPLACE)

```bash
aws s3 sync public/ s3://klminsurance.com \
  --delete
```

---

## CloudFront Cache Invalidation (Recommended)

```bash
aws cloudfront create-invalidation \
  --distribution-id <CLOUDFRONT_DISTRIBUTION_ID> \
  --paths "/*"
```

Placeholders:

```
Staging Distribution ID: <CF_DIST_ID_STAGING>
Production Distribution ID: <CF_DIST_ID_PROD>
```

---

## Post‑Publish Validation

1. Load homepage in browser
2. View page source → confirm updated build timestamp
3. Spot‑check:
   - Navigation
   - CSS/JS loading
   - Images

---

## What Is *Not* Needed

- ❌ No S3 public ACLs
- ❌ No manual file uploads
- ❌ No AWS Console interaction
- ❌ No credentials embedded in Hugo

If `aws sts get-caller-identity` works, **you are authorized**.

---

## Common Failure Points

| Issue | Cause |
|-----|------|
| AccessDenied | Missing IAM permissions |
| Old content | Forgot `--delete` |
| Wrong URLs | baseURL mismatch |
| 403 errors | CloudFront origin misconfigured |

---

## Recommended Next Step

Automate the above into:

```
workflow/publish_to_staging.py
workflow/publish_to_production.py
```

Using the existing **KLM script‑driven workflow**.

---

## Summary

You are correctly positioned to:
- Publish from a **new MacBook**
- Fully replace S3 site content
- Operate without exposing credentials
- Validate configuration before deployment

This process is **safe, repeatable, and production‑grade**.

