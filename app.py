
import streamlit as st
import ollama

st.set_page_config(page_title="My AI Chatbot", page_icon="🤖")

# Sidebar
with st.sidebar:
    st.title("🤖 My AI Chatbot")
    st.write("Your local AI assistant")

    models = [m.model for m in ollama.list().models]

    if not models:
        st.error("No Ollama models installed.")
        st.stop()

    selected_model = st.selectbox("Select Model", models)

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# Main screen
st.title("How can I help you?")

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask anything..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = ollama.chat(
                model=selected_model,
                messages=st.session_state.messages,
                stream=True
            )

            answer = st.write_stream(
                chunk["message"]["content"]
                for chunk in response
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            st.error(f"Error: {e}")
