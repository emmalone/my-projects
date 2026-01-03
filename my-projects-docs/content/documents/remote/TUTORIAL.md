---
title: "TUTORIAL"
project: remote
original_path: demo-task-api/TUTORIAL.md
modified: 2025-12-28T12:39:24.403475
---

# Task Manager API - Interactive Tutorial

Welcome! This tutorial will teach you how to use Claude Code by practicing with this demo application. This is a working session.

## What You'll Learn

By the end of this tutorial, you'll know how to:
1. Push code to GitHub
2. Access the project from your iPhone via claude.ai/code
3. Ask Claude to make changes
4. Run tests automatically
5. Create pull requests
6. Iterate based on feedback

---

## Part 1: Push to GitHub (Do This First - On Your Computer)

### Step 1: Create a GitHub Repository

```bash
# Option A: Using GitHub CLI (if installed)
gh repo create demo-task-api --public --source=. --remote=origin --push

# Option B: Manual steps
# 1. Go to https://github.com/new
# 2. Repository name: demo-task-api
# 3. Description: "Learning Claude Code with a Task Manager API"
# 4. Make it Public
# 5. DO NOT initialize with README (we already have one)
# 6. Click "Create repository"
# 7. Copy the commands shown and run them:

git remote add origin https://github.com/emarkmalone/demo-task-api.git
git branch -M main
git push -u origin main
```

### Step 2: Verify It's on GitHub

Visit: `https://github.com/emarkmalone/demo-task-api`

You should see:
- ✅ README.md with project description
- ✅ app/ directory with code
- ✅ tests/ directory
- ✅ CLAUDE.md with instructions for Claude
- ✅ 2 commits

---

## Part 2: Access from Your iPhone

### Step 1: Open Claude Code on the Web
1. On your iPhone, open Safari or Chrome
2. Navigate to: **https://claude.ai/code**
3. Sign in (requires Claude Pro/Max subscription)

### Step 2: Connect Your Repository
1. Tap "Connect GitHub" (if not already connected)
2. Select **demo-task-api** from the repository list
3. Wait for it to load (Claude will read all the files)

### Step 3: Verify Connection
Claude should show you:
- Repository name: demo-task-api
- Branch: main
- Files visible in the interface

---

## Part 3: Your First Task - Add a Priority Field

Now let's practice! Ask Claude to enhance the app.

### On Your iPhone at claude.ai/code:

**Type this message:**
```
Add a priority field to tasks. Priority should be an enum with values: low, medium, high.
Make sure to update the model, add validation, and update the tests.
```

### What Will Happen:

1. **Claude reads the code** - You'll see it examine app/models.py and app/main.py
2. **Claude makes changes** - It will:
   - Add a Priority enum
   - Update the Task model
   - Modify API endpoints
   - Add tests for the new field
3. **Claude runs tests** - Automatically verifies everything works
4. **Claude creates a commit** - With a descriptive message

### Watch For:

- ✅ All tests passing (Claude shows test output)
- ✅ Clear commit message explaining changes
- ✅ Code follows the patterns in CLAUDE.md

### Give Feedback:

If something isn't right, just reply:
```
The default priority should be 'medium' not 'low'
```

Claude will fix it and run tests again!

---

## Part 4: Create Your First Pull Request

### Ask Claude:
```
Create a pull request for the priority field feature
```

### Claude Will:
1. Create a new branch (e.g., `add-priority-field`)
2. Push the commits
3. Open a PR with:
   - Clear title
   - Summary of changes
   - Test plan

### Review the PR:
1. Tap the PR link Claude provides
2. Review the changes on GitHub (still on your iPhone!)
3. See the diff, read the description
4. Merge when satisfied

---

## Part 5: More Practice Tasks

Try these tasks to practice different workflows:

### Task 1: Add Due Dates
```
Add an optional due_date field to tasks. Use Python's date type.
```

**Learn:** Working with dates, optional fields

### Task 2: Add Task Filtering
```
Add a query parameter to filter tasks by priority in the GET /tasks endpoint
```

**Learn:** Enhancing existing endpoints

### Task 3: Add Validation
```
Make sure task titles can't be empty strings (they must have actual content)
```

**Learn:** Input validation

### Task 4: Add Statistics Endpoint
```
Create a new endpoint GET /tasks/stats that returns:
- Total number of tasks
- Number completed
- Number by priority
```

**Learn:** Aggregate endpoints, new features

### Task 5: Improve Error Messages
```
Review the error messages and make them more user-friendly and descriptive
```

**Learn:** Code review and improvements

---

## Part 6: Advanced - Iterative Development

Try this multi-step conversation:

**You:** "I want to add user authentication to this API"

**Claude:** *Will ask questions or propose a plan*

**You:** "Let's start simple with API key authentication"

**Claude:** *Implements basic API key auth*

**You:** "Now add tests for the authentication"

**Claude:** *Adds comprehensive tests*

**You:** "Update the README with how to use authentication"

**Claude:** *Updates documentation*

