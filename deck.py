import random
from card import Card
import pygame


class Deck_of_cards(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.deck = {}
        self.active_cards = []
        self.indices = [i for i in range(3**4)]
        self.card_list = self.indices

        self.amount = ["one","two","three"]
        self.shadings = ["solid","blank","striped"]
        self.colors = ["purple","red","green"]
        self.shapes = ["oval","diamond","squiggle"]
        self.card_index_extra_spots = []
        self.extra_spots = []
        self.vacant_spots = []
        self.activations = 0
        self.index_list = []
        self.activations = 0
        self.shape_num = 0
        self.number_num = 0
        self.color_num = 0
        self.shading_num = 0


    def remove_card(self, index):
        del self.deck[index]

    def draw_card(self):
        if self.card_list != []:
            random_card_index = random.choice(self.card_list)
            self.active_cards.append(random_card_index)
            self.card_list.remove(random_card_index)
            #print(len(self.card_list))
            return self.deck[random_card_index]
        else:
            return False

    #     self.deck = {}
    #     self.num_cards = []

    #     # card characteristics
    #     self.amount = ["one","two","three"]
    #     self.shadings = ["solid","blank","striped"]
    #     self.colors = ["purple","red","green"]
    #     self.shapes = ["oval","diamond","squiggle"]
    #     self.card_list = []

    def make_deck(self):

        # to make a deck run through all characteristics and all attributes
        # each card is a dictionary where the key is the string attribute and the value is the corresponding integer value. 
        # Each card is saved in the dictionary "deck" where the key is the integer value from 1-81 (81 cards in the game) and each corresponding value is a card (dictionary). 
        
        attribute_number_list = [1,2,3] # Each characteric have 3 attributes
        card_num = 0
        for shape in attribute_number_list:
            shap = self.shapes[shape-1]
            for number in attribute_number_list:
                numb = self.amount[number-1]
                for color in attribute_number_list:
                    col = self.colors[color-1]
                    for shading in attribute_number_list:
                        shad = self.shadings[shading-1]
                        numeric_attributes = [shape, number, color, shading]
                        img = pygame.image.load(f"/home/villads/github.com/VilladsHJ/set_game/playing_cards/{numeric_attributes}.png").convert()
                        card = Card(shap, numb, col, shad, [shape, number, color, shading], img)
                        self.deck[card_num] = card
                        card_num += 1


    
    def mechanics(self):
        
        for i in range(len(list(self.deck.keys()))):
            if self.deck[i].activated != 0:
                if self.deck[i].activated == 1:
                    self.activations += 1
                    self.shape_num += self.deck[i].numeric_attributes[0]
                    self.number_num += self.deck[i].numeric_attributes[1]
                    self.color_num += self.deck[i].numeric_attributes[2]
                    self.shading_num += self.deck[i].numeric_attributes[3]
                    self.deck[i].activated = 0
                    self.index_list.append(i)
                else:
                    self.activations -= 1
                    self.shape_num -= self.deck[i].numeric_attributes[0]
                    self.number_num -= self.deck[i].numeric_attributes[1]
                    self.color_num -= self.deck[i].numeric_attributes[2]
                    self.shading_num -= self.deck[i].numeric_attributes[3]
                    self.deck[i].activated = 0
                    self.index_list.remove(i)
        if self.activations == 3 and self.shape_num % 3 == 0 and self.number_num % 3 == 0 and self.color_num % 3 == 0 and self.shading_num % 3 == 0:
            print("this is a set")
            self.activations = 0
            #self.index_list
            print(self.index_list.sort(reverse=True))
            for i in self.index_list:
                self.active_cards.remove(i)
            for i in self.index_list:
                if self.deck[i].table_placement < 12:
                    self.vacant_spots.append(self.deck[i].table_placement)                    
                self.deck[i].kill()
            print(f"active_cards: {self.active_cards}")
            for i in self.active_cards:
                if self.deck[i].table_placement > 11:
                    if i in self.card_index_extra_spots:
                        pass
                    else:
                        self.card_index_extra_spots.append(i)
            print(f"card_index_extra_spots: {self.card_index_extra_spots}")
            self.index_list = []
            
            pass #check for set.
    

    # def update(self):
    #     pos = pygame.mouse.get_pos()
    #     cards_on_board = 0
    #     for i in range(len(list(self.deck[i]))):
    #         if self.deck[i].table_placement >= cards_on_board:
    #             cards_on_board = self.deck[i].table_placement
    #     for i in range(3):
    #         self.vacant_spots.append(cards_on_board+i)

    # def cards_in_deck(self):
    #     for i in range(len(self.deck)):
    #         self.num_cards.append(i)
    
    # def draw_card(self):
    #     #print(self.card_list)
    #     random_card_index = random.choice(self.card_list)
    #     #print(random_card_index)
    #     self.card_list.remove(random_card_index)
    #     return self.deck[random_card_index]


        

             

