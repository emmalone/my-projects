# My-Projects - Central Documentation Hub

## Project Overview

This repository serves as a **central hub** for tracking and documenting all projects in `/Users/mark/PycharmProjects/`. It automatically discovers projects, aggregates their documentation, and publishes everything to a secure Hugo-powered website.

## What This Project Does

1. **Project Discovery**: Automatically scans all projects in PycharmProjects
2. **Documentation Aggregation**: Collects all markdown files from all projects
3. **Inventory Tracking**: Maintains project profiles with tech stacks, Git status, and metadata
4. **Hugo Site Generation**: Creates a searchable documentation website
5. **Auto-Deployment**: Publishes to AWS S3 + CloudFront with GitHub Actions

## Repository Structure

```
my-projects/
├── CLAUDE.md                    # This file - project instructions
├── README.md                    # Project overview
├── DEPLOYMENT.md                # Deployment details and credentials
├── scan-projects.py             # Discovers projects and markdown files
├── generate-docs.py             # Generates Hugo site from inventory
├── inventory.json               # Project inventory (auto-generated)
├── projects/                    # Project profiles (auto-generated)
│   ├── klm-plan.md
│   ├── klm-migrate.md
│   └── ...
└── my-projects-docs/            # Hugo documentation site
    ├── hugo.toml                # Hugo configuration
    ├── content/                 # Generated content
    │   ├── _index.md           # Homepage
    │   ├── projects/           # Project pages
    │   ├── documents/          # All aggregated markdown files
    │   └── inventory/          # Inventory page
    └── public/                  # Built site (git ignored)
```

## Common Workflows

### Update Documentation Index

When markdown files are added/changed in any project:

```bash
# 1. Scan all projects for changes
python3 scan-projects.py

# 2. Regenerate Hugo site
python3 generate-docs.py

# 3. Commit and push (triggers auto-deployment)
git add .
git commit -m "Update documentation index"
git push
```

Site updates automatically in ~60-90 seconds via GitHub Actions.

### Test Changes Locally

```bash
# Build and serve locally
cd my-projects-docs
hugo server -D

# View at http://localhost:1313
```

### View Deployment Status

```bash
# Check recent GitHub Actions runs
gh run list --limit 5

# View specific run
gh run view <run-id>
```

## Key Scripts

### scan-projects.py

**Purpose**: Discovers all projects and markdown files
**Output**: `inventory.json` and `projects/` directory

**What it scans**:
- All directories in `/Users/mark/PycharmProjects/` (except .claude, my-projects, klm-hugo-lab)
- Git repositories and status
- Markdown files (excluding themes/, archetypes/, node_modules/, venv/)
- README files
- Tech stack detection (package.json, requirements.txt, hugo.toml, etc.)

**Exclusions**:
- `klm-hugo-lab`: Excluded due to Hugo template incompatibility
- Template files: Skips archetypes/ and themes/ directories
- Dependency folders: Skips node_modules/, venv/, .git/, dist/, build/

### generate-docs.py

**Purpose**: Creates Hugo site from inventory
**Output**: `my-projects-docs/` with all content

**What it generates**:
- Homepage with project stats
- Project pages (one per project)
- Document index (all markdown files organized by project)
- Inventory page with detailed stats
- Copies all markdown files to Hugo content directory

**Special handling**:
- Cleans content directories before regenerating (prevents old files)
- Skips Hugo shortcodes in summaries (prevents build errors)
- Adds frontmatter to documents (project, path, modified date)

## AWS Deployment

### Resources

- **S3 Bucket**: my-projects-docs (private, CloudFront-only access)
- **CloudFront Distribution**: E1JSSE49FNQVBL
- **Domain**: https://d27nsh9nz210c8.cloudfront.net
- **Lambda@Edge**: my-projects-basic-auth:1 (password protection)
- **GitHub Repo**: https://github.com/emmalone/my-projects

### Credentials

See `DEPLOYMENT.md` for complete details.

**Website Access**:
- Username: `mark`
- Password: `MyProjects2026!`

### Manual Deployment

```bash
cd my-projects-docs

# Build site
hugo --minify

# Deploy to S3
aws s3 sync public/ s3://my-projects-docs --delete --cache-control "public, max-age=3600"

# Invalidate CloudFront cache
aws cloudfront create-invalidation --distribution-id E1JSSE49FNQVBL --paths "/*"
```

### Auto-Deployment (GitHub Actions)

Located in `.github/workflows/deploy.yml`

**Triggers**: Push to main branch
**Process**:
1. Checkout repository
2. Setup Hugo
3. Build site (`hugo --minify`)
4. Sync to S3
5. Invalidate CloudFront cache

**Secrets configured**:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`

## Current Status

**Projects Tracked**: 22 (excluding klm-hugo-lab)
**Documents Indexed**: 142 markdown files
**Last Deployed**: 2026-01-03
**Site Status**: ✅ Live and operational

## Important Notes

### CRITICAL: Do NOT Run generate-docs.py on Remote/Cloud Servers

**This script MUST only be run on Mark's local machine** where `/Users/mark/PycharmProjects/` exists.

**Why this matters:**
- `generate-docs.py` copies markdown files from source projects to the Hugo content directory
- It first **deletes** existing content directories (`projects/`, `documents/`, `inventory/`)
- If run on a remote server (Claude Code web, GitHub Actions, etc.), the source files don't exist
- This causes all 142+ document files to be **permanently deleted** from the repository

**What happens if run remotely:**
1. Content directories are cleaned (deleted)
2. Script tries to copy files from `/Users/mark/PycharmProjects/...`
3. Files don't exist → copy fails silently
4. Commit includes deletion of all documents
5. Site deployment shows empty/broken pages

**Safe workflow:**
```bash
# ONLY run these on Mark's local Mac:
python3 scan-projects.py
python3 generate-docs.py

