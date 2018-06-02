import pandas as pd

# set up
horarios = {
    'AM-1': [7, 11],
    'AM-2': [11, 15],
    'PM-1': [15, 19.5],
    'PM-2': [19, 23.5],
    'Municipal': [10, 17],
    'EntregaAM': [7.5, 10],
    'EntregaAM8': [8.5, 10],
    'EntregaAM11': [11.5, 12.30],
    'EntregaPM': [13.5, 15.5]
}

# obtener locales
df_locales = pd.read_excel('VIII-distancias-duraciones2.xlsx', sheet_name='locals')
locales = df_locales['Nombre']
empresa = df_locales['Empresa']

# obtener ventanas y restricciones
windows = [
    df_locales['Lunes'],
    df_locales['Martes'],
    df_locales['Miercoles'],
    df_locales['Jueves'],
    df_locales['Viernes'],
    df_locales['Sabado']
]
restricciones = df_locales['Restriccion']

for day in windows:
    for i in range(len(day)):
        try:
            day.iloc[i] = horarios[day.iloc[i]]
        except KeyError:
            pass

# obtener tamano anden
tamano_anden = df_locales['TamanoAnden']

# obtener demandas
df_demandas = pd.read_excel('VIII-distancias-duraciones2.xlsx', sheet_name='demandas')
demands = [
    df_demandas['Lunes'],
    df_demandas['Martes'],
    df_demandas['Miercoles'],
    df_demandas['Jueves'],
    df_demandas['Viernes'],
    df_demandas['Sabado']
]

