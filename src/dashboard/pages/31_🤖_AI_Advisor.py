import streamlit as st

st.set_page_config(page_title="AI Financial Advisor", page_icon="🤖", layout="wide")
st.title("🤖 AI Financial Advisor & Chat Hub")

st.markdown("Ask questions regarding your investments, asset allocation, tax planning, and financial goals.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your AI financial collaborator. How can I help you optimize your portfolio or plan your financial goals today?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask about asset allocation, taxes, retirement, or budgeting..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response based on query keywords
    response = ""
    prompt_lower = prompt.lower()
    
    if "tax" in prompt_lower:
        response = "Based on current Indian tax regulations under the new tax regime, optimizing deductions under Section 80CCD(1B) for NPS and utilizing equity long-term capital gains (LTCG) tax exemptions up to ₹1.25 lakh can significantly lower your annual tax liability."
    elif "retire" in prompt_lower or "retirement" in prompt_lower:
        response = "To build a robust retirement corpus, aiming for a 25x to 30x multiple of your annual post-retirement expenses while leveraging equity mutual funds through a disciplined SIP approach is standard industry practice."
    elif "emergency" in prompt_lower:
        response = "It is recommended to keep 6 months of essential living expenses in liquid instruments like high-yield sweep-in accounts or liquid mutual funds."
    else:
        response = f"That is a great question regarding '{prompt}'. To give you the most accurate financial guidance, make sure your assets, liabilities, and monthly cash flows are updated across the respective dashboard modules!"

    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.info("**AI Advisor Tip:** You can ask specific questions about your portfolio diversification, risk appetite, or debt payoff strategies anytime.")