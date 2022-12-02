
from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.defaultbulletfactory import DefaultBulletFactory
from utility.constants.sounds_constants import noammo_sound


# Arma que não dispara bala
class BulletlessWeapon(Weapon):


    def __init__(self, owner: Shooter) -> None:
        super().__init__(owner, None, None, DefaultBulletFactory())

    def shoot(self, dt: float) -> None:
        noammo_sound.play()

    def __str__(self) -> str:
        return f"Buletless Weapon (No Weapon)"
