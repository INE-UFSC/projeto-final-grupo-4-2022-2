from model.entities.asteroid import Asteroid
from model.body import Body
from random import randint

from utility.constants import SCREEN_SIZE

from pygame.math import Vector2


class AsteroidFactory:
    def make_velocity(self):
        velocity = Vector2(randint(1, 1000), randint(1, 1000))
        if randint(0, 1):
            velocity.x = -velocity.x
        if randint(0, 1):
            velocity.y = -velocity.y
        velocity.scale_to_length(777/Asteroid.BIG)
        return velocity

    def make_position(self):
        return Vector2(randint(0, SCREEN_SIZE.x), randint(0, SCREEN_SIZE.y))

    def create(self, number_of_asteroids: int) -> list[Asteroid]:
        asteroids = list()
        for i in range(number_of_asteroids):
            asteroids.append(
                Asteroid(Body(self.make_position(), self.make_velocity(), Asteroid.BIG)))
        return asteroids[:]
