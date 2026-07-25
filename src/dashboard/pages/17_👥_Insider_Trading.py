import streamlit as st
import pandas as pd

st.set_page_config(page_title="Insider Trading & Shareholding", page_icon="👥", layout="wide")
st.title("👥 Insider Trading & Shareholding Tracker")

st.markdown("Monitor promoter pledges, institutional holdings (FII/DII), and open market insider transactions for Nifty 100 equities.")

@st.cache_data
def get_shareholding_data():
    return pd.DataFrame({
        "company_name": ["Tata Consultancy Services", "Reliance Industries", "HDFC Bank", "Infosys", "ITC"],
        "promoter_holding_pct": [72.3, 50.3, 0.0, 14.8, 25.5],
        "fii_holding_pct": [12.5, 23.4, 52.1, 34.2, 11.2],
        "dii_holding_pct": [9.4, 14.1, 31.5, 32.5, 51.0],
        "public_holding_pct": [5.8, 12.2, 16.4, 18.5, 12.3],
        "pledged_shares_pct": [0.0, 1.2, 0.0, 0.0, 0.0]
    })

@st.cache_data
def get_insider_deals():
    return pd.DataFrame({
        "date": ["2026-07-22", "2026-07-20", "2026-07-18", "2026-07-15"],
        "company_name": ["Reliance Industries", "Infosys", "HDFC Bank", "ITC"],
        "insider_name": ["Promoter Group", "Senior Management", "Institutional Trustee", "Executive Director"],
        "transaction_type": ["Buy", "Sell", "Buy", "Buy"],
        "shares": [150000, 45000, 200000, 50000],
        "value_cr": [43.5, 8.3, 33.0, 2.2]
    })

tab1, tab2 = st.tabs(["📊 Shareholding Patterns", "📝 Open Market Insider Deals"])

with tab1:
    st.subheader("Quarterly Shareholding Breakdown (%)")
    sh_df = get_shareholding_data()
    st.dataframe(sh_df, use_container_width=True)
    st.info("**Promoter Pledge Note:** High pledged shares (>10-15%) can indicate financial stress or liquidity constraints for the promoter group.")

with tab2:
    st.subheader("Recent Insider Transactions")
    deals_df = get_insider_deals()
    st.dataframe(deals_df, use_container_width=True)
    st.success("**Tip:** Consistent insider buying during market corrections often signals strong management confidence in future earnings growth.")