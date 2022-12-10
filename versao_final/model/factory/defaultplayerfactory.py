
from model.factory.playerfactory import PlayerFactory
from model.weapon.infinity import InfinityWeapon
from model.factory.defaultbulletfactory import DefaultBulletFactory
from model.entities.player import Player

from utility.constants.weapon_constants import WeaponConstants


class DefaultPlayerFactory(PlayerFactory):

    def create(self) -> Player:
        player = super().create()
        player.set_weapon(InfinityWeapon(
            player, WeaponConstants().cooldown, DefaultBulletFactory()))
        return player
