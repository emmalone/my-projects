---
title: "CLAUDE_CODE_IPHONE_SETUP"
project: remote
original_path: CLAUDE_CODE_IPHONE_SETUP.md
modified: 2025-12-26T15:21:39.301149
---

# Claude Code Cloud Setup - iPhone Guide

## Quick Start (5 Minutes)

### Step 1: Access Claude Code on the Web
1. Open Safari or Chrome on your iPhone
2. Navigate to: **https://claude.ai/code**
3. Sign in with your Claude account (requires Pro, Max, or Team Premium)

### Step 2: Connect GitHub
1. On the Claude Code web interface, look for "Connect GitHub" button
2. Tap to authorize Claude to access your GitHub account
3. You'll be redirected to GitHub - tap "Authorize Claude"
4. Install the Claude GitHub App:
   - Visit: **https://github.com/apps/claude**
   - Tap "Install"
   - Select which repositories Claude can access (all or specific ones)
   - Tap "Install & Authorize"

### Step 3: Start Using Claude Code
1. Return to https://claude.ai/code
2. Select a repository from the dropdown
3. Type your task in the chat (e.g., "Add a README file to this project")
4. Watch Claude work in real-time:
   - Reading files
   - Writing code
   - Running tests
   - Creating commits
5. Review the changes and provide feedback
6. When satisfied, Claude can create a Pull Request

## Understanding the Cloud Environment

### What Happens Behind the Scenes
- **Execution Environment**: Anthropic provides cloud VMs (virtual machines)
- **Isolated & Secure**: Each session runs in an isolated container
- **GitHub Access**: Claude can read your repos, create branches, and make commits
- **Terminal Access**: Claude runs bash commands, tests, and builds in the cloud
- **Real-time Feedback**: Just like your local terminal interaction

### Comparison to Local Terminal

| Feature | Local Claude Code | Cloud Claude Code |
|---------|------------------|-------------------|
| Access from iPhone | ❌ No | ✅ Yes |
| Run code & tests | ✅ Yes | ✅ Yes |
| GitHub integration | ✅ Yes | ✅ Yes |
| Install dependencies | ✅ Yes | ✅ Yes |
| Create PRs | ✅ Yes | ✅ Yes |
| Network access | ✅ Full | ⚠️ Limited (configurable) |
| Custom tools | ✅ Yes | ⚠️ Limited |

## Advanced Setup Options

### Option A: Using Anthropic's Cloud (Recommended for iPhone)
**No additional setup required!** This is the default when you visit claude.ai/code.

**Pros:**
- Zero configuration
- Works immediately
- Managed by Anthropic

**Cons:**
- Limited to Anthropic's infrastructure
- Less control over the environment

### Option B: Using AWS Resources

If you want to use your own AWS account for Claude API access:

1. **Set up AWS Bedrock Access**
   - Log into AWS Console on your computer (difficult on iPhone)
   - Enable Claude models in AWS Bedrock
   - Create IAM role with Bedrock permissions
   - Note: This requires AWS account setup on a computer

2. **Configure GitHub OIDC**
   - Set up GitHub Actions in your repository
   - Add AWS credentials as GitHub secrets
   - Configure the Claude Code workflow

3. **Documentation**: https://code.claude.com/docs/en/amazon-bedrock.md

**Note**: AWS setup is better done on a computer, not iPhone

### Option C: Using Google Cloud Platform

Similar to AWS, but uses Google Vertex AI:
- Requires GCP account setup (computer recommended)
- Configure Workload Identity Federation
- Documentation: https://code.claude.com/docs/en/google-vertex-ai.md

## iPhone-Specific Tips

### Best Practices for Mobile Use

1. **Use Landscape Mode**: Easier to see code and chat side-by-side
2. **Bookmark the URL**: Add https://claude.ai/code to your home screen
3. **Use Desktop Site Mode**: If the mobile view is cramped:
   - In Safari: Tap "aA" → "Request Desktop Website"
   - In Chrome: Tap menu → "Desktop site"
4. **External Keyboard**: Consider a Bluetooth keyboard for longer sessions

### What Works Well on iPhone
- ✅ Reviewing code changes
- ✅ Providing feedback and direction
- ✅ Approving or requesting changes
- ✅ Creating pull requests
- ✅ Monitoring progress
- ✅ Simple code edits

### What's Challenging on iPhone
- ⚠️ Viewing large diffs (lots of scrolling)
- ⚠️ Complex multi-file debugging
- ⚠️ Extended coding sessions (small screen)
- ⚠️ Typing long, detailed instructions

## GitHub Integration Features

### What Claude Can Do with GitHub

1. **Read Your Repositories**
   - Browse files and folders
   - Understand code structure
   - Analyze dependencies

2. **Make Changes**
   - Create new files
   - Edit existing code
   - Delete obsolete files
   - Refactor and improve

3. **Run Tests & Builds**
   - Execute test suites
   - Run linters
   - Build projects
   - Check for errors

4. **Create Commits**
   - Stage changes
   - Write descriptive commit messages
   - Commit to branches

5. **Manage Pull Requests**
   - Create PRs with descriptions
   - Respond to PR comments
   - Make requested changes
   - Update PRs based on feedback

### GitHub Actions Integration

For automated workflows, you can set up Claude to respond to mentions:

