from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import uuid

default_args = {
    'owner': 'patrick',
    'start_date': datetime(2026, 4, 30, 10,00),
}

def get_data():
    import requests
    import random

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError("Keine Daten erhalten")

    return random.choice(data)

def format_data(res):
    data = {}
    data['id'] = str(uuid.uuid4())
    data['post_id'] = res['id']
    data['user_id'] = res['userId']
    data['title'] = res['title']
    data['body'] = res['body']

    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: #1 minute
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send(
                'posts_stream',
                json.dumps(res).encode('utf-8')
            )
            time.sleep(2)

        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

with DAG('jsonplaceholder_posts_pipeline',
         default_args = default_args,
         schedule= '@daily',
         catchup = False) as dag:

    streaming_task = PythonOperator(
        task_id = 'stream_posts_from_api',
        python_callable = stream_data
    )

