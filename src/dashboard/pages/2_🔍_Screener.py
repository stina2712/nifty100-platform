import streamlit as st
import pandas as pd

st.set_page_config(page_title="Screener Engine", page_icon="🔍", layout="wide")
st.title("🔍 Multi-Criteria Screener Engine")

@st.cache_data
def get_sample_companies():
    return pd.DataFrame({
        "company_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel"
        ],
        "sector": ["IT", "Conglomerate", "Banking", "IT", "FMCG", "FMCG", "Infrastructure", "Telecom"],
        "roce": [28.5, 14.2, 18.1, 31.0, 25.4, 23.0, 15.0, 12.5],
        "debt_to_equity": [0.02, 0.35, 1.15, 0.05, 0.10, 0.08, 0.65, 0.90],
        "profit_cagr_3yr": [15.8, 12.4, 16.2, 14.1, 11.5, 10.2, 18.0, 22.0],
        "sales_cagr_3yr": [12.0, 10.0, 14.0, 11.0, 9.5, 8.5, 15.0, 19.0],
        "current_ratio": [2.1, 1.4, 1.8, 1.9, 2.0, 1.7, 1.3, 1.1],
        "interest_coverage": [45.0, 8.5, 12.0, 35.0, 28.0, 30.0, 6.5, 4.2]
    })

df = get_sample_companies()

tab1, tab2 = st.tabs(["Custom Filter Screener", "Preset Strategies"])

with tab1:
    st.sidebar.header("Filter Criteria")
    min_roce = st.sidebar.slider("Minimum ROCE (%)", 0.0, 50.0, 10.0, key="scr_roce")
    max_de = st.sidebar.slider("Maximum Debt-to-Equity", 0.0, 5.0, 1.0, key="scr_de")
    min_cagr = st.sidebar.slider("Min 3Y Profit CAGR (%)", -20.0, 50.0, 5.0, key="scr_cagr")

    if st.button("Run Screener", type="primary"):
        results = df[
            (df['roce'] >= min_roce) & 
            (df['debt_to_equity'] <= max_de) & 
            (df['profit_cagr_3yr'] >= min_cagr)
        ]
        
        if results.empty:
            st.warning("No companies matched the current filter criteria.")
        else:
            st.success(f"Found {len(results)} matching companies!")
            st.dataframe(results, use_container_width=True)

with tab2:
    st.subheader("Preset Investment Strategies")
    strategy = st.selectbox("Select Strategy", ["Value Pick (High ROCE, Low Debt)", "High Growth Compounders"])
    
    if strategy == "Value Pick (High ROCE, Low Debt)":
        preset_results = df[(df['roce'] >= 15.0) & (df['debt_to_equity'] <= 0.5) & (df['profit_cagr_3yr'] >= 10.0)]
    else:
        preset_results = df[(df['roce'] >= 20.0) & (df['debt_to_equity'] <= 1.0) & (df['profit_cagr_3yr'] >= 15.0)]
        
    st.info(f"Showing results for strategy: {strategy} ({len(preset_results)} matches)")
    st.dataframe(preset_results, use_container_width=True)