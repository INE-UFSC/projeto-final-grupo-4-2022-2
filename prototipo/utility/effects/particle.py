
import pygame

import random

class Particle:

    def __init__(self, position: pygame.math.Vector2 = pygame.math.Vector2(0, 0),
                 velocity: pygame.math.Vector2 = pygame.math.Vector2(0, 0),
                 radius: float = 5.0) -> None:
        self.__position = position
        self.__velocity = velocity
        self.__radius = radius
        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.__cooldown = 0

    def get_position(self) -> pygame.math.Vector2:
        return self.__position

    def set_position(self, new_position: pygame.math.Vector2) -> None:
        self.__position = new_position

    def get_velocity(self) -> pygame.math.Vector2:
        return self.__velocity

    def set_velocity(self, new_velocity: pygame.math.Vector2) -> None:
        self.__velocity = new_velocity

    def get_radius(self) -> float:
        return self.__radius

    def set_radius(self, new_radius: float) -> None:
        self.__radius = new_radius

    def get_color(self) -> tuple:
        return self.__color

    def set_color(self, new_color) -> None:
        self.__color = new_color

    def get_cooldown(self) -> float:
        return self.__cooldown

    def set_cooldown(self, new_cooldown) -> None:
        self.__cooldown = new_cooldown

    def update(self, dt: float) -> None:
        self.set_position(dt*self.get_velocity() + self.get_position())
        self.set_cooldown(self.get_cooldown() + dt)
        if self.get_cooldown() > 0.25:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.set_color((r, g, b))
            self.set_cooldown(0.0)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.get_color(), self.get_position(), self.get_radius())
