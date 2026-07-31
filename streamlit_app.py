import streamlit as st

st.title("🌙 Bem vindo ao chat Luna")
messages = st.container(height=200)
mensagem = st.chat_input("Digite sua mensagem para Luna")
if mensagem != "":
   st.write("Voce: ",mensagem)
