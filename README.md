# MTG Commander Opening Hand Monte Carlo Simulator

This Python script simulates drawing opening hands from a Magic: The Gathering Commander deck, letting you estimate the probability of drawing a specific number of lands—and visualize the results with a histogram.

## Features

- Accepts any decklist (.txt, 1 card per line; supports "N Card Name" or "Card Name" formats)
- Uses Scryfall’s API (with local cache) for perfect accuracy in recognizing land cards—even nonbasics!
- User-configurable: Number of simulated hands, minimum/maximum desired land count
- Displays the full distribution of land counts in opening hands, as a table and as a matplotlib histogram

## Example output

Using: https://moxfield.com/decks/Wwcu34oIU0CQWFHGty_lKQ

=== Magic: the Gathering Opening Hand Monte Carlo Simulation ===

Loaded 100 cards.

Checking which cards are lands (uses Scryfall, cached for speed)...

Successes: 4681 / 10000 hands (46.81%) with 3–4 lands.

==== Land Count Distribution in Opening Hand ====

Lands | Hands   | Percent
-------------------------
    0 |    304 |   3.04 %
    1 |   1497 |  14.97 %
    2 |   2880 |  28.80 %
    3 |   2965 |  29.65 %
    4 |   1716 |  17.16 %
    5 |    533 |   5.33 %
    6 |     96 |   0.96 %
    7 |      9 |   0.09 %

![Example Histogram](ExampleHistogram.png)

## Thanks
Made with help from Scryfall for card data.