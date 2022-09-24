
import pygame.math
from models.entity import Entity

class Asteroid(Entity):

    def __init__(self, position, velocity, radius, sprite=None):
        super().__init__(position, velocity, sprite, radius)

    def update(self, dt, screen_size):
        super().update(dt, screen_size)

    def get_type(self):
        return "asteroid"
