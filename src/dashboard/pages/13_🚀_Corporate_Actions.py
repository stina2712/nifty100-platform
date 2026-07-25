import streamlit as st
import pandas as pd

st.set_page_config(page_title="IPO & Corporate Actions", page_icon="🚀", layout="wide")
st.title("🚀 IPO & Corporate Actions Tracker")

st.markdown("Stay updated on upcoming initial public offerings (IPOs), dividend ex-dates, bonus issues, and stock splits.")

@st.cache_data
def get_ipo_data():
    return pd.DataFrame({
        "company_name": ["Nexus Retail Ltd.", "Apex Healthcare", "Zenith Tech Solutions", "Vanguard Infra"],
        "sector": ["Retail", "Healthcare", "IT Services", "Infrastructure"],
        "ipo_date": ["2026-08-10", "2026-08-18", "2026-09-02", "2026-09-15"],
        "price_band": ["₹450 - ₹480", "₹1,120 - ₹1,180", "₹320 - ₹340", "₹850 - ₹900"],
        "issue_size_cr": [1200.5, 3400.0, 850.0, 2100.0],
        "status": ["Upcoming", "Upcoming", "Announced", "Announced"]
    })

@st.cache_data
def get_dividends_data():
    return pd.DataFrame({
        "company_name": ["Tata Consultancy Services", "ITC", "Hindustan Unilever", "Infosys"],
        "dividend_per_share": ["₹28.00", "₹7.50", "₹22.00", "₹20.00"],
        "ex_date": ["2026-08-05", "2026-08-12", "2026-08-20", "2026-08-25"],
        "record_date": ["2026-08-06", "2026-08-13", "2026-08-21", "2026-08-26"],
        "dividend_type": ["Interim", "Final", "Interim", "Final"]
    })

tab1, tab2 = st.tabs(["🚀 Upcoming IPOs", "💰 Dividends & Splits"])

with tab1:
    st.subheader("Upcoming Mainboard IPO Calendar")
    ipo_df = get_ipo_data()
    st.dataframe(ipo_df, use_container_width=True)
    
    st.info("**IPO Note:** Price bands and issue sizes are subject to final red herring prospectus (RHP) filings with SEBI.")

with tab2:
    st.subheader("Upcoming Dividend Ex-Dates")
    div_df = get_dividends_data()
    st.dataframe(div_df, use_container_width=True)
    
    st.success("**Tip:** You must purchase or hold the stock on or before the ex-date to be eligible for the declared dividend payout.")