import pygame, sys
from classes.fruit import Fruit
from classes.snake import Snake
from constants import BOARD_COLOR_BASE, GRASS_COLOR, MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, CELL_NO_X, CELL_NO_Y, CELL_SIZE

def game_over():
    print("GAME OVER")
    pygame.quit()
    sys.exit() #exit the application

#handles in-game interaction
class Board:
    def __init__(self, screen, increment_score):
        screen.fill(BOARD_COLOR_BASE)

        self.screen = screen
        self.snake = Snake()
        self.fruit = Fruit(self.snake.get_snake())
        self.increment_score = increment_score

    def check_fruit_collision(self):
        if self.fruit.pos == self.snake.get_snake_head():
            self.fruit.spawn(self.snake.get_snake())
            self.snake.grow()
            self.increment_score()
            print("snake eats fruit")
    
    def check_fail(self):
        if self.check_wall_collision():
            print("snake hits wall")
            game_over()
        elif self.snake.check_snake_body_collision():
            print("snake hits itself")
            game_over()

    def check_wall_collision(self):
        if not 0 <= self.snake.get_snake_head().x < CELL_NO_X:
            return True
        elif not 0 <= self.snake.get_snake_head().y < CELL_NO_Y:
            return True
        else:
            return False
    
    def draw(self):
        self.screen.fill(BOARD_COLOR_BASE)
        self.draw_grass()
        self.fruit.draw_fruit(self.screen)
        self.snake.draw_snake(self.screen)
    
    def draw_grass(self):
        for row in range(CELL_NO_X):
            for col in range(CELL_NO_Y):
                if col % 2 == row % 2:
                    grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.screen, GRASS_COLOR, grass_rect)

    def update(self):
        self.snake.move_snake()
        self.check_fruit_collision()
        self.check_fail()

    def handle_keys(self, event):
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.snake.change_direction(MOVE_UP)
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake.change_direction(MOVE_DOWN)
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake.change_direction(MOVE_LEFT)
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake.change_direction(MOVE_RIGHT)
