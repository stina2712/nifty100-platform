import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Financial Goal Planner", page_icon="🎯", layout="wide")
st.title("🎯 Smart Financial Goal Planner & SIP Calculator")

st.markdown("Plan your long-term financial milestones, calculate required monthly SIP investments, and visualize wealth compounding over time.")

st.markdown("---")
st.subheader("Goal Parameters")

c1, c2, c3 = st.columns(3)
with c1:
    goal_name = st.text_input("Goal Description", value="Retirement Corpus")
with c2:
    target_amount = st.number_input("Target Amount (₹)", value=10000000.0, step=500000.0)
with c3:
    years_to_goal = st.slider("Time Horizon (Years)", min_value=1, max_value=30, value=10)

c4, c5 = st.columns(2)
with c4:
    expected_return_rate = st.slider("Expected Annual Return (%)", min_value=6.0, max_value=20.0, value=12.0)
with c5:
    annual_step_up = st.slider("Annual SIP Step-Up (%)", min_value=0.0, max_value=15.0, value=5.0)

# Monthly calculations
i = (expected_return_rate / 100.0) / 12.0
months = years_to_goal * 12

factor = (((1 + i) ** months - 1) / i) * (1 + i)
base_monthly_sip = target_amount / factor if factor > 0 else 0

st.markdown("---")
st.subheader("Investment Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Estimated Monthly SIP Required", f"₹{base_monthly_sip:,.2f}")
m2.metric("Target Goal Amount", f"₹{target_amount:,.2f}")
m3.metric("Investment Horizon", f"{years_to_goal} Years ({months} Months)")

# Generate growth trajectory dataframe for chart with exact matching lengths
months_axis = np.arange(1, months + 1)
accumulated_investment = np.zeros(months)
portfolio_value = np.zeros(months)

current_sip = base_monthly_sip
curr_val = 0.0
invested_total = 0.0

for m in range(months):
    if m > 0 and m % 12 == 0:
        current_sip *= (1.0 + (annual_step_up / 100.0))
    
    invested_total += current_sip
    curr_val = (curr_val + current_sip) * (1.0 + i)
    
    accumulated_investment[m] = invested_total
    portfolio_value[m] = curr_val

chart_df = pd.DataFrame({
    "Year": np.concatenate([months_axis / 12.0, months_axis / 12.0]),
    "Amount": np.concatenate([accumulated_investment, portfolio_value]),
    "Type": ["Total Invested Principal"] * months + ["Projected Portfolio Value"] * months
})

st.markdown("---")
st.subheader("Wealth Accumulation Projection")
fig = px.line(
    chart_df,
    x="Year",
    y="Amount",
    color="Type",
    title=f"Growth Projection for '{goal_name}'",
    labels={"Amount": "Value (₹)", "Year": "Years"}
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Financial Planning Tip:** Increasing your SIP by a small percentage each year (Step-Up SIP) dramatically reduces the monthly burden required to reach large multi-crore goals.")