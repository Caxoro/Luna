import streamlit as st

st.title("🌙 Bem vindo ao chat Luna")
mensagem = st.chat_input("Digite sua mensagem para Luna")
if mensagem != "":
   st.write("Voce: ",mensagem)
