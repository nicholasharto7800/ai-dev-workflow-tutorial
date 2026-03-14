# E-commerce Analytics Dashboard Constitution

## Core Principles

### I. Audience-First
This dashboard serves internal business users — sales managers and executives. All design decisions prioritize clarity and immediate comprehension over configurability or technical depth.

### II. At-a-Glance Summary
The primary job of the dashboard is to answer "how is the business doing?" in seconds. KPI cards (Total Revenue, Total Orders, Average Order Value) are the most important elements and must be prominent above the fold.

### III. Static Data, No Filtering
Data is loaded from a bundled static CSV (`data/sales-data.csv`). There are no date range pickers, category filters, or user-uploaded files. Simplicity over flexibility.

### IV. Visualization Hierarchy
Three visualization layers, in order of importance:
1. KPI metric cards — revenue, orders, avg order value
2. Line chart — sales trend over time
3. Bar chart — revenue or orders by product category

### V. Correctness Over Polish
Charts must be labeled clearly and totals must be accurate. Expected values: Total Sales ~$650k–$700k, Total Orders ~482. These are the acceptance criteria.

## Tech Stack

- **Streamlit** — UI framework
- **Pandas** — CSV loading and aggregation
- **Plotly** — Interactive charts
- **Python 3.11+**, **uv** — Runtime and package manager
- **GitHub** — Source control
- **Streamlit Community Cloud** — Deployment target

## Out of Scope

- Date range or category filters
- User-uploaded CSV
- Live database or API connections
- Authentication or multi-user features
- Advanced analytics or drill-down views

## Governance

This constitution defines the boundaries of the project. Features or changes that contradict these principles require explicit amendment before implementation. When in doubt, do less — prefer the simpler interpretation.

**Version**: 1.0.0 | **Ratified**: 2026-03-13 | **Last Amended**: 2026-03-13
