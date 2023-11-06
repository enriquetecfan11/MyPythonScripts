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
excel_file = 'VeleMalagaSigPac.xlsx'

# Nombre de la tabla en la base de datos
table_name = 'parcelas'

# Leer el archivo Excel en un DataFrame de pandas
df = pd.read_excel(excel_file)

try:
    connection = psycopg2.connect(user=db_user, password=db_password, host=db_host, port=db_port, database=db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Conectado a la base de datos:", record, "\n")

    #Crear la tabla en la base de datos cogiendo los datos de la primera fila
    sql_create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column_name in df.columns:
        sql_create_table_query += f'"{column_name}" TEXT, '
    sql_create_table_query = sql_create_table_query[:-2] + ");"
    cursor.execute(sql_create_table_query)

    #Si está bien, imprímelo
    print("Tabla creada correctamente en PostgreSQL\n")

    # Insertar los datos en la tabla
    for index, row in df.iterrows():
        sql_insert_query = f"INSERT INTO {table_name} VALUES ("
        for column_name in df.columns:
            sql_insert_query += f"'{row[column_name]}', "
        sql_insert_query = sql_insert_query[:-2] + ");"
        cursor.execute(sql_insert_query)
      
    connection.commit()
    print("Datos insertados correctamente en PostgreSQL\n")

except (Exception, Error) as error:
    print("Error al conectar o crear la tabla en PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexión a PostgreSQL cerrada")
