
from model.entities.abstractentity import AbstractEntity
from model.entities.defaultbullet import DefaultBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

from pygame.math import Vector2


class DefaultBulletFactory(BulletFactory):

    def create(self) -> AbstractEntity:
        body = Body(Vector2(-10, -10), Vector2(0, 0), 5)
        bullet = DefaultBullet(body, 10)
        return bullet
