import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Subscription Tracker", page_icon="🔄", layout="wide")
st.title("🔄 Recurring Subscriptions & Fixed Expenses")

st.markdown("Monitor all your recurring subscriptions, software licenses, streaming services, and fixed monthly digital expenditures.")

@st.cache_data
def get_subscription_data():
    return pd.DataFrame({
        "Service / Vendor": ["Netflix Premium", "Amazon Prime", "Spotify Family", "Cloud Storage (iCloud/Google)", "Gym Membership", "SaaS / GitHub Pro"],
        "Category": ["Entertainment", "Entertainment", "Entertainment", "Utility", "Health & Fitness", "Productivity"],
        "Billing Cycle": ["Monthly", "Annual", "Monthly", "Monthly", "Monthly", "Monthly"],
        "Monthly Cost (₹)": [650.0, 120.0, 299.0, 210.0, 2500.0, 850.0],
        "Auto-Debit": ["Yes", "Yes", "Yes", "Yes", "No", "Yes"]
    })

sub_df = get_subscription_data()

st.markdown("---")
st.subheader("Active Subscriptions & Recurring Services")
st.dataframe(sub_df, use_container_width=True)

total_monthly_subs = sub_df["Monthly Cost (₹)"].sum()
annualized_subs = total_monthly_subs * 12

st.markdown("---")
st.subheader("Subscription Expense Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Total Monthly Subscriptions", f"₹{total_monthly_subs:,.2f}")
m2.metric("Annualized Subscription Outflow", f"₹{annualized_subs:,.2f}")
m3.metric("Active Services Tracked", len(sub_df))

st.markdown("---")
st.subheader("Monthly Cost Distribution by Category")
fig = px.pie(
    sub_df,
    names="Category",
    values="Monthly Cost (₹)",
    title="Subscription Outflow Breakdown",
    hole=0.4
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Subscription Insight:** Auditing your recurring subscriptions every six months helps identify unused streaming apps or software licenses, preventing 'subscription creep' from silently draining your monthly savings.")