**You:** "Create a PR for this feature"

**Claude:** *Creates PR with all changes*

---

## Part 7: Testing Locally (Optional - On Your Computer)

While you can do everything from your iPhone, you might want to test locally:

### Run the Application:
```bash
cd /Users/mark/PycharmProjects/remote/demo-task-api
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for interactive API documentation

### Try the API:

**Create a task:**
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Claude Code", "description": "Complete the tutorial"}'
```

**Get all tasks:**
```bash
curl http://localhost:8000/tasks
```

**Interactive docs:**
Open http://localhost:8000/docs in your browser - try the API interactively!

### Run Tests:
```bash
pytest tests/ -v
```

### Check Coverage:
```bash
pytest tests/ --cov=app --cov-report=html
open htmlcov/index.html
```

---

## Part 8: Understanding the Workflow

### The Claude Code Cycle:

```
You: "Add feature X"
  ↓
Claude: Reads relevant files
  ↓
Claude: Makes changes
  ↓
Claude: Runs tests
  ↓
Claude: Creates commit
  ↓
You: Review changes
  ↓
You: "Looks good!" OR "Change Y"
  ↓
Claude: Creates PR
  ↓
You: Merge on GitHub
```

### Key Principles:

1. **Be Specific**: "Add a priority field with enum values" is better than "make it better"
2. **Review Everything**: Always check what Claude changed
3. **Iterate**: It's OK to ask for changes - that's the point!
4. **Test Everything**: Claude runs tests automatically - watch for failures
5. **Commit Often**: Each feature should be a separate commit/PR

---

## Part 9: Common Patterns

### Pattern 1: Feature Addition
```
1. You: "Add feature X"
2. Claude: Implements + tests
3. You: "Create a PR"
4. Claude: Makes PR
```

### Pattern 2: Bug Fix
```
1. You: "The app crashes when Y happens"
2. Claude: Investigates + fixes
3. Claude: Adds test to prevent regression
4. You: "Create a PR"
```

### Pattern 3: Refactoring
```
1. You: "Extract the validation logic into a separate module"
2. Claude: Refactors code
3. Claude: Verifies tests still pass
4. You: Review and approve
```

### Pattern 4: Code Review
```
1. You: "Review the code and suggest improvements"
2. Claude: Analyzes code, suggests changes
3. You: "Apply the improvements"
4. Claude: Makes changes
```

---

## Part 10: Troubleshooting

### "Tests are failing"
- Ask Claude: "Why are the tests failing? Fix them."
- Claude will investigate and fix

### "The change isn't what I wanted"
- Be specific: "Actually, I want X to work like Y"
- Claude will adjust

### "I want to undo this"
- "Revert the last commit"
- Or manually: `git reset --hard HEAD~1`

### "Claude can't access the repo"
- Check GitHub app permissions at https://github.com/apps/claude
- Make sure the repo is selected

---

## Part 11: Next Steps

Once you're comfortable with this demo:

1. **Try a real project** - Use Claude Code on your actual codebase
2. **Set up GitHub Actions** - Automate Claude with @claude mentions in PRs
3. **Customize CLAUDE.md** - Add project-specific guidelines
4. **Explore MCP servers** - Connect to external tools and services
5. **Build workflows** - Create hooks for common tasks

---

## Quick Reference

### Essential Commands (Tell Claude):

```
"Add feature X"                    # Feature development
"Fix bug Y"                        # Bug fixing
"Add tests for Z"                  # Test coverage
"Refactor X"                       # Code improvement
"Create a PR"                      # Pull request creation
"Run the tests"                    # Test execution
"What does file X do?"             # Code exploration
"Review the code for issues"       # Code review
"Update the documentation"         # Docs update
"Revert the last change"           # Undo
```

### Repository Structure:

```
demo-task-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI routes
│   └── models.py        # Pydantic models
├── tests/
│   ├── __init__.py
│   └── test_api.py      # API tests
├── requirements.txt     # Dependencies
├── CLAUDE.md           # Instructions for Claude
├── README.md           # Project docs
└── TUTORIAL.md         # This file
```

### Key Files to Know:

- **CLAUDE.md**: Guidelines for Claude Code (edit this to change how Claude works)
- **app/main.py**: All API endpoints live here
- **app/models.py**: Data models and validation
- **tests/test_api.py**: All tests - aim for 80%+ coverage

---

## Success Criteria

You'll know you've mastered Claude Code when you can:

- ✅ Make changes from your iPhone
- ✅ Run tests automatically
- ✅ Create PRs without touching code directly
- ✅ Iterate based on test results
- ✅ Review and understand Claude's changes
- ✅ Customize Claude's behavior with CLAUDE.md

---

## Getting Help

- **Claude Code docs**: https://code.claude.com/docs
- **This tutorial**: Read through again
- **Experiment**: The best way to learn is by doing!

---

**Ready to start?** Go to Part 1 and push this repo to GitHub! Then move to your iPhone and start practicing.

Happy coding with Claude!
