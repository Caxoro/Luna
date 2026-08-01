import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

if "luna_messages" not in st.session_state:
    st.session_state.luna_messages = []
if "messages" not in st.session_state:
    st.session_state.messages = []

previous_id = None

st.title("🌙 Luna - Assitente Virtual")
mensagem = st.chat_input("Digite sua mensagem para Luna")
if mensagem:
    st.session_state.messages.append(mensagem)
    for mens in st.session_state.messages:
        st.chat_message("user").write(mens)
        interaction = client.interactions.create(
            model="gemini-2.5-flash", 
            input=mens,
            previous_interaction_id=previous_id,
        )
    for ai in st.session_state.luna_messages:
        st.session_state.luna_messages.append(interaction.output_text)
        st.chat_message("ai").write(interaction.output_text)
    
    
