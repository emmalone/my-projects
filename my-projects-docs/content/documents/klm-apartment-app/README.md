---
title: "README"
project: klm-apartment-app
original_path: README.md
modified: 2026-01-02T18:04:17.656583
---

# KLM Apartment Application (KAA)

Insurance application automation system for commercial apartment buildings.

## Overview

KAA automates the process of completing insurance applications across multiple carriers by:
- Extracting data from filled PDF forms
- Storing applicant and property data in a normalized database
- Intelligently mapping form fields to database fields
- Auto-generating completed PDF applications
- Maintaining historical records of all submissions

## Technology Stack

- **Backend:** FastAPI + SQLAlchemy 2.0 + SQLite
- **Frontend:** React with TypeScript
- **PDF Processing:** pypdf, pdfplumber, ReportLab
- **Development:** Poetry, Alembic, pytest
- **Deployment:** AWS S3, GitHub Actions

## Quick Start

### Prerequisites

- Python 3.11+
- Poetry (`curl -sSL https://install.python-poetry.org | python3 -`)
- Node.js 18+ and npm
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/emmalone/klm-apartment-app.git
cd klm-apartment-app

# Install Python dependencies
poetry install

# Initialize database
poetry run alembic upgrade head

# Install frontend dependencies
cd frontend
npm install
cd ..
```

### Run Locally

```bash
# Terminal 1: Start backend
poetry run uvicorn backend.app.main:app --reload
# API will be available at http://localhost:8000
# API docs at http://localhost:8000/docs

# Terminal 2: Start frontend
cd frontend
npm start
# Frontend will be available at http://localhost:3000
```

### Run Tests

```bash
# Backend tests
poetry run pytest

# MVP test script
poetry run python scripts/test_mvp.py
```

## Project Structure

```
klm-apartment-app/
├── backend/                # FastAPI backend
│   ├── app/
│   │   ├── main.py        # FastAPI application
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── api/           # API endpoints
│   │   └── services/      # Business logic
│   └── tests/             # Backend tests
├── frontend/              # React frontend
│   └── src/
├── templates/             # PDF form templates
├── source-data/           # Source documents (not in git)
├── output/                # Generated PDFs
├── scripts/               # Utility scripts
└── alembic/               # Database migrations
```

## MVP Scope

**Focus:** Eugene Mark Malone + 2 properties (Prince Street, Middle Spring)

**Forms:**
- ACORD 125 (Commercial Insurance Application)
- ACORD 140 (Property Section)
- Miller Supplemental Application

**Goals:**
1. Extract data from existing filled forms
2. Store data in SQLite database
3. Identify missing required fields
4. Generate completed PDF applications

## Development Workflow

### Local Development (Laptop/Desktop)
- Work on `main` branch
- Test locally with dev servers
- Push to GitHub triggers auto-deploy to dev environment

### Remote Development (iPhone with Claude Code)
- Claude Code creates `claude/*` branches automatically
- Push triggers auto-deploy to dev environment
- Preview at http://dev-kaa.s3-website-us-east-1.amazonaws.com

### Deployment
- **Dev:** Auto-deploy on push to `main` or `claude/*`
- **Staging:** Manual deployment only
- **Production:** Manual deployment only (future)

## Documentation

- **[claude.md](claude.md)** - Complete project context and technical reference
- **[REQUIREMENTS.md](REQUIREMENTS.md)** - Comprehensive requirements document
- **[MVP_SCOPE.md](planning/MVP_SCOPE.md)** - MVP definition and scope
- **[CLAUDE_CODE_INSTRUCTIONS.md](CLAUDE_CODE_INSTRUCTIONS.md)** - Implementation guide

## Database Migrations

```bash
# Create new migration
poetry run alembic revision --autogenerate -m "Description"

# Apply migrations
poetry run alembic upgrade head

# Rollback
poetry run alembic downgrade -1

# View current version
poetry run alembic current
```

## API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation (Swagger UI).

## Contributing

This is a private project for KLM Insurance Solutions, Inc.

## Support

For questions or issues:
- **Developer:** Mark (mark@emm-associates.com)
- **Company:** KLM Insurance Solutions, Inc.
- **Phone:** 610-429-1330

## License

Proprietary - KLM Insurance Solutions, Inc.
