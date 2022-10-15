
from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory


class Player: ...


class BulletlessWeapon(Weapon):


    def __init__(self, owner: Player, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(owner, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float) -> None:
        pass
