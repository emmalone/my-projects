---
title: "claude"
project: klm-apartment-app
original_path: claude.md
modified: 2026-01-03T11:27:11.043352
---

# KLM Apartment Application (KAA) - Insurance Application Automation

**Complete Project Context & Technical Reference**

---

## 📋 Quick Reference

**Project Location:** `/Users/mark/PycharmProjects/klm-apartment-app`
**Repository:** https://github.com/emmalone/klm-apartment-app
**Developer:** Mark (mark@emm-associates.com)
**Company:** KLM Insurance Solutions, Inc.
**Last Updated:** January 3, 2026

---

## 🤖 Agent Usage Best Practices

### When to Use Agents

**ALWAYS use agents for:**
- **Data Extraction Tasks:** Extracting data from multiple PDFs, documents, or data sources
- **Parallel Processing:** When multiple independent tasks can run simultaneously
- **Complex Analysis:** Deep code exploration, codebase analysis, or multi-file research
- **Domain-Specific Tasks:** Tasks requiring specialized knowledge or reasoning (e.g., insurance forms, legal documents)
- **Time-Intensive Operations:** Long-running tasks that benefit from background processing

### Agent Types and Selection

#### 1. **Explore Agent** (Fast, codebase-focused)
- **Use for:** Finding files by patterns, searching code for keywords, understanding codebase structure
- **Thoroughness levels:** "quick", "medium", "very thorough"
- **Example:** "Explore the codebase to find all database models"

#### 2. **General-Purpose Agent** (Multi-step tasks)
- **Use for:** Complex multi-step workflows, data extraction, analysis tasks
- **Best with:** Sonnet model for reasoning-heavy tasks
- **Example:** "Extract all data from these 5 PDF documents and consolidate findings"

#### 3. **Plan Agent** (Architecture and design)
- **Use for:** Planning implementation strategies, designing system architecture
- **Returns:** Step-by-step plans, identifies critical files, considers trade-offs
- **Example:** "Plan the implementation of a new PDF form processing pipeline"

### Parallel Agent Execution

**Maximum Efficiency Pattern:**
```python
# Launch multiple agents in a single message block
Task(agent_a7a1888, "Extract ACORD 125 data")  # Agent 1
Task(agent_a5e7481, "Extract ACORD 140 data")  # Agent 2
Task(agent_a50f6b2, "Extract apartment app data")  # Agent 3
Task(agent_ac66a3e, "Extract quote data")  # Agent 4
Task(agent_a27410f, "Extract commercial app data")  # Agent 5

# All 5 agents run in parallel, completing in fraction of sequential time
```

**When to run agents in parallel:**
- Processing multiple independent documents/files
- Extracting data from different sources simultaneously
- Analyzing different parts of a codebase concurrently
- Running tests while performing other operations

### Agent Best Practices from This Project

**Real-world example from this session:**

1. **Initial Task:** Extract data from 17 PDF documents and identify missing fields
2. **Solution:** Launched 5 parallel agents with Sonnet for intelligent reasoning
3. **Results:**
   - All 5 agents completed successfully
   - Processed 7 data sources (including previous extractions)
   - Consolidated 211 unique fields
   - Mapped 41 fields to canonical names
   - Identified 75 missing required fields
   - Generated targeted form with only missing fields

**Key Success Factors:**
- Used Sonnet model for intelligent data extraction and reasoning
- Ran agents in true parallel (single message, multiple Task calls)
- Allowed agents to complete independently before consolidation
- Created consolidation script to merge results intelligently

### Creating Domain-Specific "Persistent" Agents

**Approach for building specialized agents that improve over time:**

#### 1. **Knowledge Base Pattern**
```
Project Structure:
/agents/
  /insurance-forms/
    knowledge-base.md      # Domain knowledge about ACORD forms
    extraction-patterns.json  # Known field patterns
    field-mappings.json    # Canonical field mappings
    agents/
      extract-acord.py     # Reusable extraction logic
      consolidate.py       # Consolidation logic
```

#### 2. **Iterative Refinement**
- Start with general-purpose agent for initial extraction
- Document successful patterns in knowledge base
- Create reusable scripts encoding learned patterns
- Each run adds to the knowledge base

