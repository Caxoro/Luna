import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Luna - Assitente Virtual")
mensagem = st.chat_input("Digite sua mensagem para Luna")
st.session_state.messages.append(mensagem)
if st.session_state.messages != "":
    for mens in st.session_state.messages:
        st.write(mens)
    
    
