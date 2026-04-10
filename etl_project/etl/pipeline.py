import pandas as pd
import os
from sqlalchemy import create_engine

from etl.anonymization import hash_value
from etl.validators import validate_dni, validate_phone, validate_email

DB_URL = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@postgres/{os.getenv('POSTGRES_DB')}"

INPUT_PATH = "/opt/airflow/data/input"
OUTPUT_PATH = "/opt/airflow/data/output"


def clean_str(value):
    if isinstance(value, str):
        return value.strip()
    return value


def run_pipeline():

    files = os.listdir(INPUT_PATH)

    clientes_files = [f for f in files if f.startswith("Clientes")]
    tarjetas_files = [f for f in files if f.startswith("Tarjetas")]

    engine = create_engine(DB_URL)

    # =========================
    # CLIENTES
    # =========================
    for file in clientes_files:

        df = pd.read_csv(f"{INPUT_PATH}/{file}", sep=';', dtype=str)

        df = df.applymap(clean_str)

        # Normalización básica
        df['correo'] = df['correo'].str.lower()

        # Validaciones
        df['dni_valid'] = df['dni'].apply(validate_dni)
        df['telefono_valid'] = df['telefono'].apply(validate_phone)
        df['correo_valid'] = df['correo'].apply(validate_email)

        # OK / KO (Y / N)
        df['dni_ok'] = df['dni_valid'].apply(lambda x: 'Y' if x else 'N')
        df['dni_ko'] = df['dni_valid'].apply(lambda x: 'N' if x else 'Y')

        df['telefono_ok'] = df['telefono_valid'].apply(lambda x: 'Y' if x else 'N')
        df['telefono_ko'] = df['telefono_valid'].apply(lambda x: 'N' if x else 'Y')

        df['correo_ok'] = df['correo_valid'].apply(lambda x: 'Y' if x else 'N')
        df['correo_ko'] = df['correo_valid'].apply(lambda x: 'N' if x else 'Y')

        # Hash DNI
        df['dni_hash'] = df['dni'].apply(hash_value)

        # Selección columnas finales
        df_final = df[[
            'cod cliente', 'nombre', 'apellido1', 'apellido2',
            'dni_hash', 'correo', 'telefono',
            'dni_ok', 'dni_ko',
            'telefono_ok', 'telefono_ko',
            'correo_ok', 'correo_ko'
        ]]

        # Renombrado columnas (IMPORTANTE por espacios)
        df_final.columns = [
            'cod_cliente', 'nombre', 'apellido1', 'apellido2',
            'dni_hash', 'correo', 'telefono',
            'dni_ok', 'dni_ko',
            'telefono_ok', 'telefono_ko',
            'correo_ok', 'correo_ko'
        ]

        # Guardar CSV limpio
        output_file = file.replace(".csv", ".cleaned.csv")
        df_final.to_csv(f"{OUTPUT_PATH}/{output_file}", sep=';', index=False)

        # Insert DB
        df_final.to_sql('clientes', engine, if_exists='append', index=False)

    # =========================
    # TARJETAS
    # =========================
    for file in tarjetas_files:

        df = pd.read_csv(f"{INPUT_PATH}/{file}", sep=';', dtype=str)

        df = df.applymap(clean_str)

        # Hash tarjeta
        df['numero_tarjeta_hash'] = df['numero_tarjeta'].apply(hash_value)

        # Hash CVV (nuevo requisito)
        df['cvv_hash'] = df['cvv'].apply(hash_value)

        # Selección columnas
        df_final = df[[
            'cod_cliente',
            'numero_tarjeta_hash',
            'cvv_hash',
            'fecha_exp'
        ]]

        # Guardar CSV limpio
        output_file = file.replace(".csv", ".cleaned.csv")
        df_final.to_csv(f"{OUTPUT_PATH}/{output_file}", sep=';', index=False)

        # Insert DB
        df_final.to_sql('tarjetas', engine, if_exists='append', index=False)