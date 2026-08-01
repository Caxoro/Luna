import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

if "luna_messages" not in st.session_state:
    st.session_state.luna_messages = []
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Luna - Assitente Virtual")
mensagem = st.chat_input("Digite sua mensagem para Luna")
interaction = client.interactions.create(
    model="gemini-3.5-flash", 
    input=mensagem,
    previous_interaction_id=st.session_state.messages.id,
    previous_interaction_id=st.session_state.luna_messages.id,
)
if mensagem:
    st.session_state.messages.append(mensagem)
    st.session_state.luna_messages.append(interaction.output_text)
    for mens in st.session_state.messages:
        st.chat_message("user").write(mensagem)
        
    for ai in st.session_state.luna_messages:
        st.chat_message("ai").write(interaction.output_text)
    
    
