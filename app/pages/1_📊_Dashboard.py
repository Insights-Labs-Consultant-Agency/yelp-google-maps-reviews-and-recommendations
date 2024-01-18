import streamlit as st
import streamlit.components.v1 as components
from utils import logo

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


# Código HTML del dashboard de QuickSight
html_code = """
    <div style="
        position: relative;
        padding-bottom: 56.25%; /* Proporción 16:9 */
        height: 0;
        overflow: hidden;
    ">
        <iframe
            src="https://us-east-2.quicksight.aws.amazon.com/sn/embed/share/accounts/018079189591/dashboards/85c5c680-f2d0-4a84-b6d0-7d8f24414031?directory_alias=insights-labs-quicksight">
            style="
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border: none;
            ">
        </iframe>
    </div>
"""


# Inserta el dashboard de QuickSight en la aplicación de Streamlit
components.html(html_code, height=720)

