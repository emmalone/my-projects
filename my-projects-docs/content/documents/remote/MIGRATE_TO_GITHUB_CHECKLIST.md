---
title: "MIGRATE_TO_GITHUB_CHECKLIST"
project: remote
original_path: demo-task-api/MIGRATE_TO_GITHUB_CHECKLIST.md
modified: 2025-12-28T14:16:44.718488
---

# Migrating Website to GitHub - Safety Checklist

## BEFORE YOU START - CRITICAL SECURITY CHECKS

### ☐ Step 1: Identify Sensitive Files

**Navigate to your project directory and look for:**

```bash
# Search for potential secret files
find . -name ".env*" -o -name "*.key" -o -name "*.pem" -o -name "config.php" -o -name "settings.py"

# Look for files with "password" or "secret" in them
grep -r "password\|secret\|api_key" --include="*.php" --include="*.py" --include="*.js" --include="*.env" .
```

**Common secret files by technology:**

**WordPress:**
- `wp-config.php` (has database credentials!)
- `.htaccess` (might have passwords)
- Upload directories with customer data

**Django/Python:**
- `settings.py` or `local_settings.py`
- `.env` files
- `secrets.json`

**React/Node:**
- `.env`, `.env.local`, `.env.production`
- `config.js` with API keys

**PHP:**
- `config.php`, `db-config.php`
- `.env`

### ☐ Step 2: Create .gitignore File

**Create a `.gitignore` file in your project root with these patterns:**

```gitignore
# Secrets and configuration
.env
.env.*
*.env
.env.local
.env.production
config.php
wp-config.php
settings.py
local_settings.py
secrets.json
*.key
*.pem
.htpasswd

# Database
*.sql
*.db
*.sqlite
*.sqlite3
database/

# Dependencies
node_modules/
vendor/
venv/
env/
__pycache__/
*.pyc

# User uploads (if large)
uploads/
media/
wp-content/uploads/

# Build outputs
dist/
build/
*.min.js
*.min.css

# OS files
.DS_Store
Thumbs.db
*.swp
*.swo

# IDE
.vscode/
.idea/
*.sublime-*

# Logs
*.log
logs/

# Temporary files
tmp/
temp/
cache/
```

### ☐ Step 3: Review What Will Be Committed

**BEFORE committing, check what git will add:**

```bash
# Initialize git (if not already done)
git init

# Add the .gitignore
git add .gitignore

# Do a DRY RUN - see what would be committed
git add --dry-run -A

# Actually see the file list
git status
```

**CAREFULLY REVIEW THIS LIST!** Look for:
- Any files with passwords/keys
- Large files (> 100MB)
- Sensitive customer data

### ☐ Step 4: Check for Hardcoded Secrets in Code

**Search your code for hardcoded credentials:**

```bash
# Look for common secret patterns
grep -r "password.*=.*['\"]" --include="*.php" --include="*.py" --include="*.js" .
grep -r "api_key.*=.*['\"]" --include="*.php" --include="*.py" --include="*.js" .
grep -r "secret.*=.*['\"]" --include="*.php" --include="*.py" --include="*.js" .

# Check for AWS keys
grep -r "AKIA" .

# Check for Stripe keys
grep -r "sk_live" .
```

**If you find hardcoded secrets:**
1. Move them to environment variables
2. Reference them via `os.getenv()` (Python) or `process.env` (Node)
3. Never commit the actual values

---

## MIGRATION STEPS

### ☐ Step 5: Backup Your Local Project

**Just in case something goes wrong:**

```bash
# Create a backup
cp -r /path/to/your/project /path/to/your/project-backup-$(date +%Y%m%d)
```

### ☐ Step 6: Check GitHub Repo Status

```bash
# See if there's anything already in the repo
git clone https://github.com/emmalone/klm-migrate.git temp-check
cd temp-check
ls -la
cd ..
rm -rf temp-check
```

**If repo has content:** You'll need to merge or decide what to keep
**If repo is empty:** You can push directly

### ☐ Step 7: Initialize Git in Your Project

```bash
# Navigate to your project
cd /path/to/your/website

# Check if git is already initialized
ls -la | grep .git

# If not, initialize it
git init

# Set up your identity (if not already done)
git config user.name "emmalone"
git config user.email "mark@emm-associates.com"
```

### ☐ Step 8: Stage Files (Carefully!)

```bash
# Add .gitignore first
git add .gitignore

# Check what will be added
git status

# If everything looks safe, add all files
git add .

# Review staged files one more time
git status
```

### ☐ Step 9: Create Initial Commit

```bash
git commit -m "Initial commit: Migrate website to GitHub

- Add website source code
- Configure .gitignore for security
- Exclude sensitive configuration files
"
```

### ☐ Step 10: Connect to GitHub Remote

```bash
# Add the remote
git remote add origin https://github.com/emmalone/klm-migrate.git

# Verify it's correct
git remote -v
```

### ☐ Step 11: Check if Remote Has Content

```bash
# Fetch to see what's on GitHub
git fetch origin

# Check branches
git branch -a
```

**If remote is empty:**
```bash
# Push directly
git push -u origin main
```

**If remote has content:**
```bash
# Pull and merge first
git pull origin main --allow-unrelated-histories

# Resolve any conflicts
# Then push
git push -u origin main
```

