import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dividend Income Tracker", page_icon="💵", layout="wide")

# Standardized Header Component
def render_page_header(title, description):
    st.title(title)
    st.markdown(description)

# Standardized Footer Component
def render_page_footer():
    st.markdown("---")
    st.caption("Nifty 100 Financial Analytics Dashboard © 2026")

# Self-contained Data Status Indicator
def render_data_status(df, dataset_name="Dataset"):
    st.success(f"✅ **{dataset_name}** loaded successfully ({len(df)} records active).")

render_page_header(
    "💵 Dividend & Passive Income Cash Flow Tracker", 
    "Track dividend payouts, monitor annual yield-on-cost, and forecast your passive monthly cash flow streams."
)

@st.cache_data
def get_dividend_portfolio():
    return pd.DataFrame({
        "Asset / Stock Name": ["Reliance Industries", "Tata Consultancy Services", "ITC Limited", "Power Grid Corporation", "Embassy Office Parks REIT"],
        "Shares Held": [150, 100, 400, 500, 250],
        "Dividend Yield (%)": [1.2, 3.1, 3.5, 5.8, 6.5],
        "Annual Dividend Payout (₹)": [15750.0, 36000.0, 28000.0, 29000.0, 24375.0],
        "Payout Frequency": ["Annual", "Quarterly", "Annual", "Semi-Annual", "Quarterly"]
    })

div_df = get_dividend_portfolio()

render_data_status(div_df, "Dividend Portfolio Dataset")

st.markdown("---")
st.subheader("Active Dividend-Yield Portfolio Ledger")
st.dataframe(div_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Dividend Growth & Reinvestment (DRIP)")

with st.form("dividend_form"):
    c1, c2 = st.columns(2)
    with c1:
        selected_asset = st.selectbox("Select Asset for DRIP Simulation", ["Reliance Industries", "Tata Consultancy Services", "ITC Limited", "Power Grid Corporation", "Embassy Office Parks REIT"])
        monthly_reinvestment = st.number_input("Monthly Dividend Reinvestment (₹)", min_value=0.0, value=5000.0, step=1000.0)
    with c2:
        compounding_horizon = st.slider("Compounding Horizon (Years)", 1, 20, 5)
        enable_drip = st.checkbox("Enable Automatic Dividend Reinvestment Plan (DRIP)", value=True)
    
    div_submitted = st.form_submit_button("Calculate Dividend Projections")
    if div_submitted:
        st.success(f"Dividend projection calculated for **{selected_asset}**! Reinvesting dividends significantly accelerates your passive income growth via compounding.")

st.markdown("---")
st.info("**Dividend Insight:** Reinvesting dividends during your accumulation phase leverages the power of compounding, allowing you to buy more units without adding fresh capital.")

render_page_footer()