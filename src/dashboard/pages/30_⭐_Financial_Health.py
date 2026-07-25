import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Financial Health Scorecard", page_icon="⭐", layout="wide")
st.title("⭐ Financial Health & Wellness Scorecard")

st.markdown("Evaluate your holistic financial fitness across key pillars: Savings, Emergency Preparedness, Debt Management, and Risk Coverage.")

@st.cache_data
def get_health_score_data():
    return pd.DataFrame({
        "Financial Pillar": [
            "Emergency Fund Reserve", 
            "Savings & Investment Rate", 
            "Debt-to-Income (DTI) Ratio", 
            "Insurance & Risk Coverage", 
            "Retirement Readiness"
        ],
        "Score Assigned (/100)": [90.0, 75.0, 85.0, 70.0, 65.0],
        "Weight (%)": [25, 25, 20, 15, 15],
        "Status": ["Strong", "Good", "Strong", "Moderate", "Moderate"]
    })

score_df = get_health_score_data()

st.markdown("---")
st.subheader("Pillar-wise Financial Health Breakdown")
st.dataframe(score_df, use_container_width=True)

# Calculate weighted overall health score
overall_score = (score_df["Score Assigned (/100)"] * (score_df["Weight (%)"] / 100.0)).sum()

st.markdown("---")
st.subheader("Overall Financial Wellness Index")

m1, m2, m3 = st.columns(3)
m1.metric("Composite Health Score", f"{overall_score:.1f} / 100")
m2.metric("Primary Strength", "Emergency Fund & DTI")
m3.metric("Primary Area to Improve", "Retirement Readiness")

st.markdown("---")
st.subheader("Score Distribution Across Pillars")
fig = px.bar(
    score_df,
    x="Financial Pillar",
    y="Score Assigned (/100)",
    color="Status",
    title="Financial Wellness Score by Category",
    text_auto=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Financial Wellness Insight:** A composite financial health score above 75 indicates strong financial resilience, allowing you to comfortably weather unexpected economic shocks and compound wealth effectively.")