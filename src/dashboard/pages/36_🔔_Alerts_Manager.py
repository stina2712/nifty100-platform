import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alerts Manager", page_icon="🔔", layout="wide")
st.title("🔔 Financial Alerts & Notification Center")

st.markdown("Configure custom financial triggers, spending guardrails, and automated threshold alerts for your portfolio.")

@st.cache_data
def get_alerts_data():
    return pd.DataFrame({
        "Alert Rule Name": ["Low Liquid Emergency Fund", "Monthly Food Budget Cap", "Crypto Portfolio Exposure Limit", "Term Insurance Renewal Due", "Credit Card Bill Reminder"],
        "Category": ["Liquidity", "Expense Control", "Asset Allocation", "Insurance", "Liability"],
        "Threshold Condition": ["< 3 Months Expenses", "> ₹15,000 / month", "> 10% of Net Worth", "30 Days Before Expiry", "5 Days Before Due Date"],
        "Status": ["Active", "Active", "Triggered", "Active", "Active"],
        "Notification Channel": ["Push & Email", "Push Notification", "Email & SMS", "Email", "SMS"]
    })

alerts_df = get_alerts_data()

st.markdown("---")
st.subheader("Configured Financial Alert Rules")
st.dataframe(alerts_df, use_container_width=True)

st.markdown("---")
st.subheader("Add New Custom Alert Rule")

with st.form("alert_form"):
    c1, c2 = st.columns(2)
    with c1:
        rule_name = st.text_input("Alert Rule Name", placeholder="e.g., High Utility Bill Warning")
        category = st.selectbox("Category", ["Expense Control", "Liquidity", "Investment Risk", "Debt & EMI", "Tax Planning"])
    with c2:
        condition = st.text_input("Threshold Condition", placeholder="e.g., > ₹5,000 in a single day")
        channel = st.selectbox("Notification Channel", ["Push Notification", "Email", "SMS", "All Channels"])
    
    submitted = st.form_submit_button("Save Alert Rule")
    if submitted:
        st.success(f"Successfully created alert rule: '{rule_name}'!")

st.markdown("---")
st.info("**Alerts Insight:** Setting proactive threshold notifications ensures you catch lifestyle inflation and portfolio imbalance early before they impact your long-term wealth goals.")