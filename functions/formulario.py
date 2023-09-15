import streamlit as st

# La base de datos
from auxiliares.db import db

# El modelo para la predicción
from auxiliares.prediccion import predecir

# Funciones
from auxiliares.crear_consulta import crear_consulta

resultado = None
df_prediccion = None

def formulario():
    global resultado
    global df_prediccion
    with st.form(key = 'my_form', clear_on_submit = True):
        columna1, columna2, columna3, columna4 = st.columns(4)
        with columna1:
            gender = st.selectbox("Gender:",  ['Male', 'Female'], key="gender")
            class_ = st.selectbox("Class:",  ['Eco', 'Eco Plus', 'Business'], key="class_")
            ease_online = st.selectbox("Ease Online Booking:", [0, 1, 2, 3, 4, 5], key="ease_online")
            seat_comfort = st.selectbox("Seat Comfort:", [0, 1, 2, 3, 4, 5], key="seat_comfort")
            baggage_handling = st.selectbox("Baggage Handling", [0, 1, 2, 3, 4, 5], key="baggage_handling")

        with columna2:
            c_type = st.selectbox("Customer Type:", ['Loyal Customer', 'disloyal Customer'], key="c_type")
            distance = st.number_input("Flight distance:", step=1, key="distance", min_value = 100, value = 100)
            gate_location = st.selectbox("Gate Location:", [0, 1, 2, 3, 4, 5], key="gate_location")
            entetairment = st.selectbox("Inflight Entetairment:", [0, 1, 2, 3, 4, 5], key="entetairment")
            checkin_service = st.selectbox("Checkin Service", [0, 1, 2, 3, 4, 5], key="checkin_service")
        
        with columna3:
            age = st.number_input("Age:", key="age", step = 1, min_value = 0, max_value = 100, value = 0)
            i_wifi_s = st.selectbox("Inflight Wifi:", [0, 1, 2, 3, 4, 5], key="i_wifi_s")
            food_drink = st.selectbox("Food and Drink:", [0, 1, 2, 3, 4, 5], key="food_drink")
            on_board_service = st.selectbox("On board service:", [0, 1, 2, 3, 4, 5], key="on_board_service")
            inflight_service = st.selectbox("Inflight Service", [0, 1, 2, 3, 4, 5], key="inflight_service")

        with columna4:
            travel_type = st.selectbox("Type of travel:", ['Business Travel', 'Personal Travel'], key="travel_type")
            dep_arr_conv = st.selectbox("Dep-Arr Covenient", [0, 1, 2, 3, 4, 5], key="dep_arr_conv")
            online_boarding = st.selectbox("Online boarding:", [0, 1, 2, 3, 4, 5], key="online_boarding")
            leg_room_service = st.selectbox("Leg Room service:", [0, 1, 2, 3, 4, 5], key="leg_room_service")
            cleanliness = st.selectbox("Cleanliness", [0, 1, 2, 3, 4, 5], key="cleanliness")

        columna5, columna6 = st.columns(2)
        with columna5:
            dep_delay = st.number_input("Departure delay minutes:", step = 1, key="dep_delay")
        
        with columna6:
            arr_delay = st.number_input("Arrival delay minutes:", step = 1, key="arr_delay")

        columna7, columna8, columna9, columna10 = st.columns(4)
        with columna7:
            if st.form_submit_button("Enviar"):
                params = [
                            gender, c_type, age, travel_type, class_, 
                            distance, i_wifi_s, dep_arr_conv, ease_online, gate_location, 
                            food_drink, online_boarding, seat_comfort, entetairment, on_board_service,
                            leg_room_service, baggage_handling, checkin_service, inflight_service, cleanliness, 
                            dep_delay, arr_delay 
                         ]
                resultado, df_prediccion = predecir(params)
                st.write('La predicción es:')
                st.write(str(df_prediccion.loc[0, 'satisfaction']))

        with columna8:
            if st.form_submit_button("Reset"):
                resultado = None
                df_prediccion = None

        with columna9:
            if st.form_submit_button("Correcto"):
                if resultado is None:
                    st.info("Debe hacer una predicción.")
                else:
                    crear_consulta('satisfaction', df_prediccion)
                    st.success("Predicción almacenada como correcta.")
                    resultado = None

        with columna10:
            if st.form_submit_button("Incorrecto"):
                if resultado is None:
                    st.info("Debe hacer una predicción.")
                else:
                    crear_consulta('satisfaction_fallidos', df_prediccion)
                    st.warning("Predicción almacenada como incorrecta.")
                    resultado = None

    