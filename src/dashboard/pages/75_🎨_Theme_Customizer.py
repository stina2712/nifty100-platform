import streamlit as st

st.set_page_config(page_title="Theme & UI Customizer", page_icon="🎨", layout="wide")
st.title("🎨 Dashboard Theme & UI Customizer")

st.markdown("Personalize your financial command center's appearance, sidebar layouts, default currencies, and notification settings.")

with st.form("theme_form"):
    c1, c2 = st.columns(2)
    with c1:
        color_theme = st.selectbox("Dashboard Accent Theme", ["Emerald Wealth (Green)", "Modern Dark & Gold", "Classic Corporate Navy", "Minimalist Slate"])
        default_currency = st.selectbox("Default Display Currency", ["INR (₹)", "USD ($)", "EUR (€)", "GBP (£)"])
    with c2:
        compact_mode = st.checkbox("Enable Compact Table Views", value=False)
        auto_refresh_data = st.checkbox("Enable Live Market Auto-Refresh", value=True)
    
    theme_submitted = st.form_submit_button("Save Dashboard Preferences")
    if theme_submitted:
        st.success("Dashboard preferences successfully saved! Your UI customization settings have been updated.")

st.markdown("---")
st.info("**Customization Insight:** Tailoring your dashboard layout and currency preference ensures maximum focus on the financial metrics that matter most to your strategy.")