import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Financial Report Exporter", page_icon="📑", layout="wide")
st.title("📑 Executive Financial Report & Export Hub")

st.markdown("Compile your complete financial metrics, asset allocations, and milestone statuses into structured executive summaries ready for export.")

@st.cache_data
def get_executive_summary():
    return pd.DataFrame({
        "Portfolio Segment": ["Core Equities & Mutual Funds", "Fixed Income & Debt", "Real Estate & Housing", "Precious Metals & Gold", "Alternative & Digital Assets"],
        "Total Valuation (₹)": [4500000.0, 1800000.0, 8500000.0, 1420000.0, 850000.0],
        "Portfolio Weight (%)": [27.3, 10.9, 51.5, 8.6, 5.2],
        "Annualized Return (%)": [14.2, 7.5, 9.8, 11.4, 18.0]
    })

exec_df = get_executive_summary()

st.markdown("---")
st.subheader("Executive Asset Breakdown")
st.dataframe(exec_df, use_container_width=True)

st.markdown("---")
st.subheader("Generate & Download Financial Report")

# Initialize session state for export readiness if not present
if "report_ready" not in st.session_state:
    st.session_state.report_ready = False

with st.form("export_form"):
    c1, c2 = st.columns(2)
    with c1:
        report_title = st.text_input("Report Header Title", value="Comprehensive Wealth & Asset Audit")
        report_format = st.selectbox("Export Document Format", ["Structured CSV Summary", "Executive Summary Matrix", "Detailed Portfolio Ledger"])
    with c2:
        include_tax_summary = st.checkbox("Include Tax & Capital Gains Breakdown", value=True)
        include_stress_test = st.checkbox("Include Macro Scenario Stress Test Results", value=True)
    
    export_submitted = st.form_submit_button("Compile Report")
    if export_submitted:
        st.session_state.report_ready = True

# Render the download button outside the form block safely
if st.session_state.report_ready:
    timestamp = datetime.now().strftime("%Y-%m-%d")
    csv_data = exec_df.to_csv(index=False).encode('utf-8')
    
    st.success(f"Report '{report_title}' successfully compiled and ready for download!")
    st.download_button(
        label="📥 Download Compiled Financial Report (CSV)",
        data=csv_data,
        file_name=f"financial_executive_report_{timestamp}.csv",
        mime="text/csv",
    )

st.markdown("---")
st.info("**Export Insight:** Regular archival of monthly or quarterly executive financial reports provides a permanent historical audit trail of your long-term wealth compounding.")