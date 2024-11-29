from confluent_kafka import Consumer
from pymongo import MongoClient

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'poke_digi_group',
    'auto.offset.reset': 'earliest'
})

client = MongoClient("mongodb://localhost:27017/")
db = client["poke_digi"]
collection = db["data"]

def consume_and_store(topic, collection):
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)  # Espera de 1 segundo
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            data = msg.value().decode('utf-8')
            print(f"Received message: {data}")
            collection.insert_one({"topic": topic, "data": data})

    except KeyboardInterrupt:
        print("Consuming interrupted.")

    finally:
        consumer.close()
