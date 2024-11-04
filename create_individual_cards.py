import pygame
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image

class ImageCrop():
    def __init__(self):
        pass
    def make_cards(self):
        file_path = "/home/villads/github.com/VilladsHJ/set_game/playing_cards/Set_cards.png"

        img = Image.open(file_path)
        img_array_org = np.array(img)

        horizontal_distance = 20
        vertical_distance = 15
        card_height = 110
        card_width = 90
        starting_y1 = 20
        starting_y2 = 130
        starting_x1 = 18
        starting_x2 = 108

        current_x1 = starting_x1
        current_x2 = starting_x2
        current_y1 = starting_y1
        current_y2 = starting_y2
        next_v = vertical_distance + card_height - 2
        next_h = horizontal_distance + card_width - 1

        v_count = -1
        h_count = -1


        # Loop that saves each individual picture under the name (shape, number, color, shading) where each is a number between 1 and 3 corresponding to that attribute (1,1,1,1).
        # the loop goes through the cards in Set_cards.png from top to bottom one row at a time.
        for s in [1,2,3]:
            if s > 1:
                starting_x1 += 1 # adjustment
                starting_x2 += 1 # adjustment
            for n in [1,2,3]:
                v_count = -1
                h_count += 1
                current_y1 = starting_y1 # reset y position (back to the top)
                current_y2 = starting_y2 # reset y position (back to the top)
                if n > 1:
                    current_y1 = starting_y1 + 1 # adjustment
                    current_y2 = starting_y2 + 1 # adjustment
                current_x1 = starting_x1 + next_h*h_count # next column
                current_x2 = starting_x2 + next_h*h_count # next column
                for c in [1,2,3]:
                    for sh in [1,2,3]:
                        v_count += 1
                        current_y1 = starting_y1 + next_v*v_count # next row
                        current_y2 = starting_y2 + next_v*v_count # next row

                        img_array = img_array_org[current_y1:current_y2, current_x1:current_x2]
                        new_img = Image.fromarray(img_array)
                        name = f"[{s}, {n}, {c}, {sh}].png"
                        new_img = new_img.save(name)
                        
