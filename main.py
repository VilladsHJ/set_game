from card import Card
from deck import Deck_of_cards
from player import Player
from cards_on_board import Cards_on_board
from table import Table
import pygame
from rectangle import Rectangle
from constants import card_width, card_height

def main():


    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock_obj = pygame.time.Clock()

    screen.fill("white")

    player1 = Player()
    player2 = Player()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    mechanisms = pygame.sprite.Group()
    
    Rectangle.containers = (updatable, drawable)
    Card.containers = (updatable, drawable)
    Deck_of_cards.containers = (updatable, mechanisms)
    

    deck_of_cards = Deck_of_cards()
    deck_of_cards.make_deck() # generate deck


    draw_button = Rectangle((1000,20), card_height/3, card_height/3, deck_of_cards)
    
    table = Table().table_layout()
    card_objs = {}
    card_buttons = {}

    # def add_cards(start, stop):
    #     for i in range(start, stop):
    #         card_buttons[i] = Rectangle(table[i], card_width, card_height)
    #         card = deck_of_cards.draw_card()
    #         board_cards.add_card(card)
    #         drawing_cards(i, card)
    #card = deck_of_cards.draw_card()
    def drawing_cards(i, table, card):
        print(f"Table placement: {i}")
        if card == False:
            return
        else:
            if i > 11: 
                deck_of_cards.extra_spots.append(i)
            card.placement = table[i]
            card.table_placement = i
            card.rect.x = table[i][0]
            card.rect.y = table[i][1]
            card.image.blit(card.img, (1,1))
            screen.blit(card.image, table[i])

        

    def update_screen(screen):
        screen.fill("white")
        for i in range(len(deck_of_cards.active_cards)):
            index = deck_of_cards.active_cards[i]
            card = deck_of_cards.deck[index]
            if card == False:
                return
            else:
                if i > 11: 
                    deck_of_cards.extra_spots.append(i)

                card.placement = table[i]
                card.table_placement = i
                card.rect.x = table[i][0]
                card.rect.y = table[i][1]
                card.image.blit(card.img, (1,1))
                screen.blit(card.image, table[i])
                screen.blit(card.image, card.placement)
    fr = 60

    #for i in range(len(list(card_objs.keys()))):
    #    screen.blit(card_objs[i], table[i])
    #    card_buttons[i].draw(screen)
        


    # more_cards = Add_cards_button((800+card_width/2, 130 + card_height/2), card_width/2, card_width/2)
    # more_cards.draw(screen)
## game loop_______

    card_selected = 0
    for i in range(12):
        card = deck_of_cards.draw_card()
        drawing_cards(i, table, card)

    while True:
        card_selected = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                for obj in updatable:
                    obj.update()
        
        for obj in mechanisms:
            obj.mechanics()
            update_screen(screen)
                
        for i in deck_of_cards.vacant_spots:
            print(deck_of_cards.vacant_spots, deck_of_cards.card_index_extra_spots)
            if deck_of_cards.card_index_extra_spots != []:
                card = deck_of_cards.deck[deck_of_cards.card_index_extra_spots[card_selected]]
                print(deck_of_cards.card_index_extra_spots)
                deck_of_cards.card_index_extra_spots.remove(deck_of_cards.card_index_extra_spots[card_selected])
                print(deck_of_cards.card_index_extra_spots)
                card_selected += 1
            else: 
                card = deck_of_cards.draw_card()
            print(f"card_index_extra_spots: {len(deck_of_cards.card_index_extra_spots)}")
            
            drawing_cards(i, table, card)
            deck_of_cards.vacant_spots.remove(i)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
            
            #restrict frame rate
        dt = clock_obj.tick(fr)/1000


    #print(board_cards.vacant_spots)
    #print(board_cards.deck)
    #print(board.deck)
    #print(deck_of_cards.deck)
    #deck_of_cards.is_set(deck_of_cards.deck[1],deck_of_cards.deck[2], deck_of_cards.deck[55], player1)
    #print(deck_of_cards.card_list)
    #print(list(Ddeck_of_cards.deck[72].values())[0])

if __name__ == "__main__":
    main()