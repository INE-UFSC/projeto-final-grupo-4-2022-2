
from model.entities.abstractentity import Entity
from model.entities.piercingbullet import PiercingBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

import utility.constants as CONSTANTE

from pygame.math import Vector2


class PiercingBulletFactory(BulletFactory):

    def create(self, position: Vector2, velocity: Vector2) -> Entity:
        body = Body(position, velocity, CONSTANTE.BULLET_SIZE)
        bullet = PiercingBullet(body, CONSTANTE.BULLET_LIFE_TIME)
        return bullet

    def __str__(self) -> str:
        return f"Piercing Bullet Factory"