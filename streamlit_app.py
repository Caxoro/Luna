import streamlit as st

messages = []

st.title("🌙 Bem vindo ao chat Luna")
container = st.container(height=500)
mensagem = st.chat_input("Digite sua mensagem para Luna")
with st.container:
if mensagem != "":
    messages.append(mensagem)
    for mens in messages:
        container.chat_message("user").write(mens)
