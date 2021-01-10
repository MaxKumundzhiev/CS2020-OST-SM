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

import pickle
import pandas as pd

# from services.mongodb.utils import MongoFactory
from kafka import KafkaConsumer, KafkaProducer


DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")
DATABASE = os.environ.get("DATABASE")

MODEL = os.environ.get("MODEL")
MODELS_CHECKPOINT = os.environ.get("MODELS_CHECKPOINT")
TASK_TYPE = os.environ.get("TASK_TYPE")

DATASET = os.environ.get('DATASET')

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")

LEGIT_TOPIC = os.environ.get("LEGIT_TOPIC")
FRAUD_TOPIC = os.environ.get("FRAUD_TOPIC")


def get_model(path):
    assert os.path.exists(path), f'Error happened'
    with open(path, 'rb') as file:
        clf = pickle.load(file)
    return clf


if __name__ == "__main__":
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    model_path = os.path.join(MODELS_CHECKPOINT, DATASET, TASK_TYPE, MODEL, 'model.pkl')
    print(model_path)
    model = get_model(model_path)

    print(MODEL, MODELS_CHECKPOINT, DATABASE, DB_URL, DB_NAME)

    for message in consumer:
        # transaction: dict = message.value
        # topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        # producer.send(topic, value=transaction)
        # print(topic, transaction)  # DEBUG
        record: dict = message.value
        print(f"GET ROW {record}")  # DEBUG

        df = pd.DataFrame.from_dict(record, orient='index')
        # df = pd.DataFrame.from_dict(record, orient='index').T.values # uncomment once spark delivered
        # @TODO delete once spark is ready, because there will be no Nan values
        record = df.fillna(df.mean()).T.values

        prediction = model.predict(record)
        print(f'PREDICTION: {prediction}')
        topic = LEGIT_TOPIC
        print(f"NEXT ROW")  # DEBUG
