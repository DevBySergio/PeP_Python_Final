"""
MÓDULO: etl.config

RESPONSABILIDAD:
- Centralizar TODA la configuración del pipeline.
- Evitar valores hardcodeados en el resto del código.

VARIABLES DE CONFIGURACIÓN:

RUTAS:
- INPUT_PATH → ruta donde se depositan los CSV de entrada
- OUTPUT_PATH → ruta donde se guardan los CSV transformados
- LOG_PATH → ruta de logs

PATRONES DE ARCHIVO:
- CLIENTES_PREFIX → "Clientes-"
- TARJETAS_PREFIX → "Tarjetas-"
- FILE_EXTENSION → ".csv"

BASE DE DATOS:
- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

SEGURIDAD:
- HASH_SALT → usado para anonimización

FORMATO DE FLAGS:
- FLAG_TRUE → "Y"
- FLAG_FALSE → "N"

INTERACCIÓN:
- Importado por TODOS los módulos ETL
- Fuente única de verdad para configuración

BUENAS PRÁCTICAS:
- Leer variables desde entorno (.env)
- Definir valores por defecto seguros
"""