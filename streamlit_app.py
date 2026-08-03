import streamlit as st
import json
from google import genai

st.title("🌙 Luna - Assitente Virtual")

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

mensagem = st.chat_input("Digite sua mensagem para Luna")

if "messages" not in st.session_state:
    st.session_state.messages = {}

for h in st.session_state.messages:
    h1 = st.session_state.messages.get("role")
    for a = st.session_state.messages:
        a1 = st.session_state.message.get("content")
        with st.chat_message(st.write([h1])):
            st.write(a1)

if mensagem:
    with st.chat_message("user"):
        st.write(mensagem)
    st.session_state.messages.update({"role": "user","content": mensagem})

    with st.chat_message("ai"):
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            store=False,
            input=mensagem,
        )
        st.write(interaction.output_text)
    st.session_state.messages.update({"role": "ai","content": interaction.output_text})
    
