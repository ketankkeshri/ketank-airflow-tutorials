"""
Module: Simple Airflow DAG Example

This module defines a simple Apache Airflow DAG with a single task. The DAG uses the
BashOperator to execute a bash command that prints a greeting message.

Author: ketankkeshri
"""
__author__ = 'ketankkeshri'

from airflow import DAG
from airflow.operators.bash import BashOperator

## Create an Object of DAG class
dag = DAG(dag_id="ketank_simplest_dag")

## Create an Object of Bash Operator
##  The Operator will require task_id, bash command to run, and the DAG to associate this tak

bash_task = BashOperator(
    task_id='print_hello',
    # Bash command to be executed
    bash_command='echo "Hello, Welcome to the Ketan Keshri\'s Channel !!!"',
    dag=dag,
)
