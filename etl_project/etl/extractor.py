"""

MÓDULO: etl.extractor

RESPONSABILIDAD:
- Descubrir y leer los ficheros de entrada.
- Filtrar solo los archivos válidos según patrón.

FUNCIONES:

1. list_input_files(input_path)
   - Lista todos los archivos disponibles en el directorio.
   - Retorna lista de nombres de archivo.

2. is_valid_file(filename, prefix)
   - Valida si el archivo cumple el patrón:
     PREFIX + YYYY-MM-DD + .csv
   - Retorna booleano.

3. filter_files_by_type(files, prefix)
   - Filtra archivos por tipo (Clientes o Tarjetas).

4. read_csv_file(file_path)
   - Lee CSV usando pandas con:
        sep=';'
        dtype=str
   - Manejo de errores:
        - encoding
        - líneas corruptas

VARIABLES CLAVE:
- input_path
- file_list
- clientes_files
- tarjetas_files

INTERACCIÓN:
- pipeline.py llama a este módulo para obtener DataFrames

SALIDA:
- DataFrames listos para transformación
"""

import os
import re
import pandas as pd

# 1. list_input_files(input_path)
def list_input_files(input_path):
    """Lista todos los archivos disponibles en el directorio."""
    try:
        return os.listdir(input_path)
    except FileNotFoundError:
        print(f"Error: La ruta {input_path} no existe.")
        return []

# 2. is_valid_file(filename, prefix)
def is_valid_file(filename, prefix):
    """Valida si el archivo cumple el patrón: PREFIX-YYYY-MM-DD.csv"""
    # Expresión regular para Prefijo-Año-Mes-Dia.csv
    pattern = rf"^{prefix}-\d{{4}}-\d{{2}}-\d{{2}}\.csv$"
    return bool(re.match(pattern, filename))

# 3. filter_files_by_type(files, prefix)
def filter_files_by_type(files, prefix):
    """Filtra la lista de archivos para quedarse solo con los del tipo indicado."""
    return [f for f in files if is_valid_file(f, prefix)]

# 4. read_csv_file(file_path)
def read_csv_file(file_path):
    """Lee el CSV usando pandas con separador ';' y tipos como string."""
    try:
        # Cargamos todo como string para no perder ceros a la izquierda (en DNIs o teléfonos)
        return pd.read_csv(file_path, sep=';', dtype=str, encoding='utf-8', on_bad_lines='warn')
    except Exception as e:
        print(f"Error al leer el archivo {file_path}: {e}")
        return None