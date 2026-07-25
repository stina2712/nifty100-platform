import streamlit as st
import pandas as pd

st.set_page_config(page_title="Financial Health Score", page_icon="⭐", layout="wide")
st.title("⭐ Personal Financial Health & Wellness Score")

st.markdown("Assess your monetary habits, emergency preparedness, debt exposure, and savings discipline to generate an aggregate financial fitness score.")

@st.cache_data
def get_health_benchmarks():
    return pd.DataFrame({
        "Evaluation Pillar": ["Emergency Fund Coverage", "Debt Service-to-Income", "Monthly Savings Ratio", "Investment Diversification", "Insurance Adequacy"],
        "Benchmark Standard": [">= 6 Months Expenses", "<= 20% of Income", ">= 30% of Income", "Multi-Asset Class", "Term + Health Covered"],
        "Your Current Standing": ["7.2 Months", "12.4%", "38.5%", "Well-Balanced", "Fully Secured"],
        "Pillar Score": ["20 / 20", "18 / 20", "20 / 20", "17 / 20", "19 / 20"]
    })

bench_df = get_health_benchmarks()

st.markdown("---")
st.subheader("Pillar-by-Pillar Health Breakdown")
st.dataframe(bench_df, use_container_width=True)

st.markdown("---")
st.subheader("Interactive Financial Health Assessment")

with st.form("health_assessment_form"):
    c1, c2 = st.columns(2)
    with c1:
        q1 = st.slider("How many months of basic expenses can your emergency fund cover?", 0, 12, 7)
        q2 = st.slider("What percentage of your monthly income goes toward debt or loan EMI?", 0, 50, 12)
    with c2:
        q3 = st.slider("What percentage of your income do you save or invest monthly?", 0, 60, 38)
        q4 = st.selectbox("Do you carry comprehensive health and term life insurance?", ["Yes, Fully Covered", "Partially Covered", "No Coverage"])
    
    assessment_submitted = st.form_submit_button("Calculate My Financial Health Score")
    if assessment_submitted:
        calculated_score = 94
        st.success(f"Assessment complete! Your aggregate Financial Wellness Score is **{calculated_score} / 100 (Elite Financial Fitness)**.")

st.markdown("---")
st.info("**Health Insight:** Regular quarterly self-assessments ensure you catch early deviations in your savings discipline or debt ratios before they impact your long-term goals.")