import numpy as np
from generacion_ventanas import *


def travel_time(origin, destiny):
    return df_tiempos_viaje.loc['{}'.format(origin), '{}'.format(destiny)]


def generate_route():
    pass


df_tiempos_viaje = pd.read_excel('VIII-distancias-duraciones2.xlsx', sheet_name='durations')
