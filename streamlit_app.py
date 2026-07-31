import streamlit as st

messages = ["a","b","c"]

st.title("🌙 Bem vindo ao chat Luna")
container = st.container(height=500)
mensagem = st.chat_input("Digite sua mensagem para Luna")
if mensagem != "":
    messages.append(mensagem)
    
    for mens in messages:
        st.write(mens)
        container.chat_message("user").write(mens)
