# La base de datos
from auxiliares.db import db

# El logger
from classes.logger import Logger

# Funciones
from auxiliares.obtener_parametros import obtener_parametros
def crear_consulta(tabla, df):

    query = f'INSERT INTO {tabla} (\
        gender, customer_type, age, type_of_travel, class,\
        flight_distance, inflight_wifi_service, departure_arrival_time_convenient, ease_of_online_booking, gate_location,\
        food_and_drink, online_boarding, seat_comfort, inflight_entetairment, onboard_service, \
        leg_room_service, baggage_handling, checkin_service, cleanliness, inflight_service, \
        departure_delay_in_minutes, arrival_delay_in_minutes, satisfaction\
        ) VALUES (\
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\
        )'

    params = obtener_parametros(df)
    db.set_data(query, params)

    # Si la encuesta es incorrecta se graba también una copia el la tabla de correctos 
    # con el resultado cambiado, para tener más datos para futuros entrenamientos.
    if tabla != 'satisfaction':
        if 'neutral' in params[22]:
            params[22] = 'satisfied'
        else:
            params[22] = 'neutral or dissatisfied'
        query = query.replace('satisfaction_fallidos', 'satisfaction')
        db.set_data(query, params)

    if tabla == 'satisfaction':
        Logger.info("Grabada una encuesta correcta.")
    else:
        Logger.info("Grabada una encuesta incorrecta.")
