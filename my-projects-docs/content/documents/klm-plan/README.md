---
title: "README"
project: klm-plan
original_path: README.md
modified: 2026-01-02T23:49:40.418787
---

# KLM Business Plan

A Hugo-based wiki for organizing business planning, product development, and strategic initiatives for KLM Insurance.

## Quick Links

- **🔒 Secure Site (HTTPS + Password)**: https://d1jrr6wppi7k7d.cloudfront.net
  - Username: `klm`
  - Password: `KLM2026Plan!`
- **🔐 S3 Bucket**: PRIVATE - Only accessible via CloudFront (secured with OAC)
- **Documentation**: See [claude.md](./claude.md) for complete workflow guide
- **Security Setup**: See [SECURITY-SETUP.md](./SECURITY-SETUP.md) for authentication details
- **S3 Security**: See [S3-SECURITY-COMPLETE.md](./S3-SECURITY-COMPLETE.md) for security implementation

## What's Inside

This repository contains structured business planning documentation for:

- **Lines of Business**: Personal Lines, Commercial Lines, Life Insurance
- **Product Innovation**: Life & Legacy Platform development
- **Marketing**: Strategy and campaign planning
- **Sales Operations**: Process and compensation structures

## Quick Start

### View Locally

```bash
# Clone the repository
git clone <your-repo-url>
cd klm-plan

# Initialize theme submodule
git submodule update --init --recursive

# Start Hugo server
hugo server -D

# View at http://localhost:1313
```

### Editing Content

#### From Desktop
1. Edit markdown files in `content/` directory
2. Commit and push to main branch
3. GitHub Actions automatically deploys to S3

#### From iPhone
1. Open GitHub mobile app or github.com
2. Navigate to the file you want to edit
3. Tap the pencil icon to edit
4. Commit changes
5. Site auto-deploys in 1-2 minutes

## Content Structure

```
content/
├── lines-of-business/
│   ├── personal-lines/
│   ├── commercial-lines/
│   └── life-insurance/
├── products/
│   ├── new-ideas/
│   ├── digital-life-vault/
│   └── worst-case-scenario-planner/
├── marketing/
└── sales-operations/
```

## Features

- **Auto-Deploy**: Push to GitHub, auto-publish to web
- **Mobile Editing**: Edit from anywhere via GitHub
- **Search**: Built-in search functionality
- **Version Control**: Complete history of all changes
- **Organized**: Hierarchical navigation structure

## Technology Stack

- **Static Site Generator**: Hugo (extended version)
- **Theme**: hugo-book (wiki-style)
- **Hosting**: AWS S3 static website hosting
- **CI/CD**: GitHub Actions
- **Version Control**: Git/GitHub

## Contributing

1. Create a new branch for major changes
2. Edit content in markdown format
3. Include proper frontmatter in all pages
4. Test locally with `hugo server`
5. Submit pull request or commit directly to main

## Deployment

Automatic deployment happens on every push to `main` branch:

1. GitHub Actions triggers
2. Hugo builds static site
3. Files sync to S3 bucket
4. Site is live in ~60 seconds

### Manual Deployment

```bash
# Build site
hugo --minify

# Deploy to S3
aws s3 sync public/ s3://klm-plan --delete
```

## Environment Setup

### Required Tools
- Git
- Hugo (extended version)
- AWS CLI (configured)
- GitHub CLI (optional)

### Installation (macOS)

```bash
# Install Hugo
brew install hugo

# Install AWS CLI
brew install awscli

# Configure AWS
aws configure
```

## GitHub Secrets

For automated deployment, configure these secrets in GitHub:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Support

- Questions: Open an issue
- Documentation: See [claude.md](./claude.md)
- Hugo Docs: https://gohugo.io/documentation/

## License

Internal use only - KLM Insurance business planning documentation.

---

Last updated: 2026-01-02
