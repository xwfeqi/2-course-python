import random

def generate_deck() -> list:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["hearts", "diamonds", "clubs", "spades"]
    return [f"{rank}_{suit}" for rank in ranks for suit in suits]

def shuffle_deck(deck: list) -> None:
    random.shuffle(deck)
