import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Real Estate Analyzer", page_icon="🏠", layout="wide")
st.title("🏠 Real Estate & REIT Investment Analyzer")

st.markdown("Evaluate direct property investments, calculate net rental yields, and analyze prominent Indian REITs.")

@st.cache_data
def get_reit_data():
    return pd.DataFrame({
        "REIT Name": ["Embassy Office Parks REIT", "Mindspace Business Parks REIT", "Brookfield India Real Estate Trust"],
        "Ticker": ["EMBASSY", "MINDSACE", "BROOKS"],
        "Unit Price (₹)": [365.50, 342.00, 268.20],
        "Dividend Yield (%)": [6.8, 6.2, 7.1],
        "Occupancy Rate (%)": [89.0, 91.5, 87.0],
        "Portfolio Type": ["Commercial Office", "Commercial Office", "Commercial Office"]
    })

reit_df = get_reit_data()

st.markdown("---")
st.subheader("Major Indian REITs Overview")
st.dataframe(reit_df, use_container_width=True)

st.markdown("---")
st.subheader("Direct Property Rental Yield Calculator")

c1, c2, c3 = st.columns(3)
with c1:
    property_price = st.number_input("Property Purchase Price (₹)", value=10000000.0, step=500000.0)
with c2:
    monthly_rent = st.number_input("Expected Monthly Rent (₹)", value=35000.0, step=5000.0)
with c3:
    annual_maintenance = st.number_input("Annual Maintenance & Taxes (₹)", value=40000.0, step=5000.0)

# Calculations
annual_rent_income = monthly_rent * 12.0
net_annual_income = annual_rent_income - annual_maintenance
gross_rental_yield = (annual_rent_income / property_price) * 100.0 if property_price > 0 else 0
net_rental_yield = (net_annual_income / property_price) * 100.0 if property_price > 0 else 0

st.markdown("---")
st.subheader("Yield Computation Summary")

m1, m2, m3 = st.columns(3)
m1.metric("Gross Rental Yield", f"{gross_rental_yield:.2f}%")
m2.metric("Net Annual Income", f"₹{net_annual_income:,.2f}")
m3.metric("Net Rental Yield", f"{net_rental_yield:.2f}%")

# Generate 10-year property appreciation projection
years = np.arange(1, 11)
appreciation_rate = 0.06
projected_values = property_price * ((1.0 + appreciation_rate) ** years)

projection_df = pd.DataFrame({
    "Year": years,
    "Projected Value (₹)": projected_values
})

st.markdown("---")
st.subheader("10-Year Property Value Appreciation Projection")
fig = px.line(
    projection_df,
    x="Year",
    y="Projected Value (₹)",
    title="Estimated Property Value Growth (6% Annual Appreciation)",
    markers=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Real Estate Insight:** While direct property offers tangible asset backing and steady rental yields, REITs provide high liquidity, professional management, and regular dividend distributions with lower capital entry barriers.")