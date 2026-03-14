# Jira Tasks — ShopSmart Sales Dashboard

**Project:** `ECOM` | **Total tasks:** 7 | **Format:** Flat list, sequenced

---

### ECOM-? — Project setup and dependencies
**Step 1 of 7**
Initialize the project and verify it runs.
- Run `uv init` in the project directory
- Add dependencies: `streamlit`, `plotly`, `pandas`
- Create `app.py` with a placeholder `st.title("ShopSmart Sales Dashboard")`
- Verify `uv run streamlit run app.py` opens in browser without errors

**Done when:** App loads in browser showing the title, no errors in terminal.

*Ref: `.specify/memory/plan.md` — Step 1*

---

### ECOM-? — Data loading
**Step 2 of 7**
Load and cache the CSV.
- Implement `load_data()` with `@st.cache_data`
- Read `data/sales-data.csv` with `pd.read_csv()`
- Parse `date` column to datetime
- Call `load_data()` in `app.py` and verify shape

**Done when:** DataFrame loads without error; `date` column is datetime dtype; ~1000 rows present.

*Ref: `.specify/memory/plan.md` — Step 2*

---

### ECOM-? — KPI metric cards
**Step 3 of 7**
Display the three top-line KPIs.
- Calculate: Total Sales (sum of `total_amount`), Total Orders (count of `order_id`), Avg Order Value
- Render with `st.columns(3)` and `st.metric()`
- Format: Total Sales as `$XXX,XXX`, Total Orders with comma, Avg Order Value as `$XXX.XX`

**Done when:** Three cards visible in a row; Total Sales ~$116,500; Total Orders = 482.

*Ref: `.specify/memory/spec.md` — KPI Cards, `.specify/memory/plan.md` — Step 3*

---

### ECOM-? — Sales trend line chart
**Step 4 of 7**
Build the monthly sales trend visualization.
- Aggregate `total_amount` by month (`dt.to_period("M")`)
- Build Plotly line chart with labeled axes
- Render full-width with `st.plotly_chart(fig, use_container_width=True)`

**Done when:** Line chart renders full-width; X-axis shows months; tooltips show currency values.

*Ref: `.specify/memory/spec.md` — Sales Trend Line Chart, `.specify/memory/plan.md` — Step 4*

---

### ECOM-? — Sales by category bar chart
**Step 5 of 7**
Build the category breakdown visualization.
- Group by `category`, sum `total_amount`, sort descending
- Build Plotly bar chart with labeled axes
- Render in left column (50% width)

**Done when:** All 5 categories shown, sorted highest to lowest; tooltips show currency values.

*Ref: `.specify/memory/spec.md` — Sales by Category Bar Chart*

---

### ECOM-? — Sales by region bar chart
**Step 6 of 7**
Build the region breakdown visualization.
- Group by `region`, sum `total_amount`, sort descending
- Build Plotly bar chart with labeled axes
- Render in right column alongside category chart (50% width)

**Done when:** All 4 regions shown, sorted highest to lowest; tooltips show currency values; side-by-side with category chart.

*Ref: `.specify/memory/spec.md` — Sales by Region Bar Chart*

---

### ECOM-? — Deploy to Streamlit Community Cloud
**Step 7 of 7**
Ship the dashboard.
- Push code to GitHub
- Connect repo to Streamlit Community Cloud
- Set main file to `app.py`
- Verify all acceptance criteria from spec are met on the live URL

**Done when:** Dashboard is publicly accessible; all 7 acceptance criteria from `.specify/memory/spec.md` pass.

*Ref: `.specify/memory/plan.md` — Step 6*
