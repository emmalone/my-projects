---
title: "claude"
project: test
original_path: claude.md
modified: 2026-01-02T23:19:33.358056
---

# Project Portfolio Manager - Project Context

**Desktop Application for Project Portfolio Management & Visualization**

---

## 📋 Quick Reference

**Project Location:** `/Users/mark/PycharmProjects/test`
**Developer:** Mark (mark@emm-associates.com)
**Purpose:** Desktop app for managing project portfolios with interactive bubble chart visualization
**Tech Stack:** Python, tkinter (GUI), matplotlib (charts), pandas (data)
**Last Updated:** January 2, 2026

---

## 🎯 Project Purpose

A comprehensive project portfolio management tool that provides:
- **Table View:** Sortable table of all projects
- **CRUD Operations:** Add, edit, delete projects
- **Portfolio Visualization:** Interactive bubble chart showing timeline, priority, and revenue
- **Data Persistence:** CSV-based storage
- **Form Validation:** Date, priority, and revenue validation

---

## 📂 Project Structure

```
/Users/mark/PycharmProjects/test/
├── claude.md                  # This file - project context
├── main.py                    # Main application window and table view
├── data_manager.py            # Data persistence and CSV operations
├── portfolio_chart.py         # Bubble chart visualization window
├── project.csv                # Data file (gitignored)
├── projectsPortfolio.py       # Original single-file version (deprecated)
├── requirements.txt           # Python dependencies
├── HelloMark.py               # Test/demo file
├── hello_world.py             # Test/demo file
├── getsetup.py                # Setup utility
└── README.md                  # User documentation
```

---

## 🚀 Quick Start

### Installation
```bash
cd /Users/mark/PycharmProjects/test
pip install -r requirements.txt
```

### Run Application
```bash
python main.py
```

---

## 📊 Features

### 1. Table View (main.py)
- Displays all projects in sortable columns:
  - Project Name
  - Start Date
  - End Date
  - Priority (1-5)
  - Status
  - Annual Revenue ($)

### 2. CRUD Operations
- **Add:** Click "Add Project" button
- **Edit:** Double-click row or select and click "Edit"
- **Delete:** Select row and click "Delete"
- **Save:** Click "Save" to persist to CSV

### 3. Portfolio Chart (portfolio_chart.py)
- **Bubble Visualization:**
  - X-axis: Timeline (Start → End dates)
  - Y-axis: Priority (1-5)
  - Bubble Size: Annual revenue
  - Bubble Color: Project status
- **Interactive Features:**
  - Numbered bubbles with legend
  - Status filter dropdown
  - Hover tooltips

### 4. Project Statuses
- Active (Green)
- Planning (Blue)
- On Hold (Amber)
- Completed (Gray)

---

## 🗂️ Data Structure

### CSV File: project.csv
```csv
name,startDate,endDate,priority,status,AnnualRevenue
Website Redesign,2025-01-15,2025-06-30,5,Active,250000
Mobile App,2025-02-01,2025-12-31,4,Planning,500000
```

### Columns:
- **name:** Project name (string)
- **startDate:** Start date in YYYY-MM-DD format
- **endDate:** End date in YYYY-MM-DD format
- **priority:** Priority level 1-5 (integer)
- **status:** Project status (string, see list above)
- **AnnualRevenue:** Annual revenue in dollars (float)

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
- `ProjectPortfolioApp`: Main window with table
- CRUD dialog windows
- Event handlers for buttons and double-click

**data_manager.py:**
- `DataManager`: Handles CSV operations
- `load_projects()`: Load from CSV
- `save_projects()`: Save to CSV
- Data validation

**portfolio_chart.py:**
- `show_portfolio_chart()`: Visualization function
- Bubble chart rendering
- Status filtering
- Legend generation

---

## 💡 Usage Tips

### Best Practices
1. **Priority 5** for critical projects
2. **Update statuses** regularly to track progress
3. **Use chart view** to identify resource allocation
4. **Export CSV** for backup or reporting
5. **Save frequently** to avoid data loss

### Common Workflows

**Add New Project:**
```
1. Click "Add Project"
2. Enter project name
3. Set start date
4. Set end date (future)
5. Choose priority (1-5)
6. Select status
7. Enter annual revenue ($)
8. Click "OK"
9. Click "Save"
```

**View Portfolio:**
```
1. Click "Show Portfolio Chart"
2. Use status filter to focus on specific types
3. Check bubble sizes for high-revenue projects
4. Review timeline distribution
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
- Ensure at least one project exists in table
- Try filtering by "All" statuses
- Check console for error messages

### Changes Not Saving
- Click "Save" button before closing
- Check file permissions on `project.csv`
- Verify CSV file exists and is readable

### Data File Corrupted
```bash
# Backup current file
cp project.csv project.csv.backup

# Create new empty file
touch project.csv
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
- ✅ Added status filtering in chart view
- ✅ Created comprehensive README

### Code Organization
- ✅ Refactored from single-file (projectsPortfolio.py) to modular structure
- ✅ Separated concerns: UI, data, visualization
- ✅ Improved maintainability

---

## 🎯 Future Enhancements

Potential improvements:
- [ ] Export to Excel/PDF reports
- [ ] Date range filtering
- [ ] Revenue sum/average statistics
- [ ] Resource allocation tracking
- [ ] Database backend (SQLite) instead of CSV
- [ ] Multi-user support
- [ ] Dashboard with KPIs
- [ ] Gantt chart view
- [ ] Integration with project management tools

---

## 🔄 Comparison to OppManagement

This project is similar to `/Users/mark/PycharmProjects/OppManagement` but focuses on:
- **Projects** (not sales opportunities)
- **Annual Revenue** (not deal value)
- **Project Status** (not sales stage)
- **Portfolio Management** (not pipeline management)

### Code Reuse
Both projects share similar architecture:
- Same GUI framework (tkinter)
- Same visualization approach (matplotlib bubbles)
- Same data persistence (CSV)
- Similar CRUD operations

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

**Project Status:** Active - Test/Development
**Current Phase:** Stable, feature complete
**Next Steps:** Consider enhancements or production deployment

---

## 💡 Notes

**Project Name:**
This directory is named "test" but contains a production-quality project portfolio manager. Consider renaming to:
- `project-portfolio-manager`
- `portfolio-management`
- `project-tracker`

**Relationship to Other Projects:**
- Similar architecture to OppManagement
- Good candidate for creating a shared library/framework
- Could serve as template for other management apps

---

*Last updated: January 2, 2026*
