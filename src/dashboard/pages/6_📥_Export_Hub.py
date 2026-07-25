import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Export & Reporting Hub", page_icon="📥", layout="wide")
st.title("📥 Export & Professional Reporting Hub")

@st.cache_data
def get_export_dataset():
    return pd.DataFrame({
        "company_id": [1, 2, 3, 4, 5, 6, 7, 8],
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

df = get_export_dataset()

st.subheader("Select Dataset to Export")
export_type = st.radio("Choose Report Format", ["Full Nifty Screener Dataset", "High ROCE Value Picks"])

if export_type == "Full Nifty Screener Dataset":
    export_df = df
else:
    export_df = df[(df['roce'] >= 15.0) & (df['debt_to_equity'] <= 0.5)]

st.markdown("---")
st.dataframe(export_df, use_container_width=True)

st.markdown("---")
st.subheader("Download Options")

col1, col2 = st.columns(2)

# CSV Export
csv_data = export_df.to_csv(index=False).encode('utf-8')
with col1:
    st.download_button(
        label="📥 Download as CSV",
        data=csv_data,
        file_name="nifty_screener_report.csv",
        mime="text/csv",
        type="primary"
    )

# Excel Export using BytesIO
output = io.BytesIO()
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    export_df.to_excel(writer, index=False, sheet_name='Screener_Results')
excel_data = output.getvalue()

with col2:
    st.download_button(
        label="📊 Download as Excel (.xlsx)",
        data=excel_data,
        file_name="nifty_screener_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        type="primary"
    )