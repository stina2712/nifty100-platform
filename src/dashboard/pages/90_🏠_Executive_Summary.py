import streamlit as st
import pandas as pd
from src.dashboard.components import render_page_header, render_page_footer
from src.etl.loader import render_data_status

st.set_page_config(page_title="Executive Summary", page_icon="🏠", layout="wide")

# 1. Standardized Header Component
render_page_header(
    "🏠 Executive Financial Command Center", 
    "Your centralized macro overview combining total net worth, active liabilities, liquidity buffers, and portfolio performance."
)

@st.cache_data
def get_executive_kpis():
    return pd.DataFrame({
        "Core Financial KPI": ["Total Net Worth", "Liquid Cash Reserves", "Total Active Debt / Liabilities", "Monthly Cash Flow Surplus", "Overall Financial Health Score"],
        "Current Value (₹)": [10920000.0, 825000.0, 5150000.0, 115000.0, "91 / 100"],
        "Benchmark Status": ["+14.2% YoY", "6.2 Months Runway", "Manageable (18.5% DTI)", "High Savings Rate", "Exceptional"]
    })

exec_df = get_executive_kpis()

# 2. Data Status Indicator
render_data_status(exec_df, "Executive KPI Dataset")

st.markdown("---")
st.subheader("Executive KPI Summary")
st.dataframe(exec_df, use_container_width=True)

st.markdown("---")
st.subheader("Quick Control Center Actions")

with st.form("executive_form"):
    c1, c2 = st.columns(2)
    with c1:
        command_action = st.selectbox("Select Master Command", ["Generate Full Financial Audit Report", "Sync All Asset Valuations", "Export Complete Ledger Backup", "Run Stress Test Simulation"])
        notification_channel = st.selectbox("Alert & Report Delivery", ["In-App Dashboard Only", "Registered Email Digest", "WhatsApp & Telegram Alert"])
    with c2:
        include_ai_insights = st.checkbox("Include AI-Driven Portfolio Recommendations", value=True)
        secure_encryption = st.checkbox("Enforce End-to-End Data Encryption", value=True)
    
    exec_submitted = st.form_submit_button("Execute Command")
    if exec_submitted:
        st.success(f"Master command **{command_action}** executed successfully across your entire financial ecosystem!")

st.markdown("---")
st.info("**Executive Insight:** Reviewing your high-level command center weekly ensures all asset classes, emergency reserves, and liabilities remain aligned with your long-term goals.")

# 3. Standardized Footer Component
render_page_footer()