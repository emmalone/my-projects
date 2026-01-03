---
title: "GITOVERVIEW"
project: remote
original_path: demo-task-api/GITOVERVIEW.md
modified: 2025-12-28T13:23:20.231345
---

# Git & GitHub Workflow - Complete Reference Guide

This document provides a comprehensive overview of the Git/GitHub workflow you've mastered through building the Task Manager API demo application.

---

## Git Concepts You Mastered

### 1. **Branches**
```
main branch (stable)
    └─ feature branch (experimental)
```
- **Purpose:** Isolate work without affecting stable code
- **Types:** main (production), feature (new work), hotfix (urgent fixes)

### 2. **Commits**
```
3b18d45 - Add web interface with task table view
```
- **What:** Snapshot of your code at a point in time
- **Hash:** Unique ID (3b18d45)
- **Message:** Description of what changed

### 3. **Remote vs Local**
```
Local (Your Computer)          Remote (GitHub)
├─ main                        ├─ origin/main
└─ add-web-task-table          └─ origin/add-web-task-table
```
- **Local:** Your machine
- **Remote:** GitHub (cloud)
- **Sync:** push (upload), pull (download), fetch (check)

### 4. **Pull Requests (PRs)**
```
Feature Branch → Review → Merge → Main Branch
```
- **Purpose:** Code review before merging
- **Benefits:** Catch bugs, share knowledge, document changes
- **Process:** Create → Review → Discuss → Approve → Merge

### 5. **Fast-Forward Merge**
```
Before:                 After:
main:     A─B           main:     A─B─C─D
feature:    └─C─D
```
- **Clean merge:** No conflicts
- **Linear history:** Easy to understand

---

## Key Git Commands Reference

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `git pull origin main` | Download & merge latest from GitHub | Start of work session |
| `git checkout -b name` | Create new branch | Start new feature |
| `git status` | Show changed files | Check what's modified |
| `git add <files>` | Stage changes for commit | Prepare to commit |
| `git commit -m "msg"` | Save snapshot | After testing changes |
| `git push -u origin branch` | Upload branch to GitHub | Share your work |
| `git fetch origin` | Check for updates | See what's on GitHub |
| `git log --oneline` | Show commit history | Review what happened |
| `git branch -a` | List all branches | See what exists |
| `git branch -d name` | Delete local branch | After merging |
| `git remote prune origin` | Clean stale references | After branch deletion |

### Additional Useful Commands

| Command | What It Does |
|---------|--------------|
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git log --graph --oneline` | Visual commit history |
| `git branch -v` | Show branches with last commit |
| `git remote -v` | Show remote repository URLs |
| `git checkout main` | Switch to main branch |
| `git restore <file>` | Discard changes in file |
| `git restore --staged <file>` | Unstage file |

---

## The Workflow Visualized

```
┌─────────────────────────────────────────────────────────────┐
│ LOCAL MACHINE (Your Computer)                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. git pull origin main                                    │
│     ↓                                                        │
│  2. git checkout -b add-web-task-table                      │
│     ↓                                                        │
│  3. Write Code (HTML, CSS, Python)                          │
│     ↓                                                        │
│  4. Test Locally (uvicorn app.main:app)                     │
│     ↓                                                        │
│  5. git add app/main.py app/templates/ app/static/          │
│     ↓                                                        │
│  6. git commit -m "Add web interface..."                    │
│     ↓                                                        │
│  7. git push -u origin add-web-task-table                   │
│                                                              │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            │ Push
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ GITHUB (Cloud)                                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  8. Create Pull Request (Web Interface)                     │
│     ↓                                                        │
│  9. Review Code (See Diffs)                                 │
│     ↓                                                        │
│ 10. Merge PR (Green Button)                                 │
│     ↓                                                        │
│ 11. Delete Branch (Cleanup)                                 │
│                                                              │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            │ Pull
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ LOCAL MACHINE (Sync Back)                                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│ 12. git checkout main                                        │
│ 13. git fetch origin                                         │
│ 14. git pull origin main                                     │
│ 15. git branch -d add-web-task-table                         │
│ 16. git remote prune origin                                  │
│                                                              │
│ ✅ COMPLETE CYCLE!                                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## State Changes Throughout the Workflow

