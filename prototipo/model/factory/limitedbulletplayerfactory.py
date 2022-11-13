
from model.factory.playerfactory import PlayerFactory
from model.weapon.default import DefaultWeapon
from model.factory.defaultbulletfactory import DefaultBulletFactory

from utility.constants.weapon_constants import WeaponConstants


class LimitedBulletPlayerFactory(PlayerFactory):

    def create(self):
        player = super().create()
        player.set_weapon(DefaultWeapon(player, WeaponConstants().cooldown,
                                        WeaponConstants().max_ammunition, DefaultBulletFactory()))
        return player

