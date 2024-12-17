import unittest
from game.card_game import CardGame
from game.deck import generate_deck

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.players = ["Human", "AI_1", "AI_2"]
        self.game = CardGame(self.players)
        self.deck = generate_deck()

    def test_deal_cards(self):
        self.game.deal_cards(self.deck)
        self.assertTrue(all(len(hand) > 0 for hand in self.game.hands.values()))
        self.assertEqual(sum(len(hand) for hand in self.game.hands.values()), len(self.deck))
        
    def test_play_turn(self):
        self.game.deal_cards(self.deck)
        player = self.players[0]
        cards = self.game.hands[player][:2]
        claim = cards[0].split('_')[0]
        self.game.play_turn(player, cards, claim)
        self.assertNotIn(cards[0], self.game.hands[player])

    def test_call_bluff(self):
        self.game.deal_cards(self.deck)
        player = self.players[0]
        ai_player = self.players[1]
        cards = self.game.hands[player][:2]
        claim = cards[0].split('_')[0]
        self.game.play_turn(player, cards, claim)
        self.game.call_bluff(ai_player)
        # Test bluff success or failure based on the claim

if __name__ == "__main__":
    unittest.main()