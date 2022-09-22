
from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, position, velocity, sprite, radius):
        self._position = position
        self._velocity = velocity
        self._sprite = sprite
        self._radius = radius
    
    def get_position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position

    def get_velocity(self):
        return self._velocity

    def set_velocity(self, new_velocity):
        self._velocity = new_velocity

    def get_sprite(self):
        return self._sprite

    def set_sprite(self, new_sprite):
        self._sprite = new_sprite

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        self._radius = new_radius

    @abstractmethod
    def update(self, dt): ...

    @abstractmethod
    def get_type(self): ...