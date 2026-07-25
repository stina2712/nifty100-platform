import streamlit as st
import pandas as pd

st.set_page_config(page_title="Expense & Budget Planner", page_icon="💸", layout="wide")
st.title("💸 Monthly Expense & Budget Allocation Planner")

st.markdown("Track and allocate your monthly cash outflows across essential, discretionary, and savings buckets.")

@st.cache_data
def get_budget_data():
    return pd.DataFrame({
        "Expense Category": ["Housing & Rent", "Groceries & Supplies", "Utilities & Bills", "Dining & Entertainment", "Transportation", "Shopping & Discretionary"],
        "Allocated Budget (₹)": [35000.0, 15000.0, 5000.0, 8000.0, 6000.0, 10000.0],
        "Actual Spent (₹)": [35000.0, 14200.0, 4850.0, 9200.0, 5800.0, 8900.0],
        "Variance (₹)": [0.0, +800.0, +150.0, -1200.0, +200.0, +1100.0],
        "Health Status": ["On Track", "Under Budget", "Under Budget", "Over Budget", "Under Budget", "Under Budget"]
    })

budget_df = get_budget_data()

st.markdown("---")
st.subheader("Monthly Category Budget Breakdown")
st.dataframe(budget_df, use_container_width=True)

st.markdown("---")
st.subheader("Log New Expense Transaction")

with st.form("expense_log_form"):
    c1, c2 = st.columns(2)
    with c1:
        expense_title = st.text_input("Expense Description", placeholder="e.g., Weekly Supermarket Grocery Run")
        expense_category = st.selectbox("Category", ["Housing & Rent", "Groceries & Supplies", "Utilities & Bills", "Dining & Entertainment", "Transportation", "Shopping & Discretionary"])
    with c2:
        expense_amt = st.number_input("Amount (₹)", min_value=1.0, value=1200.0, step=100.0)
        expense_date = st.date_input("Transaction Date")
    
    log_submitted = st.form_submit_button("Record Expense")
    if log_submitted:
        st.success(f"Successfully recorded expense: **₹{expense_amt:,.2f}** under **{expense_category}**!")

st.markdown("---")
st.info("**Budget Insight:** Reviewing category-wise variances weekly prevents end-of-month budget overruns and keeps your savings rate firmly on target.")