import random

class Cards():
    def __init__(self):
        self.deck = {}
        self.num_cards = []

        # card characteristics
        self.amount = ["one","two","three"]
        self.shadings = ["solid","blank","striped"]
        self.colors = ["purple","red","green"]
        self.shapes = ["oval","diamond","squiggle"]
        self.card_list = []

    def make_deck(self):
        # to make a deck run through all characteristics and all attributes
        # each card is a dictionary where the key is the string attribute and the value is the corresponding integer value. 
        # Each card is saved in the dictionary "deck" where the key is the integer value from 1-81 (81 cards in the game) and each corresponding value is a card (dictionary). 
        for i in range(1,3**4+1):
            self.card_list.append(i)
        
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
                        card_num += 1
                        card = {shap: shape, numb: number, col: color, shad: shading}
                        self.deck[card_num] = card

    def cards_in_deck(self):
        for i in range(len(self.deck)):
            self.num_cards.append(i)
    
    def draw_card(self):
        #print(self.card_list)
        random_card_index = random.choice(self.card_list)
        #print(random_card_index)
        self.card_list.remove(random_card_index)
        return self.deck[random_card_index]


        

             

