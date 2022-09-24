
import random
import sys
import pygame.math
from models.asteroid import Asteroid
from abc import abstractmethod


class EntitiesGenerator:

    def __init__(self, number_of_entities, screen_size):
        self._number_of_entities = number_of_entities
        self.__screen_size = screen_size

    def get_number_of_entities(self):
        return self._number_of_entities

    def set_number_of_entities(self, new_number_of_entities):
        self._number_of_entities = new_number_of_entities

    def get_screen_size(self):
        return self.__screen_size

    def set_screen_size(self, new_screen_size):
        self.__screen_size = new_screen_size

    @abstractmethod
    def generate(self): ...


class AsteroidsGenerator(EntitiesGenerator):

    SIZE_SMALL = 10
    SIZE_MEDIUM = 20
    SIZE_BIG = 30

    def __init__(self, number_of_entities, player_position, player_size, asteroid_size, screen_size):
        super().__init__(number_of_entities, screen_size)
        self.__size = asteroid_size
        self.__player_position = player_position
        self.__player_size = player_size

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        try:
            self.__size = AsteroidsGenerator.sizes[new_size.lower().strip()]
        except KeyError as e:
            print(e)
            sys.exit(1)

    def make_velocity(self):
        return pygame.math.Vector2(10,10)

    def make_position(self):
        return pygame.math.Vector2(random.randint(0, self.get_screen_size().x),
                                   random.randint(0, self.get_screen_size().y))

    def generate(self):
        asteroids = []
        for _ in range(self.get_number_of_entities()):
            asteroids.append(Asteroid(position=self.make_position(),
                                      velocity=self.make_velocity(),
                                      radius=self.get_size()))
        return asteroids[:]
