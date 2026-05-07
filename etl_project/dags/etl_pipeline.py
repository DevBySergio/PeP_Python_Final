"""
DAG de Apache Airflow encargado de orquestar el pipeline ETL.
"""
from __future__ import annotations

import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

if "/opt/airflow" not in sys.path:
    sys.path.insert(0, "/opt/airflow")

from etl.pipeline import run_pipeline


default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "retries": 1,
}


with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    description="Pipeline ETL diario para clientes y tarjetas",
    start_date=datetime(2024, 1, 1),
    schedule="0 3 * * *",
    catchup=False,
    tags=["etl", "postgres", "csv"],
) as dag:
    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_pipeline,
    )

    run_etl
