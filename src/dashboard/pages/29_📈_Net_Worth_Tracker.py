import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Net Worth Tracker", page_icon="📈", layout="wide")
st.title("📈 Net Worth & Balance Sheet Hub")

st.markdown("Consolidate your total assets and liabilities to track your true financial net worth in real-time.")

@st.cache_data
def get_balance_sheet_data():
    assets_df = pd.DataFrame({
        "Asset Category": ["Real Estate", "Equities & Mutual Funds", "Gold & Commodities", "Fixed Income / PF", "Bank & Liquid Cash"],
        "Current Value (₹)": [12500000.0, 3500000.0, 850000.0, 1800000.0, 625000.0]
    })
    
    liabilities_df = pd.DataFrame({
        "Liability Category": ["Home Loan", "Car Loan", "Personal Loan / Credit Cards"],
        "Outstanding Amount (₹)": [4500000.0, 650000.0, 335000.0]
    })
    
    return assets_df, liabilities_df

assets_df, liabilities_df = get_balance_sheet_data()

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Total Assets Breakdown")
    st.dataframe(assets_df, use_container_width=True)

with col2:
    st.subheader("Total Liabilities Breakdown")
    st.dataframe(liabilities_df, use_container_width=True)

total_assets = assets_df["Current Value (₹)"].sum()
total_liabilities = liabilities_df["Outstanding Amount (₹)"].sum()
net_worth = total_assets - total_liabilities

st.markdown("---")
st.subheader("Net Worth Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Total Assets", f"₹{total_assets:,.2f}")
m2.metric("Total Liabilities", f"₹{total_liabilities:,.2f}")
m3.metric("Net Worth", f"₹{net_worth:,.2f}", delta=f"{(net_worth/total_assets)*100:.1f}% equity ratio")

st.markdown("---")
st.subheader("Asset vs. Liability Comparison")

fig = px.bar(
    x=["Assets", "Liabilities", "Net Worth"],
    y=[total_assets, total_liabilities, net_worth],
    color=["Assets", "Liabilities", "Net Worth"],
    title="Overall Balance Sheet Position",
    text_auto=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Wealth Insight:** Growing your net worth depends not just on increasing asset values through disciplined investing, but also on systematically paying down high-interest liabilities.")