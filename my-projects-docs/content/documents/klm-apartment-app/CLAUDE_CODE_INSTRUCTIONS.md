---
title: "CLAUDE_CODE_INSTRUCTIONS"
project: klm-apartment-app
original_path: CLAUDE_CODE_INSTRUCTIONS.md
modified: 2026-01-02T16:50:37.684616
---

# Claude Code - MVP Implementation Instructions

## Objective
Build working MVP by end of day: Single property → PDF generation workflow

## Autonomous Operation Mode
- Auto-approve: ✓ Enabled
- Confirm commands: ✗ Disabled  
- Max iterations: 100
- Update CLAUDE.md every hour with progress

## Implementation Order (8 Hours)

### Phase 1: Database Foundation (90 minutes)
1. Create `backend/app/database.py`:
   - SQLAlchemy async engine setup
   - SQLite connection
   - Base declarative model

2. Create `backend/app/models/property.py`:
   ```python
   class Property(Base):
       id, name, address_street, address_city, address_state, 
       address_zip, year_built, building_value, total_units, 
       construction_type, stories
   ```

3. Create `backend/app/models/application.py`:
   ```python
   class Application(Base):
       id, property_id (FK), template_id (FK), 
       status, generated_pdf_path, created_at
   ```

4. Create `backend/app/models/form_template.py`:
   ```python
   class FormTemplate(Base):
       id, name, carrier_name, pdf_path, 
       field_mappings (JSON), created_at
   ```

5. Setup Alembic:
   - `poetry run alembic init alembic`
   - Configure alembic.ini for SQLite
   - Create initial migration
   - Run migration

**Checkpoint**: Database creates successfully, tables exist

---

### Phase 2: Pydantic Schemas (30 minutes)
1. Create `backend/app/schemas/property.py`:
   - PropertyCreate, PropertyResponse, PropertyUpdate

2. Create `backend/app/schemas/application.py`:
   - ApplicationCreate, ApplicationResponse

3. Create `backend/app/schemas/form_template.py`:
   - FormTemplateCreate, FormTemplateResponse

**Checkpoint**: Schemas import without errors

---

### Phase 3: FastAPI Application (60 minutes)
1. Create `backend/app/main.py`:
   ```python
   from fastapi import FastAPI
   from fastapi.middleware.cors import CORSMiddleware
   
   app = FastAPI(title="KAA API")
   
   # Include routers
   app.include_router(properties_router)
   app.include_router(applications_router)
   app.include_router(forms_router)
   ```

2. Create `backend/app/api/properties.py`:
   - POST /api/properties (create property)
   - GET /api/properties/{id} (get property)
   - GET /api/properties (list all)

3. Create `backend/app/api/applications.py`:
   - POST /api/applications (create application)
   - POST /api/applications/{id}/generate (generate PDF)

4. Create `backend/app/api/forms.py`:
   - POST /api/forms/upload (upload template)
   - POST /api/forms/{id}/analyze (extract fields)

**Checkpoint**: `uvicorn backend.app.main:app --reload` starts without errors

---

### Phase 4: PDF Service (2 hours)
This is the critical component. Take time to get it right.

1. Create `backend/app/services/pdf_service.py`:

```python
class PDFService:
    def analyze_form(self, pdf_path: Path) -> dict:
        """Use pdfplumber to extract all fields from PDF"""
        # Return: {field_name: {type, position, page}}
        
    def create_field_mappings(self) -> dict:
        """Hardcoded mappings for MVP"""
        return {
            "named_insured": "property.name",
            "location_address": "property.address_street",
            "location_city": "property.address_city",
            "location_state": "property.address_state",
            "location_zip": "property.address_zip",
            "year_built": "property.year_built",
            "building_limit": "property.building_value",
            "number_of_stories": "property.stories",
            "construction_type": "property.construction_type",
            "number_of_units": "property.total_units",
        }
    
    def fill_pdf(self, template_path: Path, data: dict, output_path: Path):
        """Fill PDF form fields using pypdf"""
        # 1. Open template with pypdf
        # 2. Map property data to form fields
        # 3. Fill fields
        # 4. Save to output_path
        
    def fill_pdf_overlay(self, template_path: Path, data: dict, output_path: Path):
        """Fallback: Use ReportLab to overlay data"""
        # Only implement if pypdf fails
```

**Critical**: Test with actual ACORD 125 form
- If fillable: Use pypdf method
- If not fillable: Use ReportLab overlay (harder, takes longer)

2. Create `backend/app/utils/pdf_helpers.py`:
   - Helper functions for coordinate mapping
   - PDF validation
   - Error handling

**Checkpoint**: Can fill at least ONE field in PDF successfully

---

### Phase 5: Integration (90 minutes)
1. Wire up endpoints to services:
   - POST /properties → Create property in DB
   - POST /forms/upload → Save PDF, analyze fields
   - POST /applications → Create application record
   - POST /applications/{id}/generate → Call pdf_service.fill_pdf()

2. Add error handling:
   - File not found
   - Invalid PDF
   - Missing fields
   - Database errors

