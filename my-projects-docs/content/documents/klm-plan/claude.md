---
title: "claude"
project: klm-plan
original_path: claude.md
modified: 2026-01-03T10:58:04.557385
---

# KLM Business Plan - Project Documentation

## Project Overview
This repository contains business planning documents, product ideas, and strategic planning for KLM Insurance. The content is organized using Hugo and published automatically to AWS S3 for easy access and collaboration.

## Repository Structure
```
klm-plan/
├── content/              # Hugo content (markdown files)
│   ├── _index.md        # Homepage
│   ├── lines-of-business/
│   │   ├── personal-lines/
│   │   │   ├── auto.md
│   │   │   ├── home.md
│   │   │   ├── boat.md
│   │   │   └── liability.md
│   │   ├── commercial-lines/
│   │   │   ├── apartments.md
│   │   │   └── bop.md
│   │   └── life-insurance/
│   ├── products/
│   │   ├── new-ideas/
│   │   ├── digital-life-vault/
│   │   └── worst-case-scenario-planner/
│   │       ├── document-collection.md
│   │       └── survivorship-playbook.md
│   ├── marketing/
│   │   ├── facebook.md
│   │   └── plan.md
│   └── sales-operations/
│       ├── sales-process.md
│       └── comp.md
├── static/              # Static assets (images, PDFs)
├── themes/              # Hugo theme
├── config.toml          # Hugo configuration
└── .github/
    └── workflows/
        └── deploy.yml   # Auto-deployment to S3
```

## Workflow

### 1. Creating/Editing Content
Content is written in Markdown format. Each page should include frontmatter:

```markdown
---
title: "Page Title"
date: 2026-01-02
draft: false
tags: ["product", "planning"]
---

Your content here...
```

### 2. Local Development
```bash
# Start Hugo development server
hugo server -D

# View site at http://localhost:1313
```

### 3. Publishing Content

#### From Desktop:
```bash
# Add and commit changes
git add .
git commit -m "Description of changes"
git push origin main

# GitHub Actions automatically builds and deploys to S3
```

#### From iPhone:
1. Use GitHub mobile app or web interface
2. Navigate to the file you want to edit
3. Tap "Edit" (pencil icon)
4. Make changes in markdown
5. Commit directly to main branch
6. GitHub Actions automatically deploys within 1-2 minutes

### 4. AWS S3 Hosting
- **Bucket**: klm-plan
- **Region**: us-east-1 (or your preferred region)
- **Website URL**: http://klm-plan.s3-website-us-east-1.amazonaws.com
- **CloudFront**: Optional CDN for HTTPS and custom domain

## Hugo Theme
Using **hugo-book** theme - a clean, documentation-focused theme ideal for wiki-style content:
- Clean navigation sidebar
- Search functionality
- Mobile-responsive
- Table of contents for long pages
- Nested page support

## Key Features

### Auto-Deployment Pipeline
1. Push to GitHub (from any device)
2. GitHub Actions triggers
3. Hugo builds static site
4. Files sync to S3
5. CloudFront cache invalidated
6. Secure site updated in ~60-90 seconds

### Mobile Editing
- GitHub mobile app allows full markdown editing
- Can create new files and folders
- Commit messages track all changes
- Preview changes in GitHub before committing

### Version Control Benefits
- Complete history of all changes
- Can revert to any previous version
- See who changed what and when
- Branch for major rewrites, merge when ready

## Common Tasks

### Add a New Product Idea
1. Navigate to `content/products/new-ideas/`
2. Create new file: `product-name.md`
3. Add frontmatter and content
4. Commit and push

### Reorganize Content
1. Move files in Git (preserves history)
2. Update internal links
3. Commit with descriptive message

### Add Images or PDFs
1. Place in `static/` folder
2. Reference in markdown: `![Alt text](/image.png)`
3. For PDFs: `[Download PDF](/document.pdf)`

## Environment Setup

### Prerequisites
- Git installed and configured
- GitHub CLI authenticated
- AWS CLI configured with appropriate credentials
- Hugo installed (extended version)

