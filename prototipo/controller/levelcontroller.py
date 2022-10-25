from controller.gamecontroller import GameController
from model.entities.player import Player
from utility.states.stateinendgame import StateInEndGame


class LevelController:

    def __init__(self, player: Player = None) -> None:
        self.__player = player

    def set_player(self, player: Player):
        self.__player = player

    def get_player(self) -> Player:
        return self.__player

    def update(self) -> None:
        if not self.get_player().alive():
            GameController.instance().change_state(StateInEndGame(GameController.instance().get_game()))