import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def create_deck():
    return [r + s for s in SUITS for r in RANKS]

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players):
    hands = {f"player_{i}": [deck.pop(), deck.pop()] for i in range(num_players)}
    community = [deck.pop() for _ in range(5)]
    return hands, community, deck
