import pandas as pd

#leyendo los datos de asistencias
asistenciasDataFrame = pd.read_csv('./data/asistencia_estudiantes_completo.csv')
print(asistenciasDataFrame)

#obtener informacion basica del dataframe
#print(asistenciasDataFrame.info())

#obtener las ultimas filas del dataframe
#print(asistenciasDataFrame.tail())

#obtener las primeras filas del dataframe
#print(asistenciasDataFrame.head())

#obtener estadisticas de dataframe
#print(asistenciasDataFrame.describe())

#
#print(asistenciasDataFrame['estrato'].value_counts())

