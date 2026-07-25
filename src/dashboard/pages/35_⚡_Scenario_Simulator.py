import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Scenario Simulator", page_icon="⚡", layout="wide")
st.title("⚡ Financial Scenario & Stress Testing Simulator")

st.markdown("Simulate potential economic downturns and personal financial crises to stress-test your portfolio and emergency reserves.")

# Sidebar controls for simulation
st.sidebar.header("Macro & Personal Stress Parameters")
market_drop = st.sidebar.slider("Equities & Crypto Market Correction (%)", 0, 60, 25)
job_loss_months = st.sidebar.slider("Involuntary Unemployment Duration (Months)", 0, 18, 6)
inflation_surge = st.sidebar.slider("Annual Inflation Spike (%)", 2, 20, 8)

# Base portfolio numbers
base_equities = 3500000.0
base_crypto = 385956.0
base_liquid_cash = 625000.0
monthly_expenses = 65000.0

# Calculated stressed values
stressed_equities = base_equities * (1 - market_drop / 100.0)
stressed_crypto = base_crypto * (1 - (market_drop * 1.2) / 100.0) # Crypto drops harder
emergency_cash_depletion = monthly_expenses * job_loss_months
stressed_liquid_cash = max(0.0, base_liquid_cash - emergency_cash_depletion)

total_base_portfolio = base_equities + base_crypto + base_liquid_cash
total_stressed_portfolio = stressed_equities + stressed_crypto + stressed_liquid_cash
portfolio_loss = total_base_portfolio - total_stressed_portfolio

st.markdown("---")
st.subheader("Stress Test Impact Summary")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Baseline Portfolio Value", f"₹{total_base_portfolio:,.2f}")
m2.metric("Stressed Portfolio Value", f"₹{total_stressed_portfolio:,.2f}")
m3.metric("Simulated Asset Loss", f"₹{portfolio_loss:,.2f}", delta=f"-{(portfolio_loss/total_base_portfolio*100):.1f}%", delta_color="inverse")
m4.metric("Emergency Runway Left", f"{max(0.0, (stressed_liquid_cash / monthly_expenses)):.1f} Months")

st.markdown("---")
st.subheader("Asset Valuation: Before vs. After Stress Test")

comparison_df = pd.DataFrame({
    "Asset Class": ["Equities & Mutual Funds", "Cryptocurrencies", "Liquid Cash Reserve"],
    "Baseline Value (₹)": [base_equities, base_crypto, base_liquid_cash],
    "Stressed Value (₹)": [stressed_equities, stressed_crypto, stressed_liquid_cash]
})

fig = px.bar(
    comparison_df,
    x="Asset Class",
    y=["Baseline Value (₹)", "Stressed Value (₹)"],
    barmode="group",
    title="Portfolio Comparison Under Simulated Economic Stress",
    text_auto=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Stress Test Insight:** Running financial stress tests ensures your liquid emergency buffer is robust enough to sustain you through job interruptions or severe bear markets without forced selling of long-term investments.")