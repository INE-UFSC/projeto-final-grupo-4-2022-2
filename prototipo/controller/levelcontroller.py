
from controller.gamecontroller import GameController
from model.entities.player import Player
from utility.constants.game_constants import GameConstants

# O gerenciador de level determinará quando o jogo acaba.
class LevelController:

    def __init__(self, player: Player = None) -> None:
        self.__player = player

    def set_player(self, player: Player):
        self.__player = player

    def get_player(self) -> Player:
        return self.__player

    def update(self) -> None:
        # Se o player morreu, então o jogo acaba
        if not self.get_player().alive():
            next_state = GameConstants().state_end_game
            GameController.instance().change_state(next_state)


