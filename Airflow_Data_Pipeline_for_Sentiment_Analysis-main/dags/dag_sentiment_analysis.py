# Import modul
import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Menambahkan direktori plugins ke dalam path Python
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'plugins')) 

# Import modul yang dibutuhkan dari plugins
import finnhub_mongodb_loader
import sentiment_analysis_loader

# Default arguments untuk DAG
default_args = {
    'owner': 'de-team',
    'start_date': datetime(2023, 9, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Jadwal interval untuk DAG ('0 0 * * *' artinya setiap hari jam 00:00 UTC)
schedule_interval = '0 0 * * *'

# Definisi DAG
with DAG(
    dag_id='sentiment_analysis',
    default_args=default_args,
    schedule_interval=schedule_interval,
    catchup=False,
    tags=['machine-learning']
) as dag:

    # Task untuk mengeksekusi extract_load dari finnhub_mongodb_loader
    extract_load_task = PythonOperator(
        task_id='extract_load',
        python_callable=finnhub_mongodb_loader.extract_load,
    )

    # Task untuk mengeksekusi run_analysis dari sentiment_analysis_loader
    sa_load_task = PythonOperator(
        task_id='sa_load',
        python_callable=sentiment_analysis_loader.run_analysis,
    )

    # Mengatur dependency antara task extract_load dan sa_load
    extract_load_task >> sa_load_task