# Then commit and push
git add .
git commit -m "Update documentation"
git push
```

**If you need to make changes to generate-docs.py:**
1. Edit the script file only (don't run it)
2. Commit and push the script changes
3. Mark will run it locally to regenerate content

### klm-hugo-lab Exclusion

The klm-hugo-lab project is excluded from scanning because:
- Contains HTML import files converted to markdown
- Hugo template metadata causes build failures
- Incompatible frontmatter in archetype files

If you need to include it, the problematic files are in the `imported/` directory.

### Hugo Configuration

The Hugo site is configured with:
- `refLinksErrorLevel = 'WARNING'`: Allows build with broken internal links
- `refLinksNotFoundURL = '#'`: Broken refs point to # instead of failing
- Theme: hugo-book (git submodule)

### Summary Extraction

The scan-projects.py extracts summaries by:
1. Looking for description/summary in frontmatter
2. Finding first non-heading, non-code, non-HTML paragraph
3. Skipping Hugo shortcodes (`{{% %}}`, `{{< >}}`)
4. Limiting to 200 characters

## Creating Documentation Sites for Other Projects

To create a similar documentation site for a specific project:

```bash
cd /Users/mark/PycharmProjects/hugo-docs-template

python3 deploy-hugo-docs.py \
  --project project-name \
  --username mark \
  --password YourPassword! \
  --github-org emmalone
```

See `hugo-docs-template/USAGE-EXAMPLES.md` for complete guide.

## Permissions & Auto-Approval

All AWS, Git, Hugo, and Python commands are pre-approved for Claude Code sessions.

**Settings Location**: `/Users/mark/PycharmProjects/klm-plan/.claude/settings.local.json`

Commands auto-approved:
- All AWS CLI operations
- Git operations (add, commit, push, etc.)
- Hugo commands
- Python scripts (scan-projects.py, generate-docs.py)
- GitHub CLI commands

## Architecture

```
User (iPhone/Desktop)
    ↓
GitHub Repository
    ↓ (push to main)
GitHub Actions
    ↓
Hugo Build
    ↓
AWS S3 (my-projects-docs) - Private
    ↑ (via OAC)
CloudFront Distribution (HTTPS)
    ↑ (via Lambda@Edge)
Password Protection (Basic Auth)
    ↑
User Browser
```

## Related Projects

- **klm-plan**: Business planning documentation (deployed to klm-plan-docs)
- **hugo-docs-template**: Automation scripts for creating new Hugo doc sites
- **klm-migrate**: Website migration project (deployed to klm-migrate-docs)

Each project has its own dedicated documentation site. My-Projects aggregates ALL documentation from ALL projects for cross-project search and discovery.

## Troubleshooting

### Hugo Build Fails

```bash
# Check for problematic files
cd my-projects-docs
hugo --minify

# If shortcode errors, update scan-projects.py to skip more patterns
# If template errors, check for archetype files that were copied
```

### GitHub Actions Fails

```bash
# View latest run
gh run list --limit 1

# Check logs
gh run view <run-id> --log

# Common issues:
# - AWS credentials not set (run gh secret list to verify)
# - Hugo build errors (test locally first)
# - S3 permissions (check bucket policy)
```

### Site Not Updating

```bash
# Check CloudFront cache
aws cloudfront create-invalidation --distribution-id E1JSSE49FNQVBL --paths "/*"

# Check S3 content
aws s3 ls s3://my-projects-docs/

# Verify GitHub Actions completed
gh run list --limit 3
```

## Tips for Working with Claude Code

### From iPhone/Web Claude Code Sessions

**IMPORTANT**: Remote Claude Code sessions (iPhone, web) run on cloud servers, NOT on Mark's local machine.

**Safe operations in remote sessions:**
- Edit individual content files in `my-projects-docs/content/`
- Edit `generate-docs.py` logic (but don't run it)
- Edit configuration files
- Git operations (commit, push, create PRs)

**NEVER do in remote sessions:**
- Run `python3 generate-docs.py` - will delete all documents
- Run `python3 scan-projects.py` - source projects don't exist

### From iPhone

1. Open GitHub app or web interface
2. Edit markdown files directly
3. Commit changes
4. Site auto-updates in 60-90 seconds

### Adding New Projects

New projects are automatically discovered when you run:
```bash
python3 scan-projects.py
```

No configuration needed - just add a project to PycharmProjects and scan.

### Updating Documentation

If you update markdown files in other projects, remember to:
1. Run `scan-projects.py` to update inventory
2. Run `generate-docs.py` to regenerate Hugo site
3. Commit and push to trigger deployment

## Future Enhancements

- [ ] Git hooks to auto-scan when markdown files change
- [ ] Real-time sync of documentation across projects
- [ ] Project status dashboard with activity tracking
- [ ] Cross-project TODO aggregation
- [ ] Automated project health checks

---

**Last Updated**: 2026-01-03
**Maintained by**: Mark
**Purpose**: Central documentation hub for all PycharmProjects
