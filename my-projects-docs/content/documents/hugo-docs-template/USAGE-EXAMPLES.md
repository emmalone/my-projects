---
title: "USAGE-EXAMPLES"
project: hugo-docs-template
original_path: USAGE-EXAMPLES.md
modified: 2026-01-03T10:56:20.075421
---

# Hugo Docs Automation - Usage Examples

Real-world examples of deploying documentation sites with the automation system.

## Example 1: Deploy KLM Business Plan Documentation

```bash
# Navigate to template directory
cd /Users/mark/PycharmProjects/hugo-docs-template

# Deploy
python3 deploy-hugo-docs.py \
  --project-name klm-business-plan \
  --username klm \
  --password KLM2026Plan!

# Output:
# 🚀 Starting deployment for klm-business-plan
# 📦 Bucket: klm-business-plan-docs
# 👤 GitHub: emmalone/klm-business-plan
# 🔐 Auth: klm:***************
#
# ... (deployment process)
#
# 🎉 DEPLOYMENT COMPLETE!
# ============================================================
# 📦 Project: klm-business-plan
# 🪣 S3 Bucket: klm-business-plan-docs (private)
# ☁️  CloudFront: E1Z0GEJNAKEO42
# 🌐 URL: https://d1jrr6wppi7k7d.cloudfront.net
# 🔐 Username: klm
# 🔐 Password: KLM2026Plan!
# 📚 GitHub: https://github.com/emmalone/klm-business-plan
```

### What This Creates

**Local Structure**:
```
klm-business-plan/
├── content/
│   ├── _index.md
│   ├── about/_index.md
│   ├── docs/_index.md
│   ├── guides/_index.md
│   └── reference/_index.md
├── themes/hugo-book/
├── hugo.toml
└── .github/workflows/deploy.yml
```

**AWS Resources**:
- S3: `klm-business-plan-docs` (us-east-1)
- CloudFront: Distribution with HTTPS
- Lambda@Edge: Password protection
- IAM Role: Lambda execution role

**Access**:
- URL: https://d1jrr6wppi7k7d.cloudfront.net
- Login: klm / KLM2026Plan!

---

## Example 2: Deploy Product Documentation

For a product called "Life & Legacy Platform":

```bash
python3 deploy-hugo-docs.py \
  --project-name life-legacy-platform \
  --username product \
  --password ProductDocs2026!
```

### Customize Content After Deployment

```bash
cd life-legacy-platform

# Create product sections
hugo new products/digital-vault.md
hugo new products/survivorship-playbook.md
hugo new products/beneficiary-review.md

# Edit content
vim content/products/digital-vault.md
```

Content example:
```markdown
---
title: "Digital Life & Legacy Vault"
weight: 1
---

# Digital Life & Legacy Vault

## Overview
A secure portal where clients store key documents...

## Features
- Document storage (policies, wills, passwords)
- Contact list of advisors
- Funeral preferences
- Letter-to-family
```

### Commit and Deploy

```bash
git add .
git commit -m "Add product documentation"
git push  # Auto-deploys in ~60 seconds
```

---

## Example 3: Deploy API Documentation

```bash
python3 deploy-hugo-docs.py \
  --project-name api-documentation \
  --username developer \
  --password DevApiDocs2026!
```

### Add API Reference Structure

```bash
cd api-documentation

# Create API sections
mkdir -p content/api/{authentication,endpoints,examples}

# Create endpoint docs
hugo new api/endpoints/create-user.md
hugo new api/endpoints/get-user.md
hugo new api/endpoints/update-user.md
```

Example endpoint documentation:
```markdown
---
title: "Create User"
weight: 1
---

# POST /api/v1/users

Create a new user account.

## Request

\`\`\`http
POST /api/v1/users
Content-Type: application/json
Authorization: Bearer YOUR_TOKEN

{
  "email": "user@example.com",
  "name": "John Doe",
  "role": "admin"
}
\`\`\`

## Response

\`\`\`json
{
  "id": "usr_123",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "admin",
  "created_at": "2026-01-03T10:30:00Z"
}
\`\`\`
```

