import streamlit as st

st.set_page_config(page_title="Financial Settings", page_icon="⚙️", layout="wide")
st.title("⚙️ Platform Settings & Preferences")

st.markdown("Customize your currency display, notification preferences, user profile, and system configuration.")

st.markdown("---")
st.subheader("Regional & Currency Settings")

col1, col2 = st.columns(2)
with col1:
    currency = st.selectbox("Primary Display Currency", ["INR (₹)", "USD ($)", "EUR (€)", "GBP (£)"])
    date_format = st.selectbox("Date Format", ["DD-MM-YYYY", "MM-DD-YYYY", "YYYY-MM-DD"])
with col2:
    number_format = st.selectbox("Number Formatting Style", ["Indian (Lakhs / Crores)", "Western (Millions / Billions)"])
    fiscal_start = st.selectbox("Fiscal Year Start Month", ["April", "January"])

st.markdown("---")
st.subheader("User Profile & Security")

with st.form("profile_form"):
    p1, p2 = st.columns(2)
    with p1:
        full_name = st.text_input("Full Name", value="Aarav Sharma")
        email = st.text_input("Email Address", value="aarav.sharma@example.com")
    with p2:
        occupation = st.text_input("Primary Profession", value="Software Engineer")
        risk_profile = st.selectbox("Investment Risk Tolerance", ["Aggressive Growth", "Balanced / Moderate", "Conservative"])
    
    saved_profile = st.form_submit_button("Save Profile Settings")
    if saved_profile:
        st.success("Your profile settings have been updated successfully!")

st.markdown("---")
st.subheader("Data Management & Reset")

col_r1, col_r2 = st.columns(2)
with col_r1:
    if st.button("Clear Cache & Refresh Datasets"):
        st.cache_data.clear()
        st.success("Application cache cleared successfully!")
with col_r2:
    if st.button("Reset All Tracked Modules to Default"):
        st.warning("All mock records have been reset to initial factory states.")

st.markdown("---")
st.info("**Settings Insight:** Keeping your regional currency and risk profile aligned ensures all automated portfolio recommendations and analytics reflect your accurate financial reality.")