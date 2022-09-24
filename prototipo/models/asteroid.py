
import pygame.math
from models.entity import Entity

class Asteroid(Entity):

    def __init__(self, position=pygame.math.Vector2(0,0), velocity=pygame.math.Vector2(0,0), sprite=None, radius=50):
        super().__init__(position, velocity, sprite, radius)

    def update(self, dt, screen_size):
        super().update(dt, screen_size)

    def get_type(self):
        return "asteroid"
