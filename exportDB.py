# -*- coding: utf-8 -*-
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

from pandas import ExcelWriter
from pandas import Timestamp 

# Load environment variables from .env file
load_dotenv()

# Get the values of the environment variables
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

# Database connection
connection = psycopg2.connect(user=db_user, password=db_password, host=db_host, port=db_port, database=db_name)
cursor = connection.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("Conectado a la base de datos:", record, "\n")

# Excel file name save in folder BaseDatos is "base_datos.xlsx" + timestamp
excel_file = 'BaseDatos/base_datos_' + str(Timestamp('now').value) + '.xlsx'

# Crear una instancia de ExcelWriter
writer = ExcelWriter(excel_file)

# Iterate through all tables and export each one to a separate Excel sheet
for table in ['fitosanitarios', 'productos', 'maquinaria', 'personas', 'productos', 'fitosanitariosadds', 'actividades']:
    # Read the table into a DataFrame
    df = pd.read_sql(f'SELECT * FROM {table};', connection)

    # Iterate through each column of the DataFrame
    for column in df.columns:
        # Check if the column has datetime values
        if pd.api.types.is_datetime64_any_dtype(df[column]):
            # Convert the datetime values to strings without timezones
            df[column] = df[column].dt.strftime('%Y-%m-%d')

    # Export the DataFrame to an Excel sheet
    df.to_excel(writer, sheet_name=table, index=False)


# Guardar cambios en el archivo de Excel
writer.save()

# Cerrar el objeto writer
writer.close()

# Close the database connection
cursor.close()
connection.close()
