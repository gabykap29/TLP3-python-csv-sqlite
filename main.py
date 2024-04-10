from db import crear_tabla, cargar_datos,exportar_datos_por_provincia,borrar_tabla

#si existe, borrar la tabla
borrar_tabla()
#crear la tabla en la base de datos
crear_tabla() 
#funcion para cargar los datos en la bd
cargar_datos()
#funcion para exportar los datos por provincia en csv separados
exportar_datos_por_provincia()