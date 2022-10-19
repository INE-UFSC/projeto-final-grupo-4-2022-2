
from model.entities.abstractentity import Entity
from model.entities.persistentbullet import PersistentBullet
from model.factory.bulletfactory import BulletFactory
from model.body import Body

import utility.constants as CONSTANT

from pygame.math import Vector2


class PersistentBulletFactory(BulletFactory):

    def create(self, position: Vector2, velocity: Vector2) -> Entity:
        body = Body(position, velocity, CONSTANT.BULLET_SIZE)
        bullet = PersistentBullet(body, CONSTANT.BULLET_LIFE_TIME)
        return bullet