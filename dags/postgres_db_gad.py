from airflow.models import DAG
from datetime import datetime


with DAG(
    dag_id="postgres_db_dag",
    schedule_interval="@daily",
    start_date=datetime(2025, 2, 26),
) as dag:
    pass
