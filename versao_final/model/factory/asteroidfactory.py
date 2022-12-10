
from model.entities.asteroid import Asteroid
from model.body import Body

from utility.constants.asteroid_constants import AsteroidConstants
from utility.constants.game_constants import GameConstants

from pygame.math import Vector2

import random

# Fábrica de asteroid. Gera Asteroid em posição randômica e
# com velocidade constante


class AsteroidFactory:

    def make_velocity(self) -> Vector2:
        velocity = Vector2(random.randint(1, 1000), random.randint(1, 1000))
        if random.randint(0, 1):
            velocity.x = -velocity.x
        if random.randint(0, 1):
            velocity.y = -velocity.y
        velocity.scale_to_length(AsteroidConstants().big_velocity_mag)
        return velocity

    def make_position(self) -> Vector2:
        return Vector2(random.randint(0, GameConstants().screen_size.x), random.randint(0, GameConstants().screen_size.y))

    def create(self, number_of_asteroids: int) -> list:
        asteroids = list()
        for i in range(number_of_asteroids):
            asteroid = Asteroid(
                Body(self.make_position(), self.make_velocity(), AsteroidConstants().big_size))
            asteroids.append(asteroid)
        return asteroids[:]
