import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#grafica de barras
colores = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F', '#8E44AD', '#E74C3C', '#3498DB', '#2ECC71', '#9B59B6', '#F39C12']

dataFrameAsistencia = pd.read_csv('./data/asistencia_estudiantes_completo.csv')

plt.figure(figsize=(8, 5))
sns.countplot(x='estado', data=dataFrameAsistencia, palette=colores)
plt.title('Cantidad de registros por estado')
plt.xlabel('Estado')
plt.ylabel('Cantidad de registros')
plt.tight_layout()
plt.show()

#grafica de torta
conteoTransporte = dataFrameAsistencia['medio_transporte'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(conteoTransporte, labels=conteoTransporte.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Blues"))
plt.title('Distribución por medios de transporte')
plt.tight_layout()
plt.show()

#barras agrupadas
plt.figure(figsize=(10, 6))
conteoEstadoMedioTransporte = dataFrameAsistencia.groupby(['estado', 'medio_transporte']).size().unstack(fill_value=0)
conteoEstadoMedioTransporte.plot(kind='bar', figsize=(10, 6), color=colores)
plt.title('Cantidad de registros por estado y medio de transporte')
plt.xlabel('Estados asistencia')
plt.ylabel('Medio de transporte')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#grafica de lineas
promedioTransporte = dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean().sort_values()
plt.figure(figsize=(10, 6))
plt.plot(promedioTransporte.index, promedioTransporte.values, marker='o', linestyle='-', color='purple')
plt.title('Promedio de estrato por medio de transporte')
plt.xlabel('Medio de transporte')
plt.ylabel('Promedio de estrato')
plt.grid(True)
plt.tight_layout()
plt.show()

