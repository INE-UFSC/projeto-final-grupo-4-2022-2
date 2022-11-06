
from model.entities.abstractentity import Entity
from model.body import Body
import utility.constants as CONSTANT

import pygame

# Bala abstrata
class Bullet(Entity):

    __original_bullet = pygame.transform.scale(pygame.image.load('./images/bullet/bullet.png'), (6*CONSTANT.BULLET_SIZE, 6*CONSTANT.BULLET_SIZE))

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, CONSTANT.BULLET_TAG)
        self.__lifetime = lifetime
        self.image = self.__original_bullet
        self.rect = self.image.get_rect()

    def get_lifetime(self) -> int:
        return self.__lifetime

    def set_lifetime(self, new_lifetime: int) -> int:
        self.__lifetime = new_lifetime

    def destroy(self) -> None:
        pass
    
