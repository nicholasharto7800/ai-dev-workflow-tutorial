import pandas as pd
import plotly.express as px
import streamlit as st

st.title("ShopSmart Sales Dashboard")


@st.cache_data
def load_data():
    df = pd.read_csv("data/sales-data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df


df = load_data()

# KPI Cards
total_sales = df["total_amount"].sum()
total_orders = df["order_id"].nunique()
avg_order_value = total_sales / total_orders

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# Sales Trend Line Chart
st.subheader("Sales Trend Over Time")
monthly = df.groupby(df["date"].dt.to_period("M"))["total_amount"].sum().reset_index()
monthly["date"] = monthly["date"].astype(str)
fig = px.line(
    monthly,
    x="date",
    y="total_amount",
    labels={"date": "Month", "total_amount": "Sales ($)"},
)
fig.update_traces(hovertemplate="Month: %{x}<br>Sales: $%{y:,.0f}<extra></extra>")
st.plotly_chart(fig, use_container_width=True)

# Sales by Category and Region Bar Charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Sales by Category")
    cat = (
        df.groupby("category")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig_cat = px.bar(
        cat,
        x="category",
        y="total_amount",
        labels={"category": "Category", "total_amount": "Sales ($)"},
    )
    fig_cat.update_traces(hovertemplate="Category: %{x}<br>Sales: $%{y:,.0f}<extra></extra>")
    st.plotly_chart(fig_cat, use_container_width=True)

with col_right:
    st.subheader("Sales by Region")
    reg = (
        df.groupby("region")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    fig_reg = px.bar(
        reg,
        x="region",
        y="total_amount",
        labels={"region": "Region", "total_amount": "Sales ($)"},
    )
    fig_reg.update_traces(hovertemplate="Region: %{x}<br>Sales: $%{y:,.0f}<extra></extra>")
    st.plotly_chart(fig_reg, use_container_width=True)
