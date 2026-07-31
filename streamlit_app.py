import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Luna - Assitente Virtual")
mensagem = messages.append(st.chat_input("Digite sua mensagem para Luna"))
if mensagem != "":
    for mens in st.session_state.messages:
        st.write(mensagem)
    
    
