import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="DCF Valuation Model", page_icon="💵", layout="wide")
st.title("💵 Discounted Cash Flow (DCF) Intrinsic Valuation")

@st.cache_data
def get_dcf_universe():
    return pd.DataFrame({
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel"
        ],
        "current_fcf": [45000.0, 65000.0, 55000.0, 26000.0, 20000.0, 11000.0, 14000.0, 18000.0], # in Crores INR
        "current_price": [4100.0, 2900.0, 1650.0, 1850.0, 450.0, 2500.0, 3600.0, 1200.0],
        "shares_outstanding": [37.0, 67.6, 55.0, 41.5, 125.0, 23.5, 13.8, 60.0] # in Crores
    })

df = get_dcf_universe()

st.subheader("Select Company & Valuation Assumptions")
selected_company = st.selectbox("Choose Company for DCF Analysis", df["company_name"].tolist())

comp_data = df[df["company_name"] == selected_company].iloc[0]

col1, col2, col3 = st.columns(3)
with col1:
    growth_rate = st.slider("Projected 5Y FCF Growth Rate (%)", 5.0, 30.0, 12.0, 0.5) / 100.0
with col2:
    discount_rate = st.slider("Discount Rate (WACC) (%)", 8.0, 18.0, 11.0, 0.5) / 100.0
with col3:
    terminal_growth = st.slider("Terminal Growth Rate (%)", 2.0, 6.0, 4.0, 0.5) / 100.0

# DCF Calculation Engine
base_fcf = comp_data["current_fcf"]
projected_fcfs = []
current_val = base_fcf
for _ in range(5):
    current_val *= (1 + growth_rate)
    projected_fcfs.append(current_val)

discounted_fcfs = [fcf / ((1 + discount_rate) ** (i + 1)) for i, fcf in enumerate(projected_fcfs)]
sum_discounted_fcf = sum(discounted_fcfs)

# Terminal Value
terminal_value = (projected_fcfs[-1] * (1 + terminal_growth)) / (discount_rate - terminal_growth)
discounted_terminal_value = terminal_value / ((1 + discount_rate) ** 5)

enterprise_value = sum_discounted_fcf + discounted_terminal_value
intrinsic_value_per_share = enterprise_value / comp_data["shares_outstanding"]
current_market_price = comp_data["current_price"]
margin_of_safety = ((intrinsic_value_per_share - current_market_price) / current_market_price) * 100

st.markdown("---")
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Estimated Intrinsic Value", f"₹{intrinsic_value_per_share:.2f}")
with m2:
    st.metric("Current Market Price", f"₹{current_market_price:.2f}")
with m3:
    st.metric("Margin of Safety / Premium", f"{margin_of_safety:.2f}%", delta=f"{margin_of_safety:.2f}%")

st.markdown("---")
st.subheader("5-Year Cash Flow Projections (₹ Crores)")
proj_df = pd.DataFrame({
    "Year": [f"Year {i+1}" for i in range(5)],
    "Projected FCF": [round(f, 2) for f in projected_fcfs],
    "Discounted FCF": [round(f, 2) for f in discounted_fcfs]
})
st.dataframe(proj_df, use_container_width=True)