import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alternative Investments", page_icon="🚀", layout="wide")
st.title("🚀 Alternative Investments & Startup Equity Hub")

st.markdown("Track your private company shareholdings, startup angel investments, venture debt, and alternative asset portfolios.")

@st.cache_data
def get_alternative_holdings():
    return pd.DataFrame({
        "Investment Asset / Venture": ["Fintech SaaS Seed Round", "D2C Consumer Brand Equity", "DeepTech AI Research Syndicate", "Venture Debt Fund Tranche", "Collectibles & Art Index"],
        "Asset Class": ["Startup Equity", "Startup Equity", "Startup Equity", "Private Debt", "Alternative Tangible"],
        "Invested Capital (₹)": [500000.0, 300000.0, 250000.0, 1000000.0, 200000.0],
        "Current Valuation (₹)": [850000.0, 420000.0, 300000.0, 1150000.0, 240000.0],
        "Multiple on Invested Capital (MOIC)": ["1.70x", "1.40x", "1.20x", "1.15x", "1.20x"]
    })

alt_df = get_alternative_holdings()

st.markdown("---")
st.subheader("Alternative Assets & Venture Portfolio")
st.dataframe(alt_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Alternative Asset Allocation")

with st.form("alt_sim_form"):
    c1, c2 = st.columns(2)
    with c1:
        alt_budget = st.number_input("Annual Allocation Budget for Alternatives (₹)", min_value=50000.0, value=250000.0, step=25000.0)
        target_alt_pct = st.slider("Target Portfolio Weight for Alternatives (%)", 1.0, 15.0, 5.0, 0.5)
    with c2:
        risk_appetite = st.selectbox("Venture Risk Profile", ["Early-Stage High Risk / High Growth", "Late-Stage Growth Equity", "Venture Debt & Income-Generating Alternatives"])
        liquidity_horizon = st.slider("Expected Lock-in Horizon (Years)", 3, 10, 5)
    
    alt_submitted = st.form_submit_button("Run Alternative Portfolio Model")
    if alt_submitted:
        st.success("Alternative investment simulation complete! Venture allocation profile aligns with your high-growth satellite strategy.")

st.markdown("---")
st.info("**Alternative Insight:** Alternative assets offer high asymmetry and low correlation to public equity markets, but require strict limitation (typically under 10% of net worth) due to illiquidity and venture risk.")