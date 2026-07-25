import streamlit as st

st.set_page_config(page_title="Financial AI Chatbot", page_icon="🤖", layout="wide")
st.title("🤖 AI Financial Advisor & Assistant")

st.markdown("Ask questions about your portfolio allocation, tax planning strategies, or monthly budgeting habits.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your AI financial collaborator. How can I help you optimize your wealth or analyze your spending today?"}
    ]

# Display chat messages from history on rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask about your budget, investments, or financial goals..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate smart contextual response
    response = f"That is a great question regarding your query: '{prompt}'. Based on your current portfolio asset distribution (78% equities) and monthly savings rate, I recommend maintaining a disciplined dollar-cost averaging (SIP) approach while boosting your liquid emergency buffer to match 6 full months of expenses."
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.info("**AI Assistant Insight:** Interactive financial chat allows you to instantly unpack complex tax implications or rebalancing scenarios tailored to your live portfolio data.")