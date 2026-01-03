---
title: "DATABASE_WORKFLOW"
project: klm-apartment-app
original_path: DATABASE_WORKFLOW.md
modified: 2026-01-03T11:17:02.892379
---

# Database Workflow - Questions, Answers, and Applicant Information

## 📊 Database Overview

The KAA database is designed to store all insurance application data in a flexible, normalized structure.

### Current Status

✅ **Database Created:** `kaa.db` (124 KB)
✅ **Field Mappings:** 417 records (maps questions across forms)
⚠️ **Applicant Data:** 0 records (ready to be populated)

---

## 🏗️ Database Structure

### Table 1: `field_mappings` (417 records)

**Purpose:** Maps canonical field names to form-specific field names

**Example Records:**
| Canonical Field | Form | Form Field Name | Required | Data Type |
|----------------|------|-----------------|----------|-----------|
| year_built | miller_supplemental_schema | YearBuilt | Yes | year |
| applicant's_name | miller_supplemental_schema | ApplicantName | Yes | text |
| construction_type | acord_140_schema | ConstructionType | No | text |

**What this means:**
- Same question appears on multiple forms with different names
- Database knows how to map "year_built" to each form's specific field name
- Tracks which fields are required for each form

---

### Table 2: `data_points` (0 records - ready for data)

**Purpose:** Universal storage for ALL applicant answers and information

**Schema:**
```
id                - Unique record ID
category          - Type of data (insured, property, building, fire_safety, etc.)
entity_id         - Identifies applicant/property (e.g., "eugene_malone", "prince_street")
field_name        - Canonical field name (e.g., "year_built")
field_label       - Human-readable label (e.g., "Year Built")
field_value       - The actual answer/data
data_type         - Type (text, number, date, yes_no, etc.)
source            - Where it came from (html_form, travelers_policy, etc.)
confidence        - 0.0-1.0 confidence score
required_for      - JSON array of forms that need this field
needs_review      - Flag for manual review
is_verified       - Mark as verified
created_at        - When created
updated_at        - When last updated
```

**Example Data (after import):**
| Entity ID | Category | Field Name | Field Value | Source |
|-----------|----------|------------|-------------|--------|
| eugene_malone | insured | applicant's_name | Eugene Mark Malone | html_form |
| eugene_malone | building | year_built | 1975 | html_form |
| prince_street | property | number_of_units | 3 | html_form |

---

## 🔄 Complete Workflow

### Step 1: Collect Data via HTML Form

**Form URL:** https://dev-kaa.s3.us-east-1.amazonaws.com/forms/missing-fields.html

1. Fill out the form (88 missing fields)
2. Submit - downloads `kaa_insurance_data.json`

**Example JSON:**
```json
{
  "applicant's_name": "Eugene Mark Malone",
  "mailing_address": "1554 Paoli Pike, West Chester, PA 19380",
  "year_built": "1975",
  "number_of_units": "30",
  ...
}
```

---

### Step 2: Import Data to Database

```bash
# Import form data
python3 scripts/import_form_data.py kaa_insurance_data.json eugene_malone html_form

# Output:
# 🔄 Loading form data from kaa_insurance_data.json...
#    Found 88 fields
# 🔄 Importing data for entity: eugene_malone...
#    Imported 10 fields...
#    Imported 20 fields...
#    ...
# ✅ Import complete!
#    Imported: 88 new fields
#    Skipped: 0 empty fields
#    Entity ID: eugene_malone
#    Source: html_form
```

**What happens:**
- Reads JSON file
- For each field:
  - Looks up metadata from `field_mappings`
  - Determines category automatically
  - Creates `data_point` record
  - Marks as verified (user-entered = trusted)
- Commits to database

---

### Step 3: View Database Contents

**Show Summary:**
```bash
python3 scripts/view_database.py

# Output:
# ============================================================
# KAA Database Summary
# ============================================================
# 📋 Field Mappings: 417 records
# 💾 Data Points: 88 records
# 👥 Entities (1):
#    eugene_malone: 88 fields
# 📊 Categories (7):
#    building: 15 fields
#    insured: 12 fields
#    fire_safety: 11 fields
#    ...
```

