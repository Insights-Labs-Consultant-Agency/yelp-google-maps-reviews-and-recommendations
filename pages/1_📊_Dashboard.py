import streamlit as st
from utils import logo, quicksight_dashboard

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
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

st.title("📊 Dashboard ")

quicksight_dashboard()

