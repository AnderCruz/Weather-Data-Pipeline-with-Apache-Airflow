from airflow.models import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from os.path import join
import pendulum
import pandas as pd
from datetime import timedelta

with DAG(
    'climate_data',
    start_date=pendulum.datetime(2022, 8, 22, tz='UTC'),
    schedule='0 0 * * 1'
) as dag:

    task_1 = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir -p "/home/anderjcruz/airflow/week={{ data_interval_end.strftime("%Y-%m-%d")}}"',

    )

    def extrai_dados_clima(data_interval_end):

        if isinstance(data_interval_end, str):
            data_interval_end = pendulum.parse(data_interval_end)

        start_date_str = data_interval_end.to_date_string()
        end_date_str = data_interval_end.add(days=7).to_date_string()

        city = 'Boston'
        key = '3QLZ6STEVZR6G2Y9U6A3NCQTH'

        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
            f'{city}/{start_date_str}/{end_date_str}?unitGroup=metric&include=days&key={key}&contentType=csv')

        dados = pd.read_csv(URL)

        file_path = f'/home/anderjcruz/airflow/week={start_date_str}/'

        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime','tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

    task_2 = PythonOperator(
        task_id='extrai_dados_clima',
        python_callable=extrai_dados_clima,
        op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    task_1 >> task_2

