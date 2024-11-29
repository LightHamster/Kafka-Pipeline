import matplotlib.pyplot as plt

def plot_pokemon_data(collection):
    data = collection.find({"topic": "pokemon_topic"})
    names = [d['data']['name'] for d in data]
    counts = range(len(names))

    plt.bar(counts, [1] * len(names), tick_label=names)
    plt.title("Pokémon Names")
    plt.show()

def plot_digimon_data(collection):
    data = collection.find({"topic": "digimon_topic"})
    names = [d['data']['name'] for d in data]
    counts = range(len(names))

    plt.bar(counts, [1] * len(names), tick_label=names)
    plt.title("Digimon Names")
    plt.show()
