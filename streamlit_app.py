import streamlit as st
import json
from google import genai

st.title("🌙 Luna - Assitente Virtual")

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

mensagem = st.chat_input("Digite sua mensagem para Luna")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "historico" not in st.session_state:
    st.session_state.historico = []

for h in st.session_state.messages:
    with st.chat_message(h["role"]):
        st.write(h["content"])


if mensagem:
    with st.chat_message("user"):
        st.write(mensagem)
    st.session_state.messages.append({"role": "user","content": mensagem})
    st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": mensagem}]})
    for m in st.session_state.historico:
        memoria = (f"{m}")
        st.write(memoria)
    with st.chat_message("ai"):
        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            store=False,
            input=memoria,
        )
        st.write(interaction.output_text)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    st.session_state.historico.append({"type": "luna","content": [{"type": "text", "text": interaction.output_text}]})                         
    

