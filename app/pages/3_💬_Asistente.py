import time
import os
import joblib
import streamlit as st
import google.generativeai as genai
from utils import logo

# Obtiene la api key de google generative ai del archivo secrets.toml
genai.configure(api_key=st.secrets["google"]["api_key"])


# Configuración de la pagina
st.set_page_config(
    page_title="Asistente Virtual",
    page_icon="💬",
    menu_items={
    "Get help": "https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki",
    "Report a bug": "https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/issues/new",
    "About": """
        ## Yoogle
        
        **GitHub**: https://github.com/Insights-Labs-Consultant-Agency
    """
    }
)

# Carga el logo al sidebar
logo()

# Inicializa un nuevo chat
new_chat_id = f'{time.time()}'
MODEL_ROLE = 'ai'
AI_AVATAR_ICON = '✨'

# Crea el directorio data/ si no existe
try:
    os.mkdir('data/')
except:
    # Si el directorio ya existe
    pass

# Carga los mensajes del chat (si estan disponibles)
try:
    past_chats: dict = joblib.load('data/past_chats_list')
except:
    past_chats = {}

# Permite al sidebar mostrar una lista de chats anteriores
with st.sidebar:
    st.write('# Historial')
    if st.session_state.get('chat_id') is None:
        st.session_state.chat_id = st.selectbox(
            label='Elige un chat anterior',
            options=[new_chat_id] + list(past_chats.keys()),
            format_func=lambda x: past_chats.get(x, 'Nuevo chat'),
            placeholder='_',
        )
    else:
        # Esto sucederá la primera vez que llegue la respuesta de la IA
        st.session_state.chat_id = st.selectbox(
            label='Elige un chat anterior',
            options=[new_chat_id, st.session_state.chat_id] + list(past_chats.keys()),
            index=1,
            format_func=lambda x: past_chats.get(x, 'Nuevo chat' if x != st.session_state.chat_id else st.session_state.chat_title),
            placeholder='_',
        )
    # Guarda nuevos chats después de que se haya enviado un mensaje a la IA
    # TODO: Dar al usuario la oportunidad de nombrar el chat
    st.session_state.chat_title = f'ChatSession-{st.session_state.chat_id}'

st.title("💬 Asistente Virtual")
st.caption("🚀 powered by Gemini Pro")

# # Historial de chat (permite hacer múltiples preguntas))
try:
    st.session_state.messages = joblib.load(
        f'data/{st.session_state.chat_id}-st_messages'
    )
    st.session_state.gemini_history = joblib.load(
        f'data/{st.session_state.chat_id}-gemini_messages'
    )
    print('old cache')
except:
    st.session_state.messages = []
    st.session_state.gemini_history = []
    print('new_cache made')
st.session_state.model = genai.GenerativeModel('gemini-pro')
st.session_state.chat = st.session_state.model.start_chat(
    history=st.session_state.gemini_history,
)

# Muestra el historial de mensajes del chat al volver a ejecutar la aplicación
for message in st.session_state.messages:
    with st.chat_message(
        name=message['role'],
        avatar=message.get('avatar'),
    ):
        st.markdown(message['content'])

# Reacciona al input del usuario
if prompt := st.chat_input('Tu mensaje aquí...'):
    # Almacena el chat
    if st.session_state.chat_id not in past_chats.keys():
        past_chats[st.session_state.chat_id] = st.session_state.chat_title
        joblib.dump(past_chats, 'data/past_chats_list')
    # Mostrar el mensaje del usuario en el chat container
    with st.chat_message('user'):
        st.markdown(prompt)
    # Agrega el mensaje del usuario al historial
    st.session_state.messages.append(
        dict(
            role='user',
            content=prompt,
        )
    )
    # Envia el mensaje al chat y obtiene la respuesta del modelo 
    response = st.session_state.chat.send_message(
        prompt,
        stream=True,
    )
    # Muesta la respuesta del modelo en el chat container 
    with st.chat_message(
        name=MODEL_ROLE,
        avatar=AI_AVATAR_ICON,
    ):
        message_placeholder = st.empty()
        full_response = ''
        assistant_response = response
        # Genera texto por fragmentos
        for chunk in response:
            # Simula flujo de texto como chatGPT
            # TODO: Agregar validación por si la API se detiene a mitad de camino y le falta 'texto' a la respuesta 
            for ch in chunk.text.split(' '):
                full_response += ch + ' '
                time.sleep(0.05)
                # Reescribe con un cursor al final
                message_placeholder.write(full_response + '▌')
        # Escribe el mensaje completo con placeholder
        message_placeholder.write(full_response)

    # Agrega el mensaje del modelo al historial del chat
    st.session_state.messages.append(
        dict(
            role=MODEL_ROLE,
            content=st.session_state.chat.history[-1].parts[0].text,
            avatar=AI_AVATAR_ICON,
        )
    )
    st.session_state.gemini_history = st.session_state.chat.history
    # Guarda el archivo
    joblib.dump(
        st.session_state.messages,
        f'data/{st.session_state.chat_id}-st_messages',
    )
    joblib.dump(
        st.session_state.gemini_history,
        f'data/{st.session_state.chat_id}-gemini_messages',
    )