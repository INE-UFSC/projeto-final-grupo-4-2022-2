from controller.gamecontroller import GameController
from model.entities.player import Player


class LevelController:

    def __init__(self, player: Player = None) -> None:
        self.__player = player

    def set_player(self, player: Player):
        self.__player = player

    def get_player(self) -> Player:
        return self.__player

    def update(self) -> None:
        if not self.get_player().alive():
            next_state = "inendgame"
            GameController.instance().change_state(next_state)