# E-commerce Analytics Dashboard — Specification

## Overview

A single-page Streamlit dashboard for ShopSmart's internal business team. Loads sales data from a static CSV and presents key metrics, trends, and breakdowns in a clean, executive-ready layout.

**Title:** ShopSmart Sales Dashboard

---

## Screens / Layout

### Single Page — Top to Bottom

```
┌─────────────────────────────────────────────────┐
│           ShopSmart Sales Dashboard              │
├──────────────┬──────────────┬────────────────────┤
│ Total Sales  │ Total Orders │  Avg Order Value   │
│  $XXX,XXX    │     482      │     $XXX.XX        │
├─────────────────────────────────────────────────┤
│         Sales Trend Over Time (Line)             │
│         Monthly granularity, full width          │
├──────────────────────┬──────────────────────────┤
│  Sales by Category   │    Sales by Region        │
│  (Bar, desc sorted)  │    (Bar, desc sorted)     │
└──────────────────────┴──────────────────────────┘
```

---

## Components

### KPI Cards (FR-1)
- **3 cards** in a single row: Total Sales, Total Orders, Average Order Value
- Total Sales: formatted as `$XXX,XXX` (currency, comma-separated)
- Total Orders: integer with comma separator
- Average Order Value: formatted as `$XXX.XX`
- Source column: `total_amount`

### Sales Trend Line Chart (FR-2)
- X-axis: Month (aggregated from `date` column, `YYYY-MM` grouping)
- Y-axis: Total sales amount
- Tooltips: currency-formatted value — e.g., `$45,230`
- Full-width, Plotly interactive

### Sales by Category Bar Chart (FR-3)
- Groups by `category` column, sums `total_amount`
- Sorted descending by value
- Tooltips: currency-formatted — e.g., `$45,230`
- Left column (50% width)

### Sales by Region Bar Chart (FR-4)
- Groups by `region` column, sums `total_amount`
- Sorted descending by value
- Tooltips: currency-formatted — e.g., `$45,230`
- Right column (50% width)

---

## Data

- **Source:** `data/sales-data.csv`
- **Key columns:** `date`, `order_id`, `category`, `region`, `total_amount`
- **Expected values:** Total Sales ~$116,500, Total Orders 482

---

## Out of Scope

- Filters, date pickers, dropdowns
- User-uploaded CSV
- Authentication
- Mobile layout
- Export (PDF/Excel)

---

## Acceptance Criteria

- [ ] 3 KPI cards visible and correctly calculated
- [ ] Line chart shows monthly sales trend with correct data
- [ ] Category bar chart sorted descending, all 5 categories shown
- [ ] Region bar chart sorted descending, all 4 regions shown
- [ ] All tooltips show currency-formatted values
- [ ] No errors on load
- [ ] Title reads "ShopSmart Sales Dashboard"
