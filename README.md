# My Projects - Central Hub

**Central repository for tracking all projects in PycharmProjects**

## Overview

This project serves as a meta-project that:
- Tracks all active projects in `/Users/mark/PycharmProjects`
- Maintains project status, todos, and tech stacks
- Aggregates all markdown documentation across all projects
- Hosts a comprehensive documentation website at my-projects-docs

## Structure

```
my-projects/
├── README.md                    # This file
├── projects/                    # Project inventory
│   ├── klm-plan.md             # Project profiles
│   ├── hugo-docs-template.md
│   └── my-projects.md
├── scan-projects.py             # Auto-discover projects and md files
├── generate-docs.py             # Generate Hugo docs from all md files
└── my-projects-docs/            # Hugo documentation site (auto-generated)
    ├── content/
    │   ├── projects/            # Project overviews
    │   ├── documents/           # All md files from all projects
    │   └── inventory/           # Project inventory and status
    └── hugo.toml
```

## Features

### 1. Project Inventory
- Automatic discovery of all projects in PycharmProjects
- Status tracking (active, planned, archived)
- Tech stack documentation
- Current todos and next steps
- Links to repositories

### 2. Centralized Documentation
- Aggregates ALL markdown files from ALL projects
- Organizes by project and type
- Provides summaries and full text search
- Links back to source files

### 3. Auto-Generated Documentation Site
- Hugo-powered website at my-projects-docs
- Secure HTTPS hosting via CloudFront
- Password protected
- Auto-deployment when documentation updated

## Usage

### Scan All Projects
```bash
python3 scan-projects.py
```

Discovers:
- All projects in PycharmProjects
- Git repositories and status
- Markdown files
- README contents
- Tech stack (from package.json, requirements.txt, etc.)

### Generate Documentation Site
```bash
python3 generate-docs.py
```

Creates:
- Hugo content from all markdown files
- Project inventory pages
- Document index with summaries
- Cross-project search

### Deploy Documentation Site
```bash
cd /Users/mark/PycharmProjects/hugo-docs-template
python3 deploy-hugo-docs.py \
  --project-name my-projects \
  --username mark \
  --password MyProjects2026!
```

## Automation

### Auto-Sync on Markdown File Creation
When any project creates a new .md file:
1. File is saved in local project (as normal)
2. Copy is saved to my-projects/documents/{project-name}/
3. Summary is extracted (first paragraph or frontmatter description)
4. my-projects-docs Hugo site is regenerated
5. Push to GitHub triggers auto-deployment

### Git Hook Setup (Future)
Install post-commit hook in each project:
```bash
# .git/hooks/post-commit
#!/bin/bash
python3 /Users/mark/PycharmProjects/my-projects/sync-docs.py
```

## Project Tracking

See `projects/` directory for individual project profiles.

Each project profile includes:
- **Status**: Active, Planned, On Hold, Archived
- **Description**: What the project does
- **Tech Stack**: Languages, frameworks, services
- **Current Todos**: Next steps
- **Documentation**: Links to key docs
- **Repository**: GitHub URL
- **Deployment**: Where it's deployed

## Documentation Site

**URL**: https://my-projects-docs.cloudfront.net (after deployment)
**Username**: mark
**Password**: MyProjects2026!

### Content Organization
```
my-projects-docs/
├── Projects/
│   ├── klm-plan
│   ├── hugo-docs-template
│   └── my-projects
├── Documents/
│   ├── By Project/
│   │   ├── klm-plan/
│   │   ├── hugo-docs-template/
│   │   └── ...
│   └── By Type/
│       ├── Setup Guides/
│       ├── Architecture/
│       ├── Planning/
│       └── Reference/
└── Inventory/
    ├── All Projects
    ├── Active Projects
    └── Tech Stack Index
```

## Next Steps

1. Create project inventory scripts
2. Build documentation aggregation
3. Deploy my-projects-docs Hugo site
4. Set up auto-sync hooks
5. Add project templates
6. Create status dashboard

---

**Created**: 2026-01-03
**Purpose**: Central hub for all project tracking and documentation
**Scope**: All projects in `/Users/mark/PycharmProjects/`
