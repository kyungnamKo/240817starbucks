from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator
from airflow.hooks.mysql_hook import MySqlHook
from datetime import datetime

# DAG 기본 설정
default_args = {
    'owner': 'airflow',
    'retries': 0,
}

dag = DAG(
    'dag01_insert_YMD',
    default_args=default_args,
)

def transfer_employee_data():
    # 소스 데이터베이스에서 데이터를 가져오는 MySQL hook 설정
    source_db = MySqlHook(mysql_conn_id='hugo_db')
    target_db = MySqlHook(mysql_conn_id='knko_db')
    
    # 소스 데이터베이스에서 employee 데이터를 가져오는 쿼리
    source_query = """
    SELECT employee_id, first_name, last_name, department_id, hire_date,
           YEAR(hire_date) AS hr_year, 
           MONTH(hire_date) AS hr_month, 
           DAY(hire_date) AS hr_day
    FROM employees;
    """
    
    # 소스 데이터베이스에서 데이터를 가져옴
    source_connection = source_db.get_conn()
    cursor = source_connection.cursor()
    cursor.execute(source_query)
    rows = cursor.fetchall()
    
    # 타겟 데이터베이스에 데이터 삽입
    target_connection = target_db.get_conn()
    target_cursor = target_connection.cursor()
    
    # 타겟 데이터베이스에 데이터 삽입 쿼리
    insert_query = """
    INSERT INTO employees_hiring (employee_id, first_name, last_name, department_id, hire_date, hr_year, hr_month, hr_day)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    first_name=VALUES(first_name), last_name=VALUES(last_name), department_id=VALUES(department_id), hire_date=VALUES(hire_date),
    hr_year=VALUES(hr_year), hr_month=VALUES(hr_month), hr_day=VALUES(hr_day);
    """
    
    # 각각의 row를 타겟 데이터베이스에 삽입
    for row in rows:
        target_cursor.execute(insert_query, row)
    
    # 변경사항 커밋
    target_connection.commit()
    cursor.close()
    target_cursor.close()

# PythonOperator로 데이터 전송 작업 정의
transfer_task = PythonOperator(
    task_id='transfer_employee_data_task',
    python_callable=transfer_employee_data,
    dag=dag,
)

transfer_task
