
from model.entities.abstractentity import Entity
from model.body import Body

from utility.constants.bullet_constants import BulletConstants

import pygame

# Bala abstrata
class Bullet(Entity):

    __original_bullet = pygame.transform.scale(pygame.image.load('./images/bullet/bullet.png'), (6*BulletConstants().size, 6*BulletConstants().size))

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, BulletConstants().tag)
        self.__lifetime = lifetime

        self.set_image(self.__original_bullet)
        self.set_rect(self.get_image().get_rect())

    def get_lifetime(self) -> int:
        return self.__lifetime

    def set_lifetime(self, new_lifetime: int) -> int:
        self.__lifetime = new_lifetime

    def destroy(self) -> None:
        pass
    
