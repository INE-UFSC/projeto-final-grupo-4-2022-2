from model.entities.abstractentity import AbstractEntity
from model.body import Body
from controller.entitiescontroller import EntitiesController
import utility.constants as CONST

from pygame.math import Vector2


class Asteroid(AbstractEntity):

    BIG = 30
    MEDIUM = 20
    SMALL = 10

    def __init__(self, body: Body) -> None:
        super().__init__(body, "asteroid")

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

        body.set_position(body.get_position() + body.get_velocity()*dt*1000)

    def update(self, dt: float) -> None:
        self.move(dt/1000)

    def destroy(self) -> None:
        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()

        if body.get_radius() == Asteroid.BIG:
            velocity.scale_to_length(40)
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(
                                                                       30),
                                                                   Asteroid.MEDIUM), Asteroid.MEDIUM))
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(-30),
                                                                   Asteroid.MEDIUM), Asteroid.MEDIUM))

        elif body.get_radius() == Asteroid.MEDIUM:
            velocity.scale_to_length(50)
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(
                                                                       30),
                                                                   Asteroid.SMALL), Asteroid.SMALL))
            EntitiesController.instance().add_entity(Asteroid(Body(Vector2(position),
                                                                   velocity.rotate(-30),
                                                                   Asteroid.SMALL), Asteroid.SMALL))

        EntitiesController.instance().del_entity(self)
