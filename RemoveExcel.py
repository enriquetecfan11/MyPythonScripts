import pandas as pd
import psycopg2

# Leer el archivo Excel
df = pd.read_excel('archivo_modificado.xlsx')

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    database='CuadernodeCampo',
    user='admin',
    password='admin1234'
)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Nombre de la tabla en la base de datos
tabla = 'fitosanitarios'

# Crear la tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS {} (
        id SERIAL PRIMARY KEY,
        sustancia TEXT,
        funcion TEXT,
        reglamento TEXT,
        inclusion TEXT,
        caducidad TEXT,
        principios TEXT,
        anexo TEXT
    )
""".format(tabla))

# Insertar los datos en la tabla
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO {} (sustancia, funcion, reglamento, inclusion, caducidad, principios, anexo)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """.format(tabla), row.tolist())

# Confirmar los cambios en la base de datos
conn.commit()

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
conn.close()
