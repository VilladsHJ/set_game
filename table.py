import pygame
from cards_on_board import Cards_on_board
from deck import Deck_of_cards
from constants import *

class Table():
    def __init__(self):
        self.table_spots = {}
        self.card_coordinates = {}
        self.start_x_init = 300
        self.start_y_init = 100
        
        self.c = 0
        self.r = 0
        self.counter = 0

    def table_layout(self):
        for columns in range(7):
            self.start_x = self.start_x_init
            self.start_x = self.start_x + card_width*self.c + 1
            self.c += 1
            self.r = 0
            for rows in range(3):
                self.start_y = self.start_y_init
                self.start_y = self.start_y + card_height*self.r
                self.coordinate = (self.start_x, self.start_y)
                self.card_coordinates[self.counter] = self.coordinate
                self.r += 1
                self.counter += 1
        print(self.card_coordinates[19])
        return self.card_coordinates