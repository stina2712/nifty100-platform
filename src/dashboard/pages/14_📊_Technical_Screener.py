import streamlit as st
import pandas as pd

st.set_page_config(page_title="Technical Screener", page_icon="📊", layout="wide")
st.title("📊 Technical Indicators & Moving Average Screener")

st.markdown("Filter and scan Nifty 100 equities using quantitative technical indicators like Relative Strength Index (RSI), Moving Average Crossovers, and Volume spikes.")

@st.cache_data
def get_technical_universe():
    return pd.DataFrame({
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel"
        ],
        "sector": ["IT", "Conglomerate", "Banking", "IT", "FMCG", "FMCG", "Infrastructure", "Telecom"],
        "current_price": [4100.0, 2900.0, 1650.0, 1850.0, 450.0, 2500.0, 3600.0, 1200.0],
        "rsi_14": [58.5, 42.1, 65.4, 71.2, 34.8, 48.0, 62.3, 55.0],
        "ma_signal": ["Bullish (Above 50 MA)", "Neutral", "Bullish (Above 50 MA)", "Overbought (>70 RSI)", "Oversold (<35 RSI)", "Neutral", "Bullish (Above 50 MA)", "Neutral"],
        "macd_status": ["Bullish", "Bearish", "Bullish", "Bullish", "Bearish", "Neutral", "Bullish", "Bullish"]
    })

df = get_technical_universe()

st.markdown("---")
st.subheader("Filter by Technical Criteria")

c1, c2 = st.columns(2)
with c1:
    selected_signal = st.selectbox("Moving Average Trend Signal", ["All Signals"] + df["ma_signal"].unique().tolist())
with c2:
    max_rsi = st.slider("Maximum RSI (14)", min_value=10, max_value=100, value=100)

# Apply filters
filtered_df = df[df["rsi_14"] <= max_rsi].copy()
if selected_signal != "All Signals":
    filtered_df = filtered_df[filtered_df["ma_signal"] == selected_signal]

st.markdown("---")
st.subheader("Filtered Technical Results")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.subheader("Technical Quick Guide")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("**RSI (14)**\n\nValues above 70 indicate potential overbought conditions, while values below 30 suggest oversold territory.")
with col2:
    st.success("**Moving Averages**\n\nStocks trading consistently above their 50-day and 200-day simple moving averages demonstrate strong primary upward momentum.")
with col3:
    st.warning("**MACD Crossover**\n\nMACD signal line crossovers help confirm trend reversals and entry momentum shifts.")