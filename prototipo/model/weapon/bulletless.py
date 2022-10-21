
from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory

class BulletlessWeapon(Weapon):


    def __init__(self, owner: Shooter, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(owner, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float) -> None:
        pass

    def __str__(self) -> str:
        return f"Buletless Weapon (No Weapon)"
