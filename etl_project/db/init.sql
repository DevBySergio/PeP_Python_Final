CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    correo TEXT,
    telefono TEXT,
    dni_hash TEXT,
    dni_ok CHAR(1),
    dni_ko CHAR(1),
    telefono_ok CHAR(1),
    telefono_ko CHAR(1),
    correo_ok CHAR(1),
    correo_ko CHAR(1)
);

CREATE TABLE IF NOT EXISTS tarjetas (
    id SERIAL PRIMARY KEY,
    id_cliente TEXT,
    numero_tarjeta_hash TEXT,
    cvv_hash TEXT,
    fecha_caducidad TEXT
);