---

## Example 4: Deploy to Different AWS Region

For EU-based documentation:

```bash
python3 deploy-hugo-docs.py \
  --project-name eu-compliance-docs \
  --username compliance \
  --password EUCompliance2026! \
  --region eu-west-1
```

**Resources Created**:
- S3 Bucket: `eu-compliance-docs-docs` in eu-west-1
- CloudFront: Global distribution (automatically uses EU edge locations)
- Lambda@Edge: Runs in us-east-1 (requirement), executes at edge

---

## Example 5: Deploy for Specific GitHub Organization

For a company organization:

```bash
python3 deploy-hugo-docs.py \
  --project-name company-handbook \
  --username employee \
  --password CompanyHandbook2026! \
  --github-org acme-corporation
```

**Result**:
- GitHub Repo: `github.com/acme-corporation/company-handbook`
- Can be used with organization's GitHub Enterprise

---

## Example 6: Deploy Multiple Projects

Deploy separate docs sites for different projects:

```bash
# Product docs
python3 deploy-hugo-docs.py \
  --project-name product-docs \
  --username product \
  --password ProductPass123!

# Engineering docs
python3 deploy-hugo-docs.py \
  --project-name engineering-docs \
  --username engineer \
  --password EngineerPass123!

# Marketing docs
python3 deploy-hugo-docs.py \
  --project-name marketing-docs \
  --username marketing \
  --password MarketingPass123!
```

Each gets:
- Separate S3 bucket
- Separate CloudFront distribution
- Separate GitHub repository
- Independent credentials

---

## Common Workflows

### Workflow 1: Daily Documentation Updates

```bash
# Edit content on desktop
cd my-project
vim content/docs/feature-guide.md

# Test locally
hugo server -D
# Visit http://localhost:1313

# Deploy
git add .
git commit -m "Update feature guide"
git push

# Site updates in ~60 seconds
```

### Workflow 2: Mobile Quick Fix

1. Open GitHub mobile app
2. Find file: `content/docs/troubleshooting.md`
3. Edit → Fix typo
4. Commit directly to main
5. Wait ~60 seconds
6. Refresh docs site to see change

### Workflow 3: Adding Images

```bash
cd my-project

# Add image to static folder
cp ~/Downloads/architecture-diagram.png static/images/

# Reference in markdown
vim content/docs/architecture.md
```

Markdown:
```markdown
## System Architecture

![Architecture Diagram](/images/architecture-diagram.png)
```

Commit and push:
```bash
git add static/images/architecture-diagram.png content/docs/architecture.md
git commit -m "Add architecture diagram"
git push
```

### Workflow 4: Bulk Content Migration

```bash
cd my-project

# Copy existing docs
cp -r ~/old-docs/content/* content/

# Verify structure
tree content/

# Test locally
hugo server -D

# Deploy
git add content/
git commit -m "Migrate existing documentation"
git push
```

---

## Advanced Customization

### Custom Theme Configuration

After deployment, customize the hugo-book theme:

```bash
cd my-project
vim hugo.toml
```

Add custom params:
```toml
[params]
  BookRepo = 'https://github.com/user/my-project'
  BookSearch = true
  BookToC = true
  BookComments = false
  BookMenuBundle = '/menu'
  BookSection = 'docs'
  BookLogo = '/logo.png'
```

### Custom Menu Structure

Create `content/menu/index.md`:
```markdown
---
headless: true
---

- [**Products**]({{< relref "/products" >}})
  - [Digital Vault]({{< relref "/products/digital-vault" >}})
  - [Survivorship Playbook]({{< relref "/products/survivorship-playbook" >}})

- [**API Reference**]({{< relref "/api" >}})
  - [Authentication]({{< relref "/api/auth" >}})
  - [Endpoints]({{< relref "/api/endpoints" >}})
```

### Custom Styling

Create custom CSS:
```bash
mkdir -p static/css
vim static/css/custom.css
```

```css
:root {
  --color-primary: #0066cc;
  --color-link: #0066cc;
}

.book-brand {
  color: var(--color-primary);
  font-weight: bold;
}
```

