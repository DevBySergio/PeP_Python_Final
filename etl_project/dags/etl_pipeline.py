from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow')

from etl.pipeline import run_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    'etl_pipeline',
    default_args=default_args,
    schedule_interval='0 3 * * *',  # 03:00 AM
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id='run_etl',
        python_callable=run_pipeline
    )

    run_etl