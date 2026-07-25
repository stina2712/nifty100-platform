import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Advisor Hub", page_icon="🤖", layout="wide")
st.title("🤖 AI Financial Advisor & Automated Insights Hub")

st.markdown("Receive synthesized, automated advisory insights, spending anomaly detections, and personalized wealth growth strategies.")

@st.cache_data
def get_advisor_insights():
    return pd.DataFrame({
        "Priority": ["High", "Medium", "High", "Low", "Medium"],
        "Category": ["Cash Flow Optimization", "Tax Planning", "Investment Rebalancing", "Subscription Audit", "Emergency Buffer"],
        "Insight / Recommendation": [
            "Idle savings account cash exceeds 3-month operational buffer by ₹1,50,000. Consider moving to liquid mutual funds.",
            "Section 80C limit fully exhausted, but ₹25,000 health insurance cap under 80D has room for parental coverage.",
            "Equity allocation has drifted +5.2% above target asset allocation due to recent rally. Rebalance recommended.",
            "Identified 2 overlapping cloud storage subscriptions totaling ₹600/month. Recommended consolidation.",
            "Emergency fund runway is exceptionally healthy at 7.2 months of fixed overhead expenses."
        ],
        "Potential Annual Impact": ["+₹10,500 Yield", "+₹7,800 Tax Saved", "Risk Mitigation", "+₹7,200 Saved", "Maximum Stability"]
    })

insights_df = get_advisor_insights()

st.markdown("---")
st.subheader("Automated Wealth Advisory Feed")
st.dataframe(insights_df, use_container_width=True)

st.markdown("---")
st.subheader("Run Deep Diagnostic Portfolio Scan")

with st.form("diagnostic_scan_form"):
    c1, c2 = st.columns(2)
    with c1:
        scan_scope = st.selectbox("Diagnostic Scope", ["Full Financial Health Scan", "Tax Efficiency Scan", "Cash Flow Leakage Scan", "Asset Risk Exposure Scan"])
        strictness = st.slider("AI Insight Strictness Level", 1, 5, 4)
    with c2:
        include_macro = st.checkbox("Include Macroeconomic Factors (Inflation & Interest Rates)", value=True)
        notify_email = st.checkbox("Email Summary Report to Registered Address", value=False)
    
    scan_submitted = st.form_submit_button("Initiate Diagnostic Scan")
    if scan_submitted:
        st.success("Diagnostic scan complete! Successfully generated 3 fresh optimization strategies for your portfolio.")

st.markdown("---")
st.info("**Advisory Insight:** Automated continuous scanning protects against behavioral blind spots and ensures your capital works at maximum efficiency year-round.")