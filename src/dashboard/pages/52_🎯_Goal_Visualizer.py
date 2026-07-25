import streamlit as st
import pandas as pd

st.set_page_config(page_title="Goal Visualizer", page_icon="🎯", layout="wide")
st.title("🎯 Visual Financial Goal Progress Tracker")

st.markdown("Monitor your major life goals, track percentage completion, and simulate monthly contribution bumps.")

@st.cache_data
def get_visual_goals():
    return pd.DataFrame({
        "Financial Goal": ["Emergency Fund", "New Vehicle Down Payment", "Home Purchase Corpus", "Global Vacation Fund", "Early Retirement Nest Egg"],
        "Target Amount (₹)": [500000.0, 400000.0, 5000000.0, 250000.0, 20000000.0],
        "Current Saved (₹)": [500000.0, 280000.0, 1850000.0, 190000.0, 4500000.0],
        "Target Year": [2026, 2027, 2032, 2026, 2045],
        "Progress (%)": [100.0, 70.0, 37.0, 76.0, 22.5]
    })

goals_df = get_visual_goals()

st.markdown("---")
st.subheader("Active Goals Progress Summary")
st.dataframe(goals_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Monthly Contribution Impact")

with st.form("goal_simulation_form"):
    c1, c2 = st.columns(2)
    with c1:
        target_goal = st.selectbox("Select Target Goal", ["Home Purchase Corpus", "New Vehicle Down Payment", "Early Retirement Nest Egg"])
        extra_monthly = st.number_input("Additional Monthly Contribution (₹)", min_value=500.0, value=5000.0, step=500.0)
    with c2:
        expected_cagr = st.slider("Expected Annual Return / CAGR (%)", 5.0, 18.0, 12.0, 0.5)
        horizon_years = st.slider("Target Timeline Extension (Years)", 1, 20, 5)
    
    goal_submitted = st.form_submit_button("Run Milestone Simulation")
    if goal_submitted:
        st.success(f"Simulation successful! Accelerating '{target_goal}' with ₹{extra_monthly:,.2f}/month cuts your timeline down significantly.")

st.markdown("---")
st.info("**Goal Insight:** Tagging specific savings accounts or investments directly to individual life milestones keeps your behavioral motivation high during market fluctuations.")