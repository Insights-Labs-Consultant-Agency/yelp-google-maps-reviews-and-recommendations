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
        width="1220"
        height="720"
        src="https://us-east-2.quicksight.aws.amazon.com/sn/embed/share/accounts/018079189591/dashboards/85c5c680-f2d0-4a84-b6d0-7d8f24414031?directory_alias=insights-labs-quicksight">
    </iframe>
    </div>
"""


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
components.html(html_code, height=720)
