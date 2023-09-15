import streamlit as st  # Carga Streamlit

import auxiliares.cargar_db as cargar_db # Carga la base de datos

from auxiliares.entrenamiento import entrenamiento

from functions.formulario import formulario # Carga el formulario

df = cargar_db.cargar_df() # A partir de la base de datos carga el DF para poder mostrarlo

# El título de la página tiene que ir antes de la definición de las pestañas
st.title("Aerolínea")

# Se definen las pestañas que se usarán en el contenido.
tab_form, tab_details = st.tabs(["Formulario", "Detalles"])

def main():
    entrenamiento() # Ejecuta el entrenamiento que graba el modelo entrenado en un pickle
    with tab_form:
        st.title("Formulario de encuestas")
        formulario()

    with tab_details:
        st.write("""
            El formulario se usa para introducir datos de nuevas encuestas y
            ver las predicciones del modelo.\n
            Si la predicción es marcada como correcta, la encuesta se almacenará 
            en la base de datos para futuros entrenamientos del modelo.\n
            Si la predicción es marcada como incorrecta, la encuesta 
            se almacenará en otra tabla, para diseñar otros entrenamientos
            complementarios.
        """)


if __name__ == '__main__':
    main()



