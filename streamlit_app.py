import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

mensagem = st.chat_input("Digite sua mensagem para Luna")

if "messages" not in st.session_state:
    st.session_state.messages = []

for historico in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

st.title("🌙 Luna - Assitente Virtual")

if mensagem:
    with st.chat_message("user"):
        st.write(mensagem)
    st.session_state.messages.append({"role": "user","content": mensagem})

    with st.chat_message("ai"):
       interaction = client.models.generate_content(
           model="gemini-3.6-flash", 
           contents=mensagem,
           
       )
       st.write(interaction.output_text)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    
