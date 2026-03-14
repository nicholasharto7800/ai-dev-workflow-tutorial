import pandas as pd
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
