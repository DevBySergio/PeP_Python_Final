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