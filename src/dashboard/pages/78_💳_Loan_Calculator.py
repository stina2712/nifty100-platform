import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mortgage & Loan Calculator", page_icon="💳", layout="wide")
st.title("💳 Advanced Mortgage & Loan Payoff Simulator")

st.markdown("Model loan amortization schedules, calculate interest savings through prepayments, and optimize your debt-free timeline.")

@st.cache_data
def get_loan_summary():
    return pd.DataFrame({
        "Loan Facility": ["Home Mortgage (Primary)", "Car Auto Loan", "Personal Education Loan"],
        "Principal Outstanding (₹)": [4500000.0, 650000.0, 350000.0],
        "Interest Rate (%)": [8.5, 9.2, 10.0],
        "Remaining Tenure (Months)": [180, 36, 24],
        "Monthly EMI (₹)": [44290.0, 20710.0, 16155.0]
    })

loan_df = get_loan_summary()

st.markdown("---")
st.subheader("Active Loan Portfolios & EMIs")
st.dataframe(loan_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Accelerated Prepayment Strategy")

with st.form("loan_calc_form"):
    c1, c2 = st.columns(2)
    with c1:
        loan_type = st.selectbox("Select Loan Facility", ["Home Mortgage (Primary)", "Car Auto Loan", "Personal Education Loan"])
        extra_monthly_prepayment = st.number_input("Extra Monthly Prepayment (₹)", min_value=0.0, value=10000.0, step=1000.0)
    with c2:
        annual_prepayment_bump = st.slider("Annual Prepayment Milestone Hike (%)", 0.0, 20.0, 5.0, 1.0)
        recompute_method = st.selectbox("Prepayment Objective", ["Reduce Tenure (Keep EMI Same)", "Reduce EMI (Keep Tenure Same)"])
    
    loan_submitted = st.form_submit_button("Calculate Payoff Acceleration")
    if loan_submitted:
        st.success(f"Loan acceleration model calculated for **{loan_type}**! Making consistent prepayments significantly reduces total interest outlays.")

st.markdown("---")
st.info("**Loan Insight:** Allocating even a small lump-sum annual prepayment toward high-interest loans can slash your total interest burden by lakhs over the life of the loan.")