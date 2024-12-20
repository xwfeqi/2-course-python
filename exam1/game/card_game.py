import random
from typing import List

class CardGame:
    def __init__(self, players: List[str]):
        self.players = players
        self.hands = {player: [] for player in players}
        self.discard_pile = []
        self.current_player_index = 0
        self.table_cards = []
        self.last_claim = None

    def deal_cards(self, deck: List[str]):
        random.shuffle(deck)
        num_players = len(self.players)
        for i, card in enumerate(deck):
            self.hands[self.players[i % num_players]].append(card)

    def play_turn(self, player: str, cards: List[str], claim: str):
        if not set(cards).issubset(set(self.hands[player])):
            raise ValueError(f"Player {player} does not have these cards: {cards}")
        for card in cards:
            self.hands[player].remove(card)
            self.table_cards.append(card)
        self.last_claim = claim
        print(f"{player} played {len(cards)} cards claiming they are {claim}s.")

    def call_bluff(self, challenger: str):
        print(f"{challenger} calls bluff on {self.players[self.current_player_index]}!")
        actual_ranks = [card.split('_')[0] for card in self.table_cards[-len(self.last_claim):]]

        if all(rank == self.last_claim for rank in actual_ranks):
            print(f"Bluff failed! {challenger} takes the table cards.")
            self.hands[challenger].extend(self.table_cards)
        else:
            print(f"Bluff succeeded! {self.players[self.current_player_index]} takes the table cards.")
            self.hands[self.players[self.current_player_index]].extend(self.table_cards)

        self.table_cards.clear()

    def check_winner(self):
        for player, hand in self.hands.items():
            if len(hand) == 0:
                return player
        return None

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def player_turn(self, player: str):
        """Хід людини."""
        print(f"\nYour hand: {self.hands[player]}")
        try:
            num_cards_to_play = int(input("How many cards do you want to play (1-3)? "))
            if num_cards_to_play < 1 or num_cards_to_play > 3 or num_cards_to_play > len(self.hands[player]):
                print("Invalid number of cards. Try again.")
                return self.player_turn(player)

            cards_to_play = []
            for _ in range(num_cards_to_play):
                card = input(f"Enter a card to play from your hand {self.hands[player]}: ").kl()
                if card not in self.hands[player]:
                    print("Invalid card. Try again.")
                    return self.player_turn(player)
                cards_to_play.append(card)

            claim = input("What rank are you claiming (e.g., 'A', 'K', '7')? ").strip().upper()
            self.play_turn(player, cards_to_play, claim)

        except ValueError:
            print("Invalid input. Try again.")
            return self.player_turn(player)

    def simulate_ai_turn(self, player: str):
        if not self.hands[player]:
            return
        num_cards_to_play = random.randint(1, min(3, len(self.hands[player])))
        cards_to_play = random.sample(self.hands[player], num_cards_to_play)
        claim = random.choice([card.split('_')[0] for card in cards_to_play])
        self.play_turn(player, cards_to_play, claim)

    def simulate_game(self):
        """Запуск гри з інтерактивним ходом людини."""
        while not self.check_winner():
            current_player = self.players[self.current_player_index]
            if current_player == "Human":
                print("\nYour turn!")
                self.player_turn(current_player)
            else:
                print(f"\n{current_player}'s turn.")
                self.simulate_ai_turn(current_player)

            # Рандомний виклик блефу іншими гравцями
            if random.choice([True, False]):  # 50% шанс
                challenger = random.choice([p for p in self.players if p != current_player])
                self.call_bluff(challenger)

            self.next_player()
        print(f"Winner is {self.check_winner()}!")