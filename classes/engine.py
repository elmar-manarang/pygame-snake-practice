import pygame, sys
from classes.board import Board
from classes.interface import Interface
from constants import CELL_NO_X, CELL_NO_Y, CELL_SIZE, BOARD_UPDATE_EVENT, MOVEMENT_MS_PER_EVENT

class Engine:
    __instance = None

    @staticmethod
    def getInstance():
        if Engine.__instance == None:
            Engine()
        return Engine.__instance

    def __init__(self):
        if Engine.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.initialized = False
            Engine.__instance = self

    def game_init(self):
        if self.initialized == True:
            print("Engine is initialized")
        else:
            print("GAME INIT")
            pygame.init()

            #set up the display at the beginning, engine handles setting the dimension
            screen = pygame.display.set_mode((CELL_NO_X * CELL_SIZE, CELL_NO_Y * CELL_SIZE))
            print("SCREEN SIZE:", screen.get_size())
            clock = pygame.time.Clock()
            pygame.time.set_timer(BOARD_UPDATE_EVENT, MOVEMENT_MS_PER_EVENT)

            self.screen = screen
            self.clock = clock
            self.board = Board(screen, self.increment_score)
            self.interface = Interface(screen)
            self.crunch_sound = pygame.mixer.Sound('resources/crunch.wav')
            self.crunch_sound.set_volume(0.1)

            self.initialized = True

    def game_exit(self):
        print("GAME EXIT")
        pygame.quit()
        sys.exit() #exit the application

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_exit()
            if event.type == BOARD_UPDATE_EVENT:
                self.board.update()
            if event.type == pygame.KEYDOWN:
                self.board.handle_keys(event)

    def draw(self):
        self.board.draw()
        self.interface.draw_score()
        pygame.display.update()

        self.clock.tick(60)
        #print(clock.get_time())

    def game_loop(self):
        if self.initialized != True:
            raise Exception("Game Engine not yet initialized")
        else:
            while True:
                #event loop
                self.check_events()

                #draw loop
                self.draw()

    def start_game(self):
        self.game_init()
        self.game_loop()

    def increment_score(self):
        self.crunch_sound.play()
        self.interface.increment_score()
