

from utility.states.state import State

class Game: ...

class GameController:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__game = None

    def set_game(self, game: Game):
        self.__game = game

    def get_game(self) -> Game:
        return self.__game
    
    def change_state(self, state: State):
        self.get_game().set_current_state(state)