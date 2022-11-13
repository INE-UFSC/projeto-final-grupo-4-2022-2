
from model.factory.playerfactory import PlayerFactory
from model.weapon.bulletless import BulletlessWeapon


class BulletLessPlayerFactory(PlayerFactory):

    def create(self):
        player = super().create()
        player.set_weapon(BulletlessWeapon(player))
        return player
