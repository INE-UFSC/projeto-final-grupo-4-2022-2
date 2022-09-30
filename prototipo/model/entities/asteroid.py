from model.entities.abstractentity import AbstractEntity
from model.body import Body
from controller.entitiescontroller import EntitiesController
import utility.constants as CONST

from pygame.math import Vector2


class Asteroid(AbstractEntity):

    BIG = 30
    MEDIUM = 20
    SMALL = 10

    def __init__(self, body: Body, size: int) -> None:
        super().__init__(body)
        self.__size = size

    def get_size(self) -> int:
        return self.__size

    def set_size(self, new_size: int):
        self.__size = new_size
    
    def on_collision(self, entity: AbstractEntity) -> None:
        if entity.get_type() == self.get_type():
            return
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
        self.move(dt)

    def get_type(self) -> str:
        return "asteroid"

    def destroy(self) -> None:
        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()

        if self.get_size() == Asteroid.BIG:
            velocity.scale_to_length(40)
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(30),
                                                                   Asteroid.MEDIUM), Asteroid.MEDIUM))
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(-30),
                                                                   Asteroid.MEDIUM), Asteroid.MEDIUM))   
                                                                     
        elif self.get_size() == Asteroid.MEDIUM:
            velocity.scale_to_length(50)
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(30),
                                                                   Asteroid.SMALL), Asteroid.SMALL))
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(-30),
                                                                   Asteroid.SMALL), Asteroid.SMALL))     

        EntitiesController.instance().del_entity(self)