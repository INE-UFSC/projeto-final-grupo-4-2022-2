from controller.gamecontroller import GameController
from model.entities.player import Player
from utility.states.stateinendgame import StateInEndGame


class Board:

    def __init__(self, player: Player) -> None:
        self.__player = player

    def set_player(self, player: Player):
        self.__player = player

    def get_player(self) -> Player:
        return self.__player

    def update(self) -> None:

        dead = not self.get_player().alive()
        
        if dead:
            game = GameController.instance().get_game()
            state = StateInEndGame(game)
            GameController.instance().change_state(state)