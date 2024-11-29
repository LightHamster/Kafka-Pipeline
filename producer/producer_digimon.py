from confluent_kafka import Producer
import requests

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record {msg.key()} successfully produced to {msg.topic()} [{msg.partition()}]")

def produce_digimon_data():
    response = requests.get('https://digimon-api.vercel.app/api/digimon')
    data = response.json()

    # Limitamos a los primeros 10 Digimons
    for digimon in data[:10]:  # Solo toma los primeros 10 elementos
        producer.produce(
            topic='digimon_topic',
            key=digimon['name'],
            value=str(digimon),
            callback=delivery_report
        )
        producer.flush()

if __name__ == "__main__":
    produce_digimon_data()