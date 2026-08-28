import streamlit as st
import io
import base64
import asyncio
import edge_tts
from google import genai
from google.genai import types

st.title("🌙 Luna - Assitente Virtual")

chave = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=chave)

voice = ""
output_voice = "luna_voz.mp3"

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
        if mensagem.files != []:
            for imagem in mensagem.files:
                bytes_imagem = imagem.getvalue()
                tipo_imagem = str(imagem.type)
                image_b64 = base64.b64encode(bytes_imagem).decode("utf-8")
                st.write("Usuário: ",mensagem["text"])
                st.session_state.messages.append({"role": "user","content": mensagem.text})
      
                st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": mensagem.text},
                {
                    "type": "image",
                    "data": image_b64,
                    "mime_type": f"{tipo_imagem}",
                }]})
                mensagem.files = [""]
        else:
            mensagem.files = [""]
            st.write("Usuário: ",mensagem["text"])
            st.session_state.messages.append({"role": "user","content": mensagem.text})
            st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": mensagem.text}]})
    with st.chat_message("ai"):
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            system_instruction="Voce é luna uma assistente virtual gentil e bem humana, voce gosta da cor azul, e seu criador se chama Emerson"
            "voce pode responder de maneira informal e usar girias, evite escrever textos muito longos e sempre que possivel resuma boa parte das respostas",
            store=False,
            input=st.session_state.historico,
        )
        st.write("Luna: ", interaction.steps[-1].content[0].text)
      
        communicate = edge_tts.Communicate(interaction.steps[-1].content[0].text, voice)
        await communicate.save(output_voice)
    st.session_state.messages.append({"role": "ai","content": interaction.output_text})
    st.session_state.historico.append({"type": "user_input","content": [{"type": "text", "text": interaction.output_text}]})              
    
    

