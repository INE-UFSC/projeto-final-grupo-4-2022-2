
from pygame.math import Vector2

class Particle:

    def __init__(self, position: Vector2=Vector2(0,0),
                 velocity: Vector2=Vector2(0,0),
                 radius: float=5.0) -> None:
        self.__position = position
        self.__velocity = velocity
        self.__radius = radius

    def get_position(self) -> Vector2:
        return self.__position

    def set_position(self, new_position: Vector2) -> None:
        self.__position = new_position

    def get_velocity(self) -> Vector2:
        return self.__velocity

    def set_velocity(self, new_velocity: Vector2) -> None:
        self.__velocity = new_velocity

    def get_radius(self) -> float:
        return self.__radius

    def set_radius(self, new_radius: float) -> None:
        self.__radius = new_radius

    def update(self, dt: float) -> None:
        self.set_position(dt*self.get_velocity() + self.get_position())
