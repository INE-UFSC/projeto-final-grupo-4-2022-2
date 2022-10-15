import math
from turtle import position
from model.entities.abstractentity import Entity
from model.body import Body
from controller.entitiescontroller import EntitiesController

import utility.constants as CONSTANT

from pygame.math import Vector2


class Asteroid(Entity):

    def __init__(self, body: Body) -> None:
        super().__init__(body, CONSTANT.ASTEROID_TAG)

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == CONSTANT.ASTEROID_TAG:
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

        body.move(body.get_velocity()*dt*1000)

    def update(self, dt: float) -> None:
        self.move(dt/1000)

    def destroy(self) -> None:
        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()


        if body.get_radius() == CONSTANT.BIG_ASTEROID_SIZE:
            velocity.scale_to_length(CONSTANT.VELOCITY_OF_MEDIUM_ASTEROID)
            radius = CONSTANT.MEDIUM_ASTEROID_SIZE

        elif body.get_radius() == CONSTANT.MEDIUM_ASTEROID_SIZE:
            velocity.scale_to_length(CONSTANT.VELOCITY_OF_SMALL_ASTEROID)
            radius = CONSTANT.SMALL_ASTEROID_SIZE
        
        elif body.get_radius() == CONSTANT.SMALL_ASTEROID_SIZE:
            EntitiesController.instance().register_deletion(self)
            return

        body_a = Body(Vector2(position + body.get_radius()*velocity.normalize().rotate(math.pi/2)), velocity.rotate(30), radius)
        body_b = Body(Vector2(position - body.get_radius()*velocity.normalize().rotate(math.pi/2)), velocity.rotate(-30), radius)
        EntitiesController.instance().add_entity(Asteroid(body_a))
        EntitiesController.instance().add_entity(Asteroid(body_b))

        EntitiesController.instance().register_deletion(self)
