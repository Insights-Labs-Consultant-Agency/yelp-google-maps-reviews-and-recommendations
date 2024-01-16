import streamlit as st
import streamlit.components.v1 as components
from utils import logo

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
    <iframe
        width="960"
        height="720"
        src="https://us-east-2.quicksight.aws.amazon.com/sn/embed/share/accounts/018079189591/dashboards/1077495c-a58e-4910-a34e-909e4780fb9d?directory_alias=insights-labs-quicksight">
    </iframe>
"""

# Insertar el dashboard de QuickSight en la aplicación de Streamlit
components.html(html_code, height=720)

