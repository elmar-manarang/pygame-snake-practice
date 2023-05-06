import pygame, random
from pygame.math import Vector2
from constants import CELL_NO_X, CELL_NO_Y, CELL_SIZE, FULL_BOARD

class Fruit:
    def __init__(self, snake_body):
        #grid position
        self.apple_asset = pygame.image.load('resources/apple.png').convert_alpha()
        self.spawn(snake_body)

    def get_grid_position(self):
        return self.pos

    def get_fruit_rect(self):
        return pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)

    def draw_fruit(self, surface):
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        surface.blit(self.apple_asset, fruit_rect)

    def spawn(self, snake_body):
        #we don't want the fruit to spawn where the body is
        if len(snake_body) == FULL_BOARD:
            #if the board is full, hide the last fruit
            self.x = -1
            self.y = -1
            self.pos = Vector2(-1, -1)
        else: 
            while True:
                self.x = random.randint(0, CELL_NO_X - 1)
                self.y = random.randint(0, CELL_NO_Y - 1)
                new_pos = Vector2(self.x, self.y)
                if not (new_pos in snake_body):
                    break
                else:
                    print("reattempting to re-spawn the fruit on a different location")
            self.pos = new_pos