1. Create `.github/workflows/claude.yml` in your repository
2. Add @claude in PR comments or issues
3. Claude automatically responds and makes changes
4. All from your iPhone!

**Example**: Comment "@claude please add error handling to this function" on a PR, and Claude will respond with a commit.

## Repository Configuration

### Creating a CLAUDE.md File

Add a `CLAUDE.md` file to your repository root to guide Claude:

```markdown
# Project: My App

## Tech Stack
- Python 3.11
- FastAPI
- PostgreSQL
- React frontend

## Coding Standards
- Use type hints
- Follow PEP 8
- Write docstrings for all functions
- Minimum 80% test coverage

## Testing
Run tests with: `pytest tests/`

## Deployment
This app deploys to AWS Lambda
```

Claude will read this file and follow your guidelines automatically.

### Setting Up Hooks (Advanced)

Hooks run automatically when sessions start. Create a `.claude/settings.json` file:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "pip install -r requirements.txt"
          }
        ]
      }
    ]
  }
}
```

This ensures dependencies are installed every time Claude starts working.

## Security & Best Practices

### What Claude Can Access
- ✅ Repositories you explicitly grant access to
- ✅ Public GitHub data
- ✅ GitHub allowlisted domains (by default)
- ❌ Your local machine
- ❌ Private credentials (unless you provide them)
- ❌ Other cloud resources (unless configured)

### Security Tips
1. **Review Changes**: Always review Claude's PRs before merging
2. **Limit Repository Access**: Only grant access to repos Claude needs
3. **Use Branch Protection**: Require reviews on main/master branches
4. **Monitor Activity**: Check GitHub notifications for Claude's actions
5. **Revoke Access**: Can remove Claude GitHub app anytime

### Network Access
- By default: Limited to allowlisted domains (GitHub included)
- Can be configured for full network access if needed
- All requests go through secure proxies

## Workflow Examples

### Example 1: Quick Bug Fix
```
You: "Fix the bug in src/auth.py where users can't log out"
Claude: [reads file, identifies issue, fixes it, runs tests]
You: "Looks good, create a PR"
Claude: [creates PR with description]
You: [review on iPhone, merge when ready]
```

### Example 2: New Feature
```
You: "Add a dark mode toggle to the settings page"
Claude: [analyzes codebase, plans implementation]
You: "Sounds good, go ahead"
Claude: [implements feature, adds tests, updates docs]
You: "The toggle should be in the header instead"
Claude: [moves toggle, updates tests]
You: "Perfect, create a PR"
```

### Example 3: Automated via GitHub Actions
```
[In a PR comment on iPhone]
You: "@claude please add type hints to this file"
Claude: [automatically adds type hints, commits to PR]
You: [review and merge from iPhone]
```

## Troubleshooting

### "Cannot access repository"
- Check that Claude GitHub app is installed
- Verify repository permissions in GitHub settings
- Try disconnecting and reconnecting GitHub

### "Command failed in cloud environment"
- Some commands may not be available in the cloud VM
- Check if dependencies need to be installed
- Review error messages for missing packages

### "Network request blocked"
- Claude's cloud environment has limited network access
- GitHub is allowlisted by default
- For other domains, configure network settings

### "Session timeout"
- Long-running tasks may timeout
- Break into smaller subtasks
- Use GitHub Actions for very long operations

## Moving Between Devices

### Start on iPhone, Continue on Desktop
1. Start a task on iPhone at claude.ai/code
2. On your desktop, you can:
   - Continue in web browser at claude.ai/code
   - Click "Open in CLI" to move to terminal
   - Session state is preserved

### Start on Desktop, Check on iPhone
1. Start task in local terminal or web
2. Check progress on iPhone browser
3. Provide feedback from anywhere

## Pricing & Limits

### Requirements
- **Claude Pro**: $20/month (basic access)
- **Claude Max**: More usage, better priority
- **Team Premium**: For team collaboration

### Usage Limits
- Based on your Claude subscription tier
- Cloud compute included in subscription
- Same API limits as standard Claude usage

## Getting Help

### Resources
- **Documentation**: https://code.claude.com/docs
- **GitHub App**: https://github.com/apps/claude
- **Support**: https://support.anthropic.com
- **Issues**: https://github.com/anthropics/claude-code/issues

### Common Questions
- **Q**: Can I use Claude Code without GitHub?
  **A**: GitHub is currently required for the web version

- **Q**: Does this work with GitLab or Bitbucket?
  **A**: Currently only GitHub is supported

- **Q**: Can I use this on Android?
  **A**: Yes, the web interface works on any mobile browser

- **Q**: Is there a native iOS app?
  **A**: Not yet, but the web interface is mobile-friendly

- **Q**: Can Claude access my AWS/GCP resources?
  **A**: Yes, with proper configuration (requires setup)

## Next Steps

1. **Immediate**: Visit https://claude.ai/code on your iPhone
2. **Connect**: Link your GitHub account
3. **Try it**: Start with a simple task in a test repository
4. **Explore**: Experiment with different types of requests
5. **Configure**: Add CLAUDE.md to your main projects
6. **Automate**: Set up GitHub Actions for hands-free operation

---

**You're all set!** Open https://claude.ai/code on your iPhone and start coding with Claude in the cloud.

For questions or issues, check the documentation at https://code.claude.com/docs

Last updated: December 26, 2025
