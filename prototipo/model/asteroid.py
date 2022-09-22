
import pygame.math
from model.entity import Entity

class Asteroid(Entity):

    def __init__(self, position=pygame.math.Vector2(0,0), velocity=pygame.math.Vector2(0,0), sprite=None, radius=50):
        super().__init__(position, velocity, sprite, radius)

    def update(self, dt):
        self.set_position(self.get_position() + self.get_velocity() * dt)

    def get_type(self):
        return "asteroid"
