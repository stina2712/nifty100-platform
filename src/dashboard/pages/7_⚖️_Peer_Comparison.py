import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Peer Comparison Matrix", page_icon="⚖️", layout="wide")
st.title("⚖️ Side-by-Side Peer Comparison Matrix")

@st.cache_data
def get_peer_dataset():
    return pd.DataFrame({
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel"
        ],
        "sector": ["IT", "Conglomerate", "Banking", "IT", "FMCG", "FMCG", "Infrastructure", "Telecom"],
        "roce": [28.5, 14.2, 18.1, 31.0, 25.4, 23.0, 15.0, 12.5],
        "debt_to_equity": [0.02, 0.35, 1.15, 0.05, 0.10, 0.08, 0.65, 0.90],
        "profit_cagr_3yr": [15.8, 12.4, 16.2, 14.1, 11.5, 10.2, 18.0, 22.0],
        "current_price": [4100.0, 2900.0, 1650.0, 1850.0, 450.0, 2500.0, 3600.0, 1200.0]
    })

df = get_peer_dataset()

st.subheader("Select Companies for Peer Analysis")
selected_peers = st.multiselect(
    "Choose companies to compare",
    df["company_name"].tolist(),
    default=["Tata Consultancy Services", "Infosys", "ITC", "Hindustan Unilever"]
)

if not selected_peers:
    st.warning("Please select at least one company to view comparison metrics.")
else:
    comparison_df = df[df["company_name"].isin(selected_peers)].set_index("company_name")
    
    st.markdown("---")
    st.subheader("Financial Metrics Comparison Table")
    st.dataframe(comparison_df, use_container_width=True)
    
    st.markdown("---")
    st.subheader("ROCE vs. Profit Growth Comparison")
    
    # Melt dataframe for grouped bar chart
    melted_df = comparison_df.reset_index().melt(
        id_vars=["company_name", "sector"],
        value_vars=["roce", "profit_cagr_3yr"],
        var_name="Metric",
        value_name="Percentage"
    )
    
    fig = px.bar(
        melted_df,
        x="company_name",
        y="Percentage",
        color="Metric",
        barmode="group",
        title="ROCE (%) vs 3Y Profit CAGR (%) Across Peers",
        labels={"company_name": "Company", "Percentage": "Rate (%)"}
    )
    st.plotly_chart(fig, use_container_width=True)