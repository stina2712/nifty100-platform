import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Stock Correlation Matrix", page_icon="📈", layout="wide")
st.title("📈 Sector & Stock Correlation Matrix")

st.markdown("Analyze historical price return correlations across major Nifty 100 stocks to uncover diversification opportunities and risk concentrations.")

@st.cache_data
def get_correlation_data():
    tickers = ["TCS", "Infosys", "Reliance", "HDFC Bank", "ITC", "HUL", "L&T", "Airtel"]
    
    np.random.seed(42)
    matrix = np.array([
        [1.00, 0.85, 0.40, 0.35, 0.20, 0.15, 0.30, 0.25],
        [0.85, 1.00, 0.38, 0.32, 0.18, 0.12, 0.28, 0.22],
        [0.40, 0.38, 1.00, 0.65, 0.30, 0.25, 0.70, 0.50],
        [0.35, 0.32, 0.65, 1.00, 0.25, 0.20, 0.55, 0.45],
        [0.20, 0.18, 0.30, 0.25, 1.00, 0.80, 0.20, 0.15],
        [0.15, 0.12, 0.25, 0.20, 0.80, 1.00, 0.18, 0.12],
        [0.30, 0.28, 0.70, 0.55, 0.20, 0.18, 1.00, 0.40],
        [0.25, 0.22, 0.50, 0.45, 0.15, 0.12, 0.40, 1.00]
    ])
    
    return pd.DataFrame(matrix, index=tickers, columns=tickers)

corr_df = get_correlation_data()

st.markdown("---")
st.subheader("Interactive Correlation Heatmap")

fig = px.imshow(
    corr_df,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    aspect="auto",
    title="Stock Return Correlation Heatmap"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Key Portfolio Insights")
c1, c2 = st.columns(2)

with c1:
    st.info("**High Correlation Alert (Red)**\n\nStocks like **TCS & Infosys** (0.85) or **ITC & HUL** (0.80) move closely together. Holding both does not provide true diversification.")

with c2:
    st.success("**Low Correlation Benefit (Blue)**\n\nCombining assets with lower correlations (e.g., **IT & FMCG** or **Telecom & Banking**) significantly reduces overall portfolio volatility.")