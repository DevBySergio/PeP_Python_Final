"""
DAG de Apache Airflow encargado de orquestar el pipeline ETL.

RESPONSABILIDAD:
- Definir el flujo de ejecución del pipeline.
- Programar la ejecución automática (cron).
- Invocar las funciones principales del ETL.

ELEMENTOS CLAVE:
- dag_id: nombre del pipeline (etl_pipeline)
- schedule_interval: ejecución diaria a las 03:00
- default_args: configuración base (owner, retries, etc.)

INTERACCIÓN:
- Importa y ejecuta la función principal desde etl.pipeline.run_pipeline()

MEJORAS FUTURAS:
- Separar en múltiples tareas:
  - extract_task
  - transform_task
  - load_task
"""