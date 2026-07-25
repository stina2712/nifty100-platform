import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Debt Manager", page_icon="💳", layout="wide")
st.title("💳 Debt & Liabilities Management Hub")

st.markdown("Track outstanding loans, credit card obligations, and analyze your debt-to-income (DTI) ratio.")

@st.cache_data
def get_debt_data():
    return pd.DataFrame({
        "Liability Name": ["Home Loan", "Car Loan", "Credit Card A", "Personal Loan"],
        "Category": ["Secured", "Secured", "Unsecured", "Unsecured"],
        "Outstanding Amount (₹)": [4500000.0, 650000.0, 85000.0, 250000.0],
        "Interest Rate (%)": [8.5, 9.2, 42.0, 11.5],
        "Monthly EMI (₹)": [38900.0, 13500.0, 8500.0, 5500.0]
    })

debt_df = get_debt_data()

st.markdown("---")
st.subheader("Active Liabilities Overview")
st.dataframe(debt_df, use_container_width=True)

# Summary metrics
total_debt = debt_df["Outstanding Amount (₹)"].sum()
total_monthly_emi = debt_df["Monthly EMI (₹)"].sum()

st.markdown("---")
st.subheader("Debt Summary & Obligations")

m1, m2, m3 = st.columns(3)
m1.metric("Total Outstanding Debt", f"₹{total_debt:,.2f}")
m2.metric("Total Monthly EMI Outflow", f"₹{total_monthly_emi:,.2f}")
m3.metric("Active Liabilities Count", len(debt_df))

st.markdown("---")
st.subheader("Debt Distribution by Category")
fig = px.pie(
    debt_df,
    names="Liability Name",
    values="Outstanding Amount (₹)",
    title="Outstanding Debt Breakdown",
    hole=0.4
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Debt Management Tip:** Prioritize paying off high-interest unsecured debt (like credit cards carrying 40%+ interest) first using the debt avalanche method to minimize total interest outflow.")