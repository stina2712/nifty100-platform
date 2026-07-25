import streamlit as st
import pandas as pd

st.set_page_config(page_title="Watchlist & Alerts", page_icon="⭐", layout="wide")
st.title("⭐ Personalized Watchlist & Price Alerts")

@st.cache_data
def get_watchlist_universe():
    return pd.DataFrame({
        "company_name": [
            "Tata Consultancy Services", "Reliance Industries", "HDFC Bank", 
            "Infosys", "ITC", "Hindustan Unilever", "Larsen & Toubro", "Bharti Airtel"
        ],
        "sector": ["IT", "Conglomerate", "Banking", "IT", "FMCG", "FMCG", "Infrastructure", "Telecom"],
        "current_price": [4100.0, 2900.0, 1650.0, 1850.0, 450.0, 2500.0, 3600.0, 1200.0],
        "day_change_pct": [1.2, -0.5, 0.8, 2.1, -1.0, 0.4, 1.5, -0.2]
    })

df = get_watchlist_universe()

# Initialize session state for user watchlist
if "user_watchlist" not in st.session_state:
    st.session_state.user_watchlist = ["Tata Consultancy Services", "HDFC Bank", "ITC"]

st.subheader("Manage Your Watchlist")
selected_watchlist = st.multiselect(
    "Add or remove companies from your active watchlist",
    df["company_name"].tolist(),
    default=st.session_state.user_watchlist
)
st.session_state.user_watchlist = selected_watchlist

if not selected_watchlist:
    st.warning("Your watchlist is currently empty. Select companies above to track them.")
else:
    watch_df = df[df["company_name"].isin(selected_watchlist)].copy()
    
    st.markdown("---")
    st.subheader("Watched Stocks Live Tracker")
    st.dataframe(watch_df, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Set Price Alert Thresholds")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        alert_stock = st.selectbox("Select Stock for Alert", selected_watchlist)
    with col2:
        current_p = float(watch_df[watch_df["company_name"] == alert_stock]["current_price"].values[0])
        target_price = st.number_input("Target Price (₹)", value=round(current_p * 1.05, 2))
    with col3:
        alert_type = st.selectbox("Alert Condition", ["Price crosses above target", "Price drops below target"])
        
    if st.button("Save Price Alert", type="primary"):
        st.success(f"Alert successfully configured for {alert_stock} at ₹{target_price}!")