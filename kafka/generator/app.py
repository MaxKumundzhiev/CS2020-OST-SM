# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import os
import json
from time import sleep
from typing import List

from kafka import KafkaProducer

from generator import validate_dataset, get_dataset


LEVEL = os.environ.get('LEVEL')
MODEL = os.environ.get('MODEL')
DATASET = os.environ.get('DATASET')  # CICIDC2017
KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    print(LEVEL, DATASET)
    dataset_path = validate_dataset(dataset=DATASET)
    print(dataset_path)
    dataset: List[dict] = get_dataset(dataset_path)
    print(dataset)
    _n_records = len(dataset)
    for row_index, row in enumerate(dataset):
        producer.send(TRANSACTIONS_TOPIC, value=row)
        print(f'{row_index}/{_n_records}: {row}')  # DEBUG
        sleep(SLEEP_TIME)



