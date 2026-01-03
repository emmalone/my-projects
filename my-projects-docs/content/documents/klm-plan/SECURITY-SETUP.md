---
title: "SECURITY-SETUP"
project: klm-plan
original_path: SECURITY-SETUP.md
modified: 2026-01-02T23:31:15.125958
---

# KLM Business Plan - Security Setup

## Current Status

✅ **CloudFront Distribution Created**
- Distribution ID: `E1Z0GEJNAKEO42`
- Domain: `d1jrr6wppi7k7d.cloudfront.net`
- Status: Deployed
- HTTPS: Enabled (automatic with CloudFront)

✅ **Lambda@Edge Function Created**
- Function Name: `klm-plan-basic-auth`
- Function ARN: `arn:aws:lambda:us-east-1:837716495292:function:klm-plan-basic-auth:1`
- Purpose: Basic HTTP authentication

## Login Credentials

Once Lambda@Edge is attached to CloudFront:

**Username:** `klm`
**Password:** `KLM2026Plan!`

## Manual Step Required: Attach Lambda@Edge to CloudFront

Due to CLI complexity, please complete this final step via AWS Console:

### Option 1: AWS Console (5 minutes)

1. **Go to CloudFront Console**
   - Visit: https://console.aws.amazon.com/cloudfront/v3/home
   - Click on distribution ID: `E1Z0GEJNAKEO42`

2. **Edit Behaviors**
   - Go to the "Behaviors" tab
   - Select the default behavior (check the box)
   - Click "Edit"

3. **Add Lambda@Edge Function Association**
   - Scroll down to "Function associations"
   - Under "Viewer request":
     - CloudFront Functions: Leave empty
     - Lambda@Edge: Select "Use existing Lambda@Edge function"
     - Function ARN: Paste this exactly:
       ```
       arn:aws:lambda:us-east-1:837716495292:function:klm-plan-basic-auth:1
       ```
     - Event type: `Viewer Request`
     - Include body: Leave unchecked

4. **Save Changes**
   - Click "Save changes" at the bottom
   - Wait 5-10 minutes for deployment (CloudFront distributes to all edge locations)

5. **Test It**
   - Visit: https://d1jrr6wppi7k7d.cloudfront.net
   - You should see a login prompt
   - Enter username: `klm` / password: `KLM2026Plan!`

### Option 2: Use AWS CLI Script (Alternative)

If you prefer command line, run this Python script:

```bash
# First install boto3 if needed
pip3 install boto3

# Then create and run this script
cat > attach-lambda.py << 'EOF'
import boto3
import json

cloudfront = boto3.client('cloudfront', region_name='us-east-1')

# Get current distribution config
dist_id = 'E1Z0GEJNAKEO42'
response = cloudfront.get_distribution_config(Id=dist_id)
config = response['DistributionConfig']
etag = response['ETag']

# Add Lambda@Edge to default cache behavior
config['DefaultCacheBehavior']['LambdaFunctionAssociations'] = {
    'Quantity': 1,
    'Items': [{
        'LambdaFunctionARN': 'arn:aws:lambda:us-east-1:837716495292:function:klm-plan-basic-auth:1',
        'EventType': 'viewer-request',
        'IncludeBody': False
    }]
}

# Update distribution
cloudfront.update_distribution(
    Id=dist_id,
    DistributionConfig=config,
    IfMatch=etag
)

print("✅ Lambda@Edge attached successfully!")
print("⏳ Wait 5-10 minutes for deployment to complete")
EOF

python3 attach-lambda.py
```

## After Setup is Complete

### Your Secure URLs

**Primary URL (HTTPS with auth):**
```
https://d1jrr6wppi7k7d.cloudfront.net
```

**Old URL (will remain accessible without auth):**
```
http://klm-plan.s3-website-us-east-1.amazonaws.com
```

### Recommended: Disable Public S3 Access

Once CloudFront + Lambda@Edge is working, you can make the S3 bucket private:

```bash
# Remove public access policy
aws s3api delete-bucket-policy --bucket klm-plan

# Block all public access
aws s3api put-public-access-block \
  --bucket klm-plan \
  --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
```

Then update CloudFront to use S3 origin instead of website endpoint (requires additional configuration).

## Mobile Editing Workflow (Unchanged)

1. Edit files on GitHub (mobile app or web)
2. Commit to main branch
3. GitHub Actions deploys to S3
4. CloudFront serves the updated content (with password protection)
5. Changes visible in ~60 seconds (+ CloudFront cache time)

## Changing the Password

To change the login credentials:

1. **Edit the Lambda function code:**
   ```bash
   # Edit lambda-auth.js
   # Change authUser and authPass variables
   nano lambda-auth.js

   # Repackage
   zip lambda-auth.zip lambda-auth.js

   # Update function
   aws lambda update-function-code \
     --function-name klm-plan-basic-auth \
     --zip-file fileb://lambda-auth.zip \
     --region us-east-1

   # Publish new version
   aws lambda publish-version \
     --function-name klm-plan-basic-auth \
     --region us-east-1

   # Update CloudFront to use new version (note the version number from above)
   ```

2. **Or via AWS Console:**
   - Go to Lambda Console → klm-plan-basic-auth
   - Edit code inline
   - Deploy
   - Publish new version
   - Update CloudFront behavior to use new version ARN

## Troubleshooting

### "I don't see a login prompt"
- CloudFront deployment can take 5-15 minutes
- Check distribution status: `aws cloudfront get-distribution --id E1Z0GEJNAKEO42 | grep Status`
- Hard refresh browser (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)

### "Wrong username or password"
- Verify you're using: `klm` / `KLM2026Plan!`
- Check Lambda function code has correct credentials
- Ensure you attached the Lambda@Edge to the distribution

### "GitHub Actions failing after CloudFront setup"
- Need to add CloudFront cache invalidation (see below)

## Next Steps

1. ✅ Complete the manual Lambda@Edge attachment (above)
2. ✅ Test the login at https://d1jrr6wppi7k7d.cloudfront.net
3. ⏭️ Update GitHub Actions to invalidate CloudFront cache
4. ⏭️ (Optional) Set up custom domain
5. ⏭️ (Optional) Make S3 bucket private

---

Created: 2026-01-02
Last Updated: 2026-01-02
