
from model.entities.abstractentity import Entity
from model.entities.bullet import Bullet
from model.body import Body
from controller.entitiescontroller import EntitiesController

import utility.constants as CONST

class PiercingBullet(Bullet):
    
    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: Entity) -> None:
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
            #EntitiesController.instance().del_entity(self)
            EntitiesController.instance().register_deletion(self)
        self.move(dt)
    