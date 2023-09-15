import pandas as pd

def obtener_parametros(df):
    parametros = [
        str(df.loc[0, 'Gender']),
        str(df.loc[0, 'Customer Type']),
        int(df.loc[0, 'Age']),
        str(df.loc[0, 'Type of Travel']),
        str(df.loc[0, 'Class']),
        int(df.loc[0, 'Flight Distance']),
        int(df.loc[0, 'Inflight wifi service']),
        int(df.loc[0, 'Departure/Arrival time convenient']),
        int(df.loc[0, 'Ease of Online booking']),
        int(df.loc[0, 'Gate location']),
        int(df.loc[0, 'Food and drink']),
        int(df.loc[0, 'Online boarding']),
        int(df.loc[0, 'Seat comfort']),
        int(df.loc[0, 'Inflight entertainment']),
        int(df.loc[0, 'On-board service']),
        int(df.loc[0, 'Leg room service']),
        int(df.loc[0, 'Baggage handling']),
        int(df.loc[0, 'Checkin service']),
        int(df.loc[0, 'Inflight service']),
        int(df.loc[0, 'Cleanliness']),
        int(df.loc[0, 'Departure Delay in Minutes']),
        int(df.loc[0, 'Arrival Delay in Minutes']),
        str(df.loc[0, 'satisfaction'])
    ]
    return parametros
