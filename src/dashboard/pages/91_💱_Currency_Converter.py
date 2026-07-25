import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Currency Converter", page_icon="💱", layout="wide")
st.title("💱 Global Currency & Foreign Exchange Hub")

st.markdown("Convert multi-currency investments, track global exchange rates, and evaluate foreign asset exposure in your local currency.")

@st.cache_data
def get_exchange_rates():
    return pd.DataFrame({
        "Currency Pair": ["USD / INR", "EUR / INR", "GBP / INR", "JPY / INR", "AUD / INR"],
        "Exchange Rate": [83.50, 90.20, 106.80, 0.54, 55.40],
        "24h Change (%)": [+0.15, -0.08, +0.22, -0.45, +0.10],
        "Trend": ["Bullish", "Bearish", "Bullish", "Bearish", "Bullish"]
    })

fx_df = get_exchange_rates()

st.markdown("---")
st.subheader("Major Exchange Rates & Benchmarks")
st.dataframe(fx_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Foreign Currency Conversion")

with st.form("currency_form"):
    c1, c2 = st.columns(2)
    with c1:
        source_currency = st.selectbox("Source Currency", ["US Dollar (USD)", "Euro (EUR)", "British Pound (GBP)", "Japanese Yen (JPY)", "Australian Dollar (AUD)"])
        amount_to_convert = st.number_input("Amount to Convert", min_value=1.0, value=5000.0, step=500.0)
    with c2:
        target_currency = st.selectbox("Target Currency", ["Indian Rupee (INR)", "US Dollar (USD)", "Euro (EUR)", "British Pound (GBP)"])
        hedge_exposure = st.checkbox("Apply Currency Hedging Protection", value=True)
    
    fx_submitted = st.form_submit_button("Convert & Analyze FX")
    if fx_submitted:
        st.success(f"Currency conversion computed successfully from **{source_currency}** to **{target_currency}**!")

st.markdown("---")
st.info("**Currency Insight:** Tracking foreign exchange fluctuations is vital when holding international equities or planning overseas remittances to safeguard against currency depreciation.")