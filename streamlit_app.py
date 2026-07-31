import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Bem vindo ao chat Luna")
container = st.container(height=500)
mensagem = ""

if mensagem != "":
    mensagem = st.chat_input("Digite sua mensagem para Luna")
    st.session_state.messages.append(mensagem)
    for mens in st.session_state.messages:
        container.chat_message("user").write(mens)
    
    
