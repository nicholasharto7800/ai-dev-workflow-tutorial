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
