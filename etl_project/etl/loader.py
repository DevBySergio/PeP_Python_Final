"""
MÓDULO: etl.loader

RESPONSABILIDAD:
- Insertar datos en la base de datos.

FUNCIONES:

1. load_clientes(df, engine)
   - Inserta en tabla 'clientes'
   - if_exists = 'append'

2. load_tarjetas(df, engine)
   - Inserta en tabla 'tarjetas'

3. save_output_csv(df, output_path, filename)
   - Guarda CSV transformado

VARIABLES:
- TABLE_CLIENTES
- TABLE_TARJETAS

INTERACCIÓN:
- pipeline.py
- db.connection.py

CONSIDERACIONES:
- Evitar duplicados (posible mejora futura)
- Manejo de errores de inserción
"""
import os
import pandas as pd

def load_clientes(df: pd.DataFrame, engine) -> None:
    df.to_sql("clientes", engine, if_exists="append", index=False)
    
def load_tarjetas(df: pd.DataFrame, engine) -> None:
    df.to_sql("tarjetas", engine, if_exists="append", index=False)
    
def save_output_csv(df: pd.DataFrame, output_path: str, filename: str) -> None:
    os.makedirs(output_path, exist_ok=True)
    df.to_csv(os.path.join(output_path, filename), sep=";", index=False)