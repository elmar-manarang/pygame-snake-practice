import pygame
from pygame.math import Vector2
from constants import CELL_SIZE, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT

class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.key_direction = None
        self.direction = Vector2(1,0)
        self.last_block = None
        self.init_snake_assets()

    def init_snake_assets(self):
        #TODO:: might move these assets as a helper variable
        #head assets
        self.head_up = pygame.image.load('resources/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('resources/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('resources/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('resources/head_right.png').convert_alpha()

        #tail assets
        self.tail_up = pygame.image.load('resources/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('resources/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('resources/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('resources/tail_right.png').convert_alpha()

        #body assets
        self.body_horiz = pygame.image.load('resources/body_horizontal.png').convert_alpha()
        self.body_vert = pygame.image.load('resources/body_vertical.png').convert_alpha()
        self.body_bl = pygame.image.load('resources/body_bl.png').convert_alpha()
        self.body_br = pygame.image.load('resources/body_br.png').convert_alpha()
        self.body_tl = pygame.image.load('resources/body_tl.png').convert_alpha()
        self.body_tr = pygame.image.load('resources/body_tr.png').convert_alpha()

    def get_snake(self):
        return self.body

    def get_snake_head(self):
        return self.body[0]

    def get_snake_tail(self):
        return self.body[-1]
    
    def check_snake_body_collision(self):
        return self.body.count(self.get_snake_head()) > 1

    def draw_snake(self, surface):
        for index, block in enumerate(self.body):
            snake_rect = pygame.Rect(int(block.x * CELL_SIZE), int(block.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
            asset = None
            #head
            if index == 0:
                head_dir = block - self.body[1]
                asset = self.head_asset_dir(head_dir)
            #tail
            elif index == len(self.body) - 1:
                tail_dir = self.body[len(self.body) - 2] - block
                asset = self.tail_asset_dir(tail_dir)
            #body 
            else:
                #we're tracking the direction going into the block itself,
                # easier to find the corners where it connects this way
                previous_dir = self.body[index - 1] - block
                next_dir = self.body[index + 1] - block
                asset = self.body_asset_dir(previous_dir, next_dir)
            #drawing
            if asset != None:
                surface.blit(asset, snake_rect)
            else:
                raise Exception("Snake asset cannot be found")
                #pygame.draw.rect(surface, (183, 111, 122), snake_rect)

    def head_asset_dir(self, direction):
        if direction.x == 1:
            return self.head_right
        elif direction.x == -1:
            return self.head_left
        elif direction.y == 1:
            return self.head_down
        elif direction.y == -1:
            return self.head_up
        else:
            return None
    
    def tail_asset_dir(self, direction):
        if direction.x == 1:
            return self.tail_left
        elif direction.x == -1:
            return self.tail_right
        elif direction.y == 1:
            return self.tail_up
        elif direction.y == -1:
            return self.tail_down
        else:
            return None
        
    def body_asset_dir(self, previous_dir, next_dir):
        direction_vector = previous_dir + next_dir
        if previous_dir.x != 0 and next_dir.x != 0:
            return self.body_horiz
        elif previous_dir.y != 0 and next_dir.y != 0:
            return self.body_vert
        elif direction_vector.x == 1 and direction_vector.y == 1:
            return self.body_br
        elif direction_vector.x == 1 and direction_vector.y == -1:
            return self.body_tr
        elif direction_vector.x == -1 and direction_vector.y == 1:
            return self.body_bl
        elif direction_vector.x == -1 and direction_vector.y == -1:
            return self.body_tl
        else:
            return None

    def move_snake(self):
        #determine the direction based on the saved key
        #cannot go to the opposite direction as the current direction
        if self.key_direction == MOVE_UP and self.direction.y != 1:
            self.direction = Vector2(0,-1)
        elif self.key_direction == MOVE_DOWN and self.direction.y != -1:
            self.direction = Vector2(0,1)
        elif self.key_direction == MOVE_LEFT and self.direction.x != 1:
            self.direction = Vector2(-1,0)
        elif self.key_direction == MOVE_RIGHT and self.direction.x != -1:
            self.direction = Vector2(1,0)

        #move the snake
        self.last_block = self.body[-1]
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def grow(self):
        if self.last_block != None:
            self.body.append(self.last_block)

    def change_direction(self, direction):
        #save the last pressed key
        #somehow controls feels unresponsive as the user can press a valid command then press an invalid one (see Snake.move_snake)
        #Maybe we can stack the command instead and if a valid command is pressed on a key before, use that instead
        self.key_direction = direction
