import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Macro & Indices", page_icon="🌍", layout="wide")
st.title("🌍 Global Market Indices & Macro Tracker")

st.markdown("Monitor major international stock exchanges, currency pairs, and key macroeconomic commodity prices impacting domestic markets.")

@st.cache_data
def get_macro_data():
    return pd.DataFrame({
        "indicator_name": [
            "S&P 500", "NASDAQ Composite", "FTSE 100", "Nikkei 225", 
            "USD / INR", "Crude Oil (Brent)", "Gold (Per Ounce)", "India 10Y Bond Yield"
        ],
        "category": [
            "Global Equity", "Global Equity", "Global Equity", "Global Equity", 
            "Currency", "Commodity", "Commodity", "Fixed Income"
        ],
        "current_value": [5550.20, 17720.50, 8240.10, 39500.00, 83.45, 85.20, 2380.50, 7.12],
        "daily_change_pct": [0.45, 0.85, -0.15, 1.10, -0.08, 1.25, 0.35, -0.02]
    })

df = get_macro_data()

# Category filter
selected_category = st.selectbox("Filter by Category", ["All Categories"] + df["category"].unique().tolist())

if selected_category != "All Categories":
    display_df = df[df["category"] == selected_category].copy()
else:
    display_df = df.copy()

st.markdown("---")
st.subheader("Live Macroeconomic Indicators")

# Display metrics in columns for top indicators
col1, col2, col3, col4 = st.columns(4)
metrics_to_show = ["S&P 500", "NASDAQ Composite", "USD / INR", "Crude Oil (Brent)"]

for i, name in enumerate(metrics_to_show):
    row = df[df["indicator_name"] == name].iloc[0]
    with [col1, col2, col3, col4][i]:
        st.metric(
            label=row["indicator_name"], 
            value=f"{row['current_value']:,.2f}", 
            delta=f"{row['daily_change_pct']:+.2f}%"
        )

st.markdown("---")
st.subheader("Detailed Rates Table")
st.dataframe(display_df, use_container_width=True)

st.markdown("---")
st.subheader("Daily Percentage Change Comparison")
fig = px.bar(
    df,
    x="indicator_name",
    y="daily_change_pct",
    color="category",
    title="Global Indicators Daily Performance (%)",
    labels={"indicator_name": "Indicator", "daily_change_pct": "Daily Change (%)"}
)
st.plotly_chart(fig, use_container_width=True)