from classes.engine import Engine

def start_snake_program():
    game_engine = Engine.getInstance()
    game_engine.start_game()

#checks if this is the main function (beginning)
if __name__ == "__main__":  
    start_snake_program()
