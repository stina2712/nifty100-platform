import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Crypto Portfolio Tracker", page_icon="🪙", layout="wide")
st.title("🪙 Crypto & Digital Asset Portfolio Tracker")

st.markdown("Track major cryptocurrency prices (BTC, ETH, SOL, XRP), analyze 24-hour market shifts, and manage digital asset allocations.")

@st.cache_data
def get_crypto_market_data():
    return pd.DataFrame({
        "Asset Name": ["Bitcoin", "Ethereum", "Solana", "Ripple", "Cardano"],
        "Symbol": ["BTC", "ETH", "SOL", "XRP", "ADA"],
        "Price (USD)": [67450.0, 3520.0, 185.0, 0.58, 0.45],
        "24h Change (%)": [+2.45, -1.10, +5.80, +0.90, -0.75],
        "Market Cap ($B)": [1320.5, 422.1, 85.4, 32.1, 16.2],
        "Holdings (Units)": [0.5, 3.2, 25.0, 1500.0, 2000.0]
    })

crypto_df = get_crypto_market_data()

# Calculate USD and INR values (assuming 1 USD = 83.45 INR)
usd_to_inr = 83.45
crypto_df["Total Value (USD)"] = crypto_df["Price (USD)"] * crypto_df["Holdings (Units)"]
crypto_df["Total Value (₹)"] = crypto_df["Total Value (USD)"] * usd_to_inr

st.markdown("---")
st.subheader("Market Overview & Asset Holdings")
st.dataframe(crypto_df, use_container_width=True)

total_portfolio_usd = crypto_df["Total Value (USD)"].sum()
total_portfolio_inr = crypto_df["Total Value (₹)"].sum()

st.markdown("---")
st.subheader("Portfolio Valuation Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Total Portfolio Value ($)", f"${total_portfolio_usd:,.2f}")
m2.metric("Total Portfolio Value (₹)", f"₹{total_portfolio_inr:,.2f}")
m3.metric("Tracked Assets Count", len(crypto_df))

st.markdown("---")
st.subheader("Asset Allocation Breakdown")
fig = px.pie(
    crypto_df,
    names="Symbol",
    values="Total Value (USD)",
    title="Digital Asset Portfolio Distribution",
    hole=0.4
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Crypto Risk Management Tip:** Digital assets exhibit high volatility compared to traditional equities. Diversifying across layer-1 blockchains and large-cap tokens helps mitigate concentration risk.")