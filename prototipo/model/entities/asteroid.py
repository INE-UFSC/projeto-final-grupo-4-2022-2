import math
from turtle import position
from model.entities.abstractentity import Entity
from model.body import Body
from controller.entitiescontroller import EntitiesController
import utility.constants as CONST

from pygame.math import Vector2


class Asteroid(Entity):

    BIG = 30
    MEDIUM = 20
    SMALL = 10

    def __init__(self, body: Body) -> None:
        super().__init__(body, "asteroid")

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == "asteroid":
            return
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

        body.move(body.get_velocity()*dt*1000)

    def update(self, dt: float) -> None:
        self.move(dt/1000)

    def destroy(self) -> None:
        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()

        radius = Asteroid.SMALL

        if body.get_radius() == Asteroid.BIG:
            velocity.scale_to_length(40)
            radius = Asteroid.MEDIUM

        elif body.get_radius() == Asteroid.MEDIUM:
            velocity.scale_to_length(50)
            radius = Asteroid.SMALL

        velocity.scale_to_length(40)
        body_a = Body(Vector2(position + body.get_radius()*velocity.normalize().rotate(math.pi/2)), velocity.rotate(30), radius)
        body_b = Body(Vector2(position - body.get_radius()*velocity.normalize().rotate(math.pi/2)), velocity.rotate(-30), radius)
        EntitiesController.instance().add_entity(Asteroid(body_a))
        EntitiesController.instance().add_entity(Asteroid(body_b))

        EntitiesController.instance().register_deletion(self)
