# My-Projects Deployment Information

## AWS Resources

### S3 Bucket
- **Name**: my-projects-docs
- **Region**: us-east-1
- **Access**: Private (no public access)
- **Policy**: CloudFront-only access via OAC

### CloudFront Distribution
- **ID**: E1JSSE49FNQVBL
- **Domain**: d27nsh9nz210c8.cloudfront.net
- **URL**: https://d27nsh9nz210c8.cloudfront.net
- **HTTPS**: Enabled (CloudFront SSL certificate)
- **Origin Access Control**: E4MR23NF755ZT

### Lambda@Edge Function
- **Name**: my-projects-basic-auth
- **Version**: 1
- **ARN**: arn:aws:lambda:us-east-1:837716495292:function:my-projects-basic-auth:1
- **Event Type**: viewer-request
- **Purpose**: Password authentication + URL rewriting

### IAM Role
- **Name**: my-projects-lambda-edge-role
- **ARN**: arn:aws:iam::837716495292:role/my-projects-lambda-edge-role

### GitHub Repository
- **URL**: https://github.com/emmalone/my-projects
- **Auto-Deployment**: Enabled (GitHub Actions)

## Access Information

**Secure URL**: https://d27nsh9nz210c8.cloudfront.net

**Credentials**:
- Username: `mark`
- Password: `MyProjects2026!`

## What's Deployed

The site aggregates all documentation from all projects in PycharmProjects:

- **23 Projects** tracked
- **226 Markdown Files** indexed and searchable
- **Project Profiles** with tech stack and Git info
- **Cross-Project Search** enabled
- **Inventory** with statistics and breakdowns

## Deployment Process

### Manual Deployment
```bash
cd /Users/mark/PycharmProjects/my-projects

# Scan all projects (updates inventory)
python3 scan-projects.py

# Generate Hugo site from all docs
python3 generate-docs.py

# Build Hugo site
cd my-projects-docs
hugo --minify

# Deploy to S3
aws s3 sync public/ s3://my-projects-docs --delete

# Invalidate CloudFront
aws cloudfront create-invalidation \
  --distribution-id E1JSSE49FNQVBL \
  --paths "/*"
```

### Auto-Deployment (GitHub Actions)
1. Make changes to my-projects
2. Commit and push to main branch
3. GitHub Actions automatically builds and deploys
4. Site updates in ~60-90 seconds

## Updating Documentation

### Re-scan All Projects
```bash
cd /Users/mark/PycharmProjects/my-projects

# Scan for new/updated projects and markdown files
python3 scan-projects.py

# Regenerate Hugo site with latest docs
python3 generate-docs.py

# Commit and push (triggers auto-deployment)
git add .
git commit -m "Update documentation index"
git push
```

### Manual Re-deployment
```bash
# After scanning and generating
cd my-projects-docs
hugo --minify
aws s3 sync public/ s3://my-projects-docs --delete
aws cloudfront create-invalidation --distribution-id E1JSSE49FNQVBL --paths "/*"
```

## Architecture

```
User Browser
    ↓ HTTPS (443)
CloudFront (d27nsh9nz210c8.cloudfront.net)
    ↓
Lambda@Edge (viewer-request)
    ├─ 1. Rewrite URL (/docs/ → /docs/index.html)
    └─ 2. Check Password (Basic Auth: mark/MyProjects2026!)
        ↓ (authenticated)
CloudFront Cache
    ↓ (via OAC: E4MR23NF755ZT)
S3 Bucket (my-projects-docs - PRIVATE)
    └─ Hugo Site with 226 documents from 23 projects
```

## Security

- ✅ **HTTPS**: CloudFront SSL certificate
- ✅ **Authentication**: Lambda@Edge basic HTTP auth
- ✅ **Private S3**: All public access blocks enabled
- ✅ **OAC**: S3 policy allows only CloudFront service principal
- ✅ **No Direct S3 Access**: Website endpoint disabled

## Content Breakdown

### Projects by Tech Stack
- Python: 12 projects
- Hugo: 6 projects
- Node.js: 5 projects
- GitHub Actions: 8 projects
- Docker: 3 projects
- AWS Lambda: 2 projects
- AWS CloudFront: 2 projects

### Documents by Project
- klm-plan: 54 docs
- klm-migrate: 62 docs
- klm-hugo-lab: 46 docs
- klm-apartment-app: 10 docs
- backups: 17 docs
- hugo-docs-template: 3 docs
- And 17 more projects...

## Cost Estimate

### Monthly (Typical Usage)
- S3 Storage (5 GB): $0.12
- S3 Requests: $0.05
- CloudFront Transfer (20 GB): $1.70
- CloudFront Requests (100k): $0.10
- Lambda@Edge (100k): $0.20
- **Total**: ~$2.17/month

### With Free Tier
- **Cost**: $0-0.50/month

## Maintenance

### Change Password
1. Edit `/Users/mark/PycharmProjects/hugo-docs-template/my-projects/lambda-auth.js`
2. Update `authUser` and `authPass` variables
3. Redeploy Lambda function:
```bash
cd /Users/mark/PycharmProjects/hugo-docs-template/my-projects
zip lambda-auth.zip lambda-auth.js
aws lambda update-function-code \
  --function-name my-projects-basic-auth \
  --zip-file fileb://lambda-auth.zip
aws lambda publish-version --function-name my-projects-basic-auth
```

### Add New Project
New projects in PycharmProjects are automatically discovered:
```bash
cd /Users/mark/PycharmProjects/my-projects
python3 scan-projects.py
python3 generate-docs.py
git add . && git commit -m "Add new project" && git push
```

### Delete CloudFront Distribution (If Needed)
```bash
# First disable
aws cloudfront get-distribution-config --id E1JSSE49FNQVBL > dist-config.json
# Edit dist-config.json: set "Enabled": false
aws cloudfront update-distribution --id E1JSSE49FNQVBL --if-match ETAG --distribution-config file://dist-config.json

# Wait for deployment, then delete
aws cloudfront delete-distribution --id E1JSSE49FNQVBL --if-match ETAG
```

## Verification

### Test Authentication
```bash
# Should return 401 Unauthorized
curl -I https://d27nsh9nz210c8.cloudfront.net/

# Should return 200 OK
curl -u "mark:MyProjects2026!" -I https://d27nsh9nz210c8.cloudfront.net/
```

### Test S3 Direct Access (Should Fail)
```bash
# Should return 404 or AccessDenied
curl -I http://my-projects-docs.s3-website-us-east-1.amazonaws.com
```

### Check CloudFront Status
```bash
aws cloudfront get-distribution --id E1JSSE49FNQVBL --query 'Distribution.Status'
# Should return: "Deployed"
```

## Next Steps

1. ✅ **Deployed**: my-projects-docs to AWS
2. ✅ **Secured**: Private S3 with CloudFront OAC
3. ✅ **Authenticated**: Lambda@Edge password protection
4. ⏳ **Wait**: 5-10 minutes for global CloudFront deployment
5. 📝 **Test**: Visit https://d27nsh9nz210c8.cloudfront.net with credentials
6. 🔄 **Auto-Update**: Set up GitHub secrets for auto-deployment

---

**Deployed**: 2026-01-03
**Status**: Active
**Purpose**: Central documentation hub for all PycharmProjects
