
from model.entities.player import Player
from model.weapon.weapon import Weapon
from model.body import Body


class PlayerFactory:
    def create(self, body: Body, lives: int) -> Player:
        player = Player(body, lives)
        return player
