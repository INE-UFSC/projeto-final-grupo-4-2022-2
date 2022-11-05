from utility.constants import STATE_END_GAME, ASTEROID_TAG, VELOCITY_MULTIPLIER, TIME_TO_SCORE

from controller.gamecontroller import GameController
from model.entities.player import Player


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
            next_state = STATE_END_GAME
            GameController.instance().change_state(next_state)


