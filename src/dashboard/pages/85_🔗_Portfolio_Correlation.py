import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portfolio Correlation & Diversification", page_icon="🔗", layout="wide")
st.title("🔗 Portfolio Asset Correlation & Diversification Matrix")

st.markdown("Analyze cross-asset correlations, detect portfolio concentration risks, and ensure robust diversification across uncorrelated asset classes.")

@st.cache_data
def get_correlation_matrix():
    return pd.DataFrame({
        "Asset Class": ["Large Cap Equities", "Debt & Bonds", "Gold Bullion", "Real Estate", "Crypto Assets"],
        "Large Cap Equities": [1.00, -0.15, 0.08, 0.45, 0.62],
        "Debt & Bonds": [-0.15, 1.00, 0.12, -0.05, -0.10],
        "Gold Bullion": [0.08, 0.12, 1.00, 0.20, 0.15],
        "Real Estate": [0.45, -0.05, 0.20, 1.00, 0.30],
        "Crypto Assets": [0.62, -0.10, 0.15, 0.30, 1.00]
    })

corr_df = get_correlation_matrix()

st.markdown("---")
st.subheader("Cross-Asset Correlation Matrix")
st.dataframe(corr_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Diversification Adjustments")

with st.form("correlation_form"):
    c1, c2 = st.columns(2)
    with c1:
        primary_asset = st.selectbox("Primary Focus Asset", ["Large Cap Equities", "Debt & Bonds", "Gold Bullion", "Real Estate", "Crypto Assets"])
        rebalance_strategy = st.selectbox("Diversification Objective", ["Minimize Equity Correlation", "Maximize Safe Haven Hedge", "Balanced Multi-Asset Mix"])
    with c2:
        target_uncorrelated_weight = st.slider("Target Uncorrelated Allocation Weight (%)", 5, 50, 20, 5)
        enforce_strict_limits = st.checkbox("Enforce Strict Asset Class Caps", value=True)
    
    corr_submitted = st.form_submit_button("Run Diversification Audit")
    if corr_submitted:
        st.success(f"Diversification analysis complete for **{primary_asset}**! Maintaining low or negative correlation assets protects your portfolio during market shocks.")

st.markdown("---")
st.info("**Correlation Insight:** True diversification isn't just holding multiple funds—it's holding assets that respond differently to the same economic conditions.")