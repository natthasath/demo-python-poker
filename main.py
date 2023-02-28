from poker.poker import *

deck = Deck()
deck.shuffle()

player1 = Player("Player 1")
player2 = Player("Player 2")

for i in range(5):
    player1.draw_card(deck)
    player2.draw_card(deck)

print("Player 1's hand:")
player1.show_hand()

print("Player 2's hand:")
player2.show_hand()