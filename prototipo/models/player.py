import pygame
from pygame.math import Vector2
from models.spaceship import SpaceShip

class Player(SpaceShip):

    def __init__(self, position: Vector2, velocity: Vector2, sprite, radius: float, cooldown: int, direction: Vector2):
        super().__init__(position, velocity, sprite, radius, cooldown)
        self.__direction = direction

    def get_direction(self):
        return self.__direction
    
    def get_type(self):
        pass
        
    def set_direction(self, new_direction):
        self.__direction = new_direction
    
    def accelerate(self):
        if (self.get_velocity().magnitude() == 0):
            self.set_velocity(Vector2(1, 1))
        elif (self.get_velocity().magnitude() < 100):
            self.set_velocity(self.get_velocity() * (1.10))
        elif (100 < self.get_velocity().magnitude()):
            self.set_velocity(Vector2( 100/(2**(1/2)), 100/(2**(1/2)) ))
    
    def slowdown(self):
        if self.get_velocity().magnitude() < 0.2:
            self.set_velocity(Vector2(0,0))
        else:
            self.set_velocity(self.get_velocity() * 0.96)
    
    def shoot(self):
        pass

    def update(self, dt, screen_size):
        super().update(dt, screen_size)
        
