"""
MÓDULO: etl.pipeline

RESPONSABILIDAD:
- Orquestar TODO el pipeline ETL.

FUNCIÓN PRINCIPAL:
- run_pipeline()

FLUJO:

1. Inicialización:
   - Cargar config
   - Crear conexión DB

2. Extracción:
   - Obtener lista de archivos
   - Filtrar clientes/tarjetas

3. Procesamiento CLIENTES:
   - Leer CSV
   - Transformar
   - Guardar CSV output
   - Insertar en DB

4. Procesamiento TARJETAS:
   - Mismo flujo

5. Logging:
   - Inicio
   - Fin
   - Errores

VARIABLES:
- clientes_files
- tarjetas_files
- engine

INTERACCIÓN:
- extractor
- transformer
- loader
- connection

OBJETIVO:
- Ser el punto único de ejecución del ETL
"""