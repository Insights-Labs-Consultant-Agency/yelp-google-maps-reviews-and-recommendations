import streamlit as st
from utils import logo, switch_page

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

#st.title('Bienvenido a :green[Yoo]:red[gle]! 👋')
st.write("# Bienvenido a Yoogle! 👋")

#switch_page()




