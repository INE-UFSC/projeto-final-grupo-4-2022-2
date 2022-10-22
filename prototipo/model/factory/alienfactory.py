import random
import utility.constants as CONSTANT

from pygame import Vector2

from model.weapon.weapon import Weapon
from model.body import Body
from model.entities.alien import Alien

class AlienFactory:

    def create(self) -> Alien:

        direction = self.make_direction()
        position = self.make_position(direction)
        velocity = self.make_velocity(direction)

        alien_body = Body(position, velocity, CONSTANT.ALIEN_SIZE)
        alien = Alien(alien_body, direction)
        return alien

    def make_velocity(self, direction: int) -> Vector2:
        return direction*Vector2(1, 0)*CONSTANT.ALIEN_VELOCITY


    def make_position(self, direction: int) -> Vector2:

        position = Vector2(0, random.randint(0, CONSTANT.SCREEN_SIZE.y))

        if (direction == -1):
            position.x = CONSTANT.SCREEN_SIZE.x - 10
        else:
            position.x = 10

        return position

    def make_direction(self) -> int:
        directions = (-1, 1)

        return random.choice(directions)
