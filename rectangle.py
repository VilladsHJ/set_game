import pygame
from constants import border_width




class Rectangle(pygame.sprite.Sprite):
    def __init__(self, xy, width, height, deck_of_cards):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.xy = xy
        self.width = width
        self.height = height
        self.color = pygame.Color(0,0,0)
        self.rect = pygame.Rect(xy, (self.width, self.height))
        self.active = 0
        self.deck_of_cards = deck_of_cards

    def border_color(self, activation):
        if activation and self.color != pygame.Color(255,0,0):
            self.color = pygame.Color(255,0,0)
        else:
            self.color = pygame.Color(0,0,0)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_width)

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            cards_on_board = 0
            for i in range(len(list(self.deck_of_cards.deck.keys()))):
                if self.deck_of_cards.deck[i].table_placement >= cards_on_board:
                    cards_on_board = self.deck_of_cards.deck[i].table_placement
            if cards_on_board < 19:
                for i in range(1,4):
                    self.deck_of_cards.vacant_spots.append(cards_on_board+i)
