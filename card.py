from constants import card_height, card_width
import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, shape, amount, color, shading, numeric_attributes, img, placement=(900,600), fill_color=pygame.Color(255,255,255,0)):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.shape = shape
        self.amount = amount
        self.color = color
        self.shading = shading
        self.numeric_attributes = numeric_attributes
        self.img = img
        
        
        self.card_height = card_height+2
        self.card_width = card_width+2
        self.image = pygame.Surface([self.card_width, self.card_height])
        self.placement = placement
        self.x = placement[0]-1
        self.y = placement[1]-1
        self.fill_color = fill_color
        self.image.convert_alpha()
        self.image.fill(fill_color)
        self.border_color = pygame.Color(0,0,0)
        
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.img, self.border_color, self.rect, 2)
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.table_placement = 0
        
        self.activated = 0

    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.border_color == pygame.Color(0,0,0):
                self.border_color = pygame.Color(255,0,0)
                self.activated = 1
            elif self.border_color == pygame.Color(255,0,0):
                self.border_color = pygame.Color(0,0,0)
                self.activated = -1
        

    def draw(self, screen):
        if self.placement != (900,600):
            pygame.draw.rect(screen, self.border_color, self.rect, 2)