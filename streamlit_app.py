import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

if "messages" not in st.session_state:
    st.session_state.messages = []

previous_id = None

st.title("🌙 Luna - Assitente Virtual")
mensagem = st.chat_input("Digite sua mensagem para Luna")

if mensagem:
    st.session_state.messages.append(mensagem)
    interaction = client.interactions.create(
        model="gemini-3.5-flash", 
        input=mensagem,
        previous_interaction_id=previous_id,
    )
    st.session_state.messages.append(interaction.output_text)
    for mens in st.session_state.messages:
        st.chat_message("user").write(mens[0])
        st.chat_message("ai").write(ai[1])
    
    
