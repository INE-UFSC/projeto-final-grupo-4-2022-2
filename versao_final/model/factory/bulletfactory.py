
from abc import ABC, abstractmethod

from model.entities.abstractentity import Entity

from pygame.math import Vector2

# Fábrica abstrata para as bullets
# Será utilizada na classe weapon


class BulletFactory(ABC):

    @abstractmethod
    def create(self, position: Vector2, velocity: Vector2) -> Entity: ...

    def __str__(self) -> str:
        return f"Bullet Factory ABC (!)"
