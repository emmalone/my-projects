---
title: "README"
project: test
original_path: README.md
modified: 2025-12-20T00:31:20.073336
---

# Project Portfolio Manager

A desktop application for managing and visualizing your project portfolio with an interactive bubble chart.

## Features

- **Table View**: View all projects in a sortable table
- **CRUD Operations**: Add, edit, and delete projects
- **Data Validation**: Form validation for dates, priority, and revenue
- **Portfolio Visualization**: Interactive bubble chart showing projects by timeline and priority
- **CSV Persistence**: All data saved to `project.csv`
- **Unsaved Changes Warning**: Prompts before closing with unsaved changes

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Navigate to the project directory:
```bash
cd ~/PycharmProjects/test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

### Main Window

The main window displays a table with all projects:

| Column | Description |
|--------|-------------|
| Project Name | Name of the project |
| Start Date | Project start date |
| End Date | Project end date |
| Priority | 1 (Low) to 5 (High) |
| Status | Current project status |
| Annual Revenue | Expected annual revenue |

### Managing Projects

**Add Project**
1. Click "Add Project"
2. Fill in all fields:
   - Project Name (required)
   - Start Date (YYYY-MM-DD format)
   - End Date (YYYY-MM-DD format)
   - Priority (1-5)
   - Status (dropdown)
   - Annual Revenue (in dollars)
3. Click "OK"

**Edit Project**
- Double-click any row, or
- Select a row and click "Edit Project"
- Modify fields and click "OK"

**Delete Project**
- Select a row and click "Delete Project"
- Confirm deletion

**Save Changes**
- Click "Save" to write changes to `project.csv`
- You'll be prompted to save unsaved changes when quitting

### Portfolio Chart

Click "Show Portfolio Chart" to visualize your projects:

- **Bubble Position**: Timeline (X-axis) and Priority (Y-axis)
- **Bubble Size**: Represents annual revenue
- **Bubble Color**: Indicates project status
- **Numbered Bubbles**: Match the legend on the right
- **Filter**: Use the "Status" dropdown to filter by project status

**Project Statuses & Colors:**
- Active (Green)
- Planning (Blue)
- On Hold (Amber)
- Completed (Gray)

### Data File

All data is stored in `project.csv` with the following columns:
- `name`: Project name
- `startDate`: Start date (YYYY-MM-DD)
- `endDate`: End date (YYYY-MM-DD)
- `priority`: Priority level (1-5)
- `status`: Project status
- `AnnualRevenue`: Annual revenue in dollars

## File Structure

```
test/
├── main.py                 # Main application window
├── data_manager.py         # Data persistence layer
├── portfolio_chart.py      # Visualization window
├── project.csv             # Data file
├── projectsPortfolio.py    # Original single-file version (deprecated)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Troubleshooting

**Application won't start**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.8+)

**Chart window is blank**
- Ensure you have at least one project in the table
- Try filtering by "All" statuses

**Changes not saving**
- Click "Save" button before closing
- Check file permissions on `project.csv`

## Tips

- Use Priority 5 for critical projects
- Update project statuses regularly to track progress
- Use the chart view to identify resource allocation patterns
- Export `project.csv` for backup or reporting
