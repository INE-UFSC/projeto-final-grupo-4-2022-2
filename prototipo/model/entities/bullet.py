
from model.entities.abstractentity import AbstractEntity
from controller.entitiescontroller import EntitiesController


class Bullet(AbstractEntity):

    def __init__(self, body, lifetime) -> None:
        super().__init__(body)
        self.__lifetime = lifetime

    def get_lifetime(self):
        return self.__lifetime

    def set_lifetime(self, new_lifetime):
        self.__lifetime = new_lifetime

    def on_collision(self, entity):
        entity.destroy()
        self.destroy()

    def move(self, dt, screen_size):
        body = self.get_body()

        position = body.get_position()
        if position.x < 0:
            position.x = screen_size.x
        elif screen_size.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = screen_size.y
        elif screen_size.y < position.y:
            position.y = 0

        body.set_position(body.get_position() + body.get_velocity()*dt)

    def update(self, dt, screen_size):
        self.__lifetime -= dt
        if self.get_lifetime() < 0:
            EntitiesController.instance().del_entity(self)
        self.move(dt, screen_size)

    def get_type(self):
        return "bullet"

    def destroy(self):
        EntitiesController.instance().del_entity(self)