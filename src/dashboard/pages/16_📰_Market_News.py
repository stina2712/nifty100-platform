import streamlit as st
import pandas as pd

st.set_page_config(page_title="Market News & Sentiment", page_icon="📰", layout="wide")
st.title("📰 Financial News & Sentiment Analyzer")

st.markdown("Track real-time market news headlines, automated NLP sentiment polarity scores, and corporate earnings announcements.")

@st.cache_data
def get_news_feed():
    return pd.DataFrame({
        "timestamp": ["2026-07-24 14:30", "2026-07-24 12:15", "2026-07-24 10:00", "2026-07-23 16:45"],
        "company_or_sector": ["Tata Consultancy Services", "HDFC Bank", "Reliance Industries", "ITC"],
        "headline": [
            "TCS secures multi-million dollar digital transformation deal in Europe",
            "HDFC Bank reports strong credit growth and stable asset quality in Q1",
            "Reliance announces new strategic green energy expansion timeline",
            "ITC consumer goods segment registers steady rural demand recovery"
        ],
        "sentiment": ["Bullish (+0.82)", "Bullish (+0.75)", "Bullish (+0.65)", "Neutral (+0.10)"],
        "source": ["Economic Times", "Moneycontrol", "Mint", "Business Standard"]
    })

df = get_news_feed()

st.markdown("---")
st.subheader("Filter News Feed")
selected_sector = st.selectbox("Filter by Company / Sector", ["All Feeds"] + df["company_or_sector"].unique().tolist())

if selected_sector != "All Feeds":
    display_df = df[df["company_or_sector"] == selected_sector].copy()
else:
    display_df = df.copy()

st.markdown("---")
st.subheader("Live Headline Feed & Sentiment")
for idx, row in display_df.iterrows():
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**{row['headline']}**")
            st.caption(f"Source: {row['source']} | Time: {row['timestamp']}")
        with col2:
            st.markdown(f"`{row['sentiment']}`")
        st.divider()