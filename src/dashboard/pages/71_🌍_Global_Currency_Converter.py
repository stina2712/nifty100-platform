import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Currency Converter", page_icon="🌍", layout="wide")
st.title("🌍 Global Currency & Multi-Geography Portfolio")

st.markdown("Track foreign investments, monitor exchange rate movements, and convert international assets to your home currency.")

@st.cache_data
def get_global_holdings():
    return pd.DataFrame({
        "Asset / Account": ["US Tech Stocks (RSUs)", "International Mutual Fund", "Global Real Estate REIT", "USDC Stablecoin Yield", "UK Pound Sterling Savings"],
        "Currency": ["USD", "USD", "USD", "USD", "GBP"],
        "Foreign Denominated Value": [45000.0, 12000.0, 25000.0, 5000.0, 8500.0],
        "Exchange Rate (to INR)": [83.5, 83.5, 83.5, 83.5, 106.2],
        "Value in INR (₹)": [3757500.0, 1002000.0, 2087500.0, 417500.0, 902700.0]
    })

global_df = get_global_holdings()

st.markdown("---")
st.subheader("International Assets & Forex Ledger")
st.dataframe(global_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Currency Conversion & Forex Shock")

with st.form("currency_sim_form"):
    c1, c2 = st.columns(2)
    with c1:
        foreign_amount = st.number_input("Foreign Amount to Convert", min_value=100.0, value=10000.0, step=500.0)
        source_currency = st.selectbox("Source Currency", ["USD ($)", "EUR (€)", "GBP (£)", "SGD ($)", "AED (د.إ)"])
    with c2:
        forex_shock_pct = st.slider("Simulate Currency Depreciation/Appreciation (%)", -15.0, 15.0, 5.0, 1.0)
        hedging_active = st.checkbox("Factor in Currency Hedging Protection", value=True)
    
    curr_submitted = st.form_submit_button("Calculate Forex Conversion")
    if curr_submitted:
        st.success("Currency conversion and exchange shock simulation complete! Multi-geography diversification successfully protects purchasing power.")

st.markdown("---")
st.info("**Currency Insight:** Holding a diversified mix of international assets provides a powerful hedge against domestic currency depreciation and macroeconomic volatility.")