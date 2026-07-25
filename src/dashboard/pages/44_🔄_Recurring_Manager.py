import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recurring Transactions", page_icon="🔄", layout="wide")
st.title("🔄 Recurring Bills & Subscription Manager")

st.markdown("Track and manage all your automated monthly payments, software subscriptions, utility bills, and loan EMIs.")

@st.cache_data
def get_recurring_data():
    return pd.DataFrame({
        "Subscription / Bill Name": ["Home Internet Fiber", "Streaming Services (Netflix/Prime)", "Cloud Storage Backup", "Gym Membership", "Home Loan EMI"],
        "Category": ["Utilities", "Entertainment", "Technology", "Health & Fitness", "Debt & EMI"],
        "Monthly Amount (₹)": [999.0, 1150.0, 300.0, 2500.0, 32500.0],
        "Billing Cycle": ["Monthly", "Monthly", "Monthly", "Monthly", "Monthly"],
        "Next Due Date": ["2026-08-01", "2026-08-05", "2026-08-12", "2026-08-15", "2026-08-03"],
        "Status": ["Active", "Active", "Active", "Active", "Auto-Debit On"]
    })

recurring_df = get_recurring_data()

st.markdown("---")
st.subheader("Active Recurring Expenses")
st.dataframe(recurring_df, use_container_width=True)

st.markdown("---")
st.subheader("Add New Recurring Expense / Subscription")

with st.form("recurring_form"):
    c1, c2 = st.columns(2)
    with c1:
        sub_name = st.text_input("Service / Bill Name", placeholder="e.g., Electricity Board Bill")
        category = st.selectbox("Category", ["Utilities", "Entertainment", "Technology", "Insurance", "Debt & EMI"])
    with c2:
        amount = st.number_input("Amount per Cycle (₹)", min_value=1.0, value=500.0, step=50.0)
        due_date = st.date_input("Next Due Date")
    
    submitted = st.form_submit_button("Save Recurring Bill")
    if submitted:
        st.success(f"Successfully added recurring payment for: '{sub_name}'!")

st.markdown("---")
st.info("**Subscription Insight:** Auditing your recurring subscriptions quarterly ensures you eliminate zombie subscriptions or unexpected utility price hikes before they drain your monthly cash flow.")