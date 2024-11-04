from deck import Deck_of_cards

class Cards_on_board():
    def __init__(self):
        super().__init__()
        self.vacant_spots = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    def add_card(self, card):
        #print(self.vacant_spots)
        self.first_spot = min(self.vacant_spots)
        self.vacant_spots.remove(self.first_spot)
        self.deck[self.first_spot] = card

    def remove_card_from_game(self, index):
        del self.deck[index]
        print(self.vacant_spots)
        self.vacant_spots.append(index)
        self.vacant_spots.sort()
        print(self.vacant_spots)

    def is_set(self, 
               card1, i1, 
               card2, i2, 
               card3, i3, 
               player):
        set_check_list = [] # list to contain bolean values. All values must be True to change set_check to True.
        set_check = False # will be changed to "True" if the three cards chosen are a set
        attribute_list = [] # This list will contain the sum of each attribute from each characteristics of three cards chosen
        
        message_list = ["Shape", "Amount", "Color", "Shading"]
        set_message = "This is not a set because: "
        
        # Checking attributes for each characteristic which in the card dictionary has values 1, 2 or 3. 
        # A set is must have the sum of each individual attribute modulo 3 with no remainder.

        for i in range(4):
            # list of summed attributes for each characteristic
            attribute_list.append(list(card1.values())[i] + list(card2.values())[i] + list(card3.values())[i])
            
            # check if the attribute sum modulo 3 has no remainder.
            # If False then add explanaition to set message and add False to set_check_list
            # If True, add True to set_check_list.
            if (list(card1.values())[i] + list(card2.values())[i] + list(card3.values())[i]) % 3 != 0:
                set_message += f"{message_list[i]} is off: {list(card1.keys())[i]}, {list(card2.keys())[i]}, {list(card3.keys())[i]}. "
                set_check_list.append(False)
            else:
                set_check_list.append(True)

        # Checks if set_check_list contains only True. If True then the three cards are a set and are removed from the game
        if set_check_list[0] and set_check_list[1] and set_check_list[2] and set_check_list[3]:
            set_check = True
            self.remove_card_from_game(i1)
            self.remove_card_from_game(i2)
            self.remove_card_from_game(i3)
            set_message = "Set found, well done!"
        
        #Update the player's score: +1 if cards are a set, -1 if if cards are not a set.
        self.tally(set_check, player)
        
        print(set_message)
        print(f"{player.name}'s score is now {player.score}")

        return set_check
    
    def tally(self, set_check, player):
        if set_check:
            player.score += 1
        else:
            player.score -= 1


    def table(self, deck):
        for i in range(12):
            card = self.draw_card()
            board_cards.add_card(card)
            print(list(board_cards.deck[i].values()))
            card_str = list(board_cards.deck[i].values())
            card_obj = pygame.image.load(f"/home/villads/github.com/VilladsHJ/set_game/playing_cards/{card_str}.png").convert()

    def card_selected(self):
        
        return counter