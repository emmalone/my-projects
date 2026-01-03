---
title: "MVP_SCOPE"
project: klm-apartment-app
original_path: planning/MVP_SCOPE.md
modified: 2026-01-02T16:50:57.034059
---

# KAA MVP Scope - Day 1 Target

**Created**: 2026-01-02  
**Deadline**: End of day 2026-01-02

---

## MVP Definition: Minimum Viable Product

**Goal**: Demonstrate single end-to-end workflow in 8 hours

### What MVP Includes (MUST HAVE)
1. ✓ Database schema (3 tables: properties, applications, form_templates)
2. ✓ FastAPI backend with 5 endpoints:
   - POST /api/properties - Create property
   - GET /api/properties/{id} - Get property
   - POST /api/applications - Create application from property
   - POST /api/forms/upload - Upload PDF template
   - POST /api/applications/{id}/generate - Generate filled PDF

3. ✓ PDF Processing:
   - Upload ACORD 125 form as template
   - Extract fields using pdfplumber
   - Fill form with property data using pypdf
   - Save generated PDF to output/

4. ✓ Hardcoded field mapping (no intelligence):
   - Map 10 core fields manually in code
   - Property name → "Named Insured"
   - Property address → "Location"
   - Building value → "Building Limit"
   - etc.

5. ✓ CLI test script:
   - Script to create sample property
   - Upload form template
   - Generate PDF
   - Verify output

### What MVP EXCLUDES (Later Phases)
- ❌ Field mapping intelligence
- ❌ Confidence scoring
- ❌ Multiple carriers (only 1 template)
- ❌ User authentication
- ❌ Frontend/UI
- ❌ Interested parties
- ❌ Historical tracking
- ❌ Bulk operations
- ❌ Data validation rules
- ❌ Mobile interface

---

## Day 1 Implementation Plan

### Hour 1-2: Database & Models
```python
# SQLAlchemy models
- Property (id, name, address, value, etc.)
- Application (id, property_id, template_id, status)
- FormTemplate (id, name, pdf_path, field_mappings_json)
```

### Hour 3-4: FastAPI Endpoints
- Setup FastAPI app
- 5 CRUD endpoints
- Pydantic schemas
- SQLite database connection

### Hour 5-6: PDF Processing
- pdfplumber: Extract fields from template
- pypdf: Fill template with data
- Save to output directory
- Handle errors gracefully

### Hour 7: Testing
- Create test property
- Upload ACORD 125 template
- Generate PDF
- Verify fields populated correctly

### Hour 8: Documentation
- Update CLAUDE.md
- Document API endpoints
- Create README with setup instructions

---

## Success Criteria

MVP is complete when:
1. ✓ Can run: `python scripts/test_mvp.py`
2. ✓ Creates property in database
3. ✓ Uploads PDF template
4. ✓ Generates filled PDF in output/
5. ✓ At least 5 fields correctly populated
6. ✓ All code committed to GitHub

---

## Week 1 Expansion (Days 2-7)

After MVP proven, expand to:
- Multiple form templates
- React frontend for data entry
- Field mapping UI
- User authentication
- 2-3 carriers supported

---

## Week 2-3: Production Ready

- Full field intelligence
- 10+ carriers
- Historical tracking
- Deployment to AWS
- Mobile-friendly interface

---

## Risks & Mitigation

**Risk**: PDF form is not fillable  
**Mitigation**: Test with ACORD 125 first (known fillable), fallback to ReportLab overlay

**Risk**: 8 hours not enough  
**Mitigation**: Reduce to 3 tables, 3 endpoints, 3 fields if needed

**Risk**: pypdf compatibility issues  
**Mitigation**: Have sample ACORD 125 ready for testing

---

## Files Needed for MVP

1. `backend/app/main.py` - FastAPI app
2. `backend/app/models/property.py` - SQLAlchemy models
3. `backend/app/schemas/property.py` - Pydantic schemas
4. `backend/app/services/pdf_service.py` - PDF processing
5. `backend/app/database.py` - Database setup
6. `scripts/test_mvp.py` - MVP test script
7. `pyproject.toml` - Dependencies

---

**Let's ship something today, iterate tomorrow.**
