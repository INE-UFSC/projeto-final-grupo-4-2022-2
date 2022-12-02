
from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.defaultbulletfactory import DefaultBulletFactory
from utility.constants.sounds_constants import noammo_sound


# Arma que não dispara bala
class BulletlessWeapon(Weapon):


    def __init__(self, owner: Shooter) -> None:
        super().__init__(owner, 1, None, DefaultBulletFactory())

    def shoot(self, dt: float) -> None:
        if self.get_time_since_last_shot() < self.get_cooldown():
            self.set_time_since_last_shot(self.get_time_since_last_shot() + dt)
            return
        self.set_time_since_last_shot(0)
        noammo_sound.play()

    def __str__(self) -> str:
        return f"Buletless Weapon (No Weapon)"
