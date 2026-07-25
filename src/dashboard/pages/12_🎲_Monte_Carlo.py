import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Monte Carlo Risk Analysis", page_icon="🎲", layout="wide")
st.title("🎲 Monte Carlo Portfolio Simulation & Risk Analysis")

st.markdown("Project potential future portfolio values and assess risk distribution over time using stochastic Monte Carlo simulations.")

st.markdown("---")
st.subheader("Simulation Parameters")

c1, c2, c3 = st.columns(3)
with c1:
    initial_investment = st.number_input("Initial Investment (₹)", value=100000.0, step=10000.0)
with c2:
    years = st.slider("Investment Horizon (Years)", min_value=1, max_value=20, value=5)
with c3:
    num_simulations = st.selectbox("Number of Simulations", [100, 500, 1000], index=1)

c4, c5 = st.columns(2)
with c4:
    expected_return = st.slider("Expected Annual Return (%)", min_value=5.0, max_value=25.0, value=12.0) / 100.0
with c5:
    volatility = st.slider("Annual Portfolio Volatility (%)", min_value=5.0, max_value=40.0, value=18.0) / 100.0

if st.button("Run Simulation", type="primary"):
    np.random.seed(42)
    days_per_year = 252
    total_days = years * days_per_year
    
    # Daily drift and volatility
    dt = 1.0 / days_per_year
    daily_drift = (expected_return - 0.5 * (volatility ** 2)) * dt
    daily_vol = volatility * np.sqrt(dt)
    
    # Generate random shocks
    random_shocks = np.random.normal(0, 1, (total_days, num_simulations))
    daily_returns = np.exp(daily_drift + daily_vol * random_shocks)
    
    # Calculate cumulative portfolio paths
    price_paths = np.zeros_like(daily_returns)
    price_paths[0] = initial_investment
    for t in range(1, total_days):
        price_paths[t] = price_paths[t - 1] * daily_returns[t]
        
    # Convert to dataframe for plotting
    days_axis = np.arange(total_days)
    paths_df = pd.DataFrame(price_paths, index=days_axis)
    
    st.markdown("---")
    st.subheader(f"Projected Wealth Paths ({num_simulations} Simulations)")
    
    # Sample subset of paths to plot for performance
    fig = px.line(
        paths_df.iloc[:, ::max(1, num_simulations // 50)],
        title=f"Monte Carlo Simulation over {years} Years",
        labels={"value": "Portfolio Value (₹)", "index": "Trading Days"}
    )
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Final value distribution statistics
    final_values = price_paths[-1]
    p10 = np.percentile(final_values, 10)
    p50 = np.percentile(final_values, 50)
    p90 = np.percentile(final_values, 90)
    
    st.markdown("---")
    st.subheader("Outcome Summary Statistics")
    m1, m2, m3 = st.columns(3)
    m1.metric("Conservative Outcome (10th Percentile)", f"₹{p10:,.2f}")
    m2.metric("Median Outcome (50th Percentile)", f"₹{p50:,.2f}")
    m3.metric("Optimistic Outcome (90th Percentile)", f"₹{p90:,.2f}")