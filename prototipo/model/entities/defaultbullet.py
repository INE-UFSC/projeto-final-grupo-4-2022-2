
from controller.entitiescontroller import EntitiesController

from model.entities.abstractentity import AbstractEntity
from model.entities.bullet import Bullet
from model.body import Body

import utility.constants as CONST


class DefaultBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: AbstractEntity) -> None:
        pass

    def move(self, dt: float) -> None:
        body = self.get_body()

        position = body.get_position()
        if position.x < 0:
            position.x = CONST.SCREEN_SIZE.x
        elif CONST.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONST.SCREEN_SIZE.y
        elif CONST.SCREEN_SIZE.y < position.y:
            position.y = 0

        body.move(body.get_velocity()*dt*10)

    def update(self, dt: float) -> None:
        self.set_lifetime(self.get_lifetime() - dt)
        if self.get_lifetime() < 0:
            EntitiesController.instance().del_entity(self)
        self.move(dt)
