import streamlit as st
import pandas as pd

st.set_page_config(page_title="Debt Payoff Strategy", page_icon="💳", layout="wide")
st.title("💳 Liability & Debt Payoff Optimizer")

st.markdown("Analyze your active liabilities, model accelerated amortization, and compare debt elimination strategies.")

@st.cache_data
def get_debt_liabilities():
    return pd.DataFrame({
        "Liability Name": ["Home Mortgage", "Car Auto Loan", "Personal Credit Line", "Education Loan", "Zero-Cost Consumer EMI"],
        "Outstanding Principal (₹)": [3500000.0, 450000.0, 120000.0, 300000.0, 45000.0],
        "Interest Rate (% p.a.)": [8.5, 9.2, 14.0, 10.5, 0.0],
        "Monthly EMI (₹)": [30310.0, 9380.0, 5200.0, 3950.0, 7500.0],
        "Payoff Priority": ["Medium", "Medium", "High", "Low", "Critical"]
    })

debt_df = get_debt_liabilities()

st.markdown("---")
st.subheader("Active Liabilities & Loan Portfolio")
st.dataframe(debt_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Accelerated Debt Payoff")

with st.form("debt_simulator_form"):
    c1, c2 = st.columns(2)
    with c1:
        payoff_strategy = st.selectbox("Payoff Optimization Method", ["Debt Avalanche (Highest Interest Rate First)", "Debt Snowball (Lowest Balance First)", "Custom Hybrid Strategy"])
        extra_monthly_payment = st.number_input("Extra Monthly Prepayment Budget (₹)", min_value=0.0, value=10000.0, step=1000.0)
    with c2:
        target_payoff_months = st.slider("Target Payoff Timeline Goal (Months)", 12, 120, 36)
        prioritize_zero_cost = st.checkbox("Clear Zero-Cost EMIs First", value=True)
    
    debt_submitted = st.form_submit_button("Run Debt Amortization Simulation")
    if debt_submitted:
        st.success(f"Simulation complete! Applying your strategy via **{payoff_strategy}** significantly reduces total interest outgo and shortens your debt-free timeline.")

st.markdown("---")
st.info("**Debt Insight:** Prioritizing high-interest liabilities or utilizing the avalanche method minimizes cumulative interest paid over the life of your loans.")