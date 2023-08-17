import datetime as dt
from extract import Extract
from transform import Transform
from load import Load
from airflow import DAG
from airflow.operators.python import PythonOperator

args = {
    'retries' : 2,
    'retry_delay' : dt.timedelta(minutes=1),
    'email_on_retry' : False,
    'email_on_failure' : False,
}

dag = DAG(
    'etl_dag',
    default_args=args,
    start_date=dt.datetime(2023,8,16),
    schedule=dt.timedelta(days=1),
    catchup=True
)

def run_etl():
    extract = Extract()
    df = extract.extract_data_gcp()
    transform = Transform(df)
    transformed_df = transform.transform_df_data()
    load = Load(transformed_df)
    load.load_data_bq()

PythonOperator(
    task_id = "run_etl",
    python_callable=run_etl,
    dag=dag
)
