import pygame
#Contains variables
#Dimensions
CELL_SIZE = 40
CELL_NO_X =  20
CELL_NO_Y =  20
SCORE_SiZE = 25

#Direction
MOVE_UP = "up"
MOVE_DOWN = "down"
MOVE_LEFT = "left"
MOVE_RIGHT = "right"

#Color
BOARD_COLOR_BASE = (175, 215, 70)
GRASS_COLOR = (167, 209, 61)
SCORE_COLOR = (56, 74, 12)

#Game specific constants
FULL_BOARD = (CELL_NO_X * CELL_NO_Y) - 1 #just before the snake eats the last fruit, this is the snake's length

#pygame specific constants
BOARD_UPDATE_EVENT = pygame.USEREVENT
MOVEMENT_MS_PER_EVENT = 150