
from model.weapon.weapon import Weapon

from pygame.math import Vector2


# Interface para entidades atiradoras
class Shooter(object):

    def __init__(self, weapon: Weapon, aiming_direction: Vector2, barrel_position: Vector2) -> None:
        self.__aiming_direction = aiming_direction
        self.__barrel_position = barrel_position
        self.__weapon = weapon

    def get_weapon(self) -> Weapon:
        return self.__weapon

    def set_weapon(self, new_weapon: Weapon) -> None:
        self.__weapon = new_weapon

    def get_aiming_direction(self) -> Vector2:
        return self.__aiming_direction

    def set_aiming_direction(self, new_direction) -> None:
        self.__aiming_direction = new_direction

    def get_barrel_position(self) -> Vector2:
        return self.__barrel_position

    def set_barrel_position(self, new_position: Vector2) -> None:
        self.__barrel_position = new_position

    def shoot(self, dt: float) -> None:
        self.get_weapon().shoot(dt)
