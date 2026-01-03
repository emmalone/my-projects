---
title: "README"
project: OppManagement
original_path: README.md
modified: 2025-12-20T00:31:01.729392
---

# Sales Opportunity Manager

A desktop application for managing and visualizing your sales pipeline with an interactive bubble chart.

## Features

- **Table View**: View all sales opportunities in a sortable table
- **CRUD Operations**: Add, edit, and delete opportunities
- **Data Validation**: Form validation for dates, priority, and deal values
- **Pipeline Visualization**: Interactive bubble chart showing opportunities by timeline and priority
- **CSV Persistence**: All data saved to `opportunities.csv`
- **Unsaved Changes Warning**: Prompts before closing with unsaved changes

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Navigate to the project directory:
```bash
cd ~/PycharmProjects/OppManagement
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

The main window displays a table with all sales opportunities:

| Column | Description |
|--------|-------------|
| Company/Opportunity | Name of the company or deal |
| Start Date | When the opportunity was identified |
| Expected Close | Anticipated close date |
| Priority | 1 (Low) to 5 (High) |
| Sales Stage | Current stage in pipeline |
| Deal Value | Potential revenue from the deal |

### Managing Opportunities

**Add Opportunity**
1. Click "Add Opportunity"
2. Fill in all fields:
   - Company/Opportunity name (required)
   - Start Date (YYYY-MM-DD format)
   - Expected Close Date (YYYY-MM-DD format)
   - Priority (1-5)
   - Sales Stage (dropdown)
   - Deal Value (in dollars)
3. Click "OK"

**Edit Opportunity**
- Double-click any row, or
- Select a row and click "Edit Opportunity"
- Modify fields and click "OK"

**Delete Opportunity**
- Select a row and click "Delete Opportunity"
- Confirm deletion

**Save Changes**
- Click "Save" to write changes to `opportunities.csv`
- You'll be prompted to save unsaved changes when quitting

### Pipeline Chart

Click "Show Pipeline Chart" to visualize your opportunities:

- **Bubble Position**: Timeline (X-axis) and Priority (Y-axis)
- **Bubble Size**: Represents deal value
- **Bubble Color**: Indicates sales stage
- **Numbered Bubbles**: Match the legend on the right
- **Filter**: Use the "Stage" dropdown to filter by sales stage

**Sales Stages & Colors:**
- Prospecting (Gray)
- Qualification (Blue)
- Proposal (Yellow)
- Negotiation (Orange)
- Closed Won (Green)
- Closed Lost (Red)

### Data File

All data is stored in `opportunities.csv` with the following columns:
- `company`: Company or opportunity name
- `startDate`: Start date (YYYY-MM-DD)
- `closeDate`: Expected close date (YYYY-MM-DD)
- `priority`: Priority level (1-5)
- `stage`: Sales stage
- `dealValue`: Deal value in dollars

## File Structure

```
OppManagement/
├── main.py                 # Main application window
├── data_manager.py         # Data persistence layer
├── opportunity_chart.py    # Visualization window
├── opportunities.csv       # Data file
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Troubleshooting

**Application won't start**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.8+)

**Chart window is blank**
- Ensure you have at least one opportunity in the table
- Try filtering by "All" stages

**Changes not saving**
- Click "Save" button before closing
- Check file permissions on `opportunities.csv`

## Tips

- Use Priority 5 for your hottest deals
- Update sales stages regularly to track progress
- Use the chart view to identify timeline bottlenecks
- Export `opportunities.csv` for backup or reporting
