
from model.entities.player import Player
from model.body import Body


# Constroi um player?
class PlayerFactory:

    def create(self, body: Body, lives: int) -> Player:
        player = Player(body, lives)
        return player
