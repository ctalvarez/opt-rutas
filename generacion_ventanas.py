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

days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
averages = ['prom-lunes', 'prom-martes', 'prom-miercoles', 'prom-jueves', 'prom-viernes', 'prom-sabado']
stds = ['std-lunes', 'std-martes', 'std-miercoles', 'std-jueves', 'std-viernes', 'std-sabado']
maxs = ['max-lunes', 'max-martes', 'max-miercoles', 'max-jueves', 'max-viernes', 'max-sabado']

inconsitencias = 0

for i in range(len(df_demandas)):
    for k in range(len(averages)):
        if type(df_locales[days[k]].iloc[i]) == list:
            if pd.notna(df_locales[days[k]].iloc[i][0]) and pd.notna(df_demandas[averages[k]].iloc[i]):
                continue
            elif (pd.notna(df_locales[days[k]].iloc[i][0]) or pd.notna(df_demandas[averages[k]].iloc[i])):
                print('index:', i)
                print('local:', df_locales['Nombre'][i])
                print('dia:', days[k], 'ventana:', df_locales[days[k]].iloc[i])
                print(df_demandas[averages[k]].iloc[i])
                print('-'*50)
                inconsitencias += 1
        else:
            if pd.notna(df_locales[days[k]].iloc[i]) and pd.notna(df_demandas[averages[k]].iloc[i]):
                continue
            elif (pd.notna(df_locales[days[k]].iloc[i]) or pd.notna(df_demandas[averages[k]].iloc[i])):
                print('index:', i)
                print('local:', df_locales['Nombre'][i])
                print('dia:', days[k], 'ventana:', df_locales[days[k]].iloc[i])
                print(df_demandas[averages[k]].iloc[i])
                print('-'*50)
                inconsitencias += 1
print('inconsitencias:', inconsitencias)

demands_average = [
    df_demandas['prom-lunes'],
    df_demandas['prom-martes'],
    df_demandas['prom-miercoles'],
    df_demandas['prom-jueves'],
    df_demandas['prom-viernes'],
    df_demandas['prom-sabado']
]
demands_std = [
    df_demandas['std-lunes'],
    df_demandas['std-martes'],
    df_demandas['std-miercoles'],
    df_demandas['std-jueves'],
    df_demandas['std-viernes'],
    df_demandas['std-sabado']
]

del df_demandas
del df_locales
