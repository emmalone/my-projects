---
title: "claude"
project: OppManagement
original_path: claude.md
modified: 2026-01-02T23:17:30.694629
---

# Sales Opportunity Manager - Project Context

**Desktop Application for Sales Pipeline Management & Visualization**

---

## 📋 Quick Reference

**Project Location:** `/Users/mark/PycharmProjects/OppManagement`
**Developer:** Mark (mark@emm-associates.com)
**Purpose:** Desktop app for managing sales opportunities with interactive bubble chart visualization
**Tech Stack:** Python, tkinter (GUI), matplotlib (charts), pandas (data)
**Last Updated:** January 2, 2026

---

## 🎯 Project Purpose

A comprehensive sales opportunity management tool that provides:
- **Table View:** Sortable table of all opportunities
- **CRUD Operations:** Add, edit, delete opportunities
- **Pipeline Visualization:** Interactive bubble chart showing timeline and priority
- **Data Persistence:** CSV-based storage
- **Form Validation:** Date, priority, and deal value validation

---

## 📂 Project Structure

```
/Users/mark/PycharmProjects/OppManagement/
├── claude.md                  # This file - project context
├── main.py                    # Main application window and table view
├── data_manager.py            # Data persistence and CSV operations
├── opportunity_chart.py       # Bubble chart visualization window
├── opportunities.csv          # Data file (gitignored)
├── requirements.txt           # Python dependencies
├── sampleData1.csv            # Sample data for testing
└── README.md                  # User documentation
```

---

## 🚀 Quick Start

### Installation
```bash
cd /Users/mark/PycharmProjects/OppManagement
pip install -r requirements.txt
```

### Run Application
```bash
python main.py
```

---

## 📊 Features

### 1. Table View (main.py)
- Displays all opportunities in sortable columns:
  - Company/Opportunity
  - Start Date
  - Expected Close Date
  - Priority (1-5)
  - Sales Stage
  - Deal Value ($)

### 2. CRUD Operations
- **Add:** Click "Add Opportunity" button
- **Edit:** Double-click row or select and click "Edit"
- **Delete:** Select row and click "Delete"
- **Save:** Click "Save" to persist to CSV

### 3. Pipeline Chart (opportunity_chart.py)
- **Bubble Visualization:**
  - X-axis: Timeline (Start → Close dates)
  - Y-axis: Priority (1-5)
  - Bubble Size: Deal value
  - Bubble Color: Sales stage
- **Interactive Features:**
  - Numbered bubbles with legend
  - Stage filter dropdown
  - Hover tooltips

### 4. Sales Stages
- Prospecting (Gray)
- Qualification (Blue)
- Proposal (Yellow)
- Negotiation (Orange)
- Closed Won (Green)
- Closed Lost (Red)

---

## 🗂️ Data Structure

### CSV File: opportunities.csv
```csv
company,startDate,closeDate,priority,stage,dealValue
Acme Corp,2025-01-15,2025-03-01,5,Negotiation,150000
TechStart Inc,2025-01-20,2025-04-15,4,Proposal,75000
```

### Columns:
- **company:** Company or opportunity name (string)
- **startDate:** Start date in YYYY-MM-DD format
- **closeDate:** Expected close date in YYYY-MM-DD format
- **priority:** Priority level 1-5 (integer)
- **stage:** Sales stage (string, see list above)
- **dealValue:** Deal value in dollars (float)

---

## 🔧 Technical Details

### Dependencies (requirements.txt)
```
tkinter       # GUI framework (built-in Python)
matplotlib    # Chart visualization
pandas        # Data handling
csv           # CSV file operations
```

### Key Classes

**main.py:**
- `OpportunityManager`: Main window with table
- CRUD dialog windows
- Event handlers for buttons and double-click

**data_manager.py:**
- `load_opportunities()`: Load from CSV
- `save_opportunities()`: Save to CSV
- Data validation

**opportunity_chart.py:**
- `OpportunityChart`: Visualization window
- Bubble chart rendering
- Stage filtering
- Legend generation

---

## 💡 Usage Tips

### Best Practices
1. **Priority 5** for hottest deals
2. **Update stages** regularly to track progress
3. **Use chart view** to identify timeline bottlenecks
4. **Export CSV** for backup or reporting
5. **Save frequently** to avoid data loss

### Common Workflows

**Add New Opportunity:**
```
1. Click "Add Opportunity"
2. Enter company name
3. Set start date (today or earlier)
4. Set expected close date (future)
5. Choose priority (1-5)
6. Select sales stage
7. Enter deal value ($)
8. Click "OK"
9. Click "Save"
```

**View Pipeline:**
```
1. Click "Show Pipeline Chart"
2. Use stage filter to focus on specific stages
3. Check bubble sizes for high-value deals
4. Review timeline spread
```

---

## 🐛 Troubleshooting

### Application Won't Start
```bash
# Check Python version (needs 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt
```

### Chart Window is Blank
- Ensure at least one opportunity exists in table
- Try filtering by "All" stages
- Check console for error messages

### Changes Not Saving
- Click "Save" button before closing
- Check file permissions on `opportunities.csv`
- Verify CSV file exists and is readable

### Data File Corrupted
```bash
# Restore from sample data
cp sampleData1.csv opportunities.csv
```

---

## 📝 Recent Work History

### Initial Development
- ✅ Created main window with table view
- ✅ Implemented CRUD operations (Add, Edit, Delete)
- ✅ Built data persistence layer with CSV
- ✅ Created bubble chart visualization
- ✅ Added form validation
- ✅ Implemented unsaved changes warning
- ✅ Added stage filtering in chart view
- ✅ Created comprehensive README

---

## 🎯 Future Enhancements

Potential improvements:
- [ ] Export to Excel/PDF reports
- [ ] Date range filtering
- [ ] Deal value sum/average statistics
- [ ] Email notifications for approaching close dates
- [ ] Database backend (SQLite) instead of CSV
- [ ] Multi-user support
- [ ] Dashboard with KPIs
- [ ] Calendar view of opportunities

---

## 📞 Support & Contact

**Developer Contact:**
- Mark
- Email: mark@emm-associates.com

**For Claude Code Sessions:**
- This file (`claude.md`) contains all project context
- Reference specific sections as needed
- Update this file after major changes
- Commit to git for version control

---

**Project Status:** Active - Production use
**Current Phase:** Stable, feature complete
**Next Steps:** Consider enhancements based on user feedback

---

*Last updated: January 2, 2026*
