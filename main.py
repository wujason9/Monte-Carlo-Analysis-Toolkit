import random
import matplotlib.pyplot as plt

def simulate_lands_in_hand(deck_size=100, num_lands=37, hand_size=7, wanted_lands=3, simulations=100_000):
    count_with_3plus_lands = 0
    land_counts = []

    for _ in range(simulations):
        # Build and shuffle deck
        deck = ['land'] * num_lands + ['nonland'] * (deck_size - num_lands)
        random.shuffle(deck)
        # Draw hand
        hand = deck[:hand_size]
        lands_in_hand = hand.count('land')
        land_counts.append(lands_in_hand)
        if lands_in_hand >= wanted_lands:
            count_with_3plus_lands += 1

    probability = count_with_3plus_lands / simulations
    print(f"Probability of drawing at least {wanted_lands} lands: {probability:.3%}")

    # Histogram of land counts in hand
    plt.hist(land_counts, bins=range(hand_size+2), align='left', rwidth=0.8, color="#4a90e2")
    plt.title(f'Number of Lands in Opening Hand ({simulations:,} sims)')
    plt.xlabel('Number of Lands')
    plt.ylabel('Occurrences')
    plt.xticks(range(hand_size+1))
    plt.show()

if __name__ == "__main__":
    simulate_lands_in_hand()