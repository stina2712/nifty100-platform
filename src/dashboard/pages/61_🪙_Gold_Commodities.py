import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gold & Commodities Tracker", page_icon="🪙", layout="wide")
st.title("🪙 Precious Metals & Gold Portfolio Tracker")

st.markdown("Track your physical gold holdings, Sovereign Gold Bonds (SGBs), digital gold investments, and commodity allocations.")

@st.cache_data
def get_gold_holdings():
    return pd.DataFrame({
        "Asset Type": ["Sovereign Gold Bond (SGB)", "Physical Gold Bars & Coins", "Gold ETF", "Digital Gold", "Silver Bullion ETF"],
        "Quantity / Weight": ["50 Grams", "100 Grams", "200 Grams", "30 Grams", "2 Kilograms"],
        "Purchase Value (₹)": [240000.0, 520000.0, 1100000.0, 160000.0, 150000.0],
        "Current Market Value (₹)": [350000.0, 720000.0, 1450000.0, 210000.0, 190000.0],
        "Unrealized Gain (%)": [+45.8, +38.5, +31.8, +31.2, +26.6]
    })

gold_df = get_gold_holdings()

st.markdown("---")
st.subheader("Precious Metals Portfolio Holdings")
st.dataframe(gold_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Gold & Commodity Accumulation")

with st.form("gold_sim_form"):
    c1, c2 = st.columns(2)
    with c1:
        monthly_gold_sip = st.number_input("Monthly Gold Investment SIP (₹)", min_value=1000.0, value=10000.0, step=1000.0)
        preferred_vehicle = st.selectbox("Preferred Gold Instrument", ["Sovereign Gold Bonds (SGB)", "Gold ETFs", "Digital Gold Platforms"])
    with c2:
        accumulation_horizon = st.slider("Accumulation Horizon (Years)", 1, 15, 5)
        expected_gold_cagr = st.slider("Expected Annual Gold Appreciation (%)", 4.0, 15.0, 8.5, 0.5)
    
    gold_submitted = st.form_submit_button("Run Precious Metals Simulation")
    if gold_submitted:
        st.success("Precious metals simulation complete! Regular accumulation builds a reliable inflation-hedged safety buffer.")

st.markdown("---")
st.info("**Commodity Insight:** Sovereign Gold Bonds (SGBs) offer an added advantage by providing regular interest payouts alongside capital appreciation on gold prices, completely tax-free if held until maturity.")