3. Add logging:
   - Log all PDF operations
   - Log field mappings
   - Log errors

**Checkpoint**: Can make HTTP requests through full workflow

---

### Phase 6: Test Script (60 minutes)
1. Create `scripts/test_mvp.py`:

```python
#!/usr/bin/env python3
"""MVP Test Script - Runs end-to-end workflow"""

import requests
import json
from pathlib import Path

BASE_URL = "http://localhost:8000/api"

def test_mvp():
    # 1. Create property
    property_data = {
        "name": "Sunset Apartments LLC",
        "address_street": "123 Main Street",
        "address_city": "Phoenix",
        "address_state": "AZ",
        "address_zip": "85001",
        "year_built": 1995,
        "building_value": 2500000,
        "total_units": 24,
        "construction_type": "Masonry",
        "stories": 3
    }
    
    resp = requests.post(f"{BASE_URL}/properties", json=property_data)
    property_id = resp.json()["id"]
    print(f"✓ Property created: {property_id}")
    
    # 2. Upload form template
    template_path = Path("templates/pdfs/acord_125.pdf")
    files = {"file": open(template_path, "rb")}
    resp = requests.post(f"{BASE_URL}/forms/upload", files=files)
    template_id = resp.json()["id"]
    print(f"✓ Template uploaded: {template_id}")
    
    # 3. Create application
    app_data = {
        "property_id": property_id,
        "template_id": template_id
    }
    resp = requests.post(f"{BASE_URL}/applications", json=app_data)
    application_id = resp.json()["id"]
    print(f"✓ Application created: {application_id}")
    
    # 4. Generate PDF
    resp = requests.post(f"{BASE_URL}/applications/{application_id}/generate")
    pdf_path = resp.json()["pdf_path"]
    print(f"✓ PDF generated: {pdf_path}")
    
    # 5. Verify PDF exists
    if Path(pdf_path).exists():
        print(f"✓✓✓ MVP SUCCESS! PDF exists at {pdf_path}")
        return True
    else:
        print(f"✗ MVP FAILED: PDF not found")
        return False

if __name__ == "__main__":
    test_mvp()
```

2. Get sample ACORD 125 form:
   - Search for "ACORD 125 fillable PDF download"
   - Save to `templates/pdfs/acord_125.pdf`
   - If can't find: Use any simple fillable PDF for MVP

**Checkpoint**: Script runs without errors

---

### Phase 7: Testing & Debugging (60 minutes)
1. Run test script
2. Fix any errors that appear
3. Verify at least 5 fields populated in output PDF
4. Open PDF manually to inspect

**Success Criteria**:
- ✓ Property saved to database
- ✓ Template uploaded and analyzed
- ✓ Application created
- ✓ PDF generated in output/ directory
- ✓ At least 5 fields visible in PDF

---

### Phase 8: Documentation (30 minutes)
1. Update CLAUDE.md with:
   - What was built
   - What works
   - Known issues
   - Next steps

2. Update README.md with:
   - Setup instructions tested
   - How to run MVP test

3. Git commit:
   ```bash
   git add .
   git commit -m "feat: MVP - Single property to PDF workflow"
   git push origin main
   ```

---

## Error Recovery

If stuck for > 30 minutes on any phase:
1. Reduce scope further
2. Hardcode more things
3. Skip non-essential features
4. Document as "Known Limitation"

**Remember**: Working software > Perfect software

---

## Field Mappings (Hardcoded for MVP)

If ACORD 125 field names are different, update these mappings:

```python
ACORD_125_MAPPINGS = {
    # ACORD field name → Database column
    "NamedInsured": "property.name",
    "MailingAddress": "property.address_street",
    "City": "property.address_city", 
    "State": "property.address_state",
    "ZIP": "property.address_zip",
    "LocationAddress": "property.address_street",
    "YearBuilt": "property.year_built",
    "BuildingLimit": "property.building_value",
    "NumberOfStories": "property.stories",
    "ConstructionType": "property.construction_type",
    "TotalUnits": "property.total_units",
}
```

---

## Success Definition

MVP is complete when:
1. ✓ Can run `python scripts/test_mvp.py`
2. ✓ Script completes without errors
3. ✓ PDF file created in output/
4. ✓ Can open PDF and see populated fields
5. ✓ At least 5 fields correctly filled

**Time Budget**: 8 hours  
**Extensions Allowed**: +2 hours if needed  
**Absolute Deadline**: End of day

---

## After MVP

Once working:
1. Commit to GitHub
2. Update CLAUDE.md with "MVP Complete ✓"
3. Ask Mark for next priority:
   - Add more forms?
   - Add frontend?
   - Add field mapping intelligence?
   - Deploy to AWS?

---

## Notes for Claude Code

- Don't overthink it
- Hardcode field mappings (no AI/ML for MVP)
- Use simplest approach that works
- Test each component before moving to next
- Save progress frequently (commit after each phase)
- Update CLAUDE.md every hour

**Primary Goal**: Demonstrate it CAN work  
**Secondary Goal**: Make it perfect (comes later)

Let's ship something today! 🚀
