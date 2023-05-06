import pygame
from constants import SCORE_COLOR, SCORE_SiZE, CELL_SIZE, CELL_NO_X, CELL_NO_Y

class Interface:
    def __init__(self, screen):
        self.font = pygame.font.Font('resources/PoetsenOne-Regular.ttf', SCORE_SiZE)
        # self.apple_asset = pygame.image.load('resources/apple.png').convert_alpha()
        self.screen = screen
        self.score = 0

    def increment_score(self):
        self.score += 1
        print("SCORE " + str(self.score))

    def get_score(self):
        return self.score

    def draw_score(self):
        score_text = str(self.score)
        score_surface = self.font.render(score_text, True, SCORE_COLOR)
        score_x = int(CELL_NO_X * CELL_SIZE - 60)
        score_y = int(CELL_NO_Y * CELL_SIZE - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        # apple_rect = self.apple_asset.get_rect(midright = (score_rect.left, score_rect.centery))

        self.screen.blit(score_surface, score_rect)
        # self.screen.blit(self.apple_asset, apple_rect)