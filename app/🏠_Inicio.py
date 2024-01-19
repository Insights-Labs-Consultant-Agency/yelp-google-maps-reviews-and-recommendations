import streamlit as st
from utils import logo, switch_page
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

with open('app/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


# Configuración de la página
st.set_page_config(
    page_title="Yoogle",
    page_icon="assets/yoogle-favicon-32x32.png",
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

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')


if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.title(f"Bienvenido a Yoogle, *{st.session_state['name']}*! 👋")
    st.markdown('_**Descubre, elige, y disfruta la comida vegetariana**_')

    st.divider()

    # Casos de usoc:\Users\Freddy\Downloads\config.yaml
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
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
