# Aerolinea_equipo_3

### EL PROYECTO

Se trata de automatizar las encuestas de satisfacción de los pasajeros de una aerolínea.

Se parte de un conjunto de encuestas recogidas de modo manual. A partir de estos datos se entrena un modelo de ML
que hará una predicción sobre nuevos datos.

Cuando se grabe una nueva encuesta se cuenta con un sistema de feedback para declarar si la predicción del modelo de ML es correcta o no.

Las nuevas encuestas, junto con las que ya se tenían previamente, se encuentran en una base de datos de MySQL.

### MODO DE USO

En el formulario se graban los datos de una nueva encuesta, en los distintos aspectos rlativos al vuelo, en un formulario diseñado al respoecto.
En caso de error se puede usar el botón **Reset** para restaurar el formulario y empezar de nuevo.
Cuando la encuesta esté correctamente tecleada se pulsa el botón **Enviar** para obtener una predicción.
La predicción se puede marcar como **Correcta** o **Incorrrecta** con los botones de feedback dispuestos al efecto en el formulario.
En todo caso, las nuevas encuestas se añaden automáticamente a la base de datos para furturos entrenamientos del modelo.

### ESTRUCTURA
El conjunto está organizado en la siguiente estructura:
  + Archivo **main.py**. Es el punto de entrada de la aplicación. Se ejecuta a partir de Streamlit.
  + Directorio **functions**. Contiene el archivo **formulario.py** que es el que genera el formulario de ingreso de nuevas encuestas.
  + Directorio **auxiliares**. Contiene los siguientes archivos:
    + Archivo **db.py**. Es el que crea la conexión a base de datos.
    + Archivo **cargar_db.py**. Carga el contenido de la base de datos en memoria y devuelve un DF, por si se decide mostrarlo en la página.
    + Archivo **entrenamiento.py**. Entrena un modelo con los datos existentes en la BBDD y guarda el modelo entrenado en un pickle.
    + Archivo **prediccion.py**. Efectúa una nueva predicción con la ayuda del archivo **obtener_parametros.py**.
    + Archivo **crear_consulta.py**. Una vez efectuada una predicción, y evaluado el feedback, este archivo guarda los resultados en la BBDD.
  + Directorio **conf**. Contiene el archivo **env.json** con los datos de conexión en el siguiente formato:
    <pre>
    {
        "engine":"", 
        "port": "", 
        "host": "", 
        "user": "", 
        "password": ""
    }
    </pre>
  +  Directorio **logs**. Guarda los logs de registro de consultas en **logs.log**.
  +  Directorio **pickle**. Contiene el archivo **train.pkl**, que almacena el modelo entrenado.

### PARTICIPANTES.
Este proyecto ha sido desarrollado por:
  + Gabriela Calzadilla
  + Paloma García
  + Victoria Moraleda
  + José López



# Aerolinea_equipo_3
Ejercicio Aerolinea equipo 3
