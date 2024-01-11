<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT Licencia][Licencia-shield]][Licencia-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations">
    <img src="assets/icons/insights-labs-logo.png" alt="Logo" width="80" height="80">
    
  </a>

<h3 align="center">YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS</h3>

  <p align="center">
    Desarrollo de un Data Product mediante el análisis del mercado estadounidense de comida vegetariana y afines, usando datos de Yelp y Google Maps
    <br />
    <a href="https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki"><strong>Explorar la documentación »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/issues">Request Feature</a>
  </p>
</div>



<!-- Tabla de contenido -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#acerca-del-proyecto">Acerca del Proyecto</a></li>
    <li><a href="#nuestro-cliente">Nuestro Cliente</a></li>
    <li><a href="#planteamiento-del-problema">Planteamiento del Problema</a></li>
    <li>
      <a href="#objetivos">Objetivos</a>
      <ul>
        <li><a href="#objetivo-general">Objetivo General</a></li>
        <li><a href="#objetivos-específicos">Objetivos Específicos</a></li>
      </ul>
    </li>
    <li><a href="#kpis">KPIs</a></li>
    <li>
      <a href="#alcance">Alcance</a>
      <ul>
        <li><a href="#alcance-temporal">Alcance Temporal</a></li>
        <li><a href="#alcance-espacial">Alcance Espacial</a></li>
      </ul>
    </li>
    <li><a href="#metodología-de-trabajo">Metodología de Trabajo</a></li>
    <li><a href="#data-product">Data Product</a></li>
    <li><a href="#stack-tecnológico">Stack Tecnológico</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contribuciones">Contribuciones</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#sobre-nosotros">Sobre Nosotros</a></li>
    <li><a href="#nuestro-equipo">Nuestro Equipo</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <!-- <li><a href="#agradecimientos">Agradecimientos</a></li> -->
  </ol>
</details>



<!-- Acerca del Proyecto -->
## Acerca del Proyecto

<!-- <p align="center">
  <img src="images/screenshot-api-home.png" alt="screenshot"/>
</p> -->

Este proyecto corresponde al Proyecto Final de la etapa de Labs del programa de Data Science de SoyHenry, donde se trata de analizar el mercado estadounidense de comida vegetariana y afines, usando datos de Yelp y Google Maps. Se busca entender las opiniones y preferencias de los usuarios de ambas plataformas, así como las tendencias y oportunidades de negocio en el sector. El objetivo es crear data products que permitan realizar análisis de sentimientos, predecir el crecimiento o decrecimiento del rubro de comida vegetariana y afines, sugerir las mejores ubicaciones para los nuevos locales, y crear un sistema de recomendación de restaurantes personalizado y un asistente virtual para los usuarios.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- NUESTRO CLIENTE -->
## Nuestro Cliente

Nuestro cliente es un conglomerado de empresas de restaurantes de comida vegetariana y afines, que desea expandir su mercado y ofrecer una mejor experiencia a sus clientes. El conglomerado está formado por tres franquicias: envegan, NuVegan Cafe y Veggie Grill. Puedes conocer más sobre las franquicias en la sección [Nuestro Cliente](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki#nuestro-cliente) de la documentación asociada en la Wiki.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- problem statement section -->
## Planteamiento del Problema

El mercado estadounidense de comida vegetariana está en constante crecimiento, pero también es competitivo y dinámico. Para tener éxito en este mercado, es necesario conocer a fondo el comportamiento y las opiniones de los clientes. Los datos de Yelp y Google Maps son valiosas fuentes de información sobre las opiniones y comportamientos de los usuarios pero su análisis también implica desafíos técnicos y metodológicos.

El proyecto requiere técnicas avanzadas de análisis de sentimientos y predicción de tendencias que permitan generar insights accionables para el cliente, sugerencias de ubicaciones para nuevas franquicias y recomendaciones de restaurantes personalizadas para los usuarios.

La importancia y relevancia de este proyecto radica en que se busca aportar al conocimiento y la comprensión del mercado estadounidense de comida vegetariana y afines, así como brindar soluciones que beneficien a nuestro cliente y sus usuarios. Para ampliar la información y conocer las preguntas de investigación planteadas puedes consultar la sección [Planteamiento del Problema](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki#planteamiento-del-problema) en la documentación.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


## Objetivos

### Objetivo General

- Proporcionar un análisis completo de los datos de las plataformas Yelp y Google Maps, que permita desarrollar un plan de expansión al conglomerado de franquicias de comida vegana aumentar su cuota de mercado, mejorar su reputación y satisfacer las necesidades de los consumidores veganos en los estados de Florida, Nevada y Virginia.

### Objetivos Específicos

- Detectar las localidades dentro de los estados objetivos donde hay mayor posibilidad de expansión de las franquicias, mediante un análisis de mercado que tenga en cuenta variables como la demanda, la competencia, el perfil de los clientes potenciales y los factores externos. 
- Establecer un modelo de NLP para analizar las reseñas de las franquicias e identificar las características que más valoran los consumidores veganos y obtener un informe con los aspectos positivos y negativos de cada franquicia, y las sugerencias de mejora para el menú y la oferta.
- Desarrollar un sistema de recomendación de restaurantes que pueda ofrecer recomendaciones personalizadas, basadas en las experiencias previas y las preferencias de los usuarios. 
- Realizar un chatbot basado en NLP para responder a las preguntas de los clientes y proporcionarles información sobre las franquicias, que pueda interactuar  de forma natural, fluida y precisa para resolver sus dudas, sugerencias y reclamos. 

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- KPIs section -->
## KPIs
### KPI 1 Satisfaccion al cliente
Nos permite evaluar directamente la percepción general de los clientes sobre nuestros servicios.
Metrica: cantidad de reseñas positivas que recibe el cliente.
Objetivo: aumentar un 10% las mismas en periodo trimestrales.

### KPI 2 Cantidad de Reseñas por Sucursal
Nos permite comprender cómo cada sucursal está siendo percibida por los clientes y a identificar áreas de mejora a nivel local.
Métrica: Cantidad de interacciones en las sucursales. Cantidad total de reseñas por sucursales/cantidad total de reseñas.
Objetivo: incrementar un 5% las reseñas positivas mensualmente.

### KPI 3 Satisfacción del Cliente respecto al Servicio
Nos permite comprender en detalle los aspectos específicos de nuestros servicios, que impactan en la experiencia del cliente.
Metrica: Cantidad de comentarios negativos o positivos respecto al servicio sobre cantidad de comentarios totales.
Objetivo: aumentar un 5% los comentarios positivos y disminuir 5% la cantidad de comentarios negativos mensualmente.

### KPI 4 Oferta/Demanda de comida saludable
Nos permite tomar decisiones estratégicas, sobre la expansión de nuestra oferta de comida vegetaría/vegana en áreas con alta demanda relativa.
Metrica: Cantidad de restaurantes de comida saludable/cantidad de reseñas de comida saludable por estado.
Objetivo: identificar el top 3 de ciudades potenciales por estado basados en esta métrica.
<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<!-- scope section -->
## Alcance

### Alcance Temporal
El proyecto se estructuro en tres Sprint, en un período de tres semanas totales, comenzando el 2 enero de 2024. Durante este tiempo, se realizaron análisis de los datos de Google Maps y Yelp. Se llevaron a cabo análisis georreferenciales para rastrear la popularidad y ubicación de las franquicias del cliente.
Los Sprint se distribuyeron de la siguiente manera:

📜 Sprint #1: Puesta en marcha del proyecto y Trabajo con Datos (Semana 1)

Entendimiento de la Situación Actual: Análisis de la temática y los datos disponibles.
Objetivos: Definición de objetivos concretos y KPIs asociados.
Alcance: Delimitación del trabajo y definición de tareas fuera de alcance.
Repositorio Github: Creación del repositorio colaborativo en Github.
Solución Propuesta: Detallar tareas, productos y metodologías a utilizar.
Análisis Preliminar de Calidad de Datos: Metadatos y análisis detallado sobre los datos disponibles.
Hitos y Entregables: 3 KPIs, Documentación de alcance, EDA de los datos, Implementación del stack tecnológico, Metodología de trabajo, Diseño detallado, Equipo de trabajo - Roles y responsabilidades, Cronograma - Gantt, Análisis preliminar de calidad de datos.
👨‍💻 Sprint #2: Data Engineering (Semana 2)

ETL y Modelado de Datos: Montaje de infraestructura y desarrollo de pipelines ETL.
Modelo Entidad-Relación o No-Relacional: Diseño detallado del modelo o justificación de modelo no relacional.
Análisis Exhaustivo en Muestra Representativa de Datos: Identificación de valores atípicos, distribuciones y correlaciones.
Diseño de Dashboard (Prueba de Concepto) o Producto de ML (MVP): Versión simplificada del dashboard o producto de ML con datos de muestra.
Hitos y Entregables: ETL completo, Estructura de datos implementada, Pipeline ETL automatizado, Diseño del Modelo ER, Pipelines para alimentar el DW, Data Warehouse, Validación de datos, Documentación detallada.
📈 Sprint #3: Data Analytics + ML (Semana 3)

Desarrollo de Dashboard Interactivo y Análisis de Datos: Creación de un dashboard interactivo y análisis de datos.
Implementación de Modelos de ML (si aplica): Producto/s de ML, Modelo/s de ML en producción.
Diseño de Reportes/Dashboards y KPIs: Finalización del dashboard, KPIs e informe de análisis.
Entregables Finales: Dashboard final, Producto/s de ML, Documentación y reporte final.

### Alcance Espacial
Se realizó una delimitación espacial del proyecto mediante un análisis georreferencial utilizando Google Maps para mapear las ubicaciones de las franquicias existentes del cliente, que se concentran principalmente en las costas este y oeste de los EE. UU.

Mediante un análisis de tendencias utilizando Google Trends se analizó la popularidad de la comida vegana, vegetariana y saludable en los EE. UU., para identificar los mejores estados para el plan de expansión, determinando a Nevada, Virginia y Florida como los estados más prometedores para abrir nuevas franquicias. Para conocer más detalles de como se desarrollaron estos análisis puedes consultar la documentación asociada en la sección [Alcance](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki/Alcance) de la Wiki. 



<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- METODOLOGIA -->
## Metodología de trabajo

El proyecto se desarrollará en un plazo de tres semanas, dividido en tres sprints, siguiendo una metodología ágil y colaborativa dentro de los marcos de gestión de proyectos Scrum y Kanban, y utilizando Github Projects, Github Wiki y Github Flow como herramientas de gestión, documentación y desarrollo. Estas herramientas permiten gestionar el proyecto de forma iterativa e incremental, adaptarse a los cambios y requerimientos del cliente, y entregar valor en cada sprint. Para más información sobre la [metodología de trabajo](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki/Metodolog%C3%ADa-de-Trabajo) puedes consultar la documentación asociada en la wiki.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- product section -->
## Data Product

El data product a desarrollar en este proyecto tiene como nombre Yoogle, el cual permite obtener insights sobre el mercado estadounidense de restaurantes de comida saludable y afines, utilizando datos de las plataformas Yelp y Google Maps, puede generar recomendaciones de restaurantes, recetas y cuenta con un asistente virtual. Yoogle se presenta como una aplicación web interactiva, desarrollada con la herramienta Streamlit, que proporciona una interfaz gráfica amigable y ofrece varias secciones y funcionalidades para diferentes tipos de usuarios. Para conocer más sobre nuestro producto, sus funcionalidades y características puedes consultar la documentación asociada en la sección [Descripción del Producto](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki/Descripción-del-Producto) de la wiki. 


<!-- STACK TECNOLOGICO -->
## Stack tecnológico

Para el desarrollo del proyecto, se eligió un stack tecnológico basado en servicios de AWS, que permite construir una arquitectura de datos moderna, de bajo costo y centrada en data lakes usando servicios sin servidor administrados por AWS que ofrecen una solución, escalable, flexible y segura para el procesamiento de datos. Para más información sobre el stack tecnológico, la arquitetura y el flujo de trabajo puedes consultar la documentación asociada en la sección [Stack Tecnológico](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/wiki/Stack-Tecnol%C3%B3gico) de la wiki.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<!-- USAGE EXAMPLES -->
<!-- ## Uso

<p align="right">(<a href="#readme-top">volver arriba</a>)</p> -->


<!-- roadmap section -->
## Roadmap

Este proyecto se encuentra en fase de desarrollo, puedes consultar el roadmap completo en la sección [GitHub Projects](https://github.com/orgs/Insights-Labs-Consultant-Agency/projects/2/views/4).

Consulta los [issues abiertos](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/issues) para conocer las tareas en desarrollo y los [hitos](https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/milestones) a alcanzar.


<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- CONTRIBUTING -->
## Contribuciones

Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar increíble para aprender, inspirarse y crear. Cualquier contribución que hagas será **muy apreciada**.

Si tienes una sugerencia para mejorar este proyecto, haz un fork del repositorio y crea un pull request. También puedes simplemente abrir un issue con la etiqueta *“enhancement”*. ¡No olvides darle una estrella al proyecto! Gracias de nuevo.

1. Haz un fork del Proyecto
2. Crea tu feature Branch (`git checkout -b feature/AmazingFeature`)
3. Haz commits de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz Push a la Branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- license section -->
## Licencia

Distribuido bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- About us section-->
## Sobre nosotros
**Insights Labs** 🚀 es una consultora de análisis de datos que ayuda a las empresas a tomar mejores decisiones basadas en datos. Ofrecemos servicios de investigación, visualización, modelado y machine learning, utilizando las mejores herramientas y metodologías del mercado.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- team section -->
## Nuestro Equipo

| Equipo              | Rol            | Nombre                | Contacto |
|-------------------- | -------------- | --------------------- | -------- |
| Data Infrastructure | Data Engineer  | Jimmy Pachon          | [![LinkedIn][linkedin-shield]][linkedin-pachon]  |
| Data Research       | Data Analyst   | Freddy Ampueda        | [![LinkedIn][linkedin-shield]][linkedin-ampueda] |
| Machine Learning    | Data Scientist | Freddy Pinto          | [![LinkedIn][linkedin-shield]][linkedin-pizarro] |
| Data Visualization  | Data Analyst   | Javier Pizarro        | [![LinkedIn][linkedin-shield]][linkedin-pinto]   |
| Data Visualization  | Data Analyst   | Cristopher Morales    | [![LinkedIn][linkedin-shield]][linkedin-morales] |
<!-- | Project Management  | Scrum Master   | Maximiliano Vaca Coll |           | -->
<!-- |                     | Product Owner  |                       |           | -->

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- Contact Section -->
## Contacto

- 🔗 Página Web: [www.insights-labs-consultant-agency.com](insights-labs-consultant-agency.github.io/yelp-google-maps-reviews-and-recommendations/)

- 📧 Email: insightslabsconsultantagency@gmail.com 

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- ACKNOWLEDGMENTS -->
<!-- ## Agradecimientos
Queremos agradecer a las siguientes personas y recursos que nos han ayudado a realizar este proyecto:

* A [SoyHenry](https://www.soyhenry.com/) por ofrecernos esta gran oportunidad de participar en el bootcamp de data science y aprender sobre MLOps.
* A la comunidad de Henry, especialmente a [Maximiliano Vaca Coll]() que nos ha apoyado y guiado durante el proceso de desarrollo de este proyecto.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p> -->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/FreddyPinto/recsys-steam-games.svg?style=for-the-badge
[contributors-url]: https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/FreddyPinto/recsys-steam-games.svg?style=for-the-badge
[forks-url]: https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/network/members
[stars-shield]: https://img.shields.io/github/stars/FreddyPinto/recsys-steam-games.svg?style=for-the-badge
[stars-url]: https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/stargazers
[issues-shield]: https://img.shields.io/github/issues/FreddyPinto/recsys-steam-games.svg?style=for-the-badge
[issues-url]: https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/issues
[Licencia-shield]: https://img.shields.io/github/license/FreddyPinto/recsys-steam-games.svg?style=for-the-badge
[Licencia-url]: https://github.com/Insights-Labs-Consultant-Agency/yelp-google-maps-reviews-and-recommendations/blob/main/LICENSE
[product-screenshot]: images/screenshot.jpg
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-pachon]: https://www.linkedin.com/in/jimmy-pachon-gomez-171591261/
[linkedin-ampueda]: https://www.linkedin.com/in/freddy-ampueda/
[linkedin-pizarro]: https://www.linkedin.com/in/javier-pizarro-187766111/
[linkedin-pinto]: https://www.linkedin.com/in/FreddyPinto-/
[linkedin-morales]: https://www.linkedin.com/in/cristopher-morales-04b67616b/
