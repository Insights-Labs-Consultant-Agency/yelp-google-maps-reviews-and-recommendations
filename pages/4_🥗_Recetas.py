import streamlit as st
from PIL import Image
from utils import logo, get_gemini_response

# Configura la página de Streamlit
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

# Carga el logo en el sidebar
logo()

st.title("🥗 Generador de Recetas")
st.caption("🚀 powered by Gemini Pro + Vision")
st.markdown("Sube la foto de un plato saludable y obtén la receta para prepararlo....")

#input = st.text_input("Input Prompt: ", key="input")
input = "Puedes generar la receta para el plato de la imagen. La receta debe incluir El nombre del plato, La lista de ingredientes, Los pasos de preparación y La información nutricional."
uploaded_file = st.file_uploader(
    "Selecciona una imagen...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada.", use_column_width=True)

    if st.button('Generar receta'):
        st.write('Generando receta...')
        # Si el botón de generar receta es cliqueado
        response = get_gemini_response(input, image)
        st.write('Receta generada con exito!')
        st.subheader("La receta es")
        st.write(response)
else:
    st.write('Por favor, sube una imagen para generar la receta.')

