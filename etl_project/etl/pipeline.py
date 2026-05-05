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
import os
import logging
from db.connection import get_engine
from etl.config import INPUT_PATH, OUTPUT_PATH, CLIENTES_PREFIX, TARJETAS_PREFIX
from etl.extractor import list_input_files, filter_files_by_type, read_csv_file
from etl.transformer import transform_clientes, transform_tarjetas
from etl.loader import load_clientes, load_tarjetas, save_output_csv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_pipeline() -> None:
    logger.info("Iniciando pipeline ETL")
    engine = get_engine()

    files = list_input_files(INPUT_PATH)
    clientes_files = filter_files_by_type(files, CLIENTES_PREFIX)
    tarjetas_files = filter_files_by_type(files, TARJETAS_PREFIX)

    for filename in clientes_files:
        path = os.path.join(INPUT_PATH, filename)
        df = read_csv_file(path)
        if df is None:
            continue
        result = transform_clientes(df)
        save_output_csv(result, OUTPUT_PATH, f"clean_{filename}")
        load_clientes(result, engine)
        logger.info("Procesado clientes: %s", filename)

    for filename in tarjetas_files:
        path = os.path.join(INPUT_PATH, filename)
        df = read_csv_file(path)
        if df is None:
            continue
        result = transform_tarjetas(df)
        save_output_csv(result, OUTPUT_PATH, f"clean_{filename}")
        load_tarjetas(result, engine)
        logger.info("Procesado tarjetas: %s", filename)

    logger.info("Pipeline ETL finalizado")