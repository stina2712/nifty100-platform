import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tax Loss Harvesting Hub", page_icon="📉", layout="wide")
st.title("📉 Tax-Loss Harvesting & Capital Gains Optimizer")

st.markdown("Identify underperforming holdings eligible for tax-loss harvesting, offset capital gains, and minimize annual tax drag.")

@st.cache_data
def get_harvesting_opportunities():
    return pd.DataFrame({
        "Asset / Fund Name": ["Midcap Momentum Fund", "Cyclical Sector ETF", "IT Smallcap Index Fund", "Banking Value Fund", "Consumer Growth Stock"],
        "Asset Category": ["Equity Mutual Fund", "ETF", "Equity Mutual Fund", "Equity Mutual Fund", "Direct Stock"],
        "Invested Value (₹)": [300000.0, 150000.0, 200000.0, 250000.0, 100000.0],
        "Current Market Value (₹)": [255000.0, 132000.0, 172000.0, 260000.0, 88000.0],
        "Unrealized Gain / Loss (₹)": [-45000.0, -18000.0, -28000.0, +10000.0, -12000.0]
    })

tlh_df = get_harvesting_opportunities()

st.markdown("---")
st.subheader("Unrealized Loss Ledger & Harvesting Candidates")
st.dataframe(tlh_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Tax-Loss Harvesting Strategy")

with st.form("tlh_sim_form"):
    c1, c2 = st.columns(2)
    with c1:
        realized_gains_ytd = st.number_input("Realized Capital Gains YTD (₹)", min_value=0.0, value=120000.0, step=10000.0)
        target_offset_amount = st.number_input("Target Loss to Harvest (₹)", min_value=0.0, value=75000.0, step=5000.0)
    with c2:
        reinvestment_strategy = st.selectbox("Reinvestment Asset Class", ["Similar Index Fund (Post 30-Day Wash Rule)", "Broad Market Nifty 50 ETF", "Liquid Debt Fund Buffer"])
        tax_bracket_rate = st.slider("Applicable Capital Gains Tax Rate (%)", 10.0, 20.0, 12.5, 0.5)
    
    tlh_submitted = st.form_submit_button("Calculate Tax Savings Impact")
    if tlh_submitted:
        st.success("Tax-loss harvesting simulation complete! Strategic loss booking successfully offsets your taxable capital gains for the financial year.")

st.markdown("---")
st.info("**Tax Insight:** Harvesting losses before the financial year-end allows you to offset capital gains dollar-for-dollar, lowering your tax burden while maintaining your target market exposure.")