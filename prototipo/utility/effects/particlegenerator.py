
from utility.constants.game_constants import GameConstants
from utility.effects.particle import Particle
from pygame.math import Vector2
import random

class ParticleGenerator:

    def __init__(self) -> None:
        self.__sizes = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]
        self.__cooldown = 0.05
        self.__current_cooldown = 0.0
        self.__direction = Vector2(1, 0)

    def generate(self, dt: float) -> Particle:
        self.__current_cooldown += dt
        if self.__current_cooldown < self.__cooldown:
            return

        k = 50
        self.__current_cooldown = 0.0
        size = random.choice(self.__sizes)
        position = Vector2(0.0, random.randint(
            0, GameConstants().screen_size.y))
        velocity = k * size * self.__direction
        return Particle(position, velocity, size)
