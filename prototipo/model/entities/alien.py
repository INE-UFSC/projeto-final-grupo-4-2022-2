
import random

from controller.entitiescontroller import EntitiesController

from model.entities.abstractentity import Entity
from model.entities.shooter import Shooter
from model.body import Body
from model.weapon.weapon import Weapon
from model.weapon.infinity import InfinityWeapon
from model.factory.defaultbulletfactory import DefaultBulletFactory

import utility.constants as CONSTANTE

from pygame import Vector2

class Alien(Entity, Shooter):

    def __init__(self, body: Body, direction: int):
        Entity.__init__(self, body, CONSTANTE.ALIEN_TAG)
        Shooter.__init__(self, InfinityWeapon(self, CONSTANTE.ALIEN_SHOT_COOLDOWN, DefaultBulletFactory()),
                           Vector2(1, 1).normalize(), Vector2(0, 0))
        self.__move_cooldown = 0
        self.__direction = direction

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

        self.set_move_cooldown(self.get_move_cooldown() - dt)
        if self.get_move_cooldown() < 0:
            self.set_move_cooldown(CONSTANTE.MOVE_COOLDOWN)
            body.set_velocity(CONSTANTE.DIRECTIONS[random.randint(0, len(CONSTANTE.DIRECTIONS) - 1)] * CONSTANTE.ALIEN_VELOCITY)
            body.set_velocity(Vector2(body.get_velocity().x*self.get_direction(), body.get_velocity().y))

        if position.x < 0:
            EntitiesController.instance().register_deletion(self)
        elif CONSTANTE.SCREEN_SIZE.x < position.x:
            EntitiesController.instance().register_deletion(self)

        if position.y < 0:
            position.y = CONSTANTE.SCREEN_SIZE.y
        elif CONSTANTE.SCREEN_SIZE.y < position.y:
            position.y = 0
        body.move(velocity*dt)

            
    def update(self, dt: float) -> None:
        aiming_direction = Vector2(self.get_direction(), 0).rotate(random.uniform(0,360))
        barrel_position = Vector2(aiming_direction*self.get_body().get_radius()*CONSTANTE.RADIUS_MULTIPLIER + self.get_body().get_position())
        self.set_barrel_position(barrel_position)
        self.set_aiming_direction(aiming_direction)

        self.shoot(dt)
        self.move(dt)

    def destroy(self) -> None:
        pass
