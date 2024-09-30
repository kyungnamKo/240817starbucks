from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook
from datetime import datetime

# DAG 기본 설정
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 1),
    'retries': 1,
}

dag = DAG(
    'mysql_to_mysql_etl_operator_with_python',
    default_args=default_args,
    schedule_interval=None,  # 수동 실행을 위해 None으로 설정
    catchup=False
)

# Task 1: MySQL에서 데이터 추출
extract_task = MySqlOperator(
    task_id='extract_data_task',
    mysql_conn_id='source_mysql',
    sql="SELECT * FROM employees;",
    dag=dag,
    database='test_db',
    do_xcom_push=True  # XCom에 결과를 저장하여 후속 태스크에서 사용할 수 있도록 설정
)

# Task 2: 데이터를 연도, 월, 일로 변환
def transform_data(**kwargs):
    # XCom에서 추출된 데이터 가져오기
    rows = kwargs['ti'].xcom_pull(task_ids='extract_data_task')

    # 데이터 변환 로직
    transformed_data = []
    for row in rows:
        employee_id, first_name, last_name, department_id, hire_date = row
        year, month, day = hire_date.year, hire_date.month, hire_date.day
        transformed_data.append((employee_id, first_name, last_name, department_id, hire_date, year, month, day))

    # 변환된 데이터를 XCom에 저장
    kwargs['ti'].xcom_push(key='transformed_data', value=transformed_data)

transform_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform_data,
    provide_context=True,  # context를 제공하여 XCom을 사용할 수 있도록 설정
    dag=dag
)

# Task 3: 변환된 데이터를 다른 MySQL로 적재
def load_data(**kwargs):
    transformed_data = kwargs['ti'].xcom_pull(task_ids='transform_data_task', key='transformed_data')
    
    # MySQL로 데이터 적재
    mysql_hook = MySqlHook(mysql_conn_id='target_mysql', schema='employee_db')
    
    # 데이터 삽입 쿼리
    insert_query = """
    INSERT INTO employees_hiring (employee_id, first_name, last_name, department_id, hire_date, hr_year, hr_month, hr_day)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # 데이터 삽입
    for data in transformed_data:
        mysql_hook.run(insert_query, parameters=data)

load_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    provide_context=True,
    dag=dag
)

# Task의 실행 순서 설정
extract_task >> transform_task >> load_task
