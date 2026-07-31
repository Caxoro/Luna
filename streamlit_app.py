import streamlit as st
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")

if "luna_messages" not in st.session_state:
    st.session_state.luna_messages = []
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Luna - Assitente Virtual")
mensagem = st.chat_input("Digite sua mensagem para Luna")
if mensagem:
    st.session_state.messages.append(mensagem)
    for mens in st.session_state.messages:
        st.chat_message("user").write(mens)
    
    
