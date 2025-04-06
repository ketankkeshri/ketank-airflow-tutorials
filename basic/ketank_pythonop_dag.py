"""
Author: ketankkeshri

This module demonstrates how to create a basic Airflow DAG (Directed Acyclic Graph)
that utilizes the PythonOperator. It defines a Python function that gets executed
when the associated task is triggered in the DAG.

The DAG includes a single task that calls the Python function `pyop_fun` and prints
a welcome message to demonstrate the functionality of the PythonOperator.

Modules used:
- airflow: The main Airflow library for DAG and task management.
- airflow.operators.python: The PythonOperator used to trigger a Python function.

DAG Overview:
- A DAG named 'ketank_pythonop_dag' is created with one task.
- The task prints a greeting message to the console when executed.

"""

from airflow import DAG
from airflow.operators.python import PythonOperator

## Plain Python function, which will be called when the Task is triggered
def pyop_fun():
    """
    Function to print greeting messages.

    This function is called by the PythonOperator in the Airflow DAG. It prints
    a welcome message to the console.

    """
    print("Hello, Welcome to the Ketan Keshri's Channel !!!")
    print("This is a basic DAG to demonstrate PythonOperator in Airflow")

## Create an Object of DAG class
dag = DAG(dag_id="ketank_pythonop_dag")

## Create an Object of PythonOperator
## The Operator will require task_id, python_callable, and the DAG to associate this task with
bash_task = PythonOperator(
    task_id='print_hello',
    python_callable=pyop_fun,  # Python function to be executed
    dag=dag,
)
