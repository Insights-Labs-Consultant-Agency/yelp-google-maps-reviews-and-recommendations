import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

# Logo de la página
def logo():
    add_logo("assets/yoogle-icon.png", height=300)

# Boton para cambiar de página 
def switch_page():
    cols = st.columns([2,5,1,7,1,4,1,4,2])
    if cols[1].button(" 📊 Dashboard"):
        st.switch_page("pages/1_📊_Dashboard.py")
    if cols[3].button("🍴 Recomenndaciones"):
        st.switch_page("pages/2_🍴_Recomendaciones.py")
    if cols[5].button(" 💬 Asistente"):
        st.switch_page("pages/3_💬_Asistente.py")
    if cols[7].button("🥗 Recetas"):
        st.switch_page("pages/4_🥗_Recetas.py")




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
            <iframe src="https://us-east-2.quicksight.aws.amazon.com/sn/embed/share/accounts/018079189591/dashboards/ab6aa878-b1e5-4a5a-92db-4faea9ce0126?directory_alias=insights-labs-quicksight" frameborder="0" allowfullscreen></iframe>
        </div>
    </body>
    </html>
    """

    # Inserta el dashboard de QuickSight en la aplicación de Streamlit
    components.html(html_code, height=720)


# def powerbi_dashboard():
    # width="1220"
    # height="720"
    # # Código HTML del dashboard de PowerBI
    # html_code = """
    #     <div style="
    #         position: relative;
    #         padding-bottom: 56.25%; /* Proporción 16:9 */
    #         height: 0;
    #         overflow: hidden;
    #     ">
    #         <iframe title="1.0-fp-dashboard" width="1220" height="780" src="https://app.powerbi.com/view?r=eyJrIjoiMWM4ZDI1OTUtOGU1Ny00OTU3LTg5YTUtNmIzNzQ2YmQzODViIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true">
    #         </iframe>
    #     </div>
    # """
    # Inserta el dashboard de QuickSight en la aplicación de Streamlit
    # components.html(html_code, height=720)
