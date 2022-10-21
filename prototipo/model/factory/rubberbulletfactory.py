
from model.entities.abstractentity import Entity
from model.entities.rubberbullet import RubberBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

import utility.constants as CONSTANT

from pygame.math import Vector2


class RubberBulletFactory(BulletFactory):

    def create(self, position: Vector2, velocity: Vector2) -> Entity:
        body = Body(position, velocity, CONSTANT.BULLET_SIZE)
        bullet = RubberBullet(body, CONSTANT.BULLET_LIFE_TIME)
        return bullet

    def __str__(self) -> str:
        return f"Rubber Bullet Factory"
