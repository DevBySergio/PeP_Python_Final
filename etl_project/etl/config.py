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
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_PATH = os.path.join(BASE_DIR, "data", "input")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output")
LOG_PATH = os.path.join(BASE_DIR, "logs")

CLIENTES_PREFIX = "Clientes"
TARJETAS_PREFIX = "Tarjetas"
FILE_EXTENSION = ".csv"

DB_HOST = os.getenv("POSTGRES_HOST", "postgres")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "etl_db") 
DB_USER = os.getenv("POSTGRES_USER", "etl_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "etl_pass")

HASH_SALT = os.getenv("HASH_SALT", "default_salt_change_me")

FLAG_TRUE = "Y"
FLAG_FALSE = "N"