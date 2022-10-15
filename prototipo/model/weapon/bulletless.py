
from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory

from pygame.math import Vector2


class BulletlessWeapon(Weapon):


    def __init__(self, direction: Vector2, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(direction, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float, player_position: Vector2) -> None:
        pass
