import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page

# Logo de la página
def logo():
    add_logo("app/assets/yoogle-icon.png", height=300)

# Boton para cambiar de página 
def switch_page():
    asistente = st.button("Asistente")
    recetas = st.button("Recetas")
    if asistente:
        switch_page("Asistente")
    if recetas:
        switch_page("Recetas")