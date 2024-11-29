from producer.producer_pokemon import produce_pokemon_data
from producer.producer_digimon import produce_digimon_data

if __name__ == "__main__":
    print("Produciendo datos de Pokémon...")
    produce_pokemon_data()

    print("Produciendo datos de Digimon...")
    produce_digimon_data()