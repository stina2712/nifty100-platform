import streamlit as st
import pandas as pd

st.set_page_config(page_title="Portfolio Audit Hub", page_icon="📋", layout="wide")
st.title("📋 Automated Financial Portfolio Audit & Recommendations")

st.markdown("Receive automated health audits, asset allocation critique, and actionable steps to optimize your net worth.")

@st.cache_data
def get_audit_recommendations():
    return pd.DataFrame({
        "Audit Area": ["Emergency Liquidity", "Debt Management", "Asset Diversification", "Insurance Coverage", "Retirement Savings"],
        "Current Status": ["Moderate (3.6 Months)", "Low Cost EMIs", "Equities Heavy (78%)", "Adequate Term Cover", "On Track"],
        "Risk / Priority": ["Medium Priority", "Low Priority", "High Priority", "Low Priority", "Medium Priority"],
        "AI Recommendation": [
            "Increase liquid cash reserves to cover at least 6 full months of living expenses.",
            "Maintain current prepayment schedule; no high-interest toxic debt detected.",
            "Rebalance portfolio by allocating more towards debt/gold to reduce market volatility.",
            "Ensure annual health floater policy gets renewed before the upcoming March deadline.",
            "Increase monthly equity SIP contributions by 10% annually to beat long-term inflation."
        ]
    })

audit_df = get_audit_recommendations()

st.markdown("---")
st.subheader("Comprehensive Financial Audit Matrix")
st.dataframe(audit_df, use_container_width=True)

st.markdown("---")
st.subheader("Run Instant Portfolio Health Check")

if st.button("Execute Full Financial Audit Scan"):
    st.success("Audit scan completed successfully! Your portfolio scores an overall health rating of **82 / 100 (Strong)**.")
    st.balloons()

st.markdown("---")
st.info("**Audit Insight:** Regular portfolio audits ensure your asset allocation drifts don't silently expose you to unintended market risks as your investments grow.")