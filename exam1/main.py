from game.card_game import CardGame
from game.deck import generate_deck

def main():
    # Визначаємо гравців
    players = ["Human", "AI_1", "AI_2"]

    # Генеруємо колоду карт
    deck = generate_deck()

    # Ініціалізуємо гру
    game = CardGame(players)

    # Роздаємо карти
    game.deal_cards(deck)

    # Виводимо правила гри
    print("Welcome to the card game!")
    print("Rules:")
    print("- Each player plays cards and claims a rank.")
    print("- Players can call 'bluff' on others.")
    print("- The goal is to get rid of all your cards.")
    print("\nLet's begin!\n")

    # Запускаємо гру
    game.simulate_game()

if __name__ == "__main__":
    main()
