
from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.defaultbulletfactory import DefaultBulletFactory

from utility.constants.sounds_constants import SoundsConstants

import pygame


# Arma que não dispara bala
class BulletlessWeapon(Weapon):


    def __init__(self, owner: Shooter) -> None:
        super().__init__(owner, None, None, DefaultBulletFactory())

    def shoot(self, dt: float) -> None:
        canal = SoundsConstants().noammo_channel
        som = SoundsConstants().noammo_sound
        pygame.mixer.Channel(canal).play(som)

    def __str__(self) -> str:
        return f"Buletless Weapon (No Weapon)"
