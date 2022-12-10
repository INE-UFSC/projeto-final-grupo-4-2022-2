from abc import abstractmethod
import pygame

class GFX:

    def __init__(self, lifetime: float, position: tuple, radius: float) -> None:
        self.__lifetime = lifetime
        self.__position = position
        self.__radius = radius

        # Duração em tela
        self._duration = 0

    def get_position(self) -> pygame.Vector2:
        return self.__position

    def set_position(self, position) -> None:
        self.__position = position

    def get_lifetime(self) -> float:
        return self.__lifetime

    def get_radius(self) -> float:
        return self.__radius
    
    def set_radius(self, radius: float) -> None:
        self.__radius = radius

    @abstractmethod
    def update(self) -> None:
        ...

    @abstractmethod
    def draw(self) -> None:
        ...