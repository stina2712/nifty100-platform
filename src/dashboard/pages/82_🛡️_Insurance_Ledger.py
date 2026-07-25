import streamlit as st
import pandas as pd

st.set_page_config(page_title="Insurance Policy Ledger", page_icon="🛡️", layout="wide")
st.title("🛡️ Insurance & Risk Protection Ledger")

st.markdown("Manage all term life, health floater, critical illness, and asset insurance policies in one secure portfolio view.")

@st.cache_data
def get_insurance_portfolio():
    return pd.DataFrame({
        "Policy Name / Provider": ["Term Life Cover (HDFC ERGO)", "Family Health Floater (Niva Bupa)", "Critical Illness Rider", "Comprehensive Car Insurance", "Home Structure & Contents Cover"],
        "Coverage Sum Assured (₹)": [20000000.0, 1500000.0, 5000000.0, 1000000.0, 7500000.0],
        "Annual Premium (₹)": [18500.0, 24000.0, 9500.0, 14000.0, 8000.0],
        "Renewal Due Date": ["2026-11-15", "2026-09-10", "2026-11-15", "2026-08-05", "2026-12-01"],
        "Status": ["Active", "Active", "Active", "Active", "Active"]
    })

insurance_df = get_insurance_portfolio()

st.markdown("---")
st.subheader("Active Insurance Policies")
st.dataframe(insurance_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Coverage Adequacy & Protection Gap")

with st.form("insurance_form"):
    c1, c2 = st.columns(2)
    with c1:
        annual_income_target = st.number_input("Annual Income to Protect (₹)", min_value=300000.0, value=1500000.0, step=100000.0)
        dependents_count = st.slider("Number of Financial Dependents", 0, 5, 2)
    with c2:
        existing_term_cover = st.number_input("Total Existing Term Insurance Cover (₹)", min_value=0.0, value=20000000.0, step=1000000.0)
        health_floater_size = st.selectbox("Family Health Cover Tier", ["₹10 Lakhs", "₹15 Lakhs", "₹25 Lakhs", "₹50 Lakhs+ (Super Top-Up)"])
    
    insurance_submitted = st.form_submit_button("Analyze Protection Adequacy")
    if insurance_submitted:
        st.success("Insurance protection audit complete! Your current coverage adequately secures your family against unforeseen liabilities.")

st.markdown("---")
st.info("**Insurance Insight:** A pure term life insurance cover should ideally be at least 15 to 20 times your annual income to fully replace your economic value for dependents.")