import pandas as pd
import psycopg2
import numpy as np
from psycopg2 import Error
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener los valores de las variables de entorno
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

# Ruta del archivo Excel a subir
excel_file = 'FitosanitarioFinal.xlsx'

# Nombre de la tabla en la base de datos
table_name = 'fitosanitarios'

# Leer el archivo Excel en un DataFrame de pandas
df = pd.read_excel(excel_file)

# Conexión a la base de datos
try:
    connection = psycopg2.connect(user=db_user, password=db_password, host=db_host, port=db_port, database=db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Conectado a la base de datos:", record, "\n")

    # Crear la tabla en la base de datos
    # cursor.execute(f"DROP TABLE IF EXISTS {table_name};")

    # create_table_query = f'''
    # CREATE TABLE IF NOT EXISTS {table_name} (
    #     id SERIAL PRIMARY KEY,
    #     sutanciaactiva TEXT,
    #     funcion TEXT,
    #     reglamento TEXT,
    #     inclusion TEXT,
    #     caducidad TEXT,
    #     principiosuniformes TEXT,
    #     anexoa TEXT
    # )
    # '''

    # cursor.execute(create_table_query)
    # connection.commit()

    # Ahora hay que insertar los datos del df en la tabla.
    for index, row in df.iterrows():
        if row.isnull().values.any():
            # Si hay algún valor nulo, reemplazarlo por un espacio en blanco
            row = row.replace(np.nan, ' ')

        # Sustituir los caracteres \n en los valores de texto
        row = row.apply(lambda x: x.replace('\n', ' ') if isinstance(x, str) else x)

        values = tuple(row)
        query = f"INSERT INTO {table_name} VALUES {values};"
        cursor.execute(query)

    # Confirmar los cambios en la base de datos
    connection.commit()
    print("Datos insertados correctamente.")

except Error as e:
    print("Error al conectarse a la base de datos:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexión cerrada.")
