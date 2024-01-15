import google.generativeai as genai
# from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
from utils import logo


# load_dotenv()  # Load environment variables from .env.


# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

genai.configure(api_key=st.secrets["google"]["api_key"])

# Function to load Gemini Pro Vision model and get responses

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our streamlit app


st.set_page_config(
    page_title="Recetas",
    page_icon="🥗",
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

st.header("Generador de Recetas")
st.markdown("Sube la foto de un plato saludable y obtén la receta para prepararlo....")
#input = st.text_input("Input Prompt: ", key="input")
input = "Puedes generar la receta para el plato de la imagen. La receta debe incluir El nombre del plato, La lista de ingredientes, Los pasos de preparación y La información nutricional."
uploaded_file = st.file_uploader(
    "Selecciona una imagen...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada.", use_column_width=True)


submit = st.button("Generar Receta")

# If ask button is clicked

if submit:

    response = get_gemini_response(input, image)
    st.subheader("La receta es")
    st.write(response)
