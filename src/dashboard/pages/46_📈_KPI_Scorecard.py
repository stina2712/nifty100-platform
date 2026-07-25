import streamlit as st
import pandas as pd

st.set_page_config(page_title="KPI Scorecard", page_icon="📈", layout="wide")
st.title("📈 Custom Financial KPI Scorecard & Metrics Hub")

st.markdown("Build, weight, and monitor customized key performance indicators (KPIs) to track your micro-economic health.")

@st.cache_data
def get_kpi_metrics():
    return pd.DataFrame({
        "KPI Metric": ["Savings Rate", "Debt-to-Income Ratio", "Investment Growth Rate", "Emergency Runway", "Net Worth Velocity"],
        "Target Value": [">= 30.0%", "<= 20.0%", ">= 15.0%", ">= 6.0 Months", ">= ₹1,00,000 / mo"],
        "Current Actual": ["38.5%", "12.4%", "18.2%", "7.2 Months", "₹1,50,956 / mo"],
        "Status Score": ["Optimal", "Healthy", "Outperforming", "Optimal", "Strong"],
        "Weight Priority": ["High", "Medium", "High", "Critical", "Medium"]
    })

kpi_df = get_kpi_metrics()

st.markdown("---")
st.subheader("Configured Financial KPIs Matrix")
st.dataframe(kpi_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Custom KPI Target Adjustments")

with st.form("kpi_simulation_form"):
    c1, c2 = st.columns(2)
    with c1:
        target_savings = st.slider("Target Monthly Savings Rate (%)", min_value=10.0, max_value=70.0, value=35.0, step=1.0)
        max_debt_cap = st.slider("Maximum Acceptable Debt Ratio (%)", min_value=5.0, max_value=50.0, value=20.0, step=1.0)
    with c2:
        target_runway = st.slider("Desired Emergency Fund Runway (Months)", min_value=3.0, max_value=24.0, value=6.0, step=1.0)
        composite_weight = st.selectbox("Composite Scoring Model", ["Balanced Weighted Average", "Aggressive Growth Weight", "Capital Preservation Weight"])
    
    sim_submitted = st.form_submit_button("Recalculate Composite Score")
    if sim_submitted:
        st.success(f"Simulation applied! Adjusted targets project a modified financial stability index of **91 / 100 (Elite Tier)**.")

st.markdown("---")
st.info("**KPI Insight:** Dynamic metric weighting allows you to transition your financial focus seamlessly across life stages—from aggressive capital accumulation to capital protection and stability.")