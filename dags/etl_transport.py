import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "etl"))

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

from extract import download_transport_data
from transform import clean_transport_data
from load import load_dataframe_to_postgres

# Paramètres globaux
CSV_PATH = "/opt/airflow/data/raw/intercites_ponctualite.csv"
CLEAN_PATH = "/opt/airflow/data/clean/intercites_clean.parquet"
DATA_URL = "https://data.sncf.com/explore/dataset/regularite-mensuelle-intercites/download/?format=csv"
SCHEMA_PATH = "/opt/airflow/db/schema.sql"
DB_URL = "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"

# DAG Airflow
with DAG(
    dag_id="etl_transport_data",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["etl", "sncf", "intercites"]
) as dag:

    def extract():
        print("[EXTRACT] Téléchargement des données...")
        download_transport_data(DATA_URL, CSV_PATH)

    def transform(**context):
        print("[TRANSFORM] Nettoyage des données...")
        df = clean_transport_data(CSV_PATH)
        os.makedirs(os.path.dirname(CLEAN_PATH), exist_ok=True)
        df.to_parquet(CLEAN_PATH, index=False)
        context['ti'].xcom_push(key='clean_path', value=CLEAN_PATH)

    def load(**context):
        from pandas import read_parquet
        print("[LOAD] Chargement des données dans PostgreSQL...")
        clean_path = context['ti'].xcom_pull(task_ids='transform_task', key='clean_path')
        df = read_parquet(clean_path)
        load_dataframe_to_postgres(df, DB_URL, SCHEMA_PATH)

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load
    )

    extract_task >> transform_task >> load_task
