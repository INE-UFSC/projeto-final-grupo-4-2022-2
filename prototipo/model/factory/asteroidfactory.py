
from model.entities.asteroid import Asteroid
from model.body import Body

import utility.constants as CONSTANTE

from pygame.math import Vector2

import random


class AsteroidFactory:

    def make_velocity(self):
        velocity = Vector2(random.randint(1, 1000), random.randint(1, 1000))
        if random.randint(0, 1):
            velocity.x = -velocity.x
        if random.randint(0, 1):
            velocity.y = -velocity.y
        velocity.scale_to_length(CONSTANTE.BIG_ASTEROID_VELOCITY)
        return velocity

    def make_position(self) -> Vector2:
        return Vector2(random.randint(0, CONSTANTE.SCREEN_SIZE.x), random.randint(0, CONSTANTE.SCREEN_SIZE.y))

    def create(self, number_of_asteroids: int) -> list():
        asteroids = list()
        for i in range(number_of_asteroids):
            asteroid = Asteroid(
                Body(self.make_position(), self.make_velocity(), CONSTANTE.BIG_ASTEROID_SIZE))
            asteroids.append(asteroid)
        return asteroids[:]
