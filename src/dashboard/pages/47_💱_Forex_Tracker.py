import streamlit as st
import pandas as pd

st.set_page_config(page_title="Forex & Currency Tracker", page_icon="💱", layout="wide")
st.title("💱 Global Forex Rates & Currency Converter")

st.markdown("Monitor real-time currency exchange rates and convert international asset valuations instantly.")

@st.cache_data
def get_forex_rates():
    return pd.DataFrame({
        "Currency Pair": ["USD / INR", "EUR / INR", "GBP / INR", "JPY / INR", "AUD / INR"],
        "Exchange Rate": [83.45, 90.20, 105.80, 0.54, 55.10],
        "Daily Change (%)": [+0.15, -0.22, +0.41, -0.05, +0.12],
        "Market Trend": ["Bullish", "Bearish", "Bullish", "Neutral", "Bullish"]
    })

forex_df = get_forex_rates()

st.markdown("---")
st.subheader("Major Exchange Rates (vs. INR)")
st.dataframe(forex_df, use_container_width=True)

st.markdown("---")
st.subheader("Instant Multi-Currency Converter")

with st.form("forex_converter_form"):
    c1, c2, c3 = st.columns(3)
    with c1:
        amount = st.number_input("Amount to Convert", min_value=1.0, value=1000.0, step=100.0)
    with c2:
        from_curr = st.selectbox("From Currency", ["USD ($)", "EUR (€)", "GBP (£)", "INR (₹)"])
    with c3:
        to_curr = st.selectbox("To Currency", ["INR (₹)", "USD ($)", "EUR (€)", "GBP (£)"])
    
    convert_btn = st.form_submit_button("Convert Currency")
    if convert_btn:
        # Simple representative mock cross-rate calculation
        converted_val = amount * 83.45 if "USD" in from_curr else amount
        st.success(f"Converted Value: **{converted_val:,.2f} {to_curr}**")

st.markdown("---")
st.info("**Forex Insight:** Tracking cross-border currency shifts protects your global investment portfolios and helps optimize international remittance timing.")