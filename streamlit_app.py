import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

previous_id = None

mensagem = st.chat_input("Digite sua mensagem para Luna", key="mensagem")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "mensagem" not in st.session_state:
    st.session_state.mensagem = ""
if "ai" not in st.session_state:
    st.session_state.ai = ""

st.title("🌙 Luna - Assitente Virtual")

with st.chat_message("user"):
    if mensagem:
        st.session_state.messages.append(mensagem)
        st.session_state.mensagem = mensagem
        st.write(st.session_state.mensagem)
        with st.chat_message("ai"):
            interaction = client.interactions.create(
                model="gemini-3.5-flash", 
                input=mensagem,
                previous_interaction_id=previous_id,
            )
            st.session_state.messages.append(interaction.output_text)
            st.write(st.session_state.ai, key="ai")
    
    
