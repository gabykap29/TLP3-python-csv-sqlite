# Proyecto de Python CSV y SQLite

Este proyecto consiste en una aplicación escrita en Python para manejar datos de localidades y provincias utilizando archivos CSV y una base de datos SQLite.

## Funcionalidades

- **Crear tabla en la base de datos:** La función `crear_tabla()` crea una tabla llamada `provincias` en la base de datos SQLite si no existe. Esta tabla tiene tres columnas: `id`, `nombre` y `provincia`.

- **Cargar datos desde un archivo CSV:** La función `cargar_datos()` carga datos desde un archivo CSV llamado `localidades.csv` y los inserta en la tabla `provincias` de la base de datos.

- **Exportar datos por provincia:** La función `exportar_datos_por_provincia()` exporta los datos de cada provincia a archivos CSV separados en una carpeta llamada `provincias`. Cada archivo CSV contiene los datos de las localidades de una provincia específica.

## Uso

1. Tener Python instalado en tu sistema.
2. Ejecuta el script principal `main.py` para realizar las operaciones correspondientes.

## Estructura del Proyecto

- `main.py`: Script principal que utiliza las funciones del módulo `db.py` para interactuar con la base de datos.
- `db.py`: Contiene las funciones para crear la tabla, cargar datos desde un archivo CSV y exportar datos por provincia.
- `localidades.csv`: Archivo CSV que contiene los datos de las localidades a cargar en la base de datos.
- `provincias/`: Carpeta donde se guardarán los archivos CSV exportados para cada provincia.