### Your Repository's Evolution:

```
Commit 1 (Initial):
├─ app/main.py (basic API)
├─ app/models.py
├─ tests/test_api.py
└─ README.md

    ↓ [You create feature branch]

Commit 2 (On feature branch):
├─ app/main.py (+ web endpoint)
├─ app/models.py
├─ app/templates/index.html  ← NEW
├─ app/static/style.css      ← NEW
├─ tests/test_api.py
└─ README.md

    ↓ [You merge PR]

Commit 3 (Merged to main):
├─ app/main.py (+ web endpoint)  ✅
├─ app/models.py
├─ app/templates/index.html      ✅
├─ app/static/style.css          ✅
├─ tests/test_api.py
└─ README.md
```

---

## How This Differs with Claude Code (iPhone)

### Traditional Workflow:
```
You:    Write HTML → Write CSS → Write Python → Test → Debug → Commit
Time:   2-3 hours
```

### With Claude Code (What you'll do next from iPhone):
```
You:    "Add a search bar to filter tasks by title"
Claude: [Reads code] [Writes HTML] [Updates CSS] [Modifies Python]
        [Adds tests] [Runs tests] [Commits] [Creates PR]
Time:   5 minutes
```

**Key Difference:**
- **You describe** what you want
- **Claude writes** the code
- **You review** and approve
- **Same git workflow** but faster!

---

## Your Progress Across 2 Features

### Feature #1: Priority Field (PR #1)
- Added Priority enum (LOW, MEDIUM, HIGH)
- Updated models and API
- Added 12 comprehensive tests
- **Learned:** Basic PR workflow from iPhone

### Feature #2: Web Interface (PR #2)
- Created HTML template with task table
- Added CSS with color-coded priorities
- Implemented /web endpoint
- **Learned:** Complete git workflow from desktop

---

## What's Next?

### Option 1: Practice More from Desktop
Try these features to reinforce the workflow:

**Easy:**
```
Add a "Created By" field to tasks with a default author name
```

**Medium:**
```
Add sorting options to the web table (sort by priority, date, etc.)
```

**Hard:**
```
Add ability to mark tasks complete from the web interface (requires JavaScript)
```

### Option 2: Switch to iPhone
Now that you understand the workflow, try it from claude.ai/code:

```
1. Open https://claude.ai/code on iPhone
2. Select demo-task-api
3. Say: "Add a search filter to the web page"
4. Watch Claude do the whole workflow
5. Review the PR on iPhone
6. Merge from iPhone
7. Pull locally to sync
```

### Option 3: Combine Both
Best of both worlds:

```
- Start features on iPhone (convenient)
- Review PRs on desktop (easier to see code)
- Test locally before merging (verify it works)
- Merge from either device
```

---

## Git Workflow Checklist (For Future Reference)

### Starting New Work:
- [ ] `git pull origin main` (get latest)
- [ ] `git checkout -b feature-name` (create branch)

### Making Changes:
- [ ] Write code
- [ ] Test locally
- [ ] `git status` (review changes)
- [ ] `git add <files>` (stage changes)
- [ ] `git commit -m "message"` (commit)

### Sharing Work:
- [ ] `git push -u origin feature-name` (upload)
- [ ] Create PR on GitHub
- [ ] Review code diff
- [ ] Merge PR

### After Merge:
- [ ] `git checkout main` (switch to main)
- [ ] `git pull origin main` (get merged code)
- [ ] `git branch -d feature-name` (cleanup)
- [ ] `git remote prune origin` (cleanup references)

---

## Understanding Git Status Messages

### Common Status Messages:

**"On branch main"**
- You're currently working on the main branch

**"Your branch is up to date with 'origin/main'"**
- Your local branch matches GitHub's version

**"Your branch is behind 'origin/main' by N commits"**
- GitHub has newer commits you don't have locally
- Solution: `git pull origin main`

**"Your branch is ahead of 'origin/main' by N commits"**
- You have local commits not yet on GitHub
- Solution: `git push origin main`

