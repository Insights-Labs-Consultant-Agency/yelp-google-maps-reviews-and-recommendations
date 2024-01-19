import streamlit as st
from utils import logo, switch_page

st.set_page_config(
    page_title="Yoogle",
    page_icon="app/assets/yoogle-favicon-32x32.png",
    menu_items={
    "Get help": "https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki",
    "Report a bug": "https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/issues/new",
    "About": """
        ## Yoogle
        
        **GitHub**: https://github.com/Insights-Labs-Consultant-Agency
    """
    }
)

# Agregar el logotipo a la barra lateral
logo()

st.title("Bienvenido a Yoogle! 👋")
st.markdown('_**Descubre, elige, y disfruta la comida vegetariana**_')

st.divider()

#Use Cases
with st.container():
    col1,col2=st.columns(2)
    with col1:
        st.subheader('¿Qué puedes hacer?')
        st.markdown(
            """
            Yoogle te permite acceder a una gran variedad de funcionalidades que harán tu vida más fácil y divertida. Con Yoogle, puedes:
            - _Explorar el mercado de comida vegetariana en Estados Unidos_
            - _Encontrar el restaurante ideal para ti_
            - _Conversar con un asistente virtual inteligente_
            - _Generar recetas saludables y deliciosas_
            """
            )
    with col2:
        st.subheader("¿Por qué usar Yoogle?")
        st.markdown(
            """
            Yoogle no solo te ofrece información, sino también beneficios. Al usar Yoogle, podrás:
            - _Descubrir nuevos lugares_
            - _Ahorrar tiempo y dinero_
            - _Disfrutar de una alimentación sana y variada_
            """
            )

st.divider()

st.subheader("¿Listo para explorar Yoogle?")
st.markdown(" Elige una de las opciones de abajo y empieza tu aventura gastronómica.")

switch_page()