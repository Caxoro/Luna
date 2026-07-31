import streamlit as st

messages = []

st.title("🌙 Bem vindo ao chat Luna")
container = st.container(height=500)
mensagem = ""
mensagem = st.chat_input("Digite sua mensagem para Luna")
if mensagem != "":
    mensagem += messages.append(mensagem)
    container.chat_message("user").write(mensagem)
