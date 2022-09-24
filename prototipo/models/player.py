
from models.spaceship import SpaceShip


class Player(SpaceShip):

    def __init__(self, position, velocity, sprite, radius, cooldown, direction, acceleration):
        super().__init__(position, velocity, sprite, radius, cooldown)
        self.__direction = direction

    def get_direction(self):
        return self.__direction

    def set_direction(self, new_direction):
        self.__direction = new_direction

    def shoot(self):
        pass

    def update(self, dt, screen_size):
        super().update(dt, screen_size)
