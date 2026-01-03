---
title: "acord_140_extraction_summary"
project: klm-apartment-app
original_path: data/extracted/acord_140_extraction_summary.md
modified: 2026-01-03T11:24:42.973876
---

# ACORD 140 Data Extraction Summary

**Date:** January 3, 2026
**Source File:** `/Users/mark/PycharmProjects/klm-apartment-app/source-data/Malone+140+2026.pdf`
**Output File:** `/Users/mark/PycharmProjects/klm-apartment-app/data/extracted/acord_140_filled_data.json`
**Form Version:** ACORD 140 (2016/03)
**Form Title:** Property Section - Building and Personal Property Coverage

---

## Executive Summary

The ACORD 140 form in the source data is **primarily a blank template** with minimal header information filled in. This form is intended to be completed with specific property and building details but currently only contains:

- **Date:** 1/2/2026
- **Agency:** KLM Insurance Solutions, Inc.
- **Named Insured:** Eugene M Malone
- **Producer Signature:** Brian P. Malone

**No property-specific data, building details, or coverage information has been filled in.**

---

## What is ACORD 140?

The ACORD 140 is a standardized insurance form used for **Property Section - Building and Personal Property Coverage**. It is designed to:

- Collect detailed building construction information
- Document protection systems (fire, burglar, sprinkler)
- Record building improvements and updates
- Specify coverage amounts and deductibles
- Identify additional interests (mortgagees, loss payees)
- **Attach to ACORD 125** (the main commercial insurance application)

---

## Extracted Data

### Header Information (Filled)
- **Date:** 1/2/2026
- **Agency Name:** KLM Insurance Solutions, Inc.
- **Named Insured:** Eugene M Malone
- **Producer Signature:** Brian P. Malone

### Empty Sections (Need to be Completed)

#### 1. Premises Information
- Premises number
- Street address
- Building number
- Building description

#### 2. Building Construction Details
- Construction type (Frame, Masonry, Non-combustible, etc.)
- Year built
- Number of stories
- Number of basements
- Total area (square feet)
- Protection class
- Distance to hydrant
- Distance to fire station
- Fire district code
- Building code and grade
- Roof type
- Wind class

#### 3. Building Improvements
- Wiring updates (year)
- Plumbing updates (year)
- Roofing updates (year)
- Heating updates (year)
- Other improvements

#### 4. Protection Systems
- **Sprinkler Systems:** Percentage sprinklered, type
- **Fire Alarm:** Type, manufacturer, central/local
- **Burglar Alarm:** Type, certificate, installed by, extent
- **Guards/Watchmen:** Number, clock hourly
- **Fire Protection:** Standpipes, CO2/Chemical systems

#### 5. Heating Systems
- Primary heat: Type, boiler, solid fuel
- Secondary heat: Type, boiler, solid fuel
- Woodburning stoves/fireplace inserts

#### 6. Coverage Information
- Subject of insurance
- Coverage amounts
- Coinsurance percentage
- Causes of loss
- Inflation guard percentage
- Deductible amounts and types
- Forms and conditions to apply

#### 7. Additional Coverages
- Spoilage coverage
- Sinkhole coverage (Florida)
- Mine subsidence coverage (IL, IN, KY, WV)
- Power outage
- Breakdown or contamination
- Selling price option

#### 8. Additional Interests
- Lender's loss payable
- Loss payee
- Mortgagee
- Reference/loan numbers

#### 9. Exposures
- Right exposure and distance
- Left exposure and distance
- Front exposure and distance
- Rear exposure and distance

---

## Form Status Analysis

### Completion Level: **~5%**

Only basic header information is present. The form is essentially a blank template ready for completion.

### Confidence: **High (for what's present)**

The extracted header information is clear and accurate, but represents a very small portion of the total form.

### Form Purpose

This blank ACORD 140 form appears to be a **template prepared by the agency** (KLM Insurance Solutions) for Eugene M Malone, dated 1/2/2026. It is ready to be completed with:

1. Specific property addresses
2. Building construction details
3. Protection system information
4. Coverage amounts and limits
5. Building improvement history

---

## Next Steps Required

To complete the ACORD 140 form for Eugene M Malone's properties, the following information needs to be gathered:

### For Each Property:

