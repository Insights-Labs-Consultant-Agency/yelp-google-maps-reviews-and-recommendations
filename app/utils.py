import streamlit as st
import boto3
import pandas as pd
import google.generativeai as genai
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components
from pyathena import connect
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo


# Obtiene la api key desde el archivo secrets.toml
genai.configure(api_key=st.secrets["google"]["api_key"])

# Accede a las credenciales de AWS desde st.secrets
aws_access_key_id = st.secrets["aws"]["AWS_ACCESS_KEY_ID"]
aws_secret_access_key = st.secrets["aws"]["AWS_SECRET_ACCESS_KEY"]
region_name = st.secrets["aws"]["AWS_DEFAULT_REGION"]
s3_staging_dir = st.secrets["aws"]["AWS_ATHENA_S3_STAGING_DIR"]
campaign_arn = st.secrets["aws"]["AWS_campaign_arn"]


# Inicializa el cliente de Amazon Personalize
personalize = boto3.client('personalize', region_name=region_name, aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)

personalize_runtime = boto3.client('personalize-runtime', region_name=region_name, aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)


# Define el ARN de la campaña de Amazon Personalize
campaign_arn = campaign_arn

def get_recommendations(user_id):
    # Obtiene las recomendaciones de Amazon Personalize
    response = personalize_runtime.get_recommendations(
        campaignArn = campaign_arn,
        userId = str(user_id)
    )
    
    # Extrae los IDs de los artículos recomendados
    item_list = [item['itemId'] for item in response['itemList']]
    
    # Convierte la lista de IDs en un DataFrame de pandas
    df = pd.DataFrame(item_list, columns=['Item ID'])
    
    return df.head()


def get_item_details(df):
    # Define la consulta SQL para obtener los datos de Athena
    query = """
    SELECT business_id, name, address, city, state, rating
    FROM yelp.cleaned_business_yelp
    WHERE business_id IN {}
    """.format(tuple(df['Item ID'].tolist()))  # Reemplaza df con tu DataFrame

    # Ejecuta la consulta en Amazon Athena
    cursor = connect(aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    s3_staging_dir=s3_staging_dir,
                    region_name=region_name).cursor()
    cursor.execute(query)

    # Obtiene los resultados de la consulta y los almacena en un DataFrame de pandas
    df_athena = pd.DataFrame(cursor.fetchall(), columns=['business_id','Restaurante', 'Dirección', 'Ciudad', 'Estado', 'Calificación'])

    # Une el DataFrame original con el DataFrame de Athena
    df_final = pd.merge(df, df_athena, left_on='Item ID', right_on='business_id')
    df_final = df_final.drop(columns=['business_id','Item ID'])
    return df_final


# Funcion para agregar logo al sidebar de la página
def logo():
    add_logo("app/assets/yoogle-icon.png", height=300)
    # add_logo("assets/yoogle-icon.png", height=300)

# Funcion para cargar el modelo Gemini Pro + Vision y obtener una respuesta
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


# Funcion para agregar botones de acceso directo
def switch_page():
    cols = st.columns([2,5,1,6.5,1,4,1,4,2])
    if cols[1].button(" 📊 Dashboard"):
        st.switch_page("pages/1_📊_Dashboard.py")
    if cols[3].button("🍴 Recomendaciones"):
        st.switch_page("pages/2_🍴_Recomendaciones.py")
    if cols[5].button(" 💬 Asistente"):
        st.switch_page("pages/3_💬_Asistente.py")
    if cols[7].button("🥗 Recetas"):
        st.switch_page("pages/4_🥗_Recetas.py")


# Funcion para cargar el dashboard de QuickSight en la aplicación de Streamlit
def quicksight_dashboard():
    # Código HTML del dashboard de QuickSight
    html_code = """
    <html>
    <head>
        <style>
            .iframe-container {
                overflow: hidden;
                padding-top: 56.25%; /* 16:9 */
                position: relative;
            }

            .iframe-container iframe {
                position: absolute;
                top: 0;
                left: 0;
                border: 0;
                width: 100%;
                height: 100%;
                background-color: transparent;
            }
        </style>
    </head>
    <body>
        <div class="iframe-container">
            <iframe
            width: 100%;
            height: 100%; 
            src="https://us-east-2.quicksight.aws.amazon.com/sn/embed/share/accounts/018079189591/dashboards/ab6aa878-b1e5-4a5a-92db-4faea9ce0126?directory_alias=insights-labs-quicksight" frameborder="0" allowfullscreen>
            </iframe>
        </div>
    </body>
    </html>
    """

    # Inserta el dashboard de QuickSight en la aplicación de Streamlit
    components.html(html_code, height=720)



# Funcion para cargar el dashboard de PowerBI en la aplicación de Streamlit
# def powerbi_dashboard():
# width="1220"
# height="720"
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
