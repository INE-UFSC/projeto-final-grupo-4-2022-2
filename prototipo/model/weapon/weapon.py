
from abc import ABC, abstractmethod

# from model.entities.shooter import Shooter
from model.factory.bulletfactory import BulletFactory

class Shooter: ...

class Weapon(ABC):

    def __init__(self, owner: Shooter, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        self.__owner = owner
        self.__cooldown = cooldown
        self.__ammunition = ammunition
        self.__bullet_factory = bullet_factory
        self.__time_since_last_shot = cooldown

    def get_owner(self) -> Shooter:
        return self.__owner

    def set_owner(self, new_owner: Shooter):
        self.__owner = new_owner

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

    def set_bullet_factory(self, new_bullet_factory: BulletFactory):
        self.__bullet_factory = new_bullet_factory

    def get_time_since_last_shot(self) -> float:
        return self.__time_since_last_shot

    def set_time_since_last_shot(self, new_value: float):
        self.__time_since_last_shot = new_value

    @abstractmethod
    def shoot(self, dt: float) -> None:
        pass
    
    