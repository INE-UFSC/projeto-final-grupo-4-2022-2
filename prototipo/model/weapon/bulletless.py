
from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.defaultbulletfactory import DefaultBulletFactory


# Arma que não dispara bala
class BulletlessWeapon(Weapon):


    def __init__(self, owner: Shooter) -> None:
        super().__init__(owner, None, None, DefaultBulletFactory())

    def shoot(self, dt: float) -> None:
        pass

    def __str__(self) -> str:
        return f"Buletless Weapon (No Weapon)"
