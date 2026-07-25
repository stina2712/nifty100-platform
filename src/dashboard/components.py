import streamlit as st

def render_page_header(title: str, description: str = None):
    """
    Renders a consistent, professional header for any dashboard page.
    """
    st.title(title)
    if description:
        st.markdown(f"*{description}*")
    st.divider()

def render_page_footer():
    """
    Renders a consistent footer across dashboard pages.
    """
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 0.85em;'>"
        "Nifty100 Analytics Dashboard | Powered by Streamlit & SQLite"
        "</div>",
        unsafe_allow_html=True
    )