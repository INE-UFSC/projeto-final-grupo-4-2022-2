
from model.entities.abstractentity import Entity
from model.entities.bullets.persistentbullet import PersistentBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

from utility.constants.bullet_constants import BulletConstants

from pygame.math import Vector2

# Constroi uma bala persistente


class PersistentBulletFactory(BulletFactory):

    def create(self, position: Vector2, velocity: Vector2) -> Entity:
        body = Body(position, velocity, BulletConstants().size)
        bullet = PersistentBullet(body, BulletConstants().life_time)
        return bullet

    def __str__(self) -> str:
        return f"Persistent Bullet Factory"
