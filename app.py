import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales & Revenue Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales & Revenue Analysis Dashboard")
st.caption("Interactive analysis of a sample retail dataset. All figures are illustrative.")

@st.cache_data
def load_data():
    df = pd.read_csv("data/sales_data.csv", parse_dates=["Order_Date"])
    df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
    return df

df = load_data()

with st.sidebar:
    st.header("Dashboard filters")
    date_min, date_max = df["Order_Date"].min().date(), df["Order_Date"].max().date()
    date_range = st.date_input("Order date range", value=(date_min, date_max),
                               min_value=date_min, max_value=date_max)
    regions = st.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
    products = st.multiselect("Product", sorted(df["Product"].unique()), default=sorted(df["Product"].unique()))
    channels = st.multiselect("Sales channel", sorted(df["Sales_Channel"].unique()), default=sorted(df["Sales_Channel"].unique()))

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered = df[
        df["Order_Date"].dt.date.between(start_date, end_date)
        & df["Region"].isin(regions)
        & df["Product"].isin(products)
        & df["Sales_Channel"].isin(channels)
    ]
else:
    filtered = df.iloc[0:0]

if filtered.empty:
    st.warning("No records match these filters. Adjust the selections.")
    st.stop()

revenue = filtered["Revenue"].sum()
profit = filtered["Profit"].sum()
orders = filtered["Order_ID"].nunique()
units = filtered["Quantity"].sum()
margin = profit / revenue * 100 if revenue else 0

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Total revenue", f"₹{revenue:,.0f}")
k2.metric("Total profit", f"₹{profit:,.0f}")
k3.metric("Orders", f"{orders:,}")
k4.metric("Units sold", f"{units:,}")
k5.metric("Profit margin", f"{margin:.1f}%")

st.divider()
left, right = st.columns(2)
with left:
    monthly = filtered.groupby("Month", as_index=False)[["Revenue", "Profit"]].sum()
    fig = px.line(monthly, x="Month", y=["Revenue", "Profit"], markers=True,
                  title="Revenue and profit over time", labels={"value":"Amount (₹)", "Month":"Month"})
    st.plotly_chart(fig, use_container_width=True)
with right:
    by_region = filtered.groupby("Region", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
    fig = px.bar(by_region, x="Region", y="Revenue", title="Revenue by region",
                 labels={"Revenue":"Revenue (₹)"}, text_auto=".2s")
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    by_product = filtered.groupby("Product", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
    fig = px.bar(by_product, x="Product", y="Revenue", title="Revenue by product",
                 labels={"Revenue":"Revenue (₹)"}, text_auto=".2s")
    st.plotly_chart(fig, use_container_width=True)
with right:
    by_channel = filtered.groupby("Sales_Channel", as_index=False)["Revenue"].sum()
    fig = px.pie(by_channel, names="Sales_Channel", values="Revenue", hole=.45,
                 title="Revenue share by sales channel")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Order-level data")
st.dataframe(filtered.sort_values("Order_Date", ascending=False), use_container_width=True, hide_index=True)
st.download_button("Download filtered data (CSV)", filtered.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_sales_data.csv", mime="text/csv")