### ☐ Step 12: Verify on GitHub

1. Visit: https://github.com/emmalone/klm-migrate
2. Check the file list
3. **IMPORTANT:** Look for any files that shouldn't be there
4. If you see secrets, DELETE them immediately and see "Emergency" section below

---

## ⚠️ EMERGENCY: I Accidentally Committed Secrets!

**If you pushed sensitive data to GitHub:**

### Option 1: If Just Pushed (within minutes)

1. **Delete the repository on GitHub immediately**
   - Go to repo Settings → Danger Zone → Delete

2. **Rotate all exposed credentials**
   - Change database passwords
   - Regenerate API keys
   - Update all services

3. **Fix locally and re-push**
   - Remove secrets from code
   - Add to .gitignore
   - Create new repo
   - Push clean version

### Option 2: Remove from Git History (Advanced)

```bash
# Install BFG Repo Cleaner
brew install bfg  # macOS

# Remove the file from history
bfg --delete-files config.php

# Clean up
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# Force push (WARNING: destructive)
git push --force
```

**CRITICAL:** Even after removal, assume the secrets are compromised. Always rotate them!

---

## TECHNOLOGY-SPECIFIC GUIDES

### WordPress

**Files to include:**
- ✅ `wp-content/themes/` (your custom themes)
- ✅ `wp-content/plugins/` (your custom plugins)
- ✅ Custom PHP files

**Files to EXCLUDE:**
- ❌ `wp-config.php` (has DB credentials!)
- ❌ `wp-content/uploads/` (user uploads)
- ❌ WordPress core files (can be downloaded)
- ❌ `.htaccess` (often has sensitive rules)

**Alternative approach:** Only commit your theme/plugin, not entire WP install

### Django/Python

**Create this .gitignore:**
```gitignore
*.pyc
__pycache__/
venv/
env/
.env
db.sqlite3
*.log
media/
staticfiles/
local_settings.py
```

**Environment variables approach:**
```python
# settings.py
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
```

### React/Node

**Create this .gitignore:**
```gitignore
node_modules/
.env
.env.local
.env.production
build/
dist/
npm-debug.log*
.DS_Store
```

**Environment variables:**
```javascript
// Use process.env
const apiKey = process.env.REACT_APP_API_KEY;
```

---

## BEST PRACTICES

### ☐ Use Environment Variables

**Instead of:**
```php
$db_password = "super_secret_123";  // DON'T DO THIS!
```

**Do this:**
```php
$db_password = getenv('DB_PASSWORD');
```

**Then create `.env` (and add to .gitignore):**
```
DB_PASSWORD=super_secret_123
```

### ☐ Add a README

**Create `README.md` in your project:**

```markdown
# KLM Website

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env`
3. Update `.env` with your credentials
4. Install dependencies
5. Run the application

## Environment Variables

Required variables in `.env`:
- `DATABASE_URL` - Database connection string
- `API_KEY` - API key for external service
```

### ☐ Create .env.example

**Template file (safe to commit):**

```bash
# .env.example - Template for environment variables
DATABASE_URL=postgresql://localhost/mydb
API_KEY=your_api_key_here
SECRET_KEY=generate_a_random_secret
```

**Users copy this to `.env` and fill in real values**

---

## COMMON MISTAKES TO AVOID

### ❌ Don't Commit node_modules
- Always in `.gitignore`
- Regenerate with `npm install`

### ❌ Don't Commit Database Files
- Use migrations instead
- Provide schema, not data

### ❌ Don't Commit Compiled Files
- Add `dist/`, `build/` to `.gitignore`
- Build on deployment

### ❌ Don't Commit Large Media Files
- Use Git LFS for large files
- Or store in S3/CDN

### ❌ Don't Commit with Wrong Email
- Check: `git config user.email`
- Should match your GitHub account

---

## POST-MIGRATION

### ☐ Set Up Branch Protection (Optional)

On GitHub:
1. Go to Settings → Branches
2. Add rule for `main`
3. Require pull request reviews
4. Prevent force pushes

### ☐ Add Collaborators (If Needed)

1. Settings → Collaborators
2. Add team members
3. Set appropriate permissions

### ☐ Configure GitHub Actions (Optional)

Auto-deploy on push, run tests, etc.

---

## Quick Reference

### Safe to Commit:
✅ Source code (HTML, CSS, JavaScript, Python, PHP)
✅ Templates and views
✅ Static assets (images, fonts - if not too large)
✅ Configuration templates (.env.example)
✅ Documentation (README, docs/)
✅ Tests
✅ Package files (package.json, requirements.txt, composer.json)

### NEVER Commit:
❌ .env files with real credentials
❌ Database files with data
❌ User uploads
❌ Dependency directories (node_modules, vendor)
❌ API keys, passwords, secrets
❌ Private keys (.key, .pem)
❌ Compiled/built files

---

## Need Help?

If you're unsure about any file, **DON'T COMMIT IT YET**.

Ask yourself:
1. Does this file contain passwords or API keys?
2. Is this file generated (can be rebuilt)?
3. Is this file user-uploaded content?
4. Is this file larger than 50MB?

If YES to any → Add to .gitignore

---

**Remember: Once something is on GitHub, assume it's public forever. Even if you delete it, it may be cached or archived. Prevention is key!**