#### 3. **Building "Memory" Through Documentation**
```markdown
# agents/insurance-forms/knowledge-base.md

## ACORD 125 Extraction Patterns

**Known Field Locations:**
- Applicant Name: Usually in upper left, line 2-3
- FEIN/SSN: Center header area
- Producer info: Top of page, right side

**Common Issues:**
- Blank template forms labeled as "filled"
- Multiple properties on single form
- Handwritten vs. digital signatures

**Successful Extraction Methods:**
1. Use pdfplumber for table extraction
2. Fall back to pypdf for text extraction
3. Pattern matching with regex for structured fields
```

#### 4. **Agent Skill Progression**

**Level 1: Basic Agent** (Session 1)
- Extract text from PDF
- Return raw text and basic fields

**Level 2: Pattern-Aware Agent** (Session 2)
- Use documented patterns from knowledge base
- Apply known field mappings
- Return structured data

**Level 3: Intelligent Agent** (Session 3+)
- Reference previous successful extractions
- Handle edge cases from knowledge base
- Self-improve by adding new patterns

#### 5. **Implementation Strategy**

**For this project (insurance forms):**

```python
# Create domain-specific extraction agent
class InsuranceFormAgent:
    def __init__(self):
        self.knowledge_base = load_knowledge_base()
        self.field_mappings = load_field_mappings()
        self.extraction_patterns = load_patterns()

    def extract(self, pdf_path, form_type):
        # Use accumulated knowledge
        patterns = self.extraction_patterns[form_type]
        mappings = self.field_mappings[form_type]

        # Extract with learned patterns
        data = intelligent_extract(pdf_path, patterns, mappings)

        # Update knowledge base with new findings
        self.update_knowledge_base(data)

        return data
```

**Knowledge Base Updates After Each Session:**
```bash
# After successful extraction
python3 scripts/update_knowledge_base.py \
  --session-id=2026-01-03 \
  --extractions=data/extracted/*.json \
  --confidence=high
```

### Practical Agent Usage Guidelines

**DO:**
- ✅ Use agents proactively for multi-step tasks
- ✅ Launch parallel agents for independent operations
- ✅ Choose appropriate agent type (Explore, General, Plan)
- ✅ Use Sonnet model for reasoning-intensive tasks
- ✅ Document successful patterns for future reference
- ✅ Let agents complete before processing results

**DON'T:**
- ❌ Run agents sequentially when they could run in parallel
- ❌ Use agents for simple single-step tasks (use tools directly)
- ❌ Interrupt agents before completion
- ❌ Forget to consolidate/process agent results

### Agent Model Selection

**Sonnet (Default):**
- Best for reasoning, analysis, complex extraction
- Use for: Data extraction, code analysis, planning
- Cost: Moderate

**Haiku (Fast):**
- Best for simple, quick tasks
- Use for: Basic file operations, simple searches
- Cost: Low

**Opus (Maximum Capability):**
- Best for most complex reasoning tasks
- Use for: Critical analysis, complex decision-making
- Cost: High

### Real-World Agent Performance

**This Session's Results:**
- **Task:** Extract data from 17 PDFs
- **Agents:** 5 parallel Sonnet agents
- **Total Time:** ~3 minutes (vs. 15+ minutes sequential)
- **Success Rate:** 100% (5/5 agents completed)
- **Data Quality:** 211 fields extracted, 41 mapped to canonical names
- **Cost Efficiency:** 5x speedup with parallel execution

---

## 🎯 Project Overview

KAA is an insurance application automation system designed to streamline the process of completing commercial apartment building insurance applications across multiple carriers. The system extracts data from PDF forms, stores it in a normalized database, intelligently maps common fields, and auto-generates completed applications while maintaining historical records.

### MVP Scope (Current Focus)
- **Insured:** Eugene Mark Malone
- **Properties:** 2 investment properties (Prince Street, Middle Spring)
- **Forms:** ACORD 125, ACORD 140, Miller Supplemental Application
- **Goal:** Collect existing data, identify missing fields, complete all required forms

### Technology Stack
- **Backend:** FastAPI (Python) + SQLAlchemy 2.0 + SQLite
- **Frontend:** React with TypeScript
- **PDF Processing:** pypdf, pdfplumber, ReportLab
- **Development:** Poetry for dependencies, Alembic for migrations
- **Deployment:** AWS S3 (dev/staging/production), GitHub Actions CI/CD

---

## ⚙️ Claude Code Permission Configuration

### Settings File Location
**Project Settings:** `.claude/settings.json` (committed to git)
**Local Overrides:** `.claude/settings.local.json` (gitignored)

