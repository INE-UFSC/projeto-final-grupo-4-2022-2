
from model.entities.abstractentity import Entity
from model.entities.bullets.defaultbullet import DefaultBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

from utility.constants.bullet_constants import BulletConstants

from pygame.math import Vector2

# Constroi uma bala padrão


class DefaultBulletFactory(BulletFactory):

    def create(self, position: Vector2, velocity: Vector2) -> Entity:
        body = Body(position, velocity, BulletConstants().size)
        bullet = DefaultBullet(body, BulletConstants().life_time)
        return bullet

    def __str__(self) -> str:
        return f"Default Bullet Factory"
