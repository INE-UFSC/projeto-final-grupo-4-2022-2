
from math import cos, sin, pi
import random
from typing import List
from pygame.math import Vector2
from models.asteroid import Asteroid
from abc import abstractmethod

class EntitiesGenerator:

    def __init__(self, number_of_entities, screen_size) -> None:
        self._number_of_entities = number_of_entities
        self.__screen_size = screen_size

    def get_number_of_entities(self) -> int:
        return self._number_of_entities

    def set_number_of_entities(self, new_number_of_entities) -> None:
        self._number_of_entities = new_number_of_entities

    def get_screen_size(self) -> Vector2:
        return self.__screen_size

    def set_screen_size(self, new_screen_size):
        self.__screen_size = new_screen_size

    @abstractmethod
    def generate(self): ...


class AsteroidsGenerator(EntitiesGenerator):

    SIZE_SMALL = 10
    SIZE_MEDIUM = 20
    SIZE_BIG = 30

    def __init__(self, number_of_entities, asteroid_size, screen_size):
        super().__init__(number_of_entities, screen_size)
        self.__size = asteroid_size

    def get_size(self) -> Vector2:
        return self.__size

    def set_size(self, new_size) -> None:
        self.__size = new_size

    def make_velocity(self) -> Vector2:
        mag = 300.0 /self.get_size()
        angle = random.randint(0, 360)*pi/180
        return Vector2(mag*cos(angle),mag*sin(angle))

    def make_position(self) -> Vector2:
        return Vector2(random.randint(0, self.get_screen_size().x),
                       random.randint(0, self.get_screen_size().y))

    def generate(self) -> List[Asteroid]:
        asteroids = []
        for _ in range(self.get_number_of_entities()):
            asteroids.append(Asteroid(position=self.make_position(),
                                      velocity=self.make_velocity(),
                                      radius=self.get_size()))
        return asteroids[:]
