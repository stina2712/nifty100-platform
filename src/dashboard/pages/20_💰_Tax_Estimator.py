import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tax Liability Estimator", page_icon="💰", layout="wide")
st.title("💰 Capital Gains & Tax Liability Estimator")

st.markdown("Estimate your short-term and long-term capital gains tax liabilities on equity investments and mutual fund redemptions.")

st.markdown("---")
st.subheader("Transaction Inputs")

c1, c2, c3 = st.columns(3)
with c1:
    asset_type = st.selectbox("Asset Class", ["Equity / Equity Mutual Funds", "Debt Mutual Funds", "Real Estate"])
with c2:
    purchase_value = st.number_input("Total Purchase Value (₹)", value=500000.0, step=50000.0)
with c3:
    sale_value = st.number_input("Total Sale Value (₹)", value=750000.0, step=50000.0)

c4, c5 = st.columns(2)
with c4:
    holding_period_months = st.slider("Holding Period (Months)", min_value=1, max_value=60, value=14)
with c5:
    tax_regime = st.selectbox("Tax Regime", ["New Tax Regime", "Old Tax Regime"])

# Calculations
capital_gain = sale_value - purchase_value

# Determine LTCG vs STCG based on asset class and holding period
# Equity threshold: > 12 months for LTCG
# Debt/Real estate threshold: > 24 or 36 months, simplified here as 12 months for equity benchmark
is_ltcg = False
if "Equity" in asset_type and holding_period_months > 12:
    is_ltcg = True
elif "Debt" in asset_type and holding_period_months > 36:
    is_ltcg = True

gain_type = "Long-Term Capital Gain (LTCG)" if is_ltcg else "Short-Term Capital Gain (STCG)"

# Tax rate logic (Indian Tax System benchmark approximation)
if "Equity" in asset_type:
    tax_rate = 0.125 if is_ltcg else 0.20  # Updated Union Budget benchmarks
    exemption = 125000.0 if is_ltcg else 0.0
else:
    tax_rate = 0.20 if is_ltcg else 0.30
    exemption = 0.0

taxable_gain = max(0.0, capital_gain - exemption)
estimated_tax = taxable_gain * tax_rate

st.markdown("---")
st.subheader("Tax Computation Summary")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Gross Capital Gain", f"₹{capital_gain:,.2f}")
m2.metric("Classification", gain_type)
m3.metric("Applicable Tax Rate", f"{tax_rate * 100:.1f}%")
m4.metric("Estimated Tax Liability", f"₹{estimated_tax:,.2f}")

st.markdown("---")
st.subheader("Tax Optimization Breakdown")

summary_df = pd.DataFrame({
    "Metric Component": ["Purchase Price", "Sale Price", "Gross Gain", "Exemption Limit Applied", "Taxable Amount", "Estimated Tax Payable"],
    "Amount (₹)": [purchase_value, sale_value, capital_gain, exemption, taxable_gain, estimated_tax]
})

st.dataframe(summary_df, use_container_width=True)

st.markdown("---")
st.info("**Tax Planning Tip:** Holding equities for more than 12 months qualifies them for Long-Term Capital Gains (LTCG), which benefits from lower tax rates and annual exemption thresholds.")