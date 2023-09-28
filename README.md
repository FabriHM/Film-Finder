**UNIVERSIDAD PERUANA** 

**DE CIENCIAS APLICADAS**

![](Aspose.Words.a9942042-5445-4390-9fec-15ebdc98e3e5.001.png)

Complejidad Algorítmica (DEF)

CC 184-WX 73

Título

Film Finder

Profesor: Luis Martín Canaval Sanchez


Integrantes:

Gonzales Arotinco Bruno Leonardo - u201820037

Burga Loarte Anaely - u202118264

Fabricio Raúl Huillca Mateos - u202118067





2023-2

Índice

1. [Enunciado del Proyecto](#_heading=h.gjdgxs)
1. Logro del Curso
1. [Descripción del problema](#_heading=h.gjdgxs)[.](#_heading=h.gjdgxs)[	](#_heading=h.gjdgxs)

4[.Descripción del conjunto de datos (dataset)](#_heading=h.1fob9te)[.](#_heading=h.1fob9te)[	](#_heading=h.1fob9te)

5 [.Propuesta](#_heading=h.3znysh7)[.](#_heading=h.3znysh7)[	](#_heading=h.3znysh7)


1. # <a name="_heading=h.i8pqd6cqtj61"></a>   **Enunciado del Proyecto**
El proyecto consiste en implementar un algoritmo de búsqueda usando nodos con los conceptos utilizados durante las sesiones de clase para poder desarrollar nuestro proyecto.
1. # <a name="_heading=h.kx7zxuvhw6rx"></a>**Logro del curso**

Student outcome
- # <a name="_heading=h.g877qauj3y1a"></a>Competencias Generales: Razonamiento Cuantitativo 
- # <a name="_heading=h.b9ut8hx4l73w"></a>Nivel de logro: 2




|Criterio específico|Acciones realizadas|Conclusiones|
| :- | :- | :- |
|<p>1\. Demuestra comprensión del código de ética propio de su profesión. </p><p>2\. Emite juicios sobre situaciones donde el código de ética puede verse vulnerado.</p><p>3\. Demuestra respeto por los derechos de propiedad intelectual.</p>|<p>- Todos los integrantes:</p><p>- Descripción del problema</p><p>- Data set</p><p>- Propuesta</p>|En el ámbito de la ingeniería y la tecnología, resulta fundamental la creación de sistemas de recomendación eficaces para plataformas de streaming como Netflix y HBO Max. Esto implica la aplicación de algoritmos basados en grafos para entender las preferencias de los usuarios y ofrecerles recomendaciones personalizadas. En este proceso, se hace necesario demostrar una sólida comprensión del código ético de la profesión, emitir juicios éticos en situaciones de posible conflicto con dicho código y mantener un respeto firme hacia los derechos de propiedad intelectual.|
|<p>1\. Comprende las competencias que definen el perfil profesional de la carrera. </p><p>2\. Reconoce el papel e importancia de las sociedades profesionales, en especial la IEEE Computer Society y ACM </p><p>3\. Cumple con las responsabilidades asumidas y los planes comprometidos en los proyectos en los que participa. </p><p>4\. Ante eventos que ponen en riesgo el cumplimiento de los compromisos asumidos negocia con los interesados los niveles de cumplimientos de los objetivos establecidos.</p>|<p>- Todos los integrantes:</p><p>- Descripción del problema</p><p>- Data set</p><p>- Propuesta</p>|Es esencial que el profesional de la ingeniería comprenda las habilidades que definen su perfil y reconozca la importancia de sociedades profesionales como la IEEE Computer Society y ACM. Debe cumplir con sus responsabilidades y compromisos en los proyectos en los que participa, y, en caso de eventos que puedan poner en peligro esos compromisos, debe negociar con las partes interesadas para asegurar el cumplimiento de los objetivos establecidos.|
|<p>1\. Considera mediciones de los factores que impactan en el contexto global </p><p>2\. Identifica y toma las buenas prácticas globales en el ámbito de aplicación del producto de ingeniería en diseño o desarrollo. </p><p>3\. Comprende el impacto social y ambiental que generan las soluciones en ingeniería en la sociedad actual</p><p>4\. Comprende el impacto económico que genera el desarrollo de la solución propuesta</p>|<p>- Todos los integrantes:</p><p>- Descripción del problema</p><p>- Data set</p><p>- Propuesta</p>|Debemos tener en cuenta mediciones de factores que tienen un impacto a nivel global, identificar y aplicar prácticas exitosas a nivel mundial en el diseño o desarrollo de productos de ingeniería, y comprender las repercusiones sociales, ambientales y económicas que generan las soluciones de ingeniería en la sociedad contemporánea.|

- # <a name="_heading=h.1larebgxxk8c"></a>Competencias Específicas: ABET 4 - Responsabilidad y ética (Anexo 1)

En el desarrollo de sistemas de recomendación de películas, tomamos en cuenta su responsabilidad ética. Esto implica proteger la privacidad de los usuarios, ser transparentes en cuanto a cómo funcionan los algoritmos, abordar cualquier sesgo presente, proporcionar recomendaciones de alta calidad y mantener la integridad profesional en todo momento. Estas consideraciones éticas son esenciales para asegurar que los sistemas de recomendación sean justos y beneficien a todos los usuarios.

-
1. # <a name="_heading=h.ggl6no8xx1kg"></a><a name="_heading=h.gjdgxs"></a>**Descripción del problema:**
- **Problemática:** La cuestión central que hemos enfrentado se refiere a cómo abordar el reto de ofrecer a los usuarios de servicios de streaming, como Netflix o HBO Max, recomendaciones de películas que se ajusten de manera precisa a sus preferencias individuales. Nos hemos encontrado con el desafío de mantener a los usuarios comprometidos y satisfechos en medio de una amplia variedad de opciones, asegurando que las recomendaciones sean pertinentes y personalizadas para cada uno. Nuestro programa se ha dedicado a resolver este problema mediante la aplicación de algoritmos avanzados y técnicas de análisis de datos, lo que nos ha permitido proporcionar recomendaciones que no solo enriquecen la experiencia del usuario, sino que también prolongan su compromiso con la plataforma de streaming.

- Dentro del contexto de las plataformas de streaming, como Netflix, Amazon Prime Video, Disney +, Apple TV y HBO Max, la implementación de sistemas de recomendación juega un papel esencial. Estos sistemas, respaldados por avanzados algoritmos de búsqueda, desempeñan un papel fundamental al proporcionar a los usuarios recomendaciones altamente personalizadas. Este enfoque no solo enriquece la experiencia del usuario, sino que también prolonga su compromiso con la plataforma, manteniéndolos involucrados durante períodos más extensos.

- Para alcanzar este objetivo, es esencial contar con datos detallados sobre las preferencias individuales de cada usuario, así como sobre las películas que ya han disfrutado previamente. La implementación de estos sistemas se lleva a cabo empleando el lenguaje de programación Python, una herramienta excepcionalmente eficaz para analizar datos y desarrollar algoritmos de recomendaciones personalizadas extremadamente precisos y eficientes. En última instancia, esta estrategia no sólo resulta beneficiosa para los usuarios al brindarles contenido relevante y atractivo, sino que también conduce al éxito continuado de la plataforma de streaming.
- # <a name="_heading=h.1fob9te"></a>**4.  Descripción del conjunto de datos (dataset):**
El data set se compone por 1500 entradas tomadas de imdb con información de películas. 

Se tomó en cuenta para la realización de las tablas, las siguientes características:


|Dato|Descripción|Tipo de dato|
| :-: | :-: | :-: |
|idPelicula|Es el identificador de cada película|int|
|tituloPelicula|Título que identifica a la pélicula|string|
|duracionMinutos|El tiempo que dura la película expresado en minutos|int|
|directorPelicula|Director de la pélicula|string|
|actoresPelicula|Actores de la película (separados por comas)|string|
|generoPelicula|Géneros de la película (separados por comas)|<p>string</p><p></p>|

- Mostrar mediante un grafo completo y/o subgrafos los datos recolectados.

![](Aspose.Words.a9942042-5445-4390-9fec-15ebdc98e3e5.002.png)
- # <a name="_heading=h.5wlqmxs06ajq"></a>**5. Propuesta:**
- Objetivo:
- La propuesta de solución del problema que presentamos es lo siguiente:
- Generar un grafo usando una matriz de adyacencia en memoria, para lo cual se tendrá en cuenta que cada nodo representa una película y así poder indicar que cada película ‘X’ está relacionado con cada película ‘Y’.
- Se deberá medir la relación que hay entre cada película y la cantidad de coincidencias entre sus datos.
- Se le presentará al usuario una interfaz donde el pueda ingresar el nombre de la película que desee ver y un botón para realizar la búsqueda. Al darle click a dicho botón, aparecerá para el usuario toda la información de la película y una cantidad de películas con posibles relaciones a la búsqueda.
- Cuando el usuario “**visualice**” películas de su agrado, estas se “**acercarán**” en el grafo guardado en txt, disminuyendo a los pesos un 20% que unen a dichas películas. Por ejemplo, si el usuario mira las películas A, B y C, se disminuye un 20% el peso entre A y B, A y C, B y C en el grafo

- Técnicas:

Las técnicas que vamos a  implementar son las siguientes:

- Aplicación de Técnicas de Recorrido y Búsqueda en Grafos: La utilización de técnicas de recorrido y búsqueda en grafos fue fundamental en nuestro sistema de recomendaciones de películas. Estas técnicas nos permitieron identificar patrones de interacción entre usuarios y películas, lo que mejoró la personalización de las recomendaciones al explorar las conexiones dentro de la red de preferencias de los usuarios.

- Eficiente Manejo de Datos con la Estrategia "Divide y Vencerás": Implementaremos con éxito la estrategia "Divide y Vencerás" para organizar y procesar datos relacionados con películas y usuarios. Esta estrategia simplificó la gestión de conjuntos de información extensos, lo que a su vez contribuyó a una recomendación más efectiva y precisa.

- Optimización Mediante Minimum Spanning Tree (MST): La incorporación de MST en nuestro programa permitió identificar relaciones clave entre películas y usuarios, lo que ayudó a priorizar las recomendaciones al enfocarse en las conexiones más relevantes dentro de la red de preferencias. Esto resultó en recomendaciones más significativas para los usuarios.

- Mejora de la Eficiencia con Programación Dinámica: La programación dinámica se utilizará para optimizar la eficiencia en la generación de recomendaciones. Al mejorar procesos y cálculos, logramos acelerar el proceso de selección de películas recomendadas, beneficiando tanto a los usuarios como a la plataforma de streaming en sí.

- Metodología:

Nuestra metodología en el desarrollo del programa de recomendaciones de películas en Python se basa en un enfoque colaborativo y de iteración continua. Comenzamos recolectando y procesando datos de preferencias de usuarios y detalles de películas mediante técnicas de minería de datos. En la fase de diseño, modelamos las relaciones en una red de preferencias usando análisis de grafos y aplicamos algoritmos de aprendizaje automático para mejorar las recomendaciones. La implementación se realiza en Python, con bibliotecas junto con una interfaz de usuario interactiva en Tkinter. Evaluamos y ajustamos constantemente el sistema en función de métricas y retroalimentación de usuarios, manteniendo un diálogo abierto para refinamientos continuos. Esta metodología nos permite adaptarnos a las cambiantes preferencias de los usuarios y mejorar constantemente la experiencia de recomendación de películas.

- Lenguaje de programación:

- Para el desarrollo de nuestra aplicación en Python, haremos uso de una combinación de valiosas bibliotecas y recursos. Tkinter será esencial para crear una interfaz gráfica de usuario (GUI) interactiva, mientras que Matplotlib facilitará la representación visual efectiva de datos mediante gráficos y gráficos. NetworkX será una herramienta clave para analizar y manipular redes, lo que nos permitirá modelar y entender conexiones complejas. NumPy se utilizará para operaciones matriciales eficientes, y Pandas simplificará el manejo y procesamiento de datos en forma de marcos de datos. En conjunto, estas bibliotecas y recursos nos brindarán las capacidades necesarias para crear una aplicación versátil y poderosa.
- # <a name="_heading=h.r3agy7j393jx"></a>**6. Conclusiones:**
- Utilizamos la biblioteca Tkinter para desarrollar una interfaz de usuario interactiva que permite a los usuarios interactuar de manera fácil y amigable con nuestro sistema de recomendaciones de películas.

- Para poder representar los datos, utilizaremos a los grafos como medio de conexión entre sus nodos y aristas.

- Utilizamos Matplotlib para visualizar gráficamente datos sobre las preferencias de los usuarios y las películas recomendadas, facilitando la interpretación de información compleja y fomentando la toma de decisiones basada en datos.

- El procesamiento eficiente de información y la gestión de datos tabulares, estas capacidades permiten ofrecer recomendaciones precisas y personalizadas a los usuarios, mejorando así la experiencia en nuestra plataforma de recomendaciones de películas.

- # <a name="_heading=h.kavcqy7ojzs"></a>**7.    Referencias bibliográficas:**
*Cremonesi, P., Koren, Y., & Turrin, R. (2010). Performance of recommender algorithms on top-n recommendation tasks. ACM Transactions on Intelligent Systems and Technology, 1(3), 1-20. Recuperado de:[* ](https://doi.org/10.1145/1864708.1864721)<https://doi.org/10.1145/1864708.1864721>*

*Cañibano, J. (2022).* *Creación de grafos de conocimiento a partir de código de software científico en distintos lenguajes de programación. Recuperado de:[ ](https://oa.upm.es/72746/)[https://oa.upm.es/72746/*](https://oa.upm.es/72746/)*
