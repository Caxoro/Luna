import streamlit as st
from google import genai

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

previous_id = None

mensagem = st.chat_input("Digite sua mensagem para Luna")

if "messages" not in st.session_state:
    st.session_state.messages = []

for historico in st.session_state.messages:
    with st.chat_message(historico["role"]):
        st.write(historico["content"])

st.title("🌙 Luna - Assitente Virtual")

if mensagem:
    with st.chat_message("user"):
        st.write(mensagem)
    st.session_state.messages.append({"role": "user","content": mensagem})

    with st.chat_message("ai"):
       interaction = client.interactions.create(
           model="gemini-3.6-flash", 
           input=mensagem,
           previous_interaction_id=previous_id,
       )
       st.write(interaction.output_text)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    
