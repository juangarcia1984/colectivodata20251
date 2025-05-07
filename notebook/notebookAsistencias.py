import pandas as pd

#leyendo los datos de asistencias
asistenciasDataFrame = pd.read_csv('./data/asistencia_estudiantes_completo.csv')
#print(asistenciasDataFrame)

#obtener informacion basica del dataframe
#print(asistenciasDataFrame.info())

#obtener las ultimas filas del dataframe
#print(asistenciasDataFrame.tail())

#obtener las primeras filas del dataframe
#print(asistenciasDataFrame.head())

#obtener estadisticas de dataframe
#print(asistenciasDataFrame.describe())

#obtener estadisticas de dataframe por columnas
#print(asistenciasDataFrame['estrato'].value_counts())


#FILTROS O CONSULTAS DETALLADAS
#NECESITO ENCONTRAR LOS ESTUDIANTES QUE SI ASISTIERON
estudiantesQueAsistieron = asistenciasDataFrame.query('estado=="asistio"')
#print(estudiantesQueAsistieron)

#NECESITO ENCONTRAR LOS ESTUDIANTES QUE NO ASISTIERON
estudiantesQueNoAsistieron = asistenciasDataFrame.query('estado=="inasistencia"')


#NECESITO ENCONTRAR LOS ESTUDIANTES QUE LLEGARON TARDE (JUSTIFICARON)
estudiantesQueLlegaronTarde = asistenciasDataFrame.query('estado=="justificado"')

#NECESITO ENCONTRAR LOS ESTUDIANTES DE ESTTRATO 1
estudiantesEstrato1 = asistenciasDataFrame.query('estrato==1')

#NECESITO ENCONTRAR LOS ESTUDIANTES DE ESTRATOS ALTOS
estudiantesEstratosAltos = asistenciasDataFrame.query('estrato>=4')

#NECESITO ENCONTRAR ESTUDIANTES QUE LLEGAN EN METRO
estudiantesQueLleganEnMetro = asistenciasDataFrame.query('medio_transporte=="metro"')
#print(estudiantesQueLleganEnMetro)

#NECESITO ENCONTRAR ESTUDIANTES QUE LLEGAN EN BICICLETA
estudiantesQueLleganEnBicicleta = asistenciasDataFrame.query('medio_transporte=="bicicleta"')

#NECESITO ENCONTRAR TODOS LOS ESTUDIANTES MENOS LOS QUE LLEGARON A PIE
estudiantesQueLleganAPie = asistenciasDataFrame.query('medio_transporte!="a pie"')

#NECESITO TODOS LOS REGISTROS DE ASISTENCIA DE JUNIO
estudiantesJunio = asistenciasDataFrame.query('fecha=="2025-06-01" or fecha=="2025-06-02"')
#print(estudiantesJunio)

#NECESITO TODOS LOS ESTUDIANTES QUE USAN TRANSPORTE ECOLOGICO
estudiantesTransporteEcologico = asistenciasDataFrame.query('medio_transporte=="bicicleta" or medio_transporte=="a pie"')
#print(estudiantesTransporteEcologico)

#NECESITO USAN BUS Y SON DE ESTRATO ALTOS
estudiantesEstratoAltoBus = asistenciasDataFrame.query('medio_transporte=="bus" and estrato>=4')
print(estudiantesEstratoAltoBus)

#NECESITO USAN BUS Y SON DE ESTRATO BAJO
estudiantesEstratoBajoBus = asistenciasDataFrame.query('medio_transporte=="bus" and estrato<=3')
#print(estudiantesEstratoBajoBus)

#NECESITO ESTUDIANTES QUE CAMINAN PARA LLEGAR A CLASE
estudiantesQueCaminan = asistenciasDataFrame.query('medio_transporte=="a pie"')
#print(estudiantesQueCaminan)

#CONTEOS POR AGRUPACIONES
#NECESITO EL CONTEO POR REGISTROS POR ESTADO DE ASISTENCIA
conteoAsistencia= asistenciasDataFrame.groupby('estado').size()
#print(conteoAsistencia)

#NECESITO OBTENER EL NUMERO DE REGISTROS POR ESTRATO
conteoEstrato= asistenciasDataFrame.groupby('estrato').size()
#print(conteoEstrato)

#NECESITO LA CANTIDAD DE ESTUDIANTES POR MEDIO DE TRANSPORTE
conteoMedioTransporte= asistenciasDataFrame.groupby('medio_transporte').size()
#print(conteoMedioTransporte)

#NECESITO EL PROMEDIO DE ESTRATO POR ESTADO DE ASISTENCIA
promedioEstrato= asistenciasDataFrame.groupby('estado')['estrato']
#print(promedioEstrato.mean())

#MAXIMO ESTRATO POR ESTADO
maximoEstrato= asistenciasDataFrame.groupby('estado')['estrato']
#print(maximoEstrato.max())

#MINIMO ESTRATO POR ESTADO
minimoEstrato= asistenciasDataFrame.groupby('estado')['estrato']
#print(minimoEstrato.min())

#NECESITO UN CONTEO DE ASISTENCIAS POR GRUPO Y ESTADO
conteoAsistenciasPorGrupo= asistenciasDataFrame.groupby(['grupo','estado']).size()
#print(conteoAsistenciasPorGrupo)