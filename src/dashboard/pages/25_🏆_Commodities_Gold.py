import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Commodities & Gold Tracker", page_icon="🏆", layout="wide")
st.title("🏆 Commodities & Sovereign Gold Benchmark Tracker")

st.markdown("Track precious metal spot prices, analyze gold-to-equity correlations, and evaluate alternative commodity allocations.")

@st.cache_data
def get_commodity_data():
    return pd.DataFrame({
        "Commodity / Asset": ["Gold (24K)", "Silver", "Crude Oil (WTI)", "Copper", "Natural Gas"],
        "Unit": ["10 Grams", "1 Kg", "1 Barrel", "1 Kg", "1 MMBtu"],
        "Current Price (₹)": [72500.0, 88400.0, 6850.0, 845.0, 240.0],
        "24h Change (%)": [+0.65, +1.20, -0.85, +0.40, -1.50],
        "Volatility Profile": ["Low-Medium", "High", "High", "Medium", "High"]
    })

comm_df = get_commodity_data()

st.markdown("---")
st.subheader("Precious Metals & Commodities Overview")
st.dataframe(comm_df, use_container_width=True)

st.markdown("---")
st.subheader("Gold Investment Valuation Calculator")

c1, c2, c3 = st.columns(3)
with c1:
    gold_grams = st.number_input("Gold Holdings (Grams)", value=50.0, step=5.0)
with c2:
    gold_price_per_gram = comm_df.loc[comm_df["Commodity / Asset"] == "Gold (24K)", "Current Price (₹)"].values[0] / 10.0
with c3:
    expected_cagr = st.slider("Expected Annual Gold Growth (%)", min_value=4.0, max_value=15.0, value=8.0)

total_gold_value = gold_grams * gold_price_per_gram

st.markdown("---")
st.subheader("Gold Valuation Summary")

m1, m2 = st.columns(2)
m1.metric("Current Gold Valuation", f"₹{total_gold_value:,.2f}")
m2.metric("Current Gold Price (Per Gram)", f"₹{gold_price_per_gram:,.2f}")

# Generate 5-year growth projection
years = np.arange(1, 6)
projected_gold_values = total_gold_value * ((1.0 + (expected_cagr / 100.0)) ** years)

projection_df = pd.DataFrame({
    "Year": years,
    "Projected Value (₹)": projected_gold_values
})

st.markdown("---")
st.subheader("5-Year Gold Wealth Projection")
fig = px.line(
    projection_df,
    x="Year",
    y="Projected Value (₹)",
    title=f"Gold Portfolio Growth Projection ({expected_cagr}% Annual Return)",
    markers=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Commodity Insight:** Gold acts as a crucial hedge against inflation and equity market downturns. Allocating 5% to 10% of a portfolio to precious metals helps lower overall portfolio volatility.")