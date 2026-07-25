import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Market Overview", page_icon="📊", layout="wide")
st.title("📊 Market Overview")

@st.cache_data
def get_market_data():
    return pd.DataFrame({
        "company_id": list(range(1, 16)),
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel",
            "State Bank of India", "ICICI Bank", "Axis Bank", "Kotak Mahindra Bank",
            "Wipro", "Asian Paints", "Maruti Suzuki"
        ],
        "sector": [
            "IT", "Conglomerate", "Banking", "IT", "FMCG", "FMCG", "Infrastructure", "Telecom",
            "Banking", "Banking", "Banking", "Banking", "IT", "Consumer", "Automobile"
        ],
        "roce": [28.5, 14.2, 18.1, 31.0, 25.4, 23.0, 15.0, 12.5, 16.0, 19.5, 17.2, 18.0, 26.5, 29.0, 21.0],
        "debt_to_equity": [0.02, 0.35, 1.15, 0.05, 0.10, 0.08, 0.65, 0.90, 1.20, 1.10, 0.95, 0.40, 0.04, 0.15, 0.05],
        "profit_cagr_3yr": [15.8, 12.4, 16.2, 14.1, 11.5, 10.2, 18.0, 22.0, 19.0, 20.5, 15.0, 16.5, 13.0, 14.2, 17.0]
    })

df = get_market_data()

# Metric summary cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Companies Tracked", len(df))
with col2:
    st.metric("Avg ROCE", f"{df['roce'].mean():.2f}%")
with col3:
    st.metric("Avg Debt-to-Equity", f"{df['debt_to_equity'].mean():.2f}")

st.markdown("---")
st.subheader("ROCE Distribution Across Companies")

fig = px.histogram(
    df, 
    x="roce", 
    nbins=10, 
    title="ROCE Spread (%)",
    labels={"roce": "ROCE (%)", "count": "Number of Companies"},
    color_discrete_sequence=["#1f77b4"]
)
fig.update_layout(bargap=0.1)
st.plotly_chart(fig, use_container_width=True)