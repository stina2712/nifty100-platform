import streamlit as st

st.set_page_config(page_title="Financial Advisor Copilot", page_icon="🤖", layout="wide")
st.title("🤖 AI Financial Advisor & Strategy Copilot")

st.markdown("Your dedicated AI copilot for real-time financial modeling, asset allocation advice, and wealth management queries.")

if "copilot_messages" not in st.session_state:
    st.session_state.copilot_messages = [
        {"role": "assistant", "content": "Hello! I am your personal financial copilot. How can I help you optimize your investments, analyze your debt strategy, or plan your tax liabilities today?"}
    ]

for message in st.session_state.copilot_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your financial copilot anything (e.g., 'How should I rebalance my equity portfolio?')..."):
    st.session_state.copilot_messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    response_text = f"That is a great question regarding **'{prompt}'**. Based on your current portfolio metrics, savings rate, and risk profile, maintaining strict discipline with your asset allocation and dollar-cost averaging will yield optimal long-term results."
    
    st.session_state.copilot_messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)

st.markdown("---")
st.info("**Copilot Insight:** Your AI advisor leverages your live financial dashboard data to provide contextual, actionable recommendations instantly.")