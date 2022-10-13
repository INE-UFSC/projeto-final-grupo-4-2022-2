
from abc import ABC, abstractmethod

from pygame.math import Vector2

from model.factory.bulletfactory import BulletFactory


class Player: ...

class Weapon(ABC):

    def __init__(self, direction: Vector2, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        self.__direction = direction
        self.__cooldown = cooldown
        self.__ammunition = ammunition
        self.__bullet_factory = bullet_factory
        self.__time_since_last_shot = cooldown

    def get_direction(self) -> Vector2:
        return self.__direction

    def set_direction(self, new_direction: Vector2):
        self.__direction = new_direction

    def get_cooldown(self) -> float:
        return self.__cooldown

    def set_cooldown(self, new_cooldown: float):
        self.__cooldown = new_cooldown

    def get_ammunition(self) -> int:
        return self.__ammunition

    def set_ammunition(self, new_ammunition: int):
        self.__ammunition = new_ammunition

    def get_bullet_factory(self) -> BulletFactory:
        return self.__bullet_factory

    def set_bullet_factory(self, new_bullet_factory):
        self.__bullet_factory = new_bullet_factory

    def get_time_since_last_shot(self) -> float:
        return self.__time_since_last_shot

    def set_time_since_last_shot(self, new_value):
        self.__time_since_last_shot = new_value

    @abstractmethod
    def shoot(self, dt: float, player_position: Vector2) -> None:
        pass
    
    