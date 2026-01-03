---
title: "CLAUDE"
project: remote
original_path: demo-task-api/CLAUDE.md
modified: 2025-12-26T15:25:43.428846
---

# Claude Code Instructions

## Project: Task Manager API Demo

### Purpose
This is a learning demo to showcase Claude Code workflows. It's a simple REST API for task management.

## Tech Stack
- **Framework**: FastAPI
- **Python Version**: 3.9+
- **Testing**: Pytest
- **Validation**: Pydantic

## Coding Standards

### Python Style
- Follow PEP 8
- Use type hints for all functions
- Keep functions small and focused
- Maximum line length: 100 characters

### Documentation
- Add docstrings to all public functions
- Use Google-style docstrings
- Keep comments clear and concise

### Testing
- Minimum 80% code coverage
- Test all API endpoints
- Include edge cases and error scenarios
- Use descriptive test names: `test_<action>_<expected_result>`

## Development Workflow

### Running the Application
```bash
uvicorn app.main:app --reload
```

### Running Tests
```bash
pytest tests/ -v --cov=app
```

### Code Quality Checks
```bash
# Format check
black app/ tests/ --check

# Type checking
mypy app/

# Linting
flake8 app/ tests/
```

## API Design Guidelines

### Response Format
All successful responses should return JSON with appropriate status codes:
- 200: OK (GET, PUT)
- 201: Created (POST)
- 204: No Content (DELETE)
- 404: Not Found
- 422: Validation Error

### Error Handling
- Always return clear error messages
- Include error type and details
- Use FastAPI's HTTPException

### Data Validation
- Use Pydantic models for all request/response data
- Validate all inputs
- Return meaningful validation errors

## Project-Specific Notes

### Task Model
Tasks should have:
- `id`: Unique identifier (int)
- `title`: Task title (required, max 100 chars)
- `description`: Optional description
- `completed`: Boolean status (default: false)
- `created_at`: Timestamp

### In-Memory Storage
For simplicity, this demo uses in-memory storage (a dictionary). This means:
- Data is lost when the server restarts
- No database setup required
- Perfect for learning and testing

## Common Tasks

When asked to improve this project, consider:
1. Adding input validation edge cases
2. Improving error messages
3. Adding more comprehensive tests
4. Adding logging
5. Improving documentation

## Deployment Notes
This is a demo project - not production-ready. Missing:
- Database persistence
- Authentication/authorization
- Rate limiting
- CORS configuration (if needed for frontend)
- Environment configuration
