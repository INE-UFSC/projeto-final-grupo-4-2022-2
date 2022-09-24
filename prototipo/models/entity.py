
from abc import ABC, abstractmethod
from pygame.math import Vector2


class Entity(ABC):

    def __init__(self, position, velocity, sprite, radius):
        self._position = position
        self._velocity= velocity
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

    def update(self, dt, screen_size):
        self.set_position(self.get_position() + self.get_velocity() * dt)
        current_position = self.get_position()
        if screen_size.x < current_position.x:
            self.set_position(Vector2(0, current_position.y))
        elif current_position.x < 0:
            self.set_position(Vector2(screen_size.x, current_position.y))
        
        if screen_size.y < current_position.y:
            self.set_position(Vector2(current_position.x, 0))
        elif current_position.y < 0:
            self.set_position(Vector2(current_position.x, screen_size.y))

    @abstractmethod
    def get_type(self): ...