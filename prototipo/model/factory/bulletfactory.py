
from abc import ABC, abstractmethod

from model.entities.abstractentity import Entity

from pygame.math import Vector2

class BulletFactory(ABC):

    @abstractmethod
    def create(self, position: Vector2, velocity: Vector2) -> Entity: ...
