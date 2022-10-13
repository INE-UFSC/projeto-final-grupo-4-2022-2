
from model.entities.abstractentity import Entity
from model.entities.piercingbullet import PiercingBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

from pygame.math import Vector2


class PiercingBulletFactory(BulletFactory):

    def create(self) -> Entity:
        body = Body(Vector2(-10, -10), Vector2(0, 0), 5)
        bullet = PiercingBullet(body, 10)
        return bullet
