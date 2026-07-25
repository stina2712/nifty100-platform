import streamlit as st
import pandas as pd

st.set_page_config(page_title="Audit Logs & Activity", page_icon="📜", layout="wide")
st.title("📜 User Activity & Security Audit Logs")

st.markdown("Track and review all system actions, portfolio edits, security logins, and data exports across your financial dashboard.")

@st.cache_data
def get_audit_logs():
    return pd.DataFrame({
        "Timestamp": ["2026-07-25 09:30:12", "2026-07-24 16:45:00", "2026-07-22 11:15:33", "2026-07-20 14:10:05", "2026-07-18 08:22:49"],
        "Activity Category": ["Data Export", "Portfolio Rebalance", "Security Login", "Document Vault", "Expense Update"],
        "Description": ["Exported executive financial report CSV", "Adjusted equity allocation weights to 65%", "Successful login from authorized device", "Uploaded new term insurance policy deed", "Updated monthly discretionary budget cap"],
        "Status": ["Success", "Success", "Verified", "Encrypted", "Completed"]
    })

audit_df = get_audit_logs()

st.markdown("---")
st.subheader("System Activity History")
st.dataframe(audit_df, use_container_width=True)

st.markdown("---")
st.subheader("Filter Audit Logs")

with st.form("audit_filter_form"):
    c1, c2 = st.columns(2)
    with c1:
        log_category = st.selectbox("Filter Category", ["All Categories", "Data Export", "Portfolio Rebalance", "Security Login", "Document Vault", "Expense Update"])
        date_range = st.selectbox("Timeframe Window", ["Last 7 Days", "Last 30 Days", "Year to Date", "All Time"])
    with c2:
        export_logs = st.checkbox("Download Audit Trail Report", value=False)
        security_alerts = st.checkbox("Enable Unauthorized Access Alerts", value=True)
    
    audit_submitted = st.form_submit_button("Apply Audit Filter")
    if audit_submitted:
        st.success(f"Audit log filtered successfully for category: **{log_category}**.")

st.markdown("---")
st.info("**Audit Insight:** Maintaining an immutable log of all portfolio updates and security events ensures complete accountability and trackability of your financial data.")