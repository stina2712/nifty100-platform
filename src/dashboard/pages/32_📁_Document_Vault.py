import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Document Vault", page_icon="📁", layout="wide")
st.title("📁 Secure Financial Document & Vault Manager")

st.markdown("Track and manage all your vital financial documents, policies, deeds, and upcoming renewal deadlines in one secure hub.")

@st.cache_data
def get_vault_documents():
    return pd.DataFrame({
        "Document Name": ["Term Life Policy Bond", "Health Insurance Floater", "Property Deed (Home)", "Vehicle Registration (RC)", "Last Will & Testament"],
        "Category": ["Insurance", "Insurance", "Real Estate", "Legal / Asset", "Estate Planning"],
        "Storage Location": ["Digital Vault / Cloud", "Digital Vault / Cloud", "Bank Locker #402", "Home Document Folder", "Secure Safe"],
        "Renewal / Expiry Date": ["2045-05-12", "2027-03-15", "Permanent", "2028-11-20", "Reviewed Annual"],
        "Status": ["Valid", "Valid", "Secure", "Valid", "Up-to-Date"]
    })

vault_df = get_vault_documents()

st.markdown("---")
st.subheader("Registered Financial Documents")
st.dataframe(vault_df, use_container_width=True)

st.markdown("---")
st.subheader("Vault Summary & Storage Statistics")

m1, m2, m3 = st.columns(3)
m1.metric("Total Tracked Documents", len(vault_df))
m2.metric("Storage Security Status", "Encrypted & Secure")
m3.metric("Action Required Renewals", "0 Pending")

st.markdown("---")
st.subheader("Document Distribution by Category")
fig = px.pie(
    vault_df,
    names="Category",
    title="Document Portfolio Breakdown",
    hole=0.4
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Vault Insight:** Keeping a digital encrypted record of vital insurance policies and property deeds alongside physical copies in a bank locker ensures seamless accessibility for family members during emergencies.")