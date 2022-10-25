import math
from model.entities.abstractentity import Entity
from model.body import Body
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

import utility.constants as CONSTANTE

from pygame.math import Vector2


class Asteroid(Entity):

    def __init__(self, body: Body) -> None:
        super().__init__(body, CONSTANTE.ASTEROID_TAG)

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == CONSTANTE.ASTEROID_TAG:
            return
        EntitiesController.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()

        position = body.get_position()
        if position.x < 0:
            position.x = CONSTANTE.SCREEN_SIZE.x
        elif CONSTANTE.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONSTANTE.SCREEN_SIZE.y
        elif CONSTANTE.SCREEN_SIZE.y < position.y:
            position.y = 0

        body.move(body.get_velocity()*dt*1000)

    def update(self, dt: float) -> None:
        self.move(dt/1000)

    def destroy(self) -> None:

        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()


        if body.get_radius() == CONSTANTE.BIG_ASTEROID_SIZE:
            velocity.scale_to_length(CONSTANTE.MEDIUM_ASTEROID_VELOCITY)
            radius = CONSTANTE.MEDIUM_ASTEROID_SIZE

        elif body.get_radius() == CONSTANTE.MEDIUM_ASTEROID_SIZE:
            velocity.scale_to_length(CONSTANTE.MEDIUM_ASTEROID_VELOCITY)
            radius = CONSTANTE.SMALL_ASTEROID_SIZE
        
        elif body.get_radius() == CONSTANTE.SMALL_ASTEROID_SIZE:
            EntitiesController.instance().register_deletion(self)
            return

        position_a = Vector2(position + body.get_radius()*velocity.normalize().rotate(math.pi/2))
        position_b = Vector2(position - body.get_radius()*velocity.normalize().rotate(math.pi/2))

        # Maybe define this 30 as some constant in constants.py?
        rotation = 30

        velocity_a = velocity.rotate(rotation)
        velocity_b = velocity.rotate(-rotation)

        body_a = Body(position_a, velocity_a, radius)
        body_b = Body(position_b, velocity_b, radius)

        EntitiesController.instance().add_entity(Asteroid(body_a))
        EntitiesController.instance().add_entity(Asteroid(body_b))
