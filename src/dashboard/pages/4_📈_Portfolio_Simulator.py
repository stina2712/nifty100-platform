import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Portfolio Simulator", page_icon="📈", layout="wide")
st.title("📈 Portfolio Risk & Performance Simulator")

@st.cache_data
def get_portfolio_universe():
    return pd.DataFrame({
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel",
            "State Bank of India", "ICICI Bank"
        ],
        "sector": [
            "IT", "Conglomerate", "Banking", "IT", "FMCG", "FMCG", "Infrastructure", "Telecom", "Banking", "Banking"
        ],
        "expected_return": [16.5, 14.0, 15.2, 17.0, 12.5, 11.8, 15.5, 18.0, 14.5, 16.0],
        "annualized_volatility": [18.0, 22.5, 16.0, 19.5, 14.0, 13.5, 24.0, 21.0, 23.0, 17.5]
    })

df = get_portfolio_universe()

st.subheader("Select Assets & Allocate Weights")
st.markdown("Choose companies from your tracked universe and assign investment weights (weights should ideally sum up to 100%).")

selected_stocks = st.multiselect(
    "Select Companies", 
    df["company_name"].tolist(), 
    default=["Tata Consultancy Services", "HDFC Bank", "ITC", "Bharti Airtel"]
)

if not selected_stocks:
    st.warning("Please select at least one company to simulate a portfolio.")
else:
    sub_df = df[df["company_name"].isin(selected_stocks)].copy()
    
    # Dynamic weight sliders
    weights = []
    cols = st.columns(len(selected_stocks))
    default_weight = round(100.0 / len(selected_stocks), 2)
    
    for i, row in sub_df.reset_index().iterrows():
        with cols[i]:
            w = st.slider(f"{row['company_name'][:12]}...", 0.0, 100.0, default_weight, key=f"wt_{i}")
            weights.append(w)
            
    sub_df["weight"] = weights
    total_weight = sum(weights)
    
    if total_weight > 0:
        sub_df["normalized_weight"] = sub_df["weight"] / total_weight
    else:
        sub_df["normalized_weight"] = 0

    # Calculate portfolio metrics
    portfolio_return = np.sum(sub_df["expected_return"] * sub_df["normalized_weight"])
    # Simplified blended volatility assuming some diversification correlation
    portfolio_volatility = np.sqrt(np.sum((sub_df["normalized_weight"] * sub_df["annualized_volatility"]) ** 2)) * 0.9

    st.markdown("---")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Total Weight Allocated", f"{total_weight:.1f}%")
    with m2:
        st.metric("Expected Annual Return", f"{portfolio_return:.2f}%")
    with m3:
        st.metric("Est. Portfolio Volatility (Risk)", f"{portfolio_volatility:.2f}%")

    st.markdown("---")
    st.subheader("Asset Allocation Breakdown")
    
    fig = px.pie(
        sub_df, 
        names="company_name", 
        values="normalized_weight", 
        title="Portfolio Weights Distribution",
        hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)