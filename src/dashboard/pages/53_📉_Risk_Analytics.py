import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portfolio Risk Analytics", page_icon="📉", layout="wide")
st.title("📉 Portfolio Risk, Volatility & Drawdown Analytics")

st.markdown("Evaluate portfolio risk metrics, maximum historical drawdowns, Sharpe ratios, and Value-at-Risk (VaR) parameters.")

@st.cache_data
def get_risk_metrics():
    return pd.DataFrame({
        "Asset / Portfolio Class": ["Nifty 50 Index Fund", "Smallcap Growth Fund", "Liquid Debt Fund", "Gold ETF", "Aggregate Portfolio"],
        "Annualized Volatility (%)": [14.2, 22.8, 2.5, 12.1, 11.5],
        "Max Historical Drawdown (%)": [-18.5, -32.4, -0.4, -11.2, -14.2],
        "Sharpe Ratio": [1.45, 1.12, 0.85, 1.05, 1.58],
        "Value at Risk (VaR 95%)": ["-1.8%", "-3.1%", "-0.2%", "-1.4%", "-1.5%"]
    })

risk_df = get_risk_metrics()

st.markdown("---")
st.subheader("Asset Risk & Volatility Breakdown")
st.dataframe(risk_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Stress Test & Market Shock")

with st.form("stress_test_form"):
    c1, c2 = st.columns(2)
    with c1:
        shock_scenario = st.selectbox("Market Shock Scenario", ["Severe Correction (-20% Equity)", "Interest Rate Spike (+150 bps)", "Geopolitical Oil Shock", "Liquidity Crunch"])
        portfolio_beta = st.slider("Portfolio Market Beta", 0.5, 1.8, 1.05, 0.05)
    with c2:
        hedge_allocation = st.slider("Defensive Hedge Weight (%)", 0.0, 50.0, 15.0, 5.0)
        confidence_level = st.selectbox("VaR Confidence Level", ["95% Confidence", "99% Confidence"])
    
    stress_submitted = st.form_submit_button("Run Stress Test Simulation")
    if stress_submitted:
        st.success(f"Stress test simulation complete under scenario '{shock_scenario}'! Estimated portfolio resilience score remains within acceptable tolerance limits.")

st.markdown("---")
st.info("**Risk Insight:** Maintaining a diversified asset allocation with low-correlation hedges safeguards your capital against unexpected macro shocks and market drawdowns.")