# Librerías de tratamiento de datos
import numpy as np
import pandas as pd

# Librerías de ML
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from lightgbm import LGBMClassifier

import pickle

# La base de datos
from auxiliares.db import db, tabla

def entrenamiento():
    query = f'SELECT * FROM  {tabla}'
    data = db.get_data(query)
    lineas = []
    for linea in data:
        lineas.append(linea[1:])
    columns = ['Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class',  
    'Flight Distance', 'Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking', 'Gate location', 
    'Food and drink', 'Online boarding', 'Seat comfort', 'Inflight entertainment', 'On-board service', 
    'Leg room service', 'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness', 
    'Departure Delay in Minutes', 'Arrival Delay in Minutes', 'satisfaction']

    df = pd.DataFrame(lineas, columns = columns)

    ### Convertimos la columna satisfaction en booleana con 0 o 1
    df['satisfaction'] = df['satisfaction'].map({'satisfied': 1, 'neutral or dissatisfied': 0})

    # Codificar a one-hot las columnas 'Gender', 'Customer Type', 'Type of Travel' y 'Class'
    columnas_a_codificar = ['Gender', 'Customer Type', 'Type of Travel', 'Class']
    # Usa pd.get_dummies() para realizar la codificación one-hot
    df = pd.get_dummies(df, columns=columnas_a_codificar, drop_first=False)

    # Determinamos las variables de entrada y la variable objetivo
    X_train = df.drop('satisfaction', axis=1)  # Características
    y_train = df['satisfaction']  # Etiquetas o valores objetivo

    # Convertimos las columnas booleanas de entrada, que tienen valores True y False a 1 y 0
    cols_boolean = [
        'Gender_Female', 'Gender_Male', 'Customer Type_Loyal Customer', 'Customer Type_disloyal Customer', 
        'Type of Travel_Business Travel', 'Type of Travel_Personal Travel', 'Class_Business',
        'Class_Eco', 'Class_Eco Plus'
    ]
    for col in cols_boolean:
        X_train[col] = X_train[col].astype(int)

    # Hacemos el escalado de los datos de entrada, como paso previo al entrenamiento.
    # Crea una instancia de StandardScaler
    scaler = StandardScaler()
    # Ajusta y transforma los datos de entrenamiento
    X_train_scaled = scaler.fit_transform(X_train)

    # El entrenamiento
    lgbm_model = LGBMClassifier(random_state=42)
    lgbm_model.fit(X_train_scaled, y_train)
    # Aquí no hay predicciones porque no hay conjunto de test. 
    # Todos los datos se han usado para entrenamiento. 

    with open('pickle/train.pkl', 'wb') as pkl:
        pickle.dump(lgbm_model, pkl)
    # return lgbm_model

