"""
MÓDULO: etl.cleaning

RESPONSABILIDAD:
- Normalizar y limpiar los datos antes de validación.

FUNCIONES:

1. trim_strings(df)
   - Elimina espacios al inicio y final de todos los strings.

2. normalize_case(df)
   - nombre → capitalizado
   - correo → minúsculas

3. remove_accents(text)
   - Elimina tildes y caracteres especiales.

4. normalize_phone(phone)
   - Elimina todo excepto dígitos.

5. clean_dataframe(df)
   - Aplica todas las funciones anteriores de forma orquestada.

VARIABLES:
- STRING_COLUMNS → columnas tipo texto

INTERACCIÓN:
- transformer.py utiliza este módulo

OBJETIVO:
- Garantizar consistencia antes de validar
"""
import re
import unicodedata
import pandas as pd

def trim_strings(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
    return df
 
def remove_accents(text: str) -> str:
    if not isinstance(text, str):
        return text
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c))
 
def normalize_phone(phone: str) -> str:
    if not isinstance(phone, str):
        return phone
    return re.sub(r"\D", "", phone)
 
def normalize_case(df: pd.DataFrame) -> pd.DataFrame:
    if "nombre" in df.columns:
        df["nombre"] = df["nombre"].apply(lambda x: remove_accents(x).title() if isinstance(x, str) else x)
    if "correo" in df.columns:
        df["correo"] = df["correo"].apply(lambda x: x.lower() if isinstance(x, str) else x)
    if "telefono" in df.columns:
        df["telefono"] = df["telefono"].apply(normalize_phone)
    return df
 
def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = trim_strings(df)
    df = normalize_case(df)
    return df