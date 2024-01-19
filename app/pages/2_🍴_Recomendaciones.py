import streamlit as st
from utils import logo, get_recommendations, get_item_details

st.set_page_config(
    page_title="Recomendaciones",
    page_icon="🍴",
    menu_items={
    "Get help": "https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki",
    "Report a bug": "https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/issues/new",
    "About": """
        ## Yoogle
        
        **GitHub**: https://github.com/Insights-Labs-Consultant-Agency
    """
    }
)

# Inserta el logo en el sidebar
logo()

st.title("🍴 Recomendaciones")
st.caption("🚀 powered by Amazon Personalize")
st.markdown("_¡Prepárate para descubrir los restaurantes que podrían convertirse en tus nuevos favoritos!_.")
st.markdown("Encuentra el restaurante ideal para ti, simplemente haz clic en el botón **“Generar Recomendaciones”**.")

user_id = st.text_input('Introduce tu ID de usuario')

if st.button('Generar recomendaciones'):
    # Obtiene las recomendaciones para el user_id especificado
    recommendations = get_recommendations(user_id)
    
    # Obtiene los detalles de los artículos recomendados
    item_details = get_item_details(recommendations)
    
    # Muestra los detalles de los artículos recomendados en la aplicación Streamlit
    st.dataframe(item_details)