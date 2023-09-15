# Librería de base de datos
from classes import database

import json # Librería json

# Leemos los datos de acceso
try:
    with open('conf/env.json', 'r') as datafile:
        data = json.load(datafile)
    db = database.DBAccess(engine = data['engine'], port = data['port'], host = data['host'], user = data['user'], password = data['password'])
except:
    db = database.DBAccess()

# Creamos la conexión a la base de datos
db.create_connection()
db.create_cursor()
db.select_database('aerolinea')

tabla = 'satisfaction'
