import random

def simulate_game(self):
        while not self.check_winner():
            current_player = self.players[self.current_player_index]
            print(f"{current_player}'s turn.")
            self.simulate_ai_turn(current_player)
            if random.choice([True, False]):  # Randomly call bluff or not
                challenger = random.choice([p for p in self.players if p != current_player])
                self.call_bluff(challenger)
            self.next_player()
        print(f"Winner is {self.check_winner()}!")

