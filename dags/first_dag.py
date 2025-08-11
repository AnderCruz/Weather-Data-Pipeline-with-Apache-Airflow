from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    'primeiro_dag',
    start_date=datetime(2025, 8, 8),
    schedule='@daily',
    catchup=False
) as dag:

    task_1 = EmptyOperator(task_id = 'task_1')
    task_2 = EmptyOperator(task_id = 'task_2')
    task_3 = EmptyOperator(task_id = 'task_3')
    task_4 = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir -p /home/anderjcruz/airflow/folder_{{ ds }}',
    )

    task_1 >> [task_2, task_3]
    task_3 >> task_4