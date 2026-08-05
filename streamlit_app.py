import streamlit as st
import io
from google import genai
from google.genai import types

st.title("🌙 Luna - Assitente Virtual")

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

mensagem = st.chat_input("Digite sua mensagem para Luna",
                         accept_file=True,
                         file_type=["jpg", "jpeg", "png"],)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "historico" not in st.session_state:
    st.session_state.historico = []

for h in st.session_state.messages:
    with st.chat_message(h["role"]):
        st.write(h["content"])

if mensagem:
    with st.chat_message("user"):
        st.write("Usuário: ",mensagem["text"])
        st.session_state.messages.append({"role": "user","content": mensagem})
        st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": mensagem}]})
        if mensagem["files"] != None:
            imagem = mensagem.files
            bytes_imagem = imagem.read()
            st.write(bytes_imagem)
            imagem_validada_gemini = types.Part.from_bytes(
                data=bytes_imagem,
                mime_type=imagem.type
            )
            st.session_state.historico.append(imagem_validada_gemini)
        else:
            mensagem["files"] = None
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
        st.write("Luna: ", interaction.steps[-1].content[0].text)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": interaction.output_text}]})                         
    

