import random
import requests
import time
import json
import os
import matplotlib.pyplot as plt

def monte_carlo(deck, lands, min_lands, max_lands, hands=10000):
    successes = 0
    deck_size = len(deck)
    land_counts = [0]*8  # 0–7 lands

    for _ in range(hands):
        sample_indices = random.sample(range(deck_size), 7)
        num_lands = sum(lands[i] for i in sample_indices)
        if 0 <= num_lands <= 7:
            land_counts[num_lands] += 1
        else:
            print("Unexpected number of lands in hand.")

        if min_lands <= num_lands <= max_lands:
            successes += 1

    percent = (successes / hands) * 100
    print(f"\nSuccesses: {successes} / {hands} hands ({percent:.2f}%) with {min_lands}–{max_lands} lands.\n")
    print("==== Land Count Distribution in Opening Hand ====")
    print("Lands | Hands   | Percent")
    print("-------------------------")
    for lands_in_hand in range(8):
        count = land_counts[lands_in_hand]
        pct = (count / hands) * 100
        print(f"{lands_in_hand:>5} | {count:>6} | {pct:>6.2f} %")
    print()

    # Generate histogram with matplotlib
    plt.bar(range(8), land_counts, tick_label=list(range(8)), color="#4D8CA9")
    plt.xlabel("Number of lands in opening hand")
    plt.ylabel("Number of hands")
    plt.title("MTG Commander Opening Hand Land Distribution")
    plt.tight_layout()
    plt.show()

    return percent

CACHE_FILENAME = "land_cache.json"

def load_cache(filename=CACHE_FILENAME):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache, filename=CACHE_FILENAME):
    with open(filename, "w") as f:
        json.dump(cache, f)

def is_land(card_name, cache):
    card_name_key = card_name.strip().lower()
    if card_name_key in cache:
        return cache[card_name_key]
    url = f'https://api.scryfall.com/cards/named?exact={card_name}'
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Could not find card: '{card_name}' on Scryfall. Assuming not a land.")
            result = False
        else:
            data = response.json()
            result = "Land" in data.get('type_line', "")
        cache[card_name_key] = result
        # Be polite to Scryfall!
        time.sleep(0.1)
        return result
    except Exception as e:
        print(f"Error fetching card '{card_name}': {e}")
        return False

def load_deck(filename):
    """
    Parse decklist file.
    Supports both '3 Forest' and 'Forest' notations.
    """
    deck = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if parts[0].isdigit():
                count = int(parts[0])
                card = " ".join(parts[1:])
            else:
                count = 1
                card = line
            deck.extend([card] * count)
    return deck

def precompute_lands(deck, cache):
    return [is_land(card, cache) for card in deck]

def monte_carlo(deck, lands, min_lands, max_lands, hands=10000):
    successes = 0
    deck_size = len(deck)
    land_counts = [0]*8  # 0–7 lands

    for _ in range(hands):
        sample_indices = random.sample(range(deck_size), 7)
        num_lands = sum(lands[i] for i in sample_indices)
        if 0 <= num_lands <= 7:
            land_counts[num_lands] += 1
        else:
            print("Unexpected number of lands in hand.")

        if min_lands <= num_lands <= max_lands:
            successes += 1

    percent = (successes / hands) * 100
    print(f"\nSuccesses: {successes} / {hands} hands ({percent:.2f}%) with {min_lands}–{max_lands} lands.\n")
    print("==== Land Count Distribution in Opening Hand ====")
    print("Lands | Hands   | Percent")
    print("-------------------------")
    for lands_in_hand in range(8):
        count = land_counts[lands_in_hand]
        pct = (count / hands) * 100
        print(f"{lands_in_hand:>5} | {count:>6} | {pct:>6.2f} %")
    print()

    # Generate histogram with matplotlib
    plt.bar(range(8), land_counts, tick_label=list(range(8)), color="#4D8CA9")
    plt.xlabel("Number of lands in opening hand")
    plt.ylabel("Number of hands")
    plt.title("MTG Commander Opening Hand Land Distribution")
    plt.tight_layout()
    plt.show()

    return percent

if __name__ == "__main__":
    main()