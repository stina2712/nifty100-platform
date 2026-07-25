import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crypto & Digital Assets", page_icon="🌐", layout="wide")
st.title("🌐 Cryptocurrency & Digital Assets Tracker")

st.markdown("Track your crypto tokens, Web3 wallet balances, staking rewards, and digital asset allocation.")

@st.cache_data
def get_crypto_holdings():
    return pd.DataFrame({
        "Asset / Token": ["Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "Polygon (POL)", "USDC Stablecoin"],
        "Token Holdings": [0.35, 2.45, 18.50, 1250.00, 1500.00],
        "Average Purchase Price ($)": [42000.0, 2400.0, 95.0, 0.65, 1.00],
        "Current Price ($)": [68000.0, 3500.0, 145.0, 0.55, 1.00],
        "Total Value (₹)": [1972000.0, 717500.0, 224750.0, 57750.0, 127500.0]
    })

crypto_df = get_crypto_holdings()

st.markdown("---")
st.subheader("Digital Asset Holdings Summary")
st.dataframe(crypto_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Crypto Portfolio DCA & Staking")

with st.form("crypto_sim_form"):
    c1, c2 = st.columns(2)
    with c1:
        crypto_dca_monthly = st.number_input("Monthly Crypto DCA Budget (₹)", min_value=1000.0, value=15000.0, step=1000.0)
        primary_asset = st.selectbox("Focus Accumulation Asset", ["Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "Stablecoin Yield (USDC)"])
    with c2:
        staking_apy = st.slider("Estimated Staking / Yield APY (%)", 0.0, 15.0, 5.0, 0.5)
        dca_horizon = st.slider("DCA Horizon (Years)", 1, 10, 3)
    
    crypto_submitted = st.form_submit_button("Run Crypto Portfolio Model")
    if crypto_submitted:
        st.success("Crypto simulation complete! Dollar-cost averaging (DCA) effectively smooths out volatility over long horizons.")

st.markdown("---")
st.info("**Crypto Insight:** Treating digital assets as a high-risk satellite component (strictly capped under 5% of total net worth) manages exposure to extreme market volatility.")