import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ESG Sustainability Dashboard", page_icon="🌱", layout="wide")
st.title("🌱 ESG & Corporate Sustainability Scoring")

st.markdown("Evaluate Nifty 100 corporations on Environmental, Social, and Governance (ESG) performance metrics and overall sustainability risk ratings.")

@st.cache_data
def get_esg_universe():
    return pd.DataFrame({
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel"
        ],
        "sector": ["IT", "Conglomerate", "Banking", "IT", "FMCG", "FMCG", "Infrastructure", "Telecom"],
        "esg_score": [82.5, 68.0, 79.4, 85.0, 71.2, 80.1, 74.5, 76.0],
        "environmental_score": [88.0, 58.5, 82.0, 90.5, 65.0, 84.0, 70.0, 75.0],
        "social_score": [80.0, 70.0, 78.0, 82.0, 75.0, 81.0, 76.0, 78.0],
        "governance_score": [79.5, 75.5, 78.2, 82.5, 73.6, 85.3, 77.5, 75.0],
        "risk_rating": ["Low Risk", "Medium Risk", "Low Risk", "Low Risk", "Medium Risk", "Low Risk", "Medium Risk", "Low Risk"]
    })

df = get_esg_universe()

st.markdown("---")
st.subheader("ESG Rating Filters")

c1, c2 = st.columns(2)
with c1:
    selected_risk = st.selectbox("ESG Risk Category", ["All Categories"] + df["risk_rating"].unique().tolist())
with c2:
    min_esg = st.slider("Minimum Composite ESG Score", min_value=50.0, max_value=90.0, value=65.0)

# Filter dataframe
filtered_df = df[df["esg_score"] >= min_esg].copy()
if selected_risk != "All Categories":
    filtered_df = filtered_df[filtered_df["risk_rating"] == selected_risk]

st.markdown("---")
st.subheader("Filtered Company ESG Rankings")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.subheader("Composite ESG Score Comparison")
fig = px.bar(
    filtered_df,
    x="company_name",
    y="esg_score",
    color="sector",
    title="Overall ESG Score by Company",
    labels={"company_name": "Company", "esg_score": "Composite ESG Score (0-100)"}
)
st.plotly_chart(fig, use_container_width=True)