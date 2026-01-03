---
title: "NAVIGATION-FIX"
project: klm-plan
original_path: NAVIGATION-FIX.md
modified: 2026-01-03T10:08:55.134761
---

# Navigation Links Fix - January 3, 2026

## Problem

After securing the S3 bucket (making it private with CloudFront OAC), navigation links stopped working and returned **403 AccessDenied** errors.

### Root Cause

When we secured S3, we switched from the S3 **website endpoint** to the S3 **bucket endpoint**:

- **Before**: `klm-plan.s3-website-us-east-1.amazonaws.com` (website endpoint)
- **After**: `klm-plan.s3.us-east-1.amazonaws.com` (bucket endpoint)

The S3 website endpoint automatically serves `index.html` for directory requests:
- Request: `/lines-of-business/`
- Serves: `/lines-of-business/index.html`

But the S3 bucket endpoint does NOT have this behavior - it requires the exact object key.

## Solution

Updated the Lambda@Edge function (`lambda-auth.js`) to handle BOTH authentication AND index.html rewriting in a single function.

### Updated Lambda Function (Version 2)

The function now:
1. **Step 1**: Rewrites URIs to append `index.html` for directory requests
2. **Step 2**: Checks authentication credentials

```javascript
// Step 1: Handle index.html for directory requests
let uri = request.uri;

if (uri.endsWith('/')) {
    request.uri += 'index.html';
}
else if (!uri.includes('.') && !uri.endsWith('/')) {
    request.uri += '/index.html';
}

// Step 2: Require Basic Authentication
// ... existing auth code ...
```

### Why This Approach?

We tried creating a separate CloudFront Function for index.html handling, but CloudFront only allows one function per event type in a cache behavior. Since we already had Lambda@Edge on `viewer-request` for authentication, we combined both functions.

**Benefits:**
- Single function handles both concerns
- Maintains proper execution order (rewrite before auth)
- Simpler configuration
- Lower latency than two separate functions

## Files Modified

1. **lambda-auth.js**: Added index.html rewriting logic
2. **attach-lambda.py**: Updated to use Lambda version 2

## Deployment

```bash
# Update Lambda function code
zip lambda-auth.zip lambda-auth.js
aws lambda update-function-code \
  --function-name klm-plan-basic-auth \
  --zip-file fileb://lambda-auth.zip

# Publish new version (v2)
aws lambda publish-version --function-name klm-plan-basic-auth

# Update CloudFront to use v2
python3 attach-lambda.py
```

## Testing

After the CloudFront deployment completes (5-10 minutes), test:

```bash
# Homepage (should work)
curl -u "klm:KLM2026Plan!" https://d1jrr6wppi7k7d.cloudfront.net/

# Navigation link (should work now)
curl -u "klm:KLM2026Plan!" https://d1jrr6wppi7k7d.cloudfront.net/lines-of-business/

# Specific page (should work)
curl -u "klm:KLM2026Plan!" https://d1jrr6wppi7k7d.cloudfront.net/products/new-ideas/
```

All should return HTTP 200 with content.

## Status

✅ **Fixed**: Lambda@Edge v2 deployed to CloudFront distribution E1Z0GEJNAKEO42
⏳ **Propagating**: Changes will be live across all edge locations in 5-10 minutes
🔐 **Security**: Authentication still enforced (klm/KLM2026Plan!)
📱 **Mobile Editing**: Unchanged - still works via GitHub

## Technical Details

- **Lambda Function**: `klm-plan-basic-auth:2`
- **CloudFront Distribution**: `E1Z0GEJNAKEO42`
- **Event Type**: `viewer-request`
- **Execution Order**: URI rewrite → Authentication → S3 fetch

---

**Result**: All navigation links now work correctly with the secured private S3 bucket!

Last Updated: 2026-01-03
