import streamlit as st
import openai as client

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Luna - Assitente Virtual")
mensagem = st.chat_input("Digite sua mensagem para Luna")
if mensagem:
    st.session_state.messages.append(mensagem)
    for mens in st.session_state.messages:
        st.chat_message("user").write(mens)
    
    
