import streamlit as st

st.set_page_config(page_title="AI Financial Assistant", page_icon="🤖", layout="wide")
st.title("🤖 Nifty 100 AI Financial Assistant")

st.markdown("Ask questions about company fundamentals, valuation methodologies, portfolio allocation strategies, or general market trends.")

# Initialize chat history in session state if not present
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Nifty 100 AI investment collaborator. How can I help you analyze your portfolio or screen stocks today?"}
    ]

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask about ROCE, P/E ratios, DCF valuation, or specific stocks..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate smart contextual response
    response = ""
    lower_prompt = prompt.lower()
    
    if "roce" in lower_prompt:
        response = "ROCE (Return on Capital Employed) measures how efficiently a company uses its capital to generate profits. Higher ROCE values (typically > 15-20%) indicate strong pricing power and efficient capital allocation."
    elif "dcf" in lower_prompt or "valuation" in lower_prompt:
        response = "Discounted Cash Flow (DCF) valuation estimates the intrinsic value of a company by projecting its future free cash flows and discounting them back to present value using the Weighted Average Cost of Capital (WACC)."
    elif "portfolio" in lower_prompt:
        response = "A well-diversified portfolio across non-correlated sectors (like IT, Banking, FMCG, and Infrastructure) helps minimize blended volatility while capturing steady long-term growth."
    else:
        response = f"That's a great question regarding '{prompt}'. Based on your Nifty 100 dataset, I recommend checking the **Screening Engine** or **Peer Comparison Matrix** modules to evaluate specific fundamental criteria and ratios side-by-side."

    # Append assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)