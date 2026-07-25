import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Forex Risk Analyzer", page_icon="💱", layout="wide")
st.title("💱 Real-Time Forex Risk & Exchange Rate Analyzer")

st.markdown("Track major global currency pairs against the Indian Rupee (INR), analyze forex volatility, and measure currency exposure risk.")

@st.cache_data
def get_forex_rates():
    return pd.DataFrame({
        "Currency Pair": ["USD / INR", "EUR / INR", "GBP / INR", "JPY / INR", "AUD / INR"],
        "Exchange Rate (₹)": [83.45, 90.20, 107.50, 0.53, 55.10],
        "Daily Change (%)": [+0.15, -0.25, +0.40, -0.10, +0.05],
        "30-Day Volatility": ["Low (4.2%)", "Medium (6.8%)", "Medium (7.1%)", "High (11.5%)", "Medium (8.0%)"],
        "Trend": ["Bullish", "Bearish", "Bullish", "Neutral", "Bullish"]
    })

forex_df = get_forex_rates()

st.markdown("---")
st.subheader("Major Exchange Rates (vs INR)")
st.dataframe(forex_df, use_container_width=True)

st.markdown("---")
st.subheader("Forex Exposure Calculator")

c1, c2, c3 = st.columns(3)
with c1:
    selected_pair = st.selectbox("Select Currency Pair", forex_df["Currency Pair"].tolist())
with c2:
    foreign_amount = st.number_input("Foreign Currency Amount", value=10000.0, step=1000.0)
with c3:
    hedging_pct = st.slider("Hedged Exposure (%)", min_value=0, max_value=100, value=50)

# Calculate INR Value
current_rate = forex_df.loc[forex_df["Currency Pair"] == selected_pair, "Exchange Rate (₹)"].values[0]
total_inr_value = foreign_amount * current_rate
hedged_value = total_inr_value * (hedging_pct / 100.0)
unhedged_value = total_inr_value * (1.0 - (hedging_pct / 100.0))

st.markdown("---")
st.subheader("Exposure Valuation Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Total INR Value", f"₹{total_inr_value:,.2f}")
m2.metric("Hedged Exposure", f"₹{hedged_value:,.2f}")
m3.metric("Unhedged Risk Exposure", f"₹{unhedged_value:,.2f}")

# Generate sample 30-day historical trend chart for the selected currency
days = np.arange(1, 31)
np.random.seed(42)
noise = np.random.normal(0, 0.2, 30)
historical_prices = current_rate + np.cumsum(noise)

trend_df = pd.DataFrame({
    "Day": days,
    "Exchange Rate": historical_prices
})

st.markdown("---")
st.subheader(f"30-Day Trend for {selected_pair}")
fig = px.line(
    trend_df,
    x="Day",
    y="Exchange Rate",
    title=f"Historical Exchange Rate Movement ({selected_pair})",
    markers=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Forex Risk Management Tip:** Unhedged international asset exposure is susceptible to sudden currency fluctuations. Maintaining a strategic hedge ratio helps safeguard portfolio returns against severe INR appreciation.")