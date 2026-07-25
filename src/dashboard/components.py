import streamlit as st

def render_page_header(title, description):
    st.title(title)
    st.markdown(description)

def render_page_footer():
    st.markdown("---")
    st.caption("Nifty 100 Financial Analytics Dashboard © 2026")