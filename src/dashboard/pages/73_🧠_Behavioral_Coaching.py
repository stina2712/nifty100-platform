import streamlit as st
import pandas as pd

st.set_page_config(page_title="Behavioral Coaching", page_icon="🧠", layout="wide")
st.title("🧠 Financial Habit & Behavioral Coaching Hub")

st.markdown("Identify cognitive biases, overcome emotional spending triggers, and reinforce disciplined wealth-building habits.")

@st.cache_data
def get_behavioral_metrics():
    return pd.DataFrame({
        "Behavioral Trait / Bias": ["Loss Aversion Tendency", "FOMO Investing (Fear of Missing Out)", "Impulse Retail Spending", "Confirmation Bias in Stocks", "Mental Accounting Trap"],
        "Risk Severity": ["Moderate", "Low", "High", "Moderate", "High"],
        "Corrective Rule Implemented": ["Automated Rebalancing", "Mandatory 48-Hour Cooling Rule", "Strict Discretionary Budgeting", "Third-Party Portfolio Review", "Unified Net Worth View"],
        "Habit Health Score": ["8 / 10", "9 / 10", "6 / 10", "8 / 10", "7 / 10"]
    })

behavior_df = get_behavioral_metrics()

st.markdown("---")
st.subheader("Behavioral Bias & Habit Audit")
st.dataframe(behavior_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Behavioral Rule Enforcement")

with st.form("behavior_sim_form"):
    c1, c2 = st.columns(2)
    with c1:
        cooling_period = st.slider("Impulse Purchase Cooling Period (Hours)", 0, 72, 24, 6)
        automation_level = st.selectbox("Investment Automation Level", ["100% Automated (Zero Manual Intervention)", "Semi-Automated (Manual Approval)", "Manual Execution"])
    with c2:
        emotional_discipline_rating = st.slider("Self-Rated Market Discipline (1-10)", 1, 10, 8)
        spending_trigger_focus = st.selectbox("Primary Financial Stress Trigger", ["Market Volatility Panic", "Social Media Peer Comparison", "Impulse Lifestyle Creep", "None"])
    
    behavior_submitted = st.form_submit_button("Apply Behavioral Guardrails")
    if behavior_submitted:
        st.success("Behavioral coaching parameters updated! Automated guardrails successfully protect your long-term strategy from emotional interference.")

st.markdown("---")
st.info("**Behavioral Insight:** The biggest threat to long-term wealth accumulation isn't market volatility—it's behavioral reactions like panic selling during downturns or impulse buying during bull runs.")