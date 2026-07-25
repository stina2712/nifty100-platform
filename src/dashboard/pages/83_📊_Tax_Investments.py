import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tax-Advantaged Investments", page_icon="📊", layout="wide")
st.title("📊 Tax-Advantaged Investment & Deduction Tracker")

st.markdown("Monitor your Section 80C, 80D, and NPS contributions to optimize tax savings and reduce your annual tax liability.")

@st.cache_data
def get_tax_investments():
    return pd.DataFrame({
        "Tax Saving Instrument": ["ELSS Equity Mutual Funds", "Public Provident Fund (PPF)", "National Pension System (NPS)", "Health Insurance Premium (80D)", "Term Life Insurance Premium"],
        "Section": ["Section 80C", "Section 80C", "Section 80CCD(1B)", "Section 80D", "Section 80C"],
        "Annual Limit (₹)": [150000.0, 150000.0, 50000.0, 25000.0, 150000.0],
        "Amount Invested (₹)": [150000.0, 100000.0, 50000.0, 24000.0, 18500.0],
        "Status": ["Maximized", "Active", "Maximized", "Active", "Active"]
    })

tax_inv_df = get_tax_investments()

st.markdown("---")
st.subheader("Tax-Saving Deductions Ledger")
st.dataframe(tax_inv_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Additional Tax Deductions")

with st.form("tax_invest_form"):
    c1, c2 = st.columns(2)
    with c1:
        instrument_choice = st.selectbox("Select Investment Category", ["ELSS Mutual Funds", "Public Provident Fund (PPF)", "NPS Tier-1 Voluntary", "Medical Insurance"])
        additional_investment = st.number_input("Additional Investment Amount (₹)", min_value=0.0, value=25000.0, step=5000.0)
    with c2:
        tax_slab = st.selectbox("Applicable Income Tax Slab", ["30% Slab + Surcharge", "20% Slab", "15% Slab", "10% Slab"])
        lockup_awareness = st.checkbox("Acknowledge Lock-in Period & Terms", value=True)
    
    tax_inv_submitted = st.form_submit_button("Calculate Tax Savings")
    if tax_inv_submitted:
        st.success(f"Tax saving calculation completed for **{instrument_choice}**! Maximizing eligible deductions significantly lowers your net taxable income.")

st.markdown("---")
st.info("**Tax Insight:** ELSS funds offer the shortest lock-in period (3 years) among all Section 80C investment options while providing exposure to high-growth equity markets.")