
from model.weapon.weapon import Weapon
from model.entities.player import Player
from model.factory.bulletfactory import BulletFactory

from pygame.math import Vector2


class InfinityWeapon(Weapon):

    def __init__(self, owner: Player, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(owner, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float, player_position: Vector2) -> None:
        pass