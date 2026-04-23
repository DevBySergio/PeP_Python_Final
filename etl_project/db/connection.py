import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def get_database_url() -> str:
    """
    Construye la URL de conexión a partir de variables de entorno.
    Maneja valores por defecto para el host y el puerto.
    """
    user = os.environ.get("POSTGRES_USER")
    password = os.environ.get("POSTGRES_PASSWORD")
    db_name = os.environ.get("POSTGRES_DB")
    host = os.environ.get("POSTGRES_HOST", "localhost") # Cambiado a localhost para pruebas locales fuera de Docker
    port = os.environ.get("POSTGRES_PORT", "5432")

    # Validar que las variables críticas no sean None
    if not all([user, password, db_name]):
        raise ValueError("Faltan variables de entorno críticas para la conexión a la base de datos (POSTGRES_USER, POSTGRES_PASSWORD o POSTGRES_DB).")

    # Retornar cadena de conexión DATABASE_URL
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"


def get_engine() -> Engine:
    """
    Crea y devuelve un engine de SQLAlchemy.
    """
    database_url = get_database_url()
    
    # Creación del engine con las configuraciones recomendadas
    engine = create_engine(
        database_url,
        pool_pre_ping=True,  # Evita conexiones muertas
        echo=False           # No loggear SQL en producción
    )
    
    return engine