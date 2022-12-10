
from model.body import Body
from model.entities.pickups.pickup import PickUp

from utility.constants.game_constants import GameConstants
from utility.constants.pickup_constants import PickUpConstants

import random
from pygame import Vector2

# Fábrica de alien, cuida de contruir as propriedades de cada alien


class PickUpFactory:

    def create(self, type: PickUp) -> PickUp:
        position = self.make_position()
        body = Body(position, Vector2(0, 0), PickUpConstants().size/3)

        return type(body)

    def make_position(self) -> Vector2:

        position = Vector2(random.randint(0, GameConstants(
        ).screen_size.x), random.randint(0, GameConstants().screen_size.y))

        return position
