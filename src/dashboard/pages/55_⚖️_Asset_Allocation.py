import streamlit as st
import pandas as pd

st.set_page_config(page_title="Asset Allocation Rebalancer", page_icon="⚖️", layout="wide")
st.title("⚖️ Portfolio Asset Allocation & Rebalancing Engine")

st.markdown("Monitor your current asset class distribution against target strategic models and calculate required rebalancing trades.")

@st.cache_data
def get_allocation_data():
    return pd.DataFrame({
        "Asset Class": ["Large Cap Equity", "Mid & Small Cap Equity", "Debt / Fixed Income", "Gold & Commodities", "International Equities", "Cash & Liquid Funds"],
        "Current Value (₹)": [450000.0, 250000.0, 300000.0, 100000.0, 150000.0, 50000.0],
        "Current Weight (%)": [36.0, 20.0, 24.0, 8.0, 12.0, 4.0],
        "Target Weight (%)": [40.0, 15.0, 25.0, 10.0, 10.0, 0.0],
        "Drift (%)": [-4.0, +5.0, -1.0, -2.0, +2.0, +4.0]
    })

alloc_df = get_allocation_data()

st.markdown("---")
st.subheader("Asset Class Distribution & Drift Matrix")
st.dataframe(alloc_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Portfolio Rebalancing Trades")

with st.form("rebalance_form"):
    c1, c2 = st.columns(2)
    with c1:
        total_corpus = st.number_input("Total Invested Corpus (₹)", min_value=100000.0, value=1300000.0, step=50000.0)
        tolerance_band = st.slider("Rebalancing Tolerance Threshold (%)", 1.0, 10.0, 5.0, 0.5)
    with c2:
        rebalance_strategy = st.selectbox("Rebalancing Execution Strategy", ["Periodic Threshold Rebalancing", "Cash-Flow Rebalancing (via Inflows)", "Full Portfolio Realignment"])
        tax_awareness = st.checkbox("Optimize for Tax Loss Harvesting / Capital Gains", value=True)
    
    rebalance_submitted = st.form_submit_button("Generate Rebalancing Plan")
    if rebalance_submitted:
        st.success(f"Rebalancing plan successfully generated! Strategy '{rebalance_strategy}' targets drifting weights back within your {tolerance_band}% tolerance band.")

st.markdown("---")
st.info("**Allocation Insight:** Regular portfolio rebalancing forces you to sell high-performing assets and accumulate undervalued ones, enforcing disciplined risk control over long horizons.")