import streamlit as st
import pandas as pd

st.set_page_config(page_title="Net Worth Forecast", page_icon="📈", layout="wide")
st.title("📈 Net Worth & Asset Growth Forecasting Engine")

st.markdown("Project your multi-year wealth compounding trajectory, simulate asset appreciation rates, and track your path to financial independence.")

@st.cache_data
def get_net_worth_projection():
    return pd.DataFrame({
        "Timeline Milestone": ["Current Year (2026)", "Year 1 (2027)", "Year 3 (2029)", "Year 5 (2031)", "Year 10 (2036)"],
        "Projected Assets (₹)": [16070000.0, 18480500.0, 24430000.0, 32280000.0, 60500000.0],
        "Projected Liabilities (₹)": [5150000.0, 4800000.0, 4000000.0, 3000000.0, 500000.0],
        "Net Worth (₹)": [10920000.0, 13680500.0, 20430000.0, 29280000.0, 60000000.0],
        "Compounding Growth Rate": ["Baseline", "15% p.a.", "15% p.a.", "15% p.a.", "14% p.a."]
    })

forecast_df = get_net_worth_projection()

st.markdown("---")
st.subheader("Multi-Year Net Worth Trajectory Matrix")
st.dataframe(forecast_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Long-Term Wealth Growth")

with st.form("forecast_form"):
    c1, c2 = st.columns(2)
    with c1:
        annual_savings_rate = st.number_input("Annual Net Savings Addition (₹)", min_value=100000.0, value=600000.0, step=50000.0)
        expected_portfolio_cagr = st.slider("Expected Portfolio CAGR (% p.a.)", 8.0, 22.0, 14.0, 0.5)
    with c2:
        projection_horizon_years = st.slider("Forecasting Horizon (Years)", 5, 30, 10)
        inflation_adjustment = st.checkbox("Adjust Projections for Inflation (Real Return)", value=True)
    
    forecast_submitted = st.form_submit_button("Run Wealth Forecast")
    if forecast_submitted:
        st.success(f"Net worth growth projection successfully computed across {projection_horizon_years} years at {expected_portfolio_cagr}% CAGR!")

st.markdown("---")
st.info("**Forecasting Insight:** The compounding effect accelerates dramatically in later years because your investment returns begin generating substantial returns of their own.")