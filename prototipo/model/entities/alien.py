
import random

from pygame import Vector2
from controller.entitiescontroller import EntitiesController

from model.entities.abstractentity import Entity
from model.body import Body

import utility.constants as CONSTANT


class Alien(Entity):

    def __init__(self, body: Body, direction: int):
        super().__init__(body, CONSTANT.ALIEN_TAG)
        self.__move_cooldown = 0
        self.__direction = direction

    def get_move_cooldown(self) -> float:
        return self.__move_cooldown

    def set_move_cooldown(self, new_value):
        self.__move_cooldown = new_value

    def get_direction(self) -> int:
        return self.__direction

    def set_direction(self, direction: int):
        self.__direction = direction

    def on_collision(self, entity: Entity) -> None:
        EntitiesController.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        velocity = body.get_velocity()
        position = body.get_position()

        self.set_move_cooldown(self.get_move_cooldown() - dt)
        if self.get_move_cooldown() < 0:
            self.set_move_cooldown(CONSTANT.MOVE_COOLDOWN)
            body.set_velocity(CONSTANT.DIRECTIONS[random.randint(0, len(CONSTANT.DIRECTIONS) - 1)] * CONSTANT.ALIEN_VELOCITY)
            body.set_velocity(Vector2(body.get_velocity().x*self.get_direction(), body.get_velocity().y))

        if position.x < 0:
            EntitiesController.instance().register_deletion(self)
        elif CONSTANT.SCREEN_SIZE.x < position.x:
            EntitiesController.instance().register_deletion(self)

        if position.y < 0:
            position.y = CONSTANT.SCREEN_SIZE.y
        elif CONSTANT.SCREEN_SIZE.y < position.y:
            position.y = 0

        body.move(velocity*dt)

    def update(self, dt: float) -> None:
        self.move(dt)

    def destroy(self) -> None:
        pass
