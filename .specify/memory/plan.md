# E-commerce Analytics Dashboard — Implementation Plan

## File Structure

```
.
├── app.py                  # Single entry point — all code lives here
├── data/
│   └── sales-data.csv
└── pyproject.toml
```

---

## Implementation Steps

### Step 1 — Project Setup
- Initialize project with `uv init`
- Add dependencies: `streamlit`, `plotly`, `pandas`
- `pyproject.toml` as the sole dependency file
- Verify `uv run streamlit run app.py` launches without errors

### Step 2 — Data Loading
```python
@st.cache_data
def load_data():
    df = pd.read_csv("data/sales-data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df
```
- `@st.cache_data` — loads once per session, no redundant reads
- Parse `date` column to datetime on load

### Step 3 — KPI Cards
```python
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")
```
- Use `st.metric()` — no custom HTML
- Format strings handle all number formatting

### Step 4 — Sales Trend Line Chart
```python
monthly = df.groupby(df["date"].dt.to_period("M"))["total_amount"].sum().reset_index()
fig = px.line(monthly, x="date", y="total_amount")
st.plotly_chart(fig, use_container_width=True)
```
- Aggregate by month using `.dt.to_period("M")`
- Full width via `use_container_width=True`

### Step 5 — Category & Region Bar Charts
```python
col1, col2 = st.columns(2)
with col1:
    cat = df.groupby("category")["total_amount"].sum().sort_values(ascending=False)
    st.plotly_chart(px.bar(cat), use_container_width=True)
with col2:
    reg = df.groupby("region")["total_amount"].sum().sort_values(ascending=False)
    st.plotly_chart(px.bar(reg), use_container_width=True)
```
- Two-column layout, each chart fills its column

### Step 6 — Deploy
- Push to GitHub
- Connect to Streamlit Community Cloud
- Set main file to `app.py`

---

## Key Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| Structure | Single `app.py` | Simple scope, no need for modules |
| Caching | `@st.cache_data` | Avoid re-reading CSV on every interaction |
| Chart rendering | `use_container_width=True` | Responsive, fills layout columns |
| KPI cards | `st.metric()` | Built-in, no custom HTML needed |
| Dependencies | `pyproject.toml` + uv | Matches workshop stack |