### Initial Setup Commands
```bash
# Install Hugo (macOS)
brew install hugo

# Verify installation
hugo version

# Clone repository
gh repo clone yourusername/klm-plan
cd klm-plan

# Install theme as submodule
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book

# Start local server
hugo server -D
```

### AWS Configuration
```bash
# Configure AWS credentials
aws configure

# Create S3 bucket
aws s3 mb s3://klm-plan --region us-east-1

# Enable static website hosting
aws s3 website s3://klm-plan \
  --index-document index.html \
  --error-document 404.html

# Set bucket policy for public read
# (Policy JSON provided in deployment workflow)
```

## Deployment

### GitHub Actions Workflow
Located in `.github/workflows/deploy.yml`:
- Triggers on push to main branch
- Builds Hugo site
- Syncs to S3 bucket
- Invalidates CloudFront cache (if configured)

### Manual Deployment
```bash
# Build site
hugo --minify

# Sync to S3
aws s3 sync public/ s3://klm-plan --delete

# Optional: Invalidate CloudFront
aws cloudfront create-invalidation \
  --distribution-id YOUR_DIST_ID \
  --paths "/*"
```

## Best Practices

### Content Organization
- Use descriptive file names (lowercase, hyphens)
- Keep folder structure shallow (max 3-4 levels)
- Use tags and categories for cross-linking
- Include table of contents for long documents

### Writing Style
- Use headers (##, ###) for structure
- Include links to related pages
- Add dates to time-sensitive content
- Use bullet points for scanability

### Version Control
- Commit often with clear messages
- Use branches for major reorganizations
- Tag releases for major milestones
- Include context in commit messages

## Troubleshooting

### Build Fails
- Check Hugo version compatibility
- Verify frontmatter syntax
- Check for broken internal links
- Review GitHub Actions logs

### S3 Access Issues
- Verify bucket policy allows public read
- Check AWS credentials in GitHub Secrets
- Confirm bucket name matches in workflow

### Mobile Editing Issues
- Use GitHub mobile app for best experience
- Preview changes before committing
- Keep commits small and focused
- Wait 1-2 min for deployment to complete

## Resources

### Documentation
- [Hugo Documentation](https://gohugo.io/documentation/)
- [Hugo Book Theme](https://github.com/alex-shpak/hugo-book)
- [GitHub Actions](https://docs.github.com/en/actions)
- [AWS S3 Static Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

### Support
- GitHub Issues: For tracking ideas and bugs
- Commit History: For understanding changes
- This Document: For workflow reference

## Permissions & Auto-Approval

All AWS, Git, Hugo, and development commands are pre-approved for Claude Code sessions. See [PERMISSIONS-SETUP.md](./PERMISSIONS-SETUP.md) for complete documentation.

**Settings Location**: `/Users/mark/PycharmProjects/.claude/settings.json`

**Auto-Approved Commands**:
- All AWS services (S3, CloudFront, Lambda, IAM, etc.)
- All Git and GitHub CLI commands
- All Hugo, npm, docker, python commands
- File operations in PycharmProjects directory
- Common development tools

**Protected Operations** (require confirmation):
- Pushing to main branch
- Editing dependency files (package.json, requirements.txt)
- Dangerous operations (rm -rf, sudo, chmod 777, etc.) are blocked

## Hugo Documentation Site Automation

This project's setup process has been automated for future use. See [HUGO-AUTOMATION-SYSTEM.md](./HUGO-AUTOMATION-SYSTEM.md) for details.

**One-Command Deployment**: Deploy new secure documentation sites with:
```bash
cd /Users/mark/PycharmProjects/hugo-docs-template
python3 deploy-hugo-docs.py --project-name my-project --username admin --password secret
```

Creates complete Hugo + S3 + CloudFront + Lambda@Edge + GitHub setup in ~15 minutes.

**Template Location**: `/Users/mark/PycharmProjects/hugo-docs-template/`

## Future Enhancements
- [ ] Custom domain with Route 53
- [ ] Search functionality
- [ ] PDF export of sections
- [ ] Commenting system (Utterances/Giscus)
- [ ] Analytics (privacy-focused)

---

Last Updated: 2026-01-03
Maintained by: Mark
