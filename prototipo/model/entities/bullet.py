
from model.entities.abstractentity import AbstractEntity
from controller.entitiescontroller import EntitiesController
from model.body import Body
import utility.constants as CONST

class Bullet(AbstractEntity):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body)
        self.__lifetime = lifetime

    def get_lifetime(self) -> int:
        return self.__lifetime

    def set_lifetime(self, new_lifetime: int) -> int:
        self.__lifetime = new_lifetime

    def on_collision(self, entity: AbstractEntity) -> None:
        #entity.destroy()
        self.destroy()

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

        body.set_position(body.get_position() + body.get_velocity()*dt)

    def update(self, dt: float) -> None:
        self.__lifetime -= dt
        if self.get_lifetime() < 0:
            EntitiesController.instance().del_entity(self)
        self.move(dt)

    def get_type(self) -> str:
        return "bullet"

    def destroy(self) -> None:
        EntitiesController.instance().del_entity(self)
