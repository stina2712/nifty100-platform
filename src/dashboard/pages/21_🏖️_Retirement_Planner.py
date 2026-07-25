import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retirement Cash Flow Planner", page_icon="🏖️", layout="wide")
st.title("🏖️ Retirement Corpus & Drawdown Planner")

st.markdown("Model your post-retirement phase, factoring in inflation, life expectancy, and systematic monthly withdrawals.")

st.markdown("---")
st.subheader("Retirement Assumptions")

c1, c2, c3 = st.columns(3)
with c1:
    current_age = st.number_input("Current Age", value=30, min_value=18, max_value=80)
with c2:
    retirement_age = st.number_input("Planned Retirement Age", value=60, min_value=40, max_value=90)
with c3:
    life_expectancy = st.number_input("Life Expectancy", value=85, min_value=50, max_value=105)

c4, c5, c6 = st.columns(3)
with c4:
    current_monthly_expense = st.number_input("Current Monthly Expenses (₹)", value=50000.0, step=5000.0)
with c5:
    inflation_rate = st.slider("Expected Annual Inflation (%)", min_value=3.0, max_value=10.0, value=6.0)
with c6:
    post_ret_return = st.slider("Post-Retirement Return (%)", min_value=4.0, max_value=14.0, value=8.0)

# Calculations
years_to_retirement = max(0, retirement_age - current_age)
retirement_duration = max(0, life_expectancy - retirement_age)

# Inflated monthly expense at retirement
inflation_multiplier = (1 + (inflation_rate / 100.0)) ** years_to_retirement
monthly_expense_at_retirement = current_monthly_expense * inflation_multiplier
annual_expense_at_retirement = monthly_expense_at_retirement * 12.0

# Corpus required at retirement using present value / annuity formula
r = (post_ret_return / 100.0) / 12.0
n = retirement_duration * 12.0

if r > 0:
    # Present value of annuity due or ordinary annuity approximation for corpus
    corpus_required = annual_expense_at_retirement / (post_ret_return / 100.0) * (1 - (1 + (post_ret_return / 100.0)) ** (-retirement_duration))
else:
    corpus_required = annual_expense_at_retirement * retirement_duration

st.markdown("---")
st.subheader("Retirement Milestone Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Years to Retirement", f"{years_to_retirement} Years")
m2.metric("Monthly Expense at Retirement", f"₹{monthly_expense_at_retirement:,.2f}")
m3.metric("Target Corpus Required", f"₹{corpus_required:,.2f}")

# Generate drawdown trajectory
drawdown_years = np.arange(0, retirement_duration + 1)
corpus_balance = np.zeros(len(drawdown_years))
corpus_balance[0] = corpus_required

curr_corpus = corpus_required
curr_annual_expense = annual_expense_at_retirement

for idx, yr in enumerate(drawdown_years[1:], start=1):
    # Growth then withdrawal or vice versa
    curr_corpus = (curr_corpus - curr_annual_expense) * (1.0 + (post_ret_return / 100.0))
    corpus_balance[idx] = max(0.0, curr_corpus)
    curr_annual_expense *= (1.0 + (inflation_rate / 100.0))

drawdown_df = pd.DataFrame({
    "Retirement Year": drawdown_years + retirement_age,
    "Remaining Corpus": corpus_balance
})

st.markdown("---")
st.subheader("Corpus Drawdown Trajectory")
fig = px.area(
    drawdown_df,
    x="Retirement Year",
    y="Remaining Corpus",
    title="Post-Retirement Corpus Depletion Over Time",
    labels={"Remaining Corpus": "Corpus Value (₹)", "Retirement Year": "Age / Year"}
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Retirement Insight:** Factoring in inflation is critical; living costs double roughly every 12 years at a 6% inflation rate, drastically increasing the target corpus required.")