**View Specific Applicant:**
```bash
python3 scripts/view_database.py entity eugene_malone

# Shows all 88 fields organized by category
```

**Check Missing Required Fields:**
```bash
python3 scripts/view_database.py missing eugene_malone

# Shows which required fields are still empty
```

---

### Step 4: Generate Completed Forms (Future)

```bash
# Once all data is populated
python3 scripts/generate_completed_forms.py eugene_malone

# Generates:
# - ACORD_125_eugene_malone_2026-01-03.pdf
# - ACORD_140_eugene_malone_2026-01-03.pdf
# - Miller_Supplemental_eugene_malone_2026-01-03.pdf
```

---

## 🎯 Key Features

### 1. **Universal Data Model**
- One table (`data_points`) stores ALL data
- Flexible - can add new fields without schema changes
- Tracks metadata (source, confidence, verification status)

### 2. **Entity Support**
- Multiple applicants: `eugene_malone`, `john_doe`, etc.
- Multiple properties: `prince_street`, `middle_spring`, etc.
- Each entity has its own set of data points

### 3. **Smart Categorization**
Data is automatically categorized:
- `insured` - Personal/business info
- `building` - Building structure details
- `fire_safety` - Fire protection systems
- `building_updates` - Roof, electrical, plumbing, HVAC
- `management` - Property management
- `property_type` - Student housing, senior living, etc.

### 4. **Data Quality Tracking**
- `confidence` - How confident we are (0.0-1.0)
- `needs_review` - Flag for manual review
- `is_verified` - Verified by user or admin
- `source` - Audit trail of where data came from

### 5. **Form Mapping**
- Database knows which fields go on which forms
- Can generate any form by querying relevant fields
- Handles fields that appear on multiple forms

---

## 📥 Data Sources

The database can store data from multiple sources:

1. **HTML Form** (`html_form`)
   - User-entered data
   - High confidence (1.0)
   - Auto-verified

2. **Travelers Policy** (`travelers_policy`)
   - Extracted from existing policy
   - Already imported during setup

3. **Miller Forms** (`miller_forms`)
   - Extracted from filled forms
   - Already imported during setup

4. **Manual Entry** (`manual`)
   - Data entered by staff
   - Can flag for review

---

## 🔍 Example Queries

### Get all data for an applicant:
```python
data_points = db.query(DataPoint).filter(
    DataPoint.entity_id == "eugene_malone"
).all()
```

### Get specific field value:
```python
year_built = db.query(DataPoint).filter(
    DataPoint.entity_id == "eugene_malone",
    DataPoint.field_name == "year_built"
).first()

print(year_built.field_value)  # "1975"
```

### Get all building data:
```python
building_data = db.query(DataPoint).filter(
    DataPoint.entity_id == "eugene_malone",
    DataPoint.category == "building"
).all()
```

### Find fields needing review:
```python
needs_review = db.query(DataPoint).filter(
    DataPoint.needs_review == 'true'
).all()
```

---

## 🚀 Next Steps

1. **Fill out the form** at: https://dev-kaa.s3.us-east-1.amazonaws.com/forms/missing-fields.html

2. **Import the data:**
   ```bash
   python3 scripts/import_form_data.py kaa_insurance_data.json
   ```

3. **Verify import:**
   ```bash
   python3 scripts/view_database.py
   python3 scripts/view_database.py entity eugene_malone
   ```

4. **Check for missing fields:**
   ```bash
   python3 scripts/view_database.py missing eugene_malone
   ```

5. **Generate PDFs** (script to be created)

---

## 📞 Support

For questions about the database structure or workflow:
- **Developer:** mark@emm-associates.com
- **Company:** KLM Insurance Solutions, Inc.

---

**Last Updated:** January 3, 2026
