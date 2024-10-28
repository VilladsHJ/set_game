from cards import Cards
from player import Player
from cards_on_board import Cards_on_board
import pygame

def main():

    player1 = Player()
    player2 = Player()

    board_cards = Cards_on_board()

    deck_of_cards = Cards()
    
    deck_of_cards.make_deck()
    print(deck_of_cards.deck)
    #start game:
    for i in range(12):
        card = deck_of_cards.draw_card()
        board_cards.add_card(card)


    #print(board_cards.vacant_spots)
    #print(board_cards.deck)
    #print(board.deck)
    #print(deck_of_cards.deck)
    #deck_of_cards.is_set(deck_of_cards.deck[1],deck_of_cards.deck[2], deck_of_cards.deck[55], player1)
    #print(deck_of_cards.card_list)
    #print(list(Ddeck_of_cards.deck[72].values())[0])

if __name__ == "__main__":
    main()