
from model.entities.player import Player
from model.weapon.weapon import Weapon
from model.body import Body


class PlayerFactory:
    def create(self, body: Body, lives: int, weapon: Weapon) -> Player:
        player = Player(body, lives, weapon)
        return player
