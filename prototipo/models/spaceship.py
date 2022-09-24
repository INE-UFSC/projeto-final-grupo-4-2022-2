
from abc import ABC, abstractmethod
from models.entity import Entity


class SpaceShip(Entity, ABC):

    def __init__(self, position, velocity, sprite, radius, cooldown):
        super().__init__(position, velocity, sprite, radius)
        self._cooldown = cooldown

    def get_cooldown(self):
        return self._cooldown

    def set_cooldown(self, new_cooldown):
        self._cooldown = new_cooldown

    @abstractmethod
    def shoot(self): ...

