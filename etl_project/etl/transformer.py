"""
MÓDULO: etl.transformer

RESPONSABILIDAD:
- Transformar los datos de entrada en datos listos para DB.

FUNCIONES:

1. transform_clientes(df)
   PROCESO:
   - Limpieza (cleaning.py)
   - Validación:
        dni_valid
        telefono_valid
        correo_valid
   - Generación flags:
        dni_ok / dni_ko
        telefono_ok / telefono_ko
        correo_ok / correo_ko
   - Anonimización:
        dni_hash
   - Selección y renombrado columnas

2. transform_tarjetas(df)
   PROCESO:
   - Limpieza
   - Anonimización:
        numero_tarjeta_hash
        cvv_hash
   - Eliminación de CVV original
   - Selección columnas finales

VARIABLES:
- CLIENTES_COLUMNS_FINAL
- TARJETAS_COLUMNS_FINAL

INTERACCIÓN:
- pipeline.py

OUTPUT:
- DataFrames listos para carga
"""
import pandas as pd
from etl.cleaning import clean_dataframe
from etl.validators import validate_dni, validate_phone, validate_email, generate_flag_pair
from etl.anonymization import hash_value

CLIENTES_COLUMNS_FINAL = [
    "nombre", "correo", "telefono", "dni_hash",
    "dni_ok", "dni_ko", "telefono_ok", "telefono_ko", "correo_ok", "correo_ko"
]

TARJETAS_COLUMNS_FINAL = [
    "id_cliente", "numero_tarjeta_hash", "cvv_hash", "fecha_caducidad"
]


def transform_clientes(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_dataframe(df)

    for col in ["dni", "telefono", "correo", "nombre"]:
        if col not in df.columns:
            df[col] = ""

    dni_valid = df["dni"].apply(validate_dni)
    tel_valid = df["telefono"].apply(validate_phone)
    mail_valid = df["correo"].apply(validate_email)

    df[["dni_ok", "dni_ko"]] = dni_valid.apply(lambda x: pd.Series(generate_flag_pair(x)))
    df[["telefono_ok", "telefono_ko"]] = tel_valid.apply(lambda x: pd.Series(generate_flag_pair(x)))
    df[["correo_ok", "correo_ko"]] = mail_valid.apply(lambda x: pd.Series(generate_flag_pair(x)))

    df["dni_hash"] = df["dni"].apply(hash_value)

    return df[CLIENTES_COLUMNS_FINAL]


def transform_tarjetas(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_dataframe(df)

    for col in ["id_cliente", "numero_tarjeta", "cvv", "fecha_caducidad"]:
        if col not in df.columns:
            df[col] = ""

    df["numero_tarjeta_hash"] = df["numero_tarjeta"].apply(hash_value)
    df["cvv_hash"] = df["cvv"].apply(hash_value)

    return df[TARJETAS_COLUMNS_FINAL]