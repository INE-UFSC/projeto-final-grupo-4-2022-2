
import random

from controller.entitiescontroller import EntitiesController

from model.entities.abstractentity import Entity
from model.entities.shooter import Shooter
from model.body import Body
from model.weapon.infinity import InfinityWeapon
from model.factory.defaultbulletfactory import DefaultBulletFactory

import utility.constants as CONSTANT

from pygame import Vector2
import pygame

class Alien(Entity, Shooter):

    __original_alien = pygame.transform.scale(pygame.image.load('./images/alien/alien.png'), (4*CONSTANT.ALIEN_SIZE, 3*CONSTANT.ALIEN_SIZE))

    def __init__(self, body: Body, direction: int):
        Entity.__init__(self, body, CONSTANT.ALIEN_TAG)
        Shooter.__init__(self, InfinityWeapon(self, CONSTANT.ALIEN_SHOT_COOLDOWN, DefaultBulletFactory()),
                           Vector2(1, 1).normalize(), Vector2(0, 0))
        self.__move_cooldown = 0
        self.__direction = direction

        self.set_image(self.__original_alien)
        self.set_rect(self.get_image().get_rect())

    def get_move_cooldown(self) -> float:
        return self.__move_cooldown

    def set_move_cooldown(self, new_value):
        self.__move_cooldown = new_value

    def get_direction(self) -> int:
        return self.__direction

    def set_direction(self, direction: int):
        self.__direction = direction

    def on_collision(self, entity: Entity) -> None:
        EntitiesController.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        velocity = body.get_velocity()
        position = body.get_position()

        # Trecho que cuida da mudança de direção do Alien
        # Espera um tempo e só depois muda randomicamente,
        # podendo assim permanecer na mesma direção
        self.set_move_cooldown(self.get_move_cooldown() - dt)
        if self.get_move_cooldown() < 0:
            self.set_move_cooldown(CONSTANT.MOVE_COOLDOWN)
            body.set_velocity(CONSTANT.DIRECTIONS[random.randint(0, len(CONSTANT.DIRECTIONS) - 1)] * CONSTANT.ALIEN_VELOCITY)
            body.set_velocity(Vector2(body.get_velocity().x*self.get_direction(), body.get_velocity().y))

        # Verifica se o Alien chegou ao fim da tela
        #  e, se chegou, morre
        if position.x < 0:
            EntitiesController.instance().register_deletion(self)
        elif CONSTANT.SCREEN_SIZE.x < position.x:
            EntitiesController.instance().register_deletion(self)

        if position.y < 0:
            position.y = CONSTANT.SCREEN_SIZE.y
        elif CONSTANT.SCREEN_SIZE.y < position.y:
            position.y = 0
        
        # Movimenta
        body.move(velocity*dt)

            
    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        # Determina a direção da mira randomicamente
        aiming_direction = Vector2(self.get_direction(), 0).rotate(random.uniform(0,360))
        # Evita que a bala nasça dentro do Alien
        barrel_position = Vector2(aiming_direction*self.get_body().get_radius() * CONSTANT.RADIUS_MULTIPLIER + self.get_body().get_position())

        self.set_barrel_position(barrel_position)
        self.set_aiming_direction(aiming_direction)

        # Atualiza o comportamento de tiro e de movimentação
        self.shoot(dt)
        self.move(dt)

    def destroy(self) -> None:
        pass