**"Changes not staged for commit"**
- Files are modified but not added to staging area
- Solution: `git add <files>`

**"Changes to be committed"**
- Files are staged and ready to commit
- Solution: `git commit -m "message"`

**"Untracked files"**
- New files Git isn't tracking yet
- Solution: `git add <files>` to start tracking

**"nothing to commit, working tree clean"**
- Everything is committed, no pending changes
- This is the ideal state!

---

## Understanding Git Diff Output

### Reading a Diff:

```diff
diff --git a/app/main.py b/app/main.py
index 1234567..abcdefg 100644
--- a/app/main.py
+++ b/app/main.py
@@ -5,7 +5,10 @@ from typing import Dict, List
-from fastapi import FastAPI, HTTPException, status
+from fastapi import FastAPI, HTTPException, Request, status
+from fastapi.responses import HTMLResponse
+from fastapi.staticfiles import StaticFiles
```

**Legend:**
- `---` Old version of file
- `+++` New version of file
- `-` Lines removed (shown in red)
- `+` Lines added (shown in green)
- `@@` Line numbers where changes occurred

---

## Commit Message Best Practices

### Good Commit Messages:

```
Add web interface with task table view

- Create HTML template with task table and statistics
- Add CSS styling with color-coded priority badges
- Add /web endpoint to render the page
- Mount static files and configure Jinja2 templates

This provides a user-friendly web UI to view all tasks
in addition to the existing REST API.
```

### Structure:
1. **Subject line** (50 chars or less)
   - Use imperative mood: "Add" not "Added"
   - Capitalize first letter
   - No period at the end

2. **Blank line**

3. **Body** (optional, wrap at 72 chars)
   - Explain WHAT and WHY, not HOW
   - Use bullet points for multiple changes
   - Reference issue numbers if applicable

### Examples:

**Good:**
- `Add user authentication with JWT tokens`
- `Fix memory leak in task deletion`
- `Refactor database connection pooling`
- `Update dependencies for Python 3.13 compatibility`

**Bad:**
- `Fixed stuff` (too vague)
- `Updated code` (what code?)
- `asdfasdf` (meaningless)
- `Added a feature that does this and that and the other thing and more stuff` (too long)

---

## Handling Common Git Scenarios

### Scenario 1: Made Changes on Wrong Branch

**Problem:** Started coding on main instead of a feature branch

**Solution:**
```bash
# Stash your changes
git stash

# Create and switch to correct branch
git checkout -b feature-branch

# Apply your changes
git stash pop

# Now commit as normal
git add .
git commit -m "Your message"
```

### Scenario 2: Want to Undo Last Commit

**Problem:** Committed too early or made a mistake

**Solution (if not pushed yet):**
```bash
# Undo commit but keep changes
git reset --soft HEAD~1

# Make your corrections
# Then commit again
git commit -m "Fixed message"
```

**Solution (if already pushed):**
```bash
# Create a new commit that reverses the changes
git revert HEAD

# Push the revert commit
git push origin branch-name
```

### Scenario 3: Accidentally Deleted Local Branch

**Problem:** Deleted branch before merging

**Solution:**
```bash
# Find the commit hash
git reflog

# Create branch at that commit
git checkout -b recovered-branch <commit-hash>
```

### Scenario 4: Want to See What Changed

**Problem:** Need to review changes before committing

**Solution:**
```bash
# See unstaged changes
git diff

# See staged changes
git diff --staged

# See changes in a specific file
git diff app/main.py

# See changes between branches
git diff main..feature-branch
```

### Scenario 5: Merge Conflicts

**Problem:** GitHub says there are conflicts

**Solution:**
```bash
# Update your branch with latest main
git checkout feature-branch
git pull origin main

# Fix conflicts in your editor
# Look for markers: <<<<<<<, =======, >>>>>>>

# After fixing, stage the files
git add <conflicted-files>

# Complete the merge
git commit -m "Resolve merge conflicts"

# Push the resolution
git push origin feature-branch
```

---

## Branch Naming Conventions

### Common Patterns:

**Feature branches:**
- `feature/user-authentication`
- `feature/add-dark-mode`
- `add-search-functionality`

