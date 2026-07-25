import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Data Export & Backup", page_icon="📥", layout="wide")
st.title("📥 Financial Data Export & Backup Center")

st.markdown("Download your complete financial records, transaction logs, and portfolio matrices for secure local archiving.")

@st.cache_data
def get_mock_export_data():
    return {
        "net_worth": [{"Month": "Jan", "Net Worth": 4200000}, {"Month": "Feb", "Net Worth": 4350000}, {"Month": "Mar", "Net Worth": 4510956}],
        "investments": [{"Asset": "Nifty 50 Index Fund", "Allocation": 2500000}, {"Asset": "Direct Stocks", "Allocation": 1000000}],
        "liabilities": [{"Debt": "Home Loan", "Outstanding": 2800000}]
    }

data = get_mock_export_data()

st.markdown("---")
st.subheader("Select Data Module to Export")

export_option = st.selectbox(
    "Choose Dataset",
    ["Net Worth History", "Investment Portfolio", "Liabilities & Debt Ledger", "Complete Financial Master Archive"]
)

st.markdown("---")
st.subheader("Export Options")

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Export as CSV")
    if export_option == "Net Worth History":
        df_export = pd.DataFrame(data["net_worth"])
    elif export_option == "Investment Portfolio":
        df_export = pd.DataFrame(data["investments"])
    elif export_option == "Liabilities & Debt Ledger":
        df_export = pd.DataFrame(data["liabilities"])
    else:
        df_export = pd.DataFrame(data["net_worth"]) # Master fallback
        
    csv_data = df_export.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV File",
        data=csv_data,
        file_name=f"{export_option.lower().replace(' ', '_')}_export.csv",
        mime="text/csv"
    )

with col2:
    st.markdown("##### Export as JSON")
    json_data = json.dumps(data, indent=4)
    st.download_button(
        label="Download JSON Archive",
        data=json_data,
        file_name="financial_master_archive.json",
        mime="application/json"
    )

st.markdown("---")
st.info("**Backup Insight:** Regularly downloading local backups of your financial tracking data guarantees full data sovereignty and uninterrupted historical records.")