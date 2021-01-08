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

from mongodb.handler import Factory
from kafka import KafkaConsumer, KafkaProducer

DB_URL = os.environ.get("DB_URL")
DB_NAME = os.environ.get("DB_NAME")

MODEL = os.environ.get("MODEL")

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
LEGIT_TOPIC = os.environ.get("LEGIT_TOPIC")
FRAUD_TOPIC = os.environ.get("FRAUD_TOPIC")


def is_suspicious(transaction: dict) -> bool:
    """Determine whether a transaction is suspicious."""
    return transaction["amount"] >= 900


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
    print(MODEL, DB_URL, DB_NAME)
    for message in consumer:
        # transaction: dict = message.value
        # topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        # producer.send(topic, value=transaction)
        # print(topic, transaction)  # DEBUG
        print(f"GET ROW {message.value}")  # DEBUG
        record: dict = message.value
        topic = LEGIT_TOPIC
        # print(f'WRITING TO MONGO: {record}')
        # producer.send(topic, value=record)
        Factory().run(record)
        print(f"NEXT ROW")  # DEBUG
