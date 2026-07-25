import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crypto Staking Calculator", page_icon="🪙", layout="wide")
st.title("🪙 Crypto & Web3 Staking Yield Calculator")

st.markdown("Calculate staking rewards, project compound yields across Layer-1 tokens, and track crypto passive income.")

@st.cache_data
def get_staking_portfolio():
    return pd.DataFrame({
        "Token Asset": ["Ethereum (ETH)", "Solana (SOL)", "Polygon (POL)", "Cosmos (ATOM)", "USDC Stablecoin"],
        "Staked Quantity": [2.5, 35.0, 1500.0, 45.0, 2500.0],
        "Staking APY (%)": [3.8, 6.5, 5.2, 14.5, 8.0],
        "Lockup Period": ["Liquid Staking", "3-Day Unbonding", "Unbonded", "21-Day Unbonding", "Flexible"],
        "Estimated Annual Yield (Tokens)": [0.095, 2.275, 78.0, 6.525, 200.0]
    })

stake_df = get_staking_portfolio()

st.markdown("---")
st.subheader("Active Crypto Staking Positions")
st.dataframe(stake_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Compound Staking Yields")

with st.form("staking_form"):
    c1, c2 = st.columns(2)
    with c1:
        token_choice = st.selectbox("Select Token for Simulation", ["Ethereum (ETH)", "Solana (SOL)", "Polygon (POL)", "Cosmos (ATOM)", "USDC Stablecoin"])
        additional_stake = st.number_input("Additional Tokens to Stake", min_value=0.0, value=10.0, step=1.0)
    with c2:
        staking_horizon_years = st.slider("Staking Horizon (Years)", 1, 5, 2)
        compound_frequency = st.selectbox("Reward Compounding Frequency", ["Daily Compound", "Weekly Compound", "Monthly Compound"])
    
    stake_submitted = st.form_submit_button("Calculate Staking Growth")
    if stake_submitted:
        st.success(f"Staking simulation complete for **{token_choice}**! Compounding rewards over {staking_horizon_years} years significantly maximizes your crypto accumulation.")

st.markdown("---")
st.info("**Staking Insight:** Delegating proof-of-stake tokens to secure network validators allows you to earn passive yields while maintaining long-term ownership of your digital assets.")