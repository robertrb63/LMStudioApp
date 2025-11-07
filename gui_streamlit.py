import streamlit as st
import requests

# Configuración de la API local de LM Studio
API_URL = "http://localhost:1234/v1/chat/completions"
MODEL_ID = "qwen3-4b-valiant-polaris"

st.set_page_config(page_title="🤖 LM Studio Chat", layout="centered")

st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        font-size: 16px;
    }
    .stButton > button {
        font-size: 16px;
        padding: 0.5em 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 LM Studio Chat")
st.markdown("### 💬 ¿Qué quieres preguntarle a la inteligencia artificial?")

# Entrada de texto
pregunta = st.text_input("Escribe tu pregunta para el modelo:")

# Botón para enviar
if st.button("Enviar"):
    if pregunta.strip():
        data = {
            "model": MODEL_ID,
            "messages": [{"role": "user", "content": pregunta}],
            "temperature": 0.7
        }

        try:
            response = requests.post(API_URL, headers={"Content-Type": "application/json"}, json=data)
            respuesta = response.json()["choices"][0]["message"]["content"]
            st.success("Respuesta del modelo:")
            st.write(respuesta)
        except Exception as e:
            st.error(f"Error al conectar con la API: {e}")
    else:
        st.warning("Por favor, escribe una pregunta antes de enviar.")