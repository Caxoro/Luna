import streamlit as st
from google import genai

st.title("🌙 Luna - Assitente Virtual")

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

mensagem = st.chat_input("Digite sua mensagem para Luna")

if "messages" not in st.session_state:
    st.session_state.messages = []

for historico in st.session_state.messages:
    with st.chat_message(historico["role"]):
        st.write(historico["content"])

if mensagem:
    with st.chat_message("user"):
        st.write(mensagem)
    st.session_state.messages.append({"role": "user","content": mensagem})

    with st.chat_message("ai"):
       interaction = client.interactions.create(
           model="gemini-3.6-flash",
           store=false,
           input=historico,
       )
       st.write(interaction.output_text)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    
