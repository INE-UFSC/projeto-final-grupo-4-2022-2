
from controller.entitiescontroller import EntitiesController

from model.entities.abstractentity import Entity
from model.entities.bullet import Bullet
from model.body import Body

import utility.constants as CONSTANT


class DefaultBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: Entity) -> None:
        if self.bullet_tag_check(entity.get_tag()):
            return
        self.destroy()

    def move(self, dt: float) -> None:
        body = self.get_body()

        position = body.get_position()
        if position.x < 0:
            position.x = CONSTANT.SCREEN_SIZE.x
        elif CONSTANT.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONSTANT.SCREEN_SIZE.y
        elif CONSTANT.SCREEN_SIZE.y < position.y:
            position.y = 0

        body.move(body.get_velocity()*dt*10)

    def update(self, dt: float) -> None:
        self.set_lifetime(self.get_lifetime() - dt)
        if self.get_lifetime() < 0:
            EntitiesController.instance().register_deletion(self)
        self.move(dt)