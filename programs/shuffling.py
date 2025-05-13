import random
import itertools

# Create a deck of 52 cards using itertools.product
deck = list(itertools.product(range(1, 14), [
            "Spade", "Club", "Hearts", "Diamond"]))

# Shuffle the deck
random.shuffle(deck)

# Draw 5 cards
print("Your 5-card hand:")
for i in range(5):
    number = deck[i][0]
    suit = deck[i][1]

    # Convert number to face card name if needed
    if number == 1:
        number = "Ace"
    elif number == 11:
        number = "Jack"
    elif number == 12:
        number = "Queen"
    elif number == 13:
        number = "King"

    print(f"{number} of {suit}")
