from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from hdfs import InsecureClient

# HDFS connection
hdfs_client = InsecureClient('http://namenode:9870', user='root')

def send_csv_to_hdfs(file_name):
    local_path = f'/opt/airflow/data/{file_name}'
    hdfs_path = f'/raw/{file_name}'
    df = pd.read_csv(local_path)
    with hdfs_client.write(hdfs_path, encoding='utf-8', overwrite=True) as f:
        df.to_csv(f, index=False)

# DAG definition
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 9),
    'retries': 1
}

with DAG(
    dag_id='load_csvs_to_hdfs',
    default_args=default_args,
    schedule_interval=None,   
    catchup=False,
) as dag:

    load_churn = PythonOperator(
        task_id='load_churn_csv',
        python_callable=lambda: send_csv_to_hdfs('telco_customer_churn.csv')
    )

    load_payments = PythonOperator(
        task_id='load_payments_csv',
        python_callable=lambda: send_csv_to_hdfs('payments.csv')
    )

    load_complaint = PythonOperator(
        task_id='load_complaint_csv',
        python_callable=lambda: send_csv_to_hdfs('complaints.csv')
    )

    # Run all tasks in parallel
    [load_churn, load_payments, load_complaint]
