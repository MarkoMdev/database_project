from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.extract import download_transport_data

# Paramètres
URL = "https://data.sncf.com/explore/dataset/regularite-mensuelle-intercites/download/?format=csv"
SAVE_PATH = "/opt/airflow/data/raw/ponctualite.csv"

with DAG(
    dag_id="transport_data_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["transport", "etl"],
) as dag:

    extract_task = PythonOperator(
        task_id="extract_transport_data",
        python_callable=download_transport_data,
        op_args=[URL, SAVE_PATH],
    )

    extract_task
