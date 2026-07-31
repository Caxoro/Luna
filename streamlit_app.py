import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Bem vindo ao chat Luna")
container = st.container(height=600)
mensagem = st.chat_input("Digite sua mensagem para Luna")

if mensagem != "":
    
    st.session_state.messages.append(mensagem)
    for mens in st.session_state.messages:
        container.chat_message("user").write(mens)
    
    
