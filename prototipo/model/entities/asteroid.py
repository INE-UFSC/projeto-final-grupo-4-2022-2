import math
from model.entities.abstractentity import Entity
from model.body import Body
from controller.entitiescontroller import EntitiesController

import utility.constants as CONSTANT

from pygame.math import Vector2
import pygame


class Asteroid(Entity):

    __original_big_asteroid = pygame.transform.scale(pygame.image.load('./images/asteroid/asteroid_1.png'), (3*CONSTANT.BIG_ASTEROID_SIZE, 3*CONSTANT.BIG_ASTEROID_SIZE))
    __original_medium_asteroid = pygame.transform.scale(pygame.image.load('./images/asteroid/asteroid_1.png'), (3*CONSTANT.MEDIUM_ASTEROID_SIZE, 3*CONSTANT.MEDIUM_ASTEROID_SIZE))
    __original_small_asteroid = pygame.transform.scale(pygame.image.load('./images/asteroid/asteroid_1.png'), (3*CONSTANT.SMALL_ASTEROID_SIZE, 3*CONSTANT.SMALL_ASTEROID_SIZE))
    

    def __init__(self, body: Body) -> None:
        super().__init__(body, CONSTANT.ASTEROID_TAG)
        
        if body.get_radius() == CONSTANT.BIG_ASTEROID_SIZE:
            self.set_image(Asteroid.__original_big_asteroid)
        elif body.get_radius() == CONSTANT.MEDIUM_ASTEROID_SIZE:
            self.set_image(Asteroid.__original_medium_asteroid)
        else:
            self.set_image(Asteroid.__original_small_asteroid)
            
        self.set_rect(self.get_image().get_rect())

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == CONSTANT.ASTEROID_TAG:
            return
        EntitiesController.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        position = body.get_position()

        # Verificações para fazer com que o
        # Asteroid sempre fique "dentro" da janela
        if position.x < 0:
            position.x = CONSTANT.SCREEN_SIZE.x
        elif CONSTANT.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONSTANT.SCREEN_SIZE.y
        elif CONSTANT.SCREEN_SIZE.y < position.y:
            position.y = 0

        # Atuliza a posição
        body.move(body.get_velocity()*dt)

    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        self.move(dt)

    def destroy(self) -> None:

        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()

        # Cria os Asteroid pequenos quando um maior é destruido
        # Caso seja pequeno, não é criado novos
        if body.get_radius() == CONSTANT.BIG_ASTEROID_SIZE:
            velocity.scale_to_length(CONSTANT.MEDIUM_ASTEROID_VELOCITY)
            radius = CONSTANT.MEDIUM_ASTEROID_SIZE

        elif body.get_radius() == CONSTANT.MEDIUM_ASTEROID_SIZE:
            velocity.scale_to_length(CONSTANT.MEDIUM_ASTEROID_VELOCITY)
            radius = CONSTANT.SMALL_ASTEROID_SIZE

        elif body.get_radius() == CONSTANT.SMALL_ASTEROID_SIZE:
            EntitiesController.instance().register_deletion(self)
            return

        position_a = Vector2(position + body.get_radius()
                             * velocity.normalize().rotate(math.pi/2))
        position_b = Vector2(position - body.get_radius()
                             * velocity.normalize().rotate(math.pi/2))

        # Rotação para simular a conservação de energia
        rotation = 30

        velocity_a = velocity.rotate(rotation)
        velocity_b = velocity.rotate(-rotation)

        body_a = Body(position_a, velocity_a, radius)
        body_b = Body(position_b, velocity_b, radius)

        asteroid_a = Asteroid(body_a)
        asteroid_b = Asteroid(body_b)

        # Adicionando a lista de entidades
        EntitiesController.instance().add_entity(asteroid_a)
        EntitiesController.instance().add_entity(asteroid_b)
