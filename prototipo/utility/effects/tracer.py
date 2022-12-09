
import pygame


class Tracer:
    ...


class Tracer:

    def __init__(self, position: pygame.Vector2, radius: float) -> None:

        self.__lifetime = 4
        self.__duration = 0
        self.__position = position
        self.__radius = radius

    def get_lifetime(self) -> float:
        return self.__lifetime

    def get_radius(self) -> float:
        return self.__radius

    def get_position(self) -> pygame.Vector2:
        return self.__position

    def get_duration(self) -> float:
        return self.__duration

    def set_radius(self, radius):
        self.__radius = radius

    def update(self, dt) -> None:
        self.update_duration(dt)
        old_radius = self.get_radius()
        radius_factor = 1 - (self.get_duration()/self.get_lifetime())
        new_radius = old_radius * radius_factor
        self.set_radius(new_radius)

    def draw(self, screen: pygame.surface.Surface) -> None:
        COLOR = (180, 180, 180)
        pygame.draw.circle(screen, COLOR, self.get_position(), self.get_radius())

    def update_duration(self, dt: float) -> None:
        self.__duration += dt
