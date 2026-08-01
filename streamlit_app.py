import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

previous_id = None

mensagem = st.chat_input("Digite sua mensagem para Luna")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌙 Luna - Assitente Virtual")

if mensagem:
    st.session_state.messages.append(mensagem)
    st.chat_message("user").write(mensagem)
    interaction = client.interactions.create(
        model="gemini-3.5-flash", 
        input=mensagem,
        previous_interaction_id=previous_id,
    )
    st.session_state.messages.append(interaction.output_text)
    st.chat_message("ai").write(interaction.output_text)
    
