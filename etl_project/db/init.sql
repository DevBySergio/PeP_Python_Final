CREATE TABLE IF NOT EXISTS clientes (
    cod_cliente TEXT PRIMARY KEY,
    nombre TEXT,
    apellido1 TEXT,
    apellido2 TEXT,
    dni_hash TEXT,
    correo TEXT,
    telefono TEXT,

    dni_ok CHAR(1),
    dni_ko CHAR(1),

    telefono_ok CHAR(1),
    telefono_ko CHAR(1),

    correo_ok CHAR(1),
    correo_ko CHAR(1)
);

CREATE TABLE IF NOT EXISTS tarjetas (
    id SERIAL PRIMARY KEY,
    cod_cliente TEXT,
    numero_tarjeta_hash TEXT,
    cvv_hash TEXT,
    fecha_exp TEXT
);