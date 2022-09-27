from model.entities.abstractentity import AbstractEntity
from model.entities.body import Body
from controller.entitiescontroller import EntitiesController

from pygame.math import Vector2


class Asteroid(AbstractEntity):

    sizes = {"big": 30,
             "medium": 20,
             "small": 10}

    def __init__(self, body, size) -> None:
        super().__init__(body)
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        self.__size = new_size
    
    def on_collision(self, entity):
        if entity.get_type() == self.get_type():
            return
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
        self.move(dt, screen_size)

    def get_type(self):
        return "asteroid"

    def destroy(self):
        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        if self.get_size() == "big":
            velocity.scale_to_length(40)
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(30),
                                                                   Asteroid.sizes["medium"]), "medium"))
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(-30),
                                                                   Asteroid.sizes["medium"]), "medium"))     
        elif self.get_size() == "medium":
            velocity.scale_to_length(50)
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(30),
                                                                   Asteroid.sizes["small"]), "small"))
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(-30),
                                                                   Asteroid.sizes["small"]), "small"))     

        EntitiesController.instance().del_entity(self)