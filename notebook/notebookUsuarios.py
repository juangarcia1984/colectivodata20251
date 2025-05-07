import pandas as pd

usuariosDataFrame = pd.read_excel('./data/usuarios_sistema_completo.xlsx')
#print(usuariosDataFrame)
#print(usuariosDataFrame.isnull().sum())

#NECESITO SOLO UN LISTADO DE APRENDICES O ESTUDIANTES
aprendicesDataFrame = usuariosDataFrame.query('tipo_usuario=="estudiante"')
#print(aprendicesDataFrame)

#NECESITO UN LISTADO DE SOLO INSTRUCTORES O PROFESORES
instructoresDataFrame = usuariosDataFrame.query('tipo_usuario=="docente"')
#print(instructoresDataFrame)

#NECESITO UN LISTADO DE ESPECIALISTAS EN DESARROLLO WEB O SISTEMAS
especialistasDataFrame = usuariosDataFrame.query('especialidad == "Ingenieria de Sistemas" or especialidad == "Ingenieria Electronica"')
#print(especialistasDataFrame)

#NECESITO UN LISTADO DE SOLO USUARIOS CON DIRECCION EN MEDELLIN
usuariosMedellinDataFrame = usuariosDataFrame.query('direccion == "Medellin"')
#print(usuariosMedellinDataFrame)

#NECESITO UN LISTADO DE USUARIOS CUYA DIRECCION TERMINA EN SUR
usuariosSurDataFrame = usuariosDataFrame.query('direccion.str.endswith("Sur")')
#print(usuariosSurDataFrame)

#NECESITO UN LISTADO DE ESPECIALISTAS QUE CONTENGA LA PALABRA DATOS EN SU CARGO
especialistasDatosDataFrame = usuariosDataFrame.query('especialidad.str.contains("datos")')
#print(especialistasDatosDataFrame)


#NECESITO DOCENTES DE ITAGUI
instructoresItaguiDataFrame = usuariosDataFrame.query('direccion == "Itagui"')
#print(instructoresItaguiDataFrame)


#NECESITO UNA LISTA DE NACIDOS EN LOS 90 O ANTES
nacidos90DataFrame = usuariosDataFrame.query("fecha_nacimiento <= 1990-01-01")
#print(nacidos90DataFrame)


#NECESITO UN LISTADO DE INSTRUCTORES MAYORES
instructoresMayoresDataFrame = usuariosDataFrame.query('tipo_usuario == "docente" and fecha_nacimiento <= 1980')
#print(instructoresMayoresDataFrame)



#NECESITO UN LISTADO DE PROFESORES NACIDOS EN EL NUEVO MILENIO
instructoresNuevoMilenoDataFrame = usuariosDataFrame.query('tipo_usuario == "docente" and fecha_nacimiento >= 2000')
#print(instructoresNuevoMilenoDataFrame)
