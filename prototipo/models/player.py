
import pygame
from pygame.math import Vector2
from models.entity import Entity

class Player(Entity):

    MAX_VELOCITY = 30.0

    def __init__(self, position: Vector2, velocity: Vector2, sprite, radius: float):
        super().__init__(position, velocity, sprite, radius)
        self.__direction = velocity.normalize()

    def get_type(self):
        return "player"

    def get_direction(self):
        return self.__direction
        
    def set_direction(self, new_direction):
        self.__direction = new_direction

    def rotate_clockwise(self):
        self.__direction.rotate_ip(8)

    def rotate_anticlockwise(self):
        self.__direction.rotate_ip(-8)
    
    def accelerate(self):
        if (self.get_velocity().magnitude() == 0):
            self.set_velocity(Vector2(1, 1))
        elif (self.get_velocity().magnitude() < Player.MAX_VELOCITY):
            self.set_velocity(self.get_velocity() * (1.10))
        elif (Player.MAX_VELOCITY < self.get_velocity().magnitude()):
            self.get_velocity().scale_to_length(Player.MAX_VELOCITY)
    
    def slowdown(self):
        if self.get_velocity().magnitude() < 0.2:
            self.set_velocity(Vector2(0,0))
        else:
            self.set_velocity(self.get_velocity() * 0.96)

    def update(self, dt, screen_size):
        super().update(dt, screen_size)
        self.set_velocity(self.get_direction().normalize()*self.get_velocity().magnitude())
        