### Current Configuration
The project has pre-configured permissions in `.claude/settings.json` that allow:
- ✅ All git commands (status, add, commit, push, etc.)
- ✅ Python commands (poetry, pytest, alembic, uvicorn)
- ✅ AWS CLI commands (S3, CloudFront)
- ✅ GitHub CLI commands (gh run, gh secret, gh pr)
- ✅ Reading all project files
- ✅ Editing code files (py, tsx, ts, jsx, js, yml, toml, json)
- ✅ WebSearch and approved domain fetches

**Default Mode:** `acceptEdits` - Auto-accepts file edits without prompting

### Key Permission Rules
```json
"allow": [
  "Bash(git:*)",              // All git commands
  "Bash(poetry:*)",           // Poetry dependency management
  "Bash(pytest:*)",           // Testing
  "Bash(alembic:*)",          // Database migrations
  "Bash(uvicorn:*)",          // FastAPI server
  "Bash(aws s3:*)",           // AWS S3 operations
  "Bash(gh:*)",               // GitHub CLI
  "Read(/Users/mark/PycharmProjects/klm-apartment-app/**)",
  "Edit(**/*.py)",            // Python files
  "Edit(**/*.ts)",            // TypeScript
  "Edit(**/*.tsx)",           // React TypeScript
  "Edit(**/*.json)",          // Config files
  "Edit(**/*.md)",            // Documentation
  "WebSearch"
],
"deny": [
  "Read(.env*)",              // Protect environment files
  "Bash(rm -rf:*)",           // Prevent destructive deletes
  "Bash(sudo:*)",             // No sudo commands
  "Bash(git push --force:*)"  // No force pushes
]
```

### View Active Permissions
In any Claude Code session, type:
```
/permissions
```

---

## 🔑 Credentials & API Keys

### AWS Account
- **Account ID:** 837716495292
- **IAM User:** klm-hugo
- **Access Key ID:** AKIA4GC6LJO6OIIMIIRY
- **Region:** us-east-1
- **AWS CLI Profile:** default

**Verify AWS Access:**
```bash
aws sts get-caller-identity
# Should return Account: 837716495292, User: klm-hugo
```

