import streamlit as st  # Carga Streamlit

# Librerías de tratamiento de datos
import numpy as np
import pandas as pd

import pickle

# La base de datos
from auxiliares.db import db

def predecir(datos_de_prediccion):
    columns = ['Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class',  
    'Flight Distance', 'Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking', 'Gate location', 
    'Food and drink', 'Online boarding', 'Seat comfort', 'Inflight entertainment', 'On-board service', 
    'Leg room service', 'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness', 
    'Departure Delay in Minutes', 'Arrival Delay in Minutes']

    # Usa np.reshape para darle la forma adecuada a la lista (22 filas y 1 columna)
    lista_de_datos = np.array(datos_de_prediccion).reshape(-1, 1)
    # Se crea el DF con loss datos recibidos.
    df = pd.DataFrame(lista_de_datos.T, columns = columns)
    # Se crea una copia para luego guardarlo en base de datos. Esta copia no será transformada para la predicción.
    df_recibido = df

    # Codificar a one-hot las columnas 'Gender', 'Customer Type', 'Type of Travel' y 'Class'
    columnas_a_codificar = ['Gender', 'Customer Type', 'Type of Travel', 'Class']
    # Usa pd.get_dummies() para realizar la codificación one-hot
    df = pd.get_dummies(df, columns=columnas_a_codificar, drop_first=False)

    cols_reales = df.columns

    # Convertimos las columnas booleanas de entrada, que tienen valores True y False a 1 y 0
    # teniendo en cuenta que algunas columnas pueden no existir.
    # Las que no existan serán las qque no se han creado en la conversión a one hot
    cols_boolean = [
        'Gender_Female', 'Gender_Male', 'Customer Type_Loyal Customer', 'Customer Type_disloyal Customer', 
        'Type of Travel_Business Travel', 'Type of Travel_Personal Travel', 'Class_Business', 
        'Class_Eco', 'Class_Eco Plus'
    ]

    # Convertimos todas las columnas a int
    for col in df.columns:
        df[col] = df[col].astype(int)

    # Agregamos las columnas que no existen
    for i, col in enumerate(cols_boolean):
        if col in cols_reales:
            df[col] = df[col].astype(int)
        else:
            df[col] = 0
    
    with open('pickle/train.pkl', 'rb') as pkl:
        modelo = pickle.load(pkl) # Carga el modelo ya entrenado, desde un archivo pickle.
    prediction = modelo.predict(df) 

    # Se añade la predicción al df recibido
    df_recibido['satisfaction'] = prediction
    df_recibido['satisfaction'] = df_recibido['satisfaction'].map({1: 'satisfied', 0: 'neutral or dissatisfied'})

    return True, df_recibido


    

