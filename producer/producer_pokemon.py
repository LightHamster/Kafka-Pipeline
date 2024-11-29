from confluent_kafka import Producer
import requests

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed for record {msg.key()}: {err}")
    else:
        print(f"Record {msg.key()} successfully produced to {msg.topic()} [{msg.partition()}]")

def produce_pokemon_data():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10')
    data = response.json()
    for pokemon in data['results']:
        producer.produce(
            topic='pokemon_topic',
            key=pokemon['name'],
            value=str(pokemon),
            callback=delivery_report
        )
        producer.flush()

if __name__ == "__main__":
    produce_pokemon_data()