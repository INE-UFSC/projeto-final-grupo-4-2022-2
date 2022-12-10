
from model.entities.abstractentity import Entity
from model.entities.bullets.piercingbullet import PiercingBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

from utility.constants.bullet_constants import BulletConstants

from pygame.math import Vector2

# Constroi uma bala penetrante


class PiercingBulletFactory(BulletFactory):

    def create(self, position: Vector2, velocity: Vector2) -> Entity:
        body = Body(position, velocity, BulletConstants().size)
        bullet = PiercingBullet(body, BulletConstants().life_time)
        return bullet

    def __str__(self) -> str:
        return f"Piercing Bullet Factory"
