import pygame
from constants import SCORE_COLOR, FONT_COLOR, SMALL_FONT_SIZE, BIG_FONT_SIZE, CELL_SIZE, CELL_NO_X, CELL_NO_Y

class Interface:
    def __init__(self, screen):
        self.small_font = pygame.font.Font('resources/PoetsenOne-Regular.ttf', SMALL_FONT_SIZE)
        self.big_font = pygame.font.Font('resources/PoetsenOne-Regular.ttf', BIG_FONT_SIZE)
        # self.apple_asset = pygame.image.load('resources/apple.png').convert_alpha()
        self.game_over_state = False
        self.screen = screen
        self.score = 0

    def restart(self):
        self.score = 0
        self.game_over_state = False

    def game_over(self):
        self.game_over_state = True

    def increment_score(self):
        self.score += 1
        print("SCORE " + str(self.score))

    def get_score(self):
        return self.score

    def draw_score(self):
        score_text = str(self.score)
        score_surface = self.small_font.render(score_text, True, SCORE_COLOR)
        score_x = int(CELL_NO_X * CELL_SIZE - 60)
        score_y = int(CELL_NO_Y * CELL_SIZE - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        # apple_rect = self.apple_asset.get_rect(midright = (score_rect.left, score_rect.centery))
        self.screen.blit(score_surface, score_rect)
        # self.screen.blit(self.apple_asset, apple_rect)

        if self.game_over_state == True:
            game_over_surface = self.big_font.render("GAME OVER", True, FONT_COLOR)
            game_over_message_x = int((CELL_NO_X * CELL_SIZE) / 2)
            game_over_message_y = int(((CELL_NO_Y * CELL_SIZE) / 2) - 30)
            game_over_rect = game_over_surface.get_rect(center = (game_over_message_x, game_over_message_y))
            self.screen.blit(game_over_surface, game_over_rect)

            restart_message_surface = self.small_font.render("Press 'R' to restart!", True, FONT_COLOR)
            restart_message_x = int((CELL_NO_X * CELL_SIZE) / 2)
            restart_message_y = int(((CELL_NO_Y * CELL_SIZE) / 2) + 30)
            restart_message_rect = restart_message_surface.get_rect(center = (restart_message_x, restart_message_y))
            self.screen.blit(restart_message_surface, restart_message_rect)