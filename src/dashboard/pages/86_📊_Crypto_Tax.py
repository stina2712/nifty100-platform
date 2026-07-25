import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crypto Tax Calculator", page_icon="📊", layout="wide")
st.title("📊 Crypto & Digital Asset Tax Calculator")

st.markdown("Calculate capital gains tax, track token disposals, and evaluate tax obligations across your Web3 transactions.")

@st.cache_data
def get_crypto_tax_ledger():
    return pd.DataFrame({
        "Token / Asset": ["Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "Uniswap (UNI)"],
        "Acquisition Date": ["2024-05-12", "2025-01-10", "2025-06-15", "2024-11-20"],
        "Disposal Date": ["2026-03-10", "2026-05-01", "Active Holding", "2026-02-14"],
        "Capital Gain / Loss (₹)": [450000.0, 120000.0, 0.0, -35000.0],
        "Holding Period": ["Long-Term", "Short-Term", "Long-Term", "Short-Term"]
    })

crypto_tax_df = get_crypto_tax_ledger()

st.markdown("---")
st.subheader("Digital Asset Capital Gains Ledger")
st.dataframe(crypto_tax_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Crypto Tax Liability")

with st.form("crypto_tax_form"):
    c1, c2 = st.columns(2)
    with c1:
        tax_jurisdiction = st.selectbox("Tax Jurisdiction", ["India (30% Flat Crypto Tax + 1% TDS)", "United States (Standard Capital Gains)", "United Kingdom (CGT Rates)"])
        offset_losses = st.checkbox("Offset Short-Term Losses Against Gains", value=False)
    with c2:
        include_mining_staking_income = st.checkbox("Include Staking & Mining Rewards as Income", value=True)
        tds_credit_claimed = st.number_input("TDS Deducted at Source (₹)", min_value=0.0, value=15000.0, step=1000.0)
    
    crypto_tax_submitted = st.form_submit_button("Compute Crypto Tax Liability")
    if crypto_tax_submitted:
        st.success("Crypto tax computation complete! Review your realized capital gains ledger before filing your annual returns.")

st.markdown("---")
st.info("**Crypto Tax Insight:** Keeping a meticulous record of all wallet-to-wallet transfers, decentralized exchange swaps, and fiat off-ramps is vital for accurate tax reporting.")