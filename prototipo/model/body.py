from pygame.math import Vector2

class Body:

    def __init__(self, position: Vector2, velocity: Vector2, radius: int):
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

    def get_radius(self) -> int:
        return self.__radius

    def set_radius(self, new_radius: Vector2) -> None:
        self.__radius = new_radius

    # Vector2 + float?
    # Não entendi esses dois métodos
    def move(self, value):
        self.set_position(self.get_position() + value)

    def accelerate(self, value):
        self.set_velocity(self.get_velocity() + value)