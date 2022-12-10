
from model.factory.playerfactory import PlayerFactory
from model.weapon.bulletless import BulletlessWeapon
from model.entities.player import Player


class BulletLessPlayerFactory(PlayerFactory):

    def create(self) -> Player:
        player = super().create()
        player.set_weapon(BulletlessWeapon(player))
        return player
