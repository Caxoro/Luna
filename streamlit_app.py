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
        st.session_state.messages.append({"role": "user","content": mensagem})
        st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": mensagem}]})
    with st.chat_message("ai"):
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            system_instruction="Voce é luna uma assistente virtual gentil e bem humana, voce gosta da cor azul, e seu criador se chama Emerson"
            "voce pode responder de maneira informal e usar girias, evite escrever textos muito longos e sempre que possivel resuma boa parte das respostas",
            store=False,
            input=st.session_state.historico,
        )
        for m in interaction.steps:
            st.session_state.historico.append(m.model_dump())
            st.write(m)
        
        st.write(interaction.steps[-1].content[0].text)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": interaction.output_text}]})                         
    

