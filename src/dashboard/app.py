import streamlit as st

st.set_page_config(
    page_title="Nifty 100 Financial Analytics Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📈 Nifty 100 Financial Analytics Platform")
st.markdown("---")

st.markdown("""
### Welcome to the Analytics Dashboard!
Use the sidebar navigation to explore different modules:

* **📊 Overview:** Key metrics, sector breakdown, and macro distributions.
* **🔍 Screener:** Interactive multi-criteria screener and preset filters.
* **📈 Company Analysis:** Deep dive into company performance trends and ratios.
""")

st.sidebar.success("Select a page above.")