Reference in `hugo.toml`:
```toml
[params]
  BookCustomCSS = ['/css/custom.css']
```

---

## Integration Examples

### Integrate with Existing Hugo Site

If you already have a Hugo site and want to add secure AWS hosting:

```bash
# Navigate to existing site
cd my-existing-hugo-site

# Ensure hugo-book theme is installed
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book

# Run just the AWS deployment parts
# (manually run the S3, CloudFront, Lambda steps from deploy script)

# Or: Use deploy script and skip Hugo setup
# Edit deploy-hugo-docs.py to skip create_hugo_site() step
```

### Integrate with CI/CD Pipeline

Use the GitHub Actions workflow as a template for other CI/CD systems:

**GitLab CI** (`.gitlab-ci.yml`):
```yaml
deploy:
  stage: deploy
  image: klakegg/hugo:ext-alpine
  script:
    - hugo --minify
    - aws s3 sync public/ s3://my-bucket --delete
    - aws cloudfront create-invalidation --distribution-id XYZ --paths "/*"
  only:
    - main
```

**Jenkins** (Jenkinsfile):
```groovy
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'hugo --minify'
      }
    }
    stage('Deploy') {
      steps {
        sh 'aws s3 sync public/ s3://my-bucket --delete'
        sh 'aws cloudfront create-invalidation --distribution-id XYZ --paths "/*"'
      }
    }
  }
}
```

---

## Troubleshooting Examples

### Example 1: Bucket Name Already Taken

**Error**:
```
ClientError: An error occurred (BucketAlreadyExists) when calling CreateBucket
```

**Solution**: Choose a more unique project name
```bash
# Instead of:
python3 deploy-hugo-docs.py --project-name docs ...

# Use:
python3 deploy-hugo-docs.py --project-name acme-product-docs ...
```

### Example 2: GitHub Authentication Failed

**Error**:
```
⚠️  Could not determine GitHub username. Please login with: gh auth login
```

**Solution**:
```bash
gh auth login
# Follow prompts to authenticate
# Then re-run deployment script
```

### Example 3: IAM Permissions Issue

**Error**:
```
ClientError: User is not authorized to perform: cloudfront:CreateDistribution
```

**Solution**: Add CloudFront permissions to IAM user
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "cloudfront:*",
      "s3:*",
      "lambda:*",
      "iam:CreateRole",
      "iam:AttachRolePolicy"
    ],
    "Resource": "*"
  }]
}
```

---

## Next Steps After Deployment

### 1. Customize Content Structure

```bash
cd my-project

# Create your own sections
hugo new section1/_index.md
hugo new section2/_index.md

# Add pages
hugo new section1/topic1.md
hugo new section1/topic2.md
```

### 2. Set Up Monitoring

```bash
# Enable CloudFront logging
aws cloudfront update-distribution \
  --id YOUR_DIST_ID \
  --logging-config Enabled=true,Bucket=logs-bucket.s3.amazonaws.com,Prefix=cloudfront/

# Set up CloudWatch alarms
aws cloudwatch put-metric-alarm \
  --alarm-name high-error-rate \
  --metric-name 5xxErrorRate \
  --namespace AWS/CloudFront \
  --statistic Average \
  --period 300 \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold
```

### 3. Add Custom Domain

```bash
# Request certificate
aws acm request-certificate \
  --domain-name docs.example.com \
  --validation-method DNS

# Update CloudFront distribution
# (Add alternate domain name and certificate ARN)

# Update Route 53
aws route53 change-resource-record-sets \
  --hosted-zone-id Z123456 \
  --change-batch file://dns-record.json
```

### 4. Enhance Security

Options:
- Replace basic auth with OAuth (Auth0, Okta)
- Add IP allowlisting to Lambda@Edge
- Enable AWS WAF for additional protection
- Set up MFA for GitHub repository

---

**Created**: 2026-01-03
**Purpose**: Real-world usage examples for Hugo docs automation
**Use Cases**: Business docs, API docs, product docs, engineering wikis
