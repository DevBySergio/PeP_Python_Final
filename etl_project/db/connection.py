"""
MÓDULO: db.connection

RESPONSABILIDAD:
- Gestionar la conexión a la base de datos PostgreSQL.
- Centralizar la creación del engine de SQLAlchemy.
- Evitar duplicidad de lógica de conexión en el resto del proyecto.

OBJETIVO:
Proveer una función estándar (`get_engine`) que permita a cualquier módulo
(ETL, loader, etc.) obtener una conexión a la base de datos de forma consistente.

---

CONFIGURACIÓN:

Las credenciales y parámetros de conexión deben obtenerse desde variables
de entorno (definidas en el archivo .env), nunca hardcodeadas.

VARIABLES DE ENTORNO ESPERADAS:

- POSTGRES_USER       → Usuario de la base de datos
- POSTGRES_PASSWORD   → Contraseña
- POSTGRES_DB         → Nombre de la base de datos
- POSTGRES_HOST       → Host (por defecto: 'postgres' en Docker)
- POSTGRES_PORT       → Puerto (por defecto: 5432)

---

VARIABLES INTERNAS (NOMENCLATURA ESTÁNDAR):

- DB_USER             → Usuario
- DB_PASSWORD         → Contraseña
- DB_NAME             → Nombre de la base de datos
- DB_HOST             → Host del servicio
- DB_PORT             → Puerto
- DATABASE_URL        → Cadena de conexión completa

FORMATO DATABASE_URL:
postgresql+psycopg2://user:password@host:port/db_name

---

FUNCIONES:

1. get_database_url()
   - Construye la URL de conexión a partir de variables de entorno.
   - Debe manejar valores por defecto (host, port).
   - Devuelve string DATABASE_URL.

2. get_engine()
   - Crea y devuelve un engine de SQLAlchemy.
   - Debe ser reutilizable (singleton opcional).
   - Configuración recomendada:
        - pool_pre_ping=True (evita conexiones muertas)
        - echo=False (no loggear SQL en producción)

---

INTERACCIÓN CON OTROS MÓDULOS:

- etl.loader → utiliza get_engine() para insertar datos
- etl.pipeline → puede inicializar conexión general
- tests → pueden mockear esta función

---

BUENAS PRÁCTICAS A IMPLEMENTAR:

- No abrir conexiones manuales → usar SQLAlchemy engine
- No imprimir credenciales en logs
- Validar que variables críticas no sean None
- Posibilidad de lanzar excepción clara si falta configuración

---

POSIBLES EXTENSIONES FUTURAS:

- Soporte para múltiples bases de datos
- Pooling avanzado
- Reintentos de conexión
- Integración con secrets manager (AWS, Vault, etc.)

---

EJEMPLO DE USO (en otros módulos):

from db.connection import get_engine

engine = get_engine()

df.to_sql("clientes", engine, if_exists="append", index=False)

---

NOTA IMPORTANTE:

Este módulo NO debe:
- Ejecutar queries directamente
- Contener lógica de negocio
- Depender de pandas u otros módulos ETL

Su única responsabilidad es la conexión.
"""