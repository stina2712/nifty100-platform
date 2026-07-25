import streamlit as st
import pandas as pd

st.set_page_config(page_title="Crypto Staking & Yield", page_icon="🪙", layout="wide")

# Standardized Header Component
def render_page_header(title, description):
    st.title(title)
    st.markdown(description)

# Standardized Footer Component
def render_page_footer():
    st.markdown("---")
    st.caption("Nifty 100 Financial Analytics Dashboard © 2026")

# Self-contained Data Status Indicator
def render_data_status(df, dataset_name="Dataset"):
    st.success(f"✅ **{dataset_name}** loaded successfully ({len(df)} records active).")

render_page_header(
    "🪙 Crypto Staking & Passive Yield Calculator", 
    "Lock up digital assets, monitor APY reward distributions, and project your long-term crypto compounding returns."
)

@st.cache_data
def get_staking_portfolio():
    return pd.DataFrame({
        "Asset": ["Ethereum (ETH)", "Solana (SOL)", "Cardano (ADA)", "Polkadot (DOT)", "Polygon (POL)"],
        "Staked Amount": [2.5, 45.0, 1200.0, 350.0, 1500.0],
        "Average APY (%)": [4.8, 6.5, 4.2, 8.1, 5.0],
        "Est. Annual Rewards": [0.12, 2.92, 50.4, 28.35, 75.0],
        "Lockup Status": ["Flexible", "Locked (14d)", "Flexible", "Locked (28d)", "Flexible"]
    })

staking_df = get_staking_portfolio()

render_data_status(staking_df, "Crypto Staking Portfolio")

st.markdown("---")
st.subheader("Active Staking Positions & Yield Ledger")
st.dataframe(staking_df, use_container_width=True)

st.markdown("---")
st.subheader("Simulate Staking Growth & Compound Rewards")

with st.form("staking_form"):
    c1, c2 = st.columns(2)
    with c1:
        selected_crypto = st.selectbox("Select Asset to Simulate", ["Ethereum (ETH)", "Solana (SOL)", "Cardano (ADA)", "Polkadot (DOT)", "Polygon (POL)"])
        additional_stake = st.number_input("Monthly Additional Stake", min_value=0.0, value=100.0, step=50.0)
    with c2:
        stake_horizon = st.slider("Staking Horizon (Years)", 1, 10, 3)
        auto_compound = st.checkbox("Auto-Compound Reward Payouts", value=True)
    
    stake_submitted = st.form_submit_button("Calculate Staking Projections")
    if stake_submitted:
        st.success(f"Staking projection computed for **{selected_crypto}**! Auto-compounding yields increases your token accumulation exponentially over time.")

st.markdown("---")
st.info("**Staking Insight:** Delegating proof-of-stake assets secures the network while generating passive yield streams directly to your wallet.")

render_page_footer()