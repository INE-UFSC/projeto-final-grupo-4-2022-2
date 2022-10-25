from game import Game
from controller.gamecontroller import GameController

game_controller = GameController.instance()
game_controller.set_game(Game("Pousando em congonhas"))
game_controller.run()
