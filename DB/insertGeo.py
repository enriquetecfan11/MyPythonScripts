import psycopg2
import geopandas as gpd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from geoalchemy2 import Geometry

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener los valores de las variables de entorno
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

# Conectarse a la base de datos
try:
    connection = psycopg2.connect(user=db_user, password=db_password, host=db_host, port=db_port, database=db_name)
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Conectado a la base de datos:", record, "\n")
except Error as e:
    print("Error al conectarse a la base de datos:", e)

# Leer el archivo GeoJSON en un GeoDataFrame de GeoPandas
gdf = gpd.read_file('map2.geojson')

# Checkear que ha leído bien el archivo
print(gdf.head())

# Establecer la conexión a la base de datos PostgreSQL
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Crear la tabla en la base de datos
gdf.to_sql('sigpacvelez', engine, if_exists='replace', index=False, dtype={'geometry': Geometry('GEOMETRY', srid=4326)})

# Cargar los datos en la tabla
with engine.connect() as conn:
    conn.execute(f"ALTER TABLE nombre_tabla ADD PRIMARY KEY (id);")
    gdf.to_sql('nombre_tabla', conn, if_exists='append', index=False, method='multi')

# Cerrar la conexión a la base de datos
connection.close()
