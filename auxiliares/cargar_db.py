# Importamos las librerías
import csv
import numpy as np
import pandas as pd

# La base de datos
from auxiliares.db import db, tabla

query = f'SELECT * FROM {tabla}'
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

def cargar_df():
    return df


