import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mutual Fund Overlap Analyzer", page_icon="🔄", layout="wide")
st.title("🔄 Mutual Fund & ETF Overlap Analyzer")

st.markdown("Analyze stock holdings overlap between popular Indian mutual funds and index ETFs to eliminate portfolio redundancy.")

@st.cache_data
def get_fund_holdings():
    return {
        "Nippon India Nifty 50 BeES": ["Reliance Industries", "TCS", "HDFC Bank", "Infosys", "ITC", "HUL", "L&T", "Bharti Airtel"],
        "Axis Bluechip Fund": ["TCS", "HDFC Bank", "Infosys", "ICICI Bank", "L&T", "Axis Bank", "Bharti Airtel"],
        "SBI Large & Midcap Fund": ["Reliance Industries", "HDFC Bank", "State Bank of India", "L&T", "ITC", "Tata Motors", "Infosys"]
    }

funds = get_fund_holdings()

st.markdown("---")
st.subheader("Select Funds to Compare")

c1, c2 = st.columns(2)
with c1:
    fund_a = st.selectbox("Fund A", list(funds.keys()), index=0)
with c2:
    fund_b = st.selectbox("Fund B", list(funds.keys()), index=1)

holdings_a = set(funds[fund_a])
holdings_b = set(funds[fund_b])

common_stocks = holdings_a.intersection(holdings_b)
total_unique = holdings_a.union(holdings_b)
overlap_percentage = (len(common_stocks) / len(total_unique)) * 100 if total_unique else 0

st.markdown("---")
st.subheader("Overlap Analysis Results")

m1, m2, m3 = st.columns(3)
m1.metric("Shared Holdings Count", len(common_stocks))
m2.metric("Portfolio Overlap Score", f"{overlap_percentage:.1f}%")
m3.metric("Combined Unique Stocks", len(total_unique))

st.markdown("---")
st.subheader("Detailed Stock Overlap Breakdown")

overlap_df = pd.DataFrame({
    "Stock Name": list(total_unique),
    f"In {fund_a}": [stock in holdings_a for stock in total_unique],
    f"In {fund_b}": [stock in holdings_b for stock in total_unique],
    "Status": ["Shared Overlap" if stock in common_stocks else "Unique to One Fund" for stock in total_unique]
})

st.dataframe(overlap_df, use_container_width=True)

st.markdown("---")
st.info("**Diversification Tip:** An overlap score above 50-60% typically indicates redundant holdings, meaning owning both funds provides limited incremental diversification.")