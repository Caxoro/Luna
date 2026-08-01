import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

mensagem = st.chat_input("Digite sua mensagem para Luna")

previous_id = None

interaction = client.interactions.create(
        model="gemini-3.5-flash", 
        input=mensagem,
        previous_interaction_id=previous_id,
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "mensagem" not in st.session_state:
    st.session_state.mensagem = mensagem
if "ai" not in st.session_state:
    st.session_state.ai = interaction.output_text

st.title("🌙 Luna - Assitente Virtual")

if mensagem:
    st.session_state.messages.append(mensagem)
    st.chat_message("user").write(st.session_state.mensagem)
    st.session_state.messages.append(interaction.output_text)
    st.chat_message("ai").write(st.session_state.ai)
    
    
