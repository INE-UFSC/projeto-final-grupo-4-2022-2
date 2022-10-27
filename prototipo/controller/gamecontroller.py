
class Game: ...

class GameController:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self, game: Game = None):
        self.__game = game

    def set_game(self, game: Game):
        self.__game = game

    def get_game(self) -> Game:
        return self.__game
    
    def change_state(self, state_str: str):
        self.get_game().change_state(state_str)

    def run(self):
        self.get_game().run()