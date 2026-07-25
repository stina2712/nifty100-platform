import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Emergency Fund Analyzer", page_icon="🚨", layout="wide")
st.title("🚨 Emergency Fund & Liquidity Health Analyzer")

st.markdown("Track your liquid cash reserves, calculate emergency runway months, and ensure resilience against financial shocks.")

@st.cache_data
def get_liquid_assets():
    return pd.DataFrame({
        "Asset / Account": ["Savings Account A", "High-Yield Sweep Account", "Liquid Mutual Funds", "Digital Wallet / Cash"],
        "Institution": ["HDFC Bank", "ICICI Bank", "Zerodha Coin", "UPI / Cash"],
        "Current Balance (₹)": [150000.0, 250000.0, 200000.0, 25000.0],
        "Liquidity Speed": ["Instant", "Same-Day", "T+1 Working Day", "Instant"]
    })

liquid_df = get_liquid_assets()

st.markdown("---")
st.subheader("Liquid Asset Reserves")
st.dataframe(liquid_df, use_container_width=True)

total_liquid_cash = liquid_df["Current Balance (₹)"].sum()

st.markdown("---")
st.subheader("Emergency Runway Calculator")

c1, c2 = st.columns(2)
with c1:
    monthly_essential_expense = st.number_input("Monthly Essential Expenses (₹)", value=50000.0, step=5000.0)
with c2:
    target_runway_months = st.slider("Target Safety Runway (Months)", min_value=3, max_value=12, value=6)

# Calculations
runway_months = total_liquid_cash / monthly_essential_expense if monthly_essential_expense > 0 else 0.0
target_emergency_corpus = monthly_essential_expense * target_runway_months
emergency_gap = max(0.0, target_emergency_corpus - total_liquid_cash)

st.markdown("---")
st.subheader("Liquidity Health Summary")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Liquid Reserves", f"₹{total_liquid_cash:,.2f}")
m2.metric("Current Runway", f"{runway_months:.1f} Months")
m3.metric("Target Emergency Corpus", f"₹{target_emergency_corpus:,.2f}")
m4.metric("Emergency Fund Gap", f"₹{emergency_gap:,.2f}")

st.markdown("---")
st.subheader("Liquid Reserves Distribution")
fig = px.pie(
    liquid_df,
    names="Asset / Account",
    values="Current Balance (₹)",
    title="Breakdown of Liquid Cash & Equivalents",
    hole=0.4
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Emergency Fund Insight:** Financial planners universally recommend maintaining 6 months of essential living expenses in highly liquid instruments (like sweep-in accounts or liquid funds) to safeguard against unexpected job loss or medical emergencies.")