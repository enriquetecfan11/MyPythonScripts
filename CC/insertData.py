import psycopg2
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener las varibles de entorno
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')

# Configura la conexión a la base de datos
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)

# Checka la conxio a la base de datos
try:
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print("Conectado a la base de datos:", db_version, "\n")

except Error as e:
  print("Error al conectarse a la base de datos:", e)


# Crea un cursor para ejecutar las consultas
cur = conn.cursor()

try:
    # Inserciones para la tabla de actividades
    actividades = [
        ('Actividad 1', '2023-06-01', '2 horas', 1, 'Producto 1', 'Máquina 1', 'Personal 1', False, '2020-06-01', '2020-06-01'),
        ('Actividad 2', '2023-06-02', '3 horas', 2, 'Producto 2', 'Máquina 2', 'Personal 2', True, '2020-06-02', '2020-06-02'),
        ('Actividad 3', '2023-06-12', '3 horas', 2, 'Producto 2', 'Máquina 2', 'Personal 2', True, '2020-06-02', '2020-06-02'),
        ('Actividad 4', '2023-06-30', '3 horas', 2, 'Producto 2', 'Máquina 2', 'Personal 2', False, '2020-06-02', '2020-06-02'),
        ('Actividad 5', '2023-06-29', '3 horas', 2, 'Producto 2', 'Máquina 2', 'Personal 2', True, '2020-06-02', '2020-06-02'),
        ('Actividad 6', '2023-06-18', '3 horas', 2, 'Producto 2', 'Máquina 2', 'Personal 2', False, '2020-06-02', '2020-06-02'),
    ]

    # Ejecuta la inserción de actividades
    cur.executemany("""
        INSERT INTO public.actividades
        (actividad, fecha, tiempo, nparcela, producto, maquina, personal, hecho, "createdAt", "updatedAt")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, actividades)

    # Inserciones para la tabla maquinaria
    maquinaria = [
      ('Marca 1', 'AABBCC-1234', 'Tipo 1', '2020-01-01', 'Nº 1', '2020-06-02', '2020-06-02'),
      ('Marca 2', 'AABBCC-1234', 'Tipo 2', '2020-01-01', 'Nº 2', '2020-06-02', '2020-06-02'),
      ('Marca 3', 'AABBCC-1234', 'Tipo 3', '2020-01-01', 'Nº 3', '2020-06-02', '2020-06-02'),
      ('Marca 4', 'AABBCC-1234', 'Tipo 4', '2020-01-01', 'Nº 4', '2020-06-02', '2020-06-02'),
      ('Marca 5', 'AABBCC-1234', 'Tipo 5', '2020-01-01', 'Nº 5', '2020-06-02', '2020-06-02'),
      ('Marca 6', 'AABBCC-1234', 'Tipo 6', '2020-01-01', 'Nº 6', '2020-06-02', '2020-06-02'),
    ]

    # Ejecuta la inserción de maquinaria
    cur.executemany("""
        INSERT INTO public.maquinaria
        (marca, matricula, tipo, fechacompra, nroma, "createdAt", "updatedAt")
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, maquinaria)

    # Inserciones para la tabla personal
    personas = [
      ('Persona 1', 12345678, 1234, False, True, False, True, '2020-06-02', '2020-06-02'),
      ('Persona 2', 12345678, 1234, True, True, False, True, '2020-06-02', '2020-06-02'),
      ('Persona 3', 12345678, 1234, True, True, False, True, '2020-06-02', '2020-06-02'),
      ('Persona 4', 12345678, 1234, True, True, False, True, '2020-06-02', '2020-06-02'),
      ('Persona 5', 12345678, 1234, False, True, False, True, '2020-06-02', '2020-06-02'),
    ]

    # Ejecuta la inserción de personal
    cur.executemany("""
        INSERT INTO public.personas
        (nombre, nif, ninscripcion, carnetfito, cualificado, fumigacion, piloto, "createdAt", "updatedAt")
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,personas)

    # Inserciones para la tabla de productos
    productos = [
        ('Producto 1', 'Tipo 1', 100, '2020-06-02', '2020-06-02'),
        ('Producto 2', 'Tipo 2', 200, '2020-06-02', '2020-06-02'),
        ('Producto 3', 'Tipo 3', 300, '2020-06-02', '2020-06-02'),
        ('Producto 4', 'Tipo 4', 400, '2020-06-02', '2020-06-02'),
        ('Producto 5', 'Tipo 5', 500, '2020-06-02', '2020-06-02'),
        ('Producto 6', 'Tipo 6', 600, '2020-06-02', '2020-06-02'),
    ]

    # Ejecuta la inserción de productos
    cur.executemany("""
        INSERT INTO public.productos
        (nombre, tipo, cantidad, "createdAt", "updatedAt")
        VALUES (%s, %s, %s, %s, %s)
    """, productos)

    # Confirma los cambios en la base de datos
    conn.commit()
    print("Las inserciones se realizaron correctamente.")

except (Exception, psycopg2.DatabaseError) as error:
    # Si ocurre algún error, se realiza un rollback en la base de datos
    conn.rollback()
    print("Ocurrió un error al realizar las inserciones:", error)

finally:
    # Cierra el cursor y la conexión a la base de datos
    cur.close()
    conn.close()
