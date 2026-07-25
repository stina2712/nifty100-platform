import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Milestone Tracker", page_icon="🎯", layout="wide")
st.title("🎯 Financial Milestone & Life Goals Tracker")

st.markdown("Set, track, and monitor your long-term financial milestones and life goals alongside accumulated progress.")

@st.cache_data
def get_milestone_data():
    return pd.DataFrame({
        "Milestone Goal": ["Child Higher Education", "Down Payment for Vacation Home", "Early Retirement Corpus", "World Tour Vacation", "Startup Seed Capital"],
        "Category": ["Family & Education", "Real Estate", "Retirement", "Lifestyle", "Business"],
        "Target Amount (₹)": [3500000.0, 2000000.0, 15000000.0, 600000.0, 2500000.0],
        "Current Saved (₹)": [1200000.0, 1400000.0, 6500000.0, 400000.0, 1000000.0],
        "Target Year": [2032, 2028, 2045, 2027, 2030],
        "Priority": ["High", "Medium", "High", "Low", "Medium"]
    })

milestone_df = get_milestone_data()
milestone_df["Progress (%)"] = (milestone_df["Current Saved (₹)"] / milestone_df["Target Amount (₹)"] * 100).round(1)

st.markdown("---")
st.subheader("Active Financial Milestones")
st.dataframe(milestone_df, use_container_width=True)

total_target = milestone_df["Target Amount (₹)"].sum()
total_saved = milestone_df["Current Saved (₹)"].sum()
overall_progress = (total_saved / total_target * 100) if total_target > 0 else 0.0

st.markdown("---")
st.subheader("Milestone Portfolio Summary")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Goals Target", f"₹{total_target:,.2f}")
m2.metric("Total Accumulated Savings", f"₹{total_saved:,.2f}")
m3.metric("Overall Progress", f"{overall_progress:.1f}%")
m4.metric("Active Milestones", len(milestone_df))

st.markdown("---")
st.subheader("Progress Across Life Goals")
fig = px.bar(
    milestone_df,
    x="Milestone Goal",
    y=["Current Saved (₹)", "Target Amount (₹)"],
    barmode="group",
    title="Accumulated Savings vs Target Amount per Goal",
    text_auto=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Milestone Insight:** Linking specific mutual fund SIPs to individual life milestones ensures dedicated compounding and prevents dipping into long-term wealth pools for short-term expenses.")