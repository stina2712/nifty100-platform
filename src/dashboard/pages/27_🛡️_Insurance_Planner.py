import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Insurance Planner", page_icon="🛡️", layout="wide")
st.title("🛡️ Insurance & Risk Coverage Planner")

st.markdown("Evaluate your life and health insurance coverage, assess coverage gaps, and secure your family's financial future.")

@st.cache_data
def get_insurance_data():
    return pd.DataFrame({
        "Policy Name": ["Term Life Cover", "Family Health Floater", "Critical Illness Cover", "Personal Accident Cover"],
        "Category": ["Life Insurance", "Health Insurance", "Health Insurance", "Accident Insurance"],
        "Sum Assured (₹)": [15000000.0, 1000000.0, 2500000.0, 5000000.0],
        "Annual Premium (₹)": [14500.0, 22000.0, 8500.0, 4500.0],
        "Status": ["Active", "Active", "Active", "Active"]
    })

ins_df = get_insurance_data()

st.markdown("---")
st.subheader("Active Insurance Portfolio")
st.dataframe(ins_df, use_container_width=True)

total_life_cover = ins_df.loc[ins_df["Category"] == "Life Insurance", "Sum Assured (₹)"].sum()
total_health_cover = ins_df.loc[ins_df["Category"] == "Health Insurance", "Sum Assured (₹)"].sum()
total_annual_premium = ins_df["Annual Premium (₹)"].sum()

st.markdown("---")
st.subheader("Human Life Value (HLV) & Coverage Assessment")

c1, c2, c3 = st.columns(3)
with c1:
    annual_income = st.number_input("Annual Income (₹)", value=1200000.0, step=100000.0)
with c2:
    current_liabilities = st.number_input("Total Liabilities/Loans (₹)", value=5000000.0, step=500000.0)
with c3:
    target_multiple = st.slider("Recommended Income Multiple", min_value=10, max_value=20, value=15)

# Recommended life cover = (Annual Income * Multiple) + Liabilities
recommended_life_cover = (annual_income * target_multiple) + current_liabilities
coverage_gap = max(0.0, recommended_life_cover - total_life_cover)

st.markdown("---")
st.subheader("Coverage Summary & Gap Analysis")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Existing Life Cover", f"₹{total_life_cover:,.2f}")
m2.metric("Recommended Target Cover", f"₹{recommended_life_cover:,.2f}")
m3.metric("Life Coverage Gap", f"₹{coverage_gap:,.2f}")
m4.metric("Total Annual Premium Outflow", f"₹{total_annual_premium:,.2f}")

st.markdown("---")
st.subheader("Insurance Portfolio Distribution")
fig = px.bar(
    ins_df,
    x="Policy Name",
    y="Sum Assured (₹)",
    color="Category",
    title="Sum Assured Breakdown Across Policies",
    text_auto=True
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.info("**Insurance Insight:** A standard rule of thumb is to maintain a life insurance cover equal to 15x your annual income plus outstanding liabilities to ensure complete financial security for dependents.")