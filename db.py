import _sqlite3
import os
import csv
connectDB = _sqlite3.connect('provincias.db')
def crear_tabla():
    try:
        # Crear la tabla
        connectDB = _sqlite3.connect('provincias.db')
        cursor = connectDB.cursor()
        cursor.execute('''
            CREATE TABLE provincias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                provincia TEXT NOT NULL
            )
        ''')
        connectDB.commit()
        # en caso de error mostrar el mensaje de error
    except _sqlite3.OperationalError as error:
        print(f'Error al crear la tabla: {error}')
        
    # Cerrar la conexión y el cursor
    finally:
        cursor.close()
        connectDB.close()
    
#Borrar tabla
def borrar_tabla():
    try:
        connectDB = _sqlite3.connect('provincias.db')
        cursor = connectDB.cursor()
        cursor.execute('DROP TABLE provincias')
        connectDB.commit()
        print('Tabla borrada exitosamente')
    except _sqlite3.OperationalError as error:
        print(f'Error al borrar la tabla: {error}')
    finally:
        cursor.close()
        connectDB.close()

# Cargar datos desde un archivo CSV
def cargar_datos():
    connectDB = _sqlite3.connect('provincias.db')
    cursor = connectDB.cursor()
    with open('localidades.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        # Saltear la primer fila que contiene los nombres de las columnas
        next(lector)
        for fila in lector:
            provincia = fila[0]
            id_localidad = fila[1]
            localidad = fila[2]
            cp = fila[3]
            id_prov_mstr = fila[4]
            cursor.execute('''
                INSERT INTO provincias (nombre, provincia)
                VALUES (?, ?)
            ''', (localidad, provincia))
    connectDB.commit()
    cursor.close()  # Cerrar el cursor después de usarlo
    connectDB.close()  # Cerrar la conexión después de usarla




def exportar_datos_por_provincia():
    try: 
        connectDB = _sqlite3.connect('provincias.db')
        cursor = connectDB.cursor()
        cursor.execute('SELECT DISTINCT provincia FROM provincias')
        provincias = cursor.fetchall()
        
        for provincia in provincias:
            nombre_provincia = provincia[0]
            cursor.execute('SELECT * FROM provincias WHERE provincia = ?', (nombre_provincia,))
            datos_provincia = cursor.fetchall()
            
            # Crear un archivo CSV para cada provincia
            #crear una carpeta para guardar los archivos
            if not os.path.exists('./provincias'):
                os.makedirs('./provincias')
                
            nombre_archivo = f'./provincias/{nombre_provincia}.csv'
            with open(nombre_archivo, 'w', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerow(['ID', 'Nombre', 'Localidades'])
                escritor_csv.writerows(datos_provincia)
            
            print(f"Datos exportados para la provincia {nombre_provincia}")
    except _sqlite3.OperationalError as error:
        print(f'Error al exportar los datos: {error}')
    except open as error:
        print(f'Error al abrir el archivo: {error}')
    finally:
        cursor.close()
        connectDB.close()


