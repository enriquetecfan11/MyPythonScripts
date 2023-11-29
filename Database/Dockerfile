# Utiliza la imagen base de PostgreSQL
FROM postgres:latest

# Instala las extensiones de PostGIS y las herramientas relacionadas
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-13-postgis-3 \
        postgresql-13-postgis-3-scripts \
        postgis \
    && rm -rf /var/lib/apt/lists/*

# Copia un archivo SQL para inicializar la base de datos
COPY init.sql /docker-entrypoint-initdb.d/

# Expone el puerto 5432 para acceder a la base de datos
EXPOSE 5432