**Bug fixes:**
- `fix/login-crash`
- `bugfix/memory-leak`
- `hotfix/security-vulnerability`

**Refactoring:**
- `refactor/database-layer`
- `cleanup/remove-deprecated-code`

**Documentation:**
- `docs/update-readme`
- `docs/api-documentation`

**Best Practices:**
- Use lowercase with hyphens
- Be descriptive but concise
- Include issue number if applicable: `feature/123-user-auth`

---

## Git Configuration Tips

### Essential Git Config:

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Enable credential caching (macOS)
git config --global credential.helper osxkeychain

# Colorize output
git config --global color.ui auto

# Set default editor
git config --global core.editor "nano"  # or vim, code, etc.

# Show current config
git config --list
```

---

## GitHub-Specific Features

### Pull Request Features:

**Reviewers:**
- Request specific people to review your code
- They can approve or request changes

**Labels:**
- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Documentation improvements
- `help wanted` - Extra attention needed

**Milestones:**
- Group related PRs and issues
- Track progress toward a release

**Draft PRs:**
- Create PR but mark it as work-in-progress
- Prevents accidental merging
- Good for getting early feedback

**PR Templates:**
- Create `.github/pull_request_template.md`
- Auto-fills PR description with a template

---

## Troubleshooting

### "Authentication failed"
**Problem:** Can't push to GitHub

**Solution:**
- Use Personal Access Token instead of password
- Configure credential helper: `git config --global credential.helper osxkeychain`
- Generate new token: https://github.com/settings/tokens

### "Your branch has diverged"
**Problem:** Local and remote have different commits

**Solution:**
```bash
# See the differences
git log HEAD..origin/main --oneline

# If you want to keep your changes on top
git pull --rebase origin main

# Or merge
git pull origin main
```

### "Permission denied"
**Problem:** Can't access repository

**Solution:**
- Check you're logged into correct GitHub account
- Verify repository permissions
- Check if you're a collaborator on the repo

---

## Quick Reference Card

### Daily Workflow:
```bash
# Start work
git pull origin main
git checkout -b feature-name

# Make changes, test

# Save work
git add .
git commit -m "Description"
git push -u origin feature-name

# Create PR on GitHub, merge

# Sync back
git checkout main
git pull origin main
git branch -d feature-name
```

### Emergency Commands:
```bash
# Undo unstaged changes
git restore <file>

# Unstage files
git restore --staged <file>

# See what you're about to commit
git diff --staged

# Abort a merge
git merge --abort

# See recent actions
git reflog
```

---

## Learning Resources

### Official Documentation:
- **Git Docs:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com
- **Pro Git Book:** https://git-scm.com/book (free online)

### Interactive Learning:
- **Learn Git Branching:** https://learngitbranching.js.org
- **GitHub Learning Lab:** https://lab.github.com

### Cheat Sheets:
- **GitHub Cheat Sheet:** https://training.github.com/downloads/github-git-cheat-sheet.pdf
- **Git Command Explorer:** https://gitexplorer.com

---

## Final Summary

### Skills Mastered:

✅ Creating feature branches
✅ Staging and committing changes
✅ Writing good commit messages
✅ Pushing to GitHub
✅ Creating pull requests
✅ Reviewing code diffs
✅ Merging PRs
✅ Syncing local with remote
✅ Branch cleanup

### The Complete Professional Workflow:

```
1. git pull origin main              → Start with latest code
2. git checkout -b feature-branch    → Create isolated workspace
3. [Write code]                      → Make your changes
4. [Test locally]                    → Verify it works
5. git add <files>                   → Stage changes
6. git commit -m "message"           → Save snapshot
7. git push -u origin feature-branch → Upload to GitHub
8. [Create PR on GitHub]             → Request review/merge
9. [Review & Merge PR]               → Merge to main
10. git checkout main                → Switch back to main
11. git fetch origin                 → Check for updates
12. git pull origin main             → Get merged changes
13. git branch -d feature-branch     → Delete local branch
14. git remote prune origin          → Clean up references
```

---

**You now have a complete reference guide for Git and GitHub workflows!**

*This document covers everything you've learned through hands-on practice with the Task Manager API demo project.*
