-- Crear la tabla fitosanitarios
CREATE TABLE fitosanitarios (
    id SERIAL PRIMARY KEY,
    sustancia TEXT,
    funcion TEXT,
    reglamento TEXT,
    inclusion TEXT,
    caducidad TEXT,
    principios TEXT,
    anexo TEXT
);