### GitHub
- **Repository:** emmalone/klm-apartment-app
- **GitHub User:** emmalone
- **GitHub CLI:** Authenticated with workflow scope
- **Actions Secrets:**
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION` = us-east-1
  - `S3_DEV_BUCKET` = dev-kaa

### Claude API (Production)
- **Current:** Using personal Max plan for development
- **Production:** Will shift to API key (pay-per-use) when deploying

---

## 🌐 Deployment Environments

The project supports **3 development scenarios** with 3 deployment environments:

### Development Scenarios

#### Scenario 1: Laptop/Desktop Development (Mac/PC)
- **Branch:** `main`
- **Testing:** Local dev server + auto-deploy to dev
- **Local URL:** http://localhost:8000 (API), http://localhost:3000 (Frontend)
- **Dev URL:** http://dev-kaa.s3-website-us-east-1.amazonaws.com
- **Deploy to Staging:** Manual control only
- **Auto-deploy to Dev:** ✅ YES - Every push to main
- **Auto-deploy to Staging:** ❌ NO - Manual control only

#### Scenario 2: iPhone Development (Claude Code + GitHub)
- **Branch:** `claude/**` (auto-created by Claude Code)
- **Testing:** Auto-deploy to dev environment
- **URL:** http://dev-kaa.s3-website-us-east-1.amazonaws.com
- **Deploy:** ✅ AUTOMATIC on push to any `claude/**` branch
- **Target Bucket:** `dev-kaa`

#### Scenario 3: Staging Deployment
- **Target:** staging-kaa bucket
- **Deploy Method:** Manual control ONLY
- **Auto-deploy:** ❌ DISABLED - You control when staging updates

---

### Environment Details

### 1. Local Development
- **API URL:** http://localhost:8000
- **Frontend URL:** http://localhost:3000
- **Database:** SQLite (`kaa.db` in project root)
- **Purpose:** Local development and testing on laptop/desktop
- **Start Backend:** `poetry run uvicorn backend.app.main:app --reload`
- **Start Frontend:** `cd frontend && npm start`

### 2. Dev Environment (Auto-Deploy Always)
- **URL:** http://dev-kaa.s3-website-us-east-1.amazonaws.com
- **S3 Bucket:** dev-kaa
- **Region:** us-east-1
- **Purpose:** Always-current development preview for both laptop and iPhone work
- **Trigger:** ✅ Auto-deploys on push to `main` OR `claude/**` branches
- **Workflow:** `.github/workflows/deploy-dev.yml`
- **Cache:** 5 minutes (max-age=300)

**When It Deploys:**
- ✅ Automatically when you push to `main` (laptop/desktop work)
- ✅ Automatically when you push to any `claude/**` branch (iPhone work)
- Preview ready in ~30 seconds after push

### 3. Staging (Manual Deployment Only)
- **URL:** http://staging-kaa.s3-website-us-east-1.amazonaws.com
- **S3 Bucket:** staging-kaa
- **Purpose:** Business review and stakeholder approval
- **Deploy Method:** ⚠️ MANUAL ONLY - Python script or manual AWS sync
- **Cache:** 1 hour (max-age=3600)

**Deployment Command (From Laptop/Desktop ONLY):**
```bash
cd /Users/mark/PycharmProjects/klm-apartment-app
# Deploy script to be created
python scripts/deploy_staging.py
```

**Important:** Staging does NOT auto-deploy. You have full control over when changes go to staging.

### 4. Production (Future)
- **URL:** TBD (when ready for production)
- **S3 Bucket:** production-kaa
- **Status:** 🔄 Not yet configured
- **Purpose:** Live application for agency use
- **Deploy Script:** `scripts/deploy_production.py` (to be created)

---

## 🔄 Git Branch Strategy

### Branches
- **`main`** - Primary development branch (laptop/desktop work)
- **`claude/**`** - Auto-created by Claude Code on iPhone (e.g., `claude/add-feature-xyz`)

### Workflow

#### Working on Laptop/Desktop:
```bash
# Work directly on main branch
git checkout main
git pull origin main

# Make changes locally
# ... edit files ...

# Test locally
poetry run uvicorn backend.app.main:app --reload

# When satisfied, commit to main
git add .
git commit -m "Your changes"
git push origin main

# Deploy to staging when ready (manual control)
python scripts/deploy_staging.py
```

#### Working on iPhone with Claude Code:
```
Claude Code automatically:
1. Creates branch: claude/feature-name-xyz
2. Makes changes
3. Commits changes
4. Pushes to GitHub
5. Auto-deploys to dev-kaa S3 bucket

Preview at: http://dev-kaa.s3-website-us-east-1.amazonaws.com

When ready:
- Create PR to merge claude/* branch into main
- Or ask Claude to merge directly to main
```

### Important Notes
- **No staging branch** - Staging deployment is controlled manually
- **No auto-deploy to staging** - You decide when staging updates
- **iPhone work previews on dev** - All `claude/**` branches auto-deploy to dev-kaa
- **Laptop work stays local** - Test locally, deploy to staging when ready

---

## 📂 Project Structure

```
/Users/mark/PycharmProjects/klm-apartment-app/
├── claude.md                           # ⭐ This file - project context
├── REQUIREMENTS.md                     # Complete requirements doc
├── MVP_SCOPE.md                        # MVP definition
├── CLAUDE_CODE_INSTRUCTIONS.md         # Implementation instructions
├── CONVERSATION_SUMMARY.md             # Handoff document
├── README.md                           # Project overview
├── pyproject.toml                      # Python dependencies (Poetry)
├── .gitignore                          # Git ignore rules
│
├── .claude/                            # Claude Code configuration
│   └── settings.json                   # Permissions
│
├── .github/workflows/                  # GitHub Actions
│   ├── deploy-dev.yml                  # Auto-deploy dev branch
│   └── deploy-staging.yml              # Manual staging deploy (disabled)
│
├── backend/                            # FastAPI backend
│   ├── app/
│   │   ├── main.py                     # FastAPI application
│   │   ├── database.py                 # Database setup
│   │   ├── models/                     # SQLAlchemy models
│   │   │   ├── applicant.py
│   │   │   ├── property.py
│   │   │   ├── application.py
│   │   │   ├── carrier.py
│   │   │   └── form_template.py
│   │   ├── schemas/                    # Pydantic schemas
│   │   ├── api/                        # API endpoints
│   │   │   ├── applicants.py
│   │   │   ├── properties.py
│   │   │   ├── applications.py
│   │   │   └── forms.py
│   │   ├── services/                   # Business logic
│   │   │   ├── pdf_service.py          # PDF processing
│   │   │   └── field_mapping.py        # Field mapping intelligence
│   │   └── utils/                      # Helper functions
│   └── tests/                          # Backend tests
│
├── frontend/                           # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/                 # React components
│   │   ├── pages/                      # Page components
│   │   ├── services/                   # API clients
│   │   └── App.tsx
│   ├── package.json
│   └── tsconfig.json
│
├── alembic/                            # Database migrations
│   ├── versions/                       # Migration files
│   └── env.py
│
├── templates/                          # PDF templates
│   └── pdfs/
│       ├── acord_125.pdf               # ACORD 125 form
│       ├── acord_140.pdf               # ACORD 140 form
│       └── miller_supplemental.pdf     # Miller Supplemental
│
├── source-data/                        # Source documents
│   ├── Malone+125+2026.pdf
│   ├── Malone+140+2026.pdf
│   ├── Millers+supplemental+24+Middle+Spring.pdf
│   └── Millers+supplemental+20+S+Prince+St.pdf
│
├── output/                             # Generated PDFs
│   └── applications/
│
└── scripts/                            # Utility scripts
    ├── test_mvp.py                     # MVP test script
    ├── deploy_staging.py               # Staging deployment
    └── deploy_production.py            # Production deployment
```

---

## 📝 Data Architecture

### Core Entities

#### 1. Applicants
- Personal/business information
- Contact details
- SSN/EIN, DOB
- One applicant → many properties

#### 2. Properties
- Address, parcel number
- Building details (year built, construction, units)
- Financial data (value, replacement cost)
- One property → many applications

#### 3. Applications
- Links applicant + property + carrier
- Status tracking (Draft → Submitted → Bound)
- Generated PDF references
- Historical archive

#### 4. Carriers
- Insurance company information
- NAIC number
- Required forms list

#### 5. Form Templates
- PDF template files
- Field definitions
- Mapping to database fields
- Version control

### Database Tables
See `REQUIREMENTS.md` Section 3 for complete table schemas.

---

## 🚀 Development Workflows

### Initial Setup
```bash
# Clone repository
git clone https://github.com/emmalone/klm-apartment-app.git
cd klm-apartment-app

# Install Poetry (if not installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install Python dependencies
poetry install

# Initialize database
poetry run alembic upgrade head

# Install frontend dependencies
cd frontend
npm install
cd ..

# Start backend
poetry run uvicorn backend.app.main:app --reload

# Start frontend (in separate terminal)
cd frontend
npm start
```

### Testing
```bash
# Run backend tests
poetry run pytest

# Run MVP test
poetry run python scripts/test_mvp.py

# Check code quality
poetry run ruff check .
poetry run mypy backend/
```

### Database Migrations
```bash
# Create new migration
poetry run alembic revision --autogenerate -m "Description"

# Apply migrations
poetry run alembic upgrade head

# Rollback migration
poetry run alembic downgrade -1
```

---

## 📚 Important Documentation Files

### Project Planning
- **`claude.md`** - This file - complete project context
- **`REQUIREMENTS.md`** - Comprehensive requirements (18 pages)
- **`MVP_SCOPE.md`** - MVP definition and scope
- **`CLAUDE_CODE_INSTRUCTIONS.md`** - Implementation guide
- **`CONVERSATION_SUMMARY.md`** - Project handoff document

### Technical Documentation
- **`README.md`** - Project overview and setup
- **`API.md`** - API documentation (to be created)
- **`DATABASE.md`** - Database schema reference (to be created)

---

## 🐛 Troubleshooting

### Backend Won't Start
**Problem:** `uvicorn` fails to start
**Solution:** Check database connection
```bash
# Verify database file exists
ls -la kaa.db

# Check alembic migrations
poetry run alembic current

# Reinitialize if needed
rm kaa.db
poetry run alembic upgrade head
```

### Frontend Can't Connect to API
**Problem:** CORS errors or connection refused
**Solution:** Verify backend is running and CORS configured
```bash
# Check backend is running
curl http://localhost:8000/api/health

# Check CORS settings in backend/app/main.py
# Should allow http://localhost:3000
```

### PDF Processing Errors
**Problem:** pypdf fails to fill forms
**Solution:** Verify PDF is fillable
```bash
# Test PDF fields
poetry run python -c "
from pypdf import PdfReader
reader = PdfReader('templates/pdfs/acord_125.pdf')
if '/AcroForm' in reader.trailer['/Root']:
    print('PDF is fillable')
    fields = reader.get_fields()
    print(f'Found {len(fields)} fields')
else:
    print('PDF is NOT fillable - use ReportLab overlay')
"
```

### GitHub Actions Failing
**Problem:** Deploy workflow fails with AWS errors
**Solution:** Check GitHub secrets
```bash
gh secret list
# Should show:
# - AWS_ACCESS_KEY_ID
# - AWS_SECRET_ACCESS_KEY
# - AWS_REGION
# - S3_DEV_BUCKET
```

---

## 🎯 Recent Work History

### January 2, 2026 (Initial Setup)
- ✅ Created project structure
- ✅ Defined comprehensive requirements
- ✅ Created MVP scope
- ✅ Set up claude.md for project context
- ✅ Configured GitHub CLI and AWS CLI
- 🔄 Next: Initialize git repository and create GitHub repo

---

## 📋 Outstanding Tasks

### Priority 1 - Project Setup
- [ ] Initialize git repository
- [ ] Create GitHub repository `emmalone/klm-apartment-app`
- [ ] Set up AWS S3 buckets (dev-kaa, staging-kaa, production-kaa)
- [ ] Configure GitHub Actions workflows
- [ ] Create .claude/settings.json

### Priority 2 - MVP Development
- [ ] Set up FastAPI backend structure
- [ ] Set up React frontend structure
- [ ] Create database models (SQLAlchemy)
- [ ] Implement PDF extraction (parse existing filled forms)
- [ ] Implement PDF filling (generate completed forms)
- [ ] Create test data for Eugene Mark Malone + 2 properties

### Priority 3 - MVP Completion
- [ ] Extract data from source-data PDFs
- [ ] Identify missing fields for ACORD 125, 140, Miller Supplemental
- [ ] Complete all required forms for Eugene Mark Malone
- [ ] Test end-to-end workflow
- [ ] Deploy to dev environment

### Priority 4 - Future Enhancements
- [ ] Add field mapping intelligence
- [ ] Support multiple carriers
- [ ] Add user authentication
- [ ] Create reporting dashboards
- [ ] Deploy to production

---

## 🔗 Useful Links

**Production Sites:**
- Dev Preview: http://dev-kaa.s3-website-us-east-1.amazonaws.com (when deployed)
- Staging: http://staging-kaa.s3-website-us-east-1.amazonaws.com (when deployed)

**External Services:**
- AWS Console: https://console.aws.amazon.com (Account: 837716495292)
- GitHub Repository: https://github.com/emmalone/klm-apartment-app
- GitHub Actions: https://github.com/emmalone/klm-apartment-app/actions

**Technical Resources:**
- FastAPI Documentation: https://fastapi.tiangolo.com/
- SQLAlchemy 2.0: https://docs.sqlalchemy.org/
- pypdf: https://pypdf.readthedocs.io/
- pdfplumber: https://github.com/jsvine/pdfplumber
- ReportLab: https://www.reportlab.com/docs/reportlab-userguide.pdf

---

## 💡 Pro Tips

### Working Remotely (iPhone/iPad)
1. Make changes with Claude Code on iPhone
2. Claude automatically creates branch and commits
3. Push triggers auto-deploy to dev
4. Preview at dev URL within 30 seconds

### Faster Local Development
```bash
# Use --reload for auto-restart on code changes
poetry run uvicorn backend.app.main:app --reload

# Run frontend in watch mode (default)
cd frontend && npm start
```

### Testing PDF Processing
```bash
# Analyze PDF form fields
poetry run python -c "
import pdfplumber
with pdfplumber.open('templates/pdfs/acord_125.pdf') as pdf:
    for page in pdf.pages:
        print(f'Page {page.page_number}:')
        for field in page.annots or []:
            print(f'  {field}')
"
```

---

## 🏢 Company Information

**KLM Insurance Solutions, Inc.**
- **Address:** 1554 Paoli Pike, West Chester, PA 19380
- **Phone:** 610-429-1330
- **Email:** info@klminsurance.com
- **Website:** www.klminsurance.com

---

## 📞 Support & Contact

**Developer Contact:**
- Mark
- Email: mark@emm-associates.com
- GitHub: emmalone

**For Claude Code Sessions:**
- This file (`claude.md`) contains all project context
- Reference specific sections as needed
- Update this file after major milestones
- Commit changes to keep it in sync across devices

---

**Project Status:** Initial Setup
**Current Phase:** Environment configuration and repository setup
**Next Milestone:** MVP development - Extract and fill insurance forms

---

*Last session work: Initial project setup, requirements definition, and infrastructure planning*
