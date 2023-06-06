# Usar la imagen oficial de PostgreSQL
FROM postgres

# Copiar el archivo SQL de inicialización a la imagen
COPY init.sql /docker-entrypoint-initdb.d/

# Configurar las variables de entorno de PostgreSQL
ENV POSTGRES_DB "cuadernodecampo"
ENV POSTGRES_USER "admin"
ENV POSTGRES_PASSWORD "mondejar"
ENV POSTGRES_HOST "localhost"
ENV POSTGRES_PORT 5432

# Exponer el puerto 5432 para la comunicación con la base de datos
EXPOSE 5432/tcp
