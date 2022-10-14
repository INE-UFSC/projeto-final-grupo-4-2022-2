
from model.entities.abstractentity import Entity
from model.entities.rubberbullet import RubberBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

from pygame.math import Vector2


class RubberBulletFactory(BulletFactory):

    def create(self, position: Vector2, velocity: Vector2) -> Entity:
        body = Body(position, velocity, 5)
        bullet = RubberBullet(body, 10)
        return bullet
