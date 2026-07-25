import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tax Planning & Estimator", page_icon="📊", layout="wide")
st.title("📊 Income Tax Planning & Deductions Estimator")

st.markdown("Estimate your annual tax obligations, evaluate old vs. new tax regime slabs, and track eligible deduction limits.")

@st.cache_data
def get_tax_deductions_data():
    return pd.DataFrame({
        "Section / Instrument": ["Section 80C (PPF, ELSS, EPF)", "Section 80D (Health Insurance)", "Section 24 (Home Loan Interest)", "Section 80CCD(1B) (NPS)", "Standard Deduction"],
        "Maximum Limit (₹)": [150000.0, 25000.0, 200000.0, 50000.0, 50000.0],
        "Utilized Amount (₹)": [150000.0, 25000.0, 150000.0, 50000.0, 50000.0],
        "Status": ["Fully Utilized", "Fully Utilized", "Partially Utilized", "Fully Utilized", "Claimed"]
    })

tax_df = get_tax_deductions_data()

st.markdown("---")
st.subheader("Tax Deduction Tracker (Old Regime)")
st.dataframe(tax_df, use_container_width=True)

st.markdown("---")
st.subheader("Quick Tax Liability Estimator")

with st.form("tax_estimator_form"):
    c1, c2 = st.columns(2)
    with c1:
        annual_income = st.number_input("Gross Annual Income (₹)", min_value=100000.0, value=1200000.0, step=50000.0)
        regime = st.selectbox("Tax Regime", ["New Tax Regime", "Old Tax Regime"])
    with c2:
        total_deductions = st.number_input("Total Eligible Deductions (₹)", min_value=0.0, value=375000.0, step=10000.0)
        state_cess = st.selectbox("Health & Education Cess", ["4% Standard Applied"])
    
    calc_submitted = st.form_submit_button("Calculate Estimated Tax")
    if calc_submitted:
        taxable_amt = max(0.0, annual_income - (total_deductions if regime == "Old Tax Regime" else 50000.0))
        estimated_tax = taxable_amt * 0.15 # Representative mock effective calculation slab
        st.success(f"Estimated Tax Liability under {regime}: **₹{estimated_tax:,.2f}**")

st.markdown("---")
st.info("**Tax Insight:** Optimizing your tax-saving allocations early in the financial year prevents last-minute panic investments and maximizes compounding returns.")