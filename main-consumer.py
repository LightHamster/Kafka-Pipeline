from consumer.consumer import consume_and_store
from consumer.plot_data import plot_pokemon_data, plot_digimon_data
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["poke_digi"]
collection = db["data"]

# Topics de Kafka
POKEMON_TOPIC = "pokemon_topic"
DIGIMON_TOPIC = "digimon_topic"

if __name__ == "__main__":
    print("Consumiendo datos de Pokémon...")
    consume_and_store(POKEMON_TOPIC, collection)

    print("Consumiendo datos de Digimon...")
    consume_and_store(DIGIMON_TOPIC, collection)

    # Graficar los datos
    print("Generando gráficos de Pokémon...")
    plot_pokemon_data(collection)

    print("Generando gráficos de Digimon...")
    plot_digimon_data(collection)