1. **Property Identification**
   - Street address
   - Premises number
   - Building number and description

2. **Building Construction**
   - Construction type classification
   - Year built
   - Number of stories
   - Total square footage
   - Roof type and condition
   - Building code compliance

3. **Protection Class Information**
   - ISO Protection Class
   - Distance to nearest fire hydrant
   - Distance to fire station
   - Fire district information

4. **Protection Systems**
   - Sprinkler system (if any): type, coverage percentage
   - Fire alarm: type, monitoring
   - Burglar alarm: type, monitoring, certificate
   - Other fire protection equipment

5. **Building Systems**
   - Heating type (gas, oil, electric, etc.)
   - Electrical system (amperage, update year)
   - Plumbing update history

6. **Recent Improvements**
   - Wiring updates with years
   - Plumbing updates with years
   - Roofing updates with years
   - Heating system updates with years
   - Other major improvements

7. **Coverage Needs**
   - Building coverage amount
   - Business personal property amount
   - Coinsurance percentage
   - Deductible amounts
   - Additional coverages needed

8. **Financial Interests**
   - Mortgagee information (if applicable)
   - Loss payee designation
   - Lender's loss payable clause

---

## Comparison with Other Forms

This ACORD 140 should be compared with:

- **ACORD 125** (main application) - for consistency
- **Miller Supplemental Applications** - for property-specific details
- **Property inspection reports** - for building condition
- **Appraisal reports** - for replacement cost values

---

## Data Sources Needed

To complete this form, gather information from:

1. **Property Deeds and Records**
   - Legal descriptions
   - Ownership information
   - Parcel numbers

2. **Building Permits and Certificates**
   - Building code compliance
   - Improvement permits
   - Occupancy certificates

3. **Fire Department Records**
   - Protection class rating
   - Hydrant locations
   - Inspection reports

4. **Contractor Records**
   - Wiring updates
   - Plumbing updates
   - Roofing work
   - HVAC installations

5. **Alarm System Documentation**
   - Certificate numbers
   - Monitoring agreements
   - Service contracts

6. **Mortgage Documents**
   - Lender information
   - Loan numbers
   - Loss payee requirements

7. **Property Appraisals**
   - Replacement cost values
   - Building square footage
   - Construction classification

---

## Technical Notes

- **Form Version:** ACORD 140 (2016/03) - March 2016 version
- **Pages:** 3 pages total
  - Page 1: Primary premises information
  - Page 2: Additional premises information (for multiple buildings)
  - Page 3: Signatures and fraud warnings
- **Related Forms:**
  - Attaches to ACORD 125
  - References ACORD 810 (Business Income/Extra Expense)
  - References ACORD 811 (Value Reporting)
  - References ACORD 45 (Additional Interest)
  - References ACORD 101 (Additional Remarks)

---

## Extraction Metadata

- **Extraction Date:** 2026-01-03
- **Extraction Method:** Manual PDF read with Claude Code Read tool
- **Confidence Level:** High (for header data), N/A (for property details - not present)
- **Data Quality:** Template only - no substantive property data
- **Completeness:** ~5% (header information only)

---

## Recommendations

1. **Locate Completed ACORD 140 Forms**: Search for any previously completed ACORD 140 forms for Eugene M Malone's properties (20 S Prince St, 24 Middle Spring Ave)

2. **Review Miller Supplemental Applications**: The Miller Supplemental forms in the source-data folder may contain building details that should populate this ACORD 140

3. **Property Inspections**: Schedule or review property inspections to gather:
   - Construction details
   - Protection systems
   - Building improvements
   - Current condition

4. **Cross-Reference with ACORD 125**: Ensure consistency between the ACORD 125 (main application) and this ACORD 140 (property section)

5. **Gather Missing Data**: Create a data collection checklist based on the empty fields identified in this extraction

---

## Files Generated

1. **JSON Data File**: `/Users/mark/PycharmProjects/klm-apartment-app/data/extracted/acord_140_filled_data.json`
   - Machine-readable structured data
   - All form fields mapped
   - Empty fields clearly marked

2. **Summary Report**: This file
   - Human-readable analysis
   - Recommendations
   - Next steps

---

*Report generated by Claude Code data extraction process*
*Project: KLM Apartment Application (KAA) - Insurance Application Automation*
