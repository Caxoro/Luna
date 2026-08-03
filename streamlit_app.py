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
    for m in interaction.steps:
        st.session_state.historico.append(m.model_dump())
        st.write(m)
    with st.chat_message("ai"):
        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            store=False,
            input=st.session_state.historico,
        )
        st.write(interaction.steps[-1].content[0].text)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    st.session_state.historico.append({"type": "luna","content": [{"type": "text", "text": interaction.output_text}]})                         
    

