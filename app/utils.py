import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page
import streamlit.components.v1 as components


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


def quicksight_dashboard():
    # Código HTML del dashboard de QuickSight
    html_code = """
    <html>
    <head>
        <style>
            .iframe-container {
                overflow: hidden;
                padding-top: 56.25%; /* 16:9 */
                position: relative;
            }

            .iframe-container iframe {
                position: absolute;
                top: 0;
                left: 0;
                border: 0;
                width: 100%;
                height: 100%;
                background-color: transparent;
            }
        </style>
    </head>
    <body>
        <div class="iframe-container">
            <iframe src="https://us-east-2.quicksight.aws.amazon.com/sn/embed/share/accounts/018079189591/dashboards/85c5c680-f2d0-4a84-b6d0-7d8f24414031?directory_alias=insights-labs-quicksight" frameborder="0" allowfullscreen></iframe>
        </div>
    </body>
    </html>
    """

    # Inserta el dashboard de QuickSight en la aplicación de Streamlit
    components.html(html_code, height=720)