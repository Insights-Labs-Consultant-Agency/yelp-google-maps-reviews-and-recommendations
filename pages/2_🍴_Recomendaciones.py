import streamlit as st
from utils import logo

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

logo()

st.title("🍴 Recomendaciones")
