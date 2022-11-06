from abc import ABC, abstractmethod
from model.body import Body

import pygame

class Entity:
    ...

# Classe abstrata para aplicar polimorfismo
# Ela será a base de todas as entidades do jogo
class Entity(ABC, pygame.sprite.Sprite):

    next_id = 0

    def __init__(self, body: Body, tag: str):
        pygame.sprite.Sprite.__init__(self)
        self.__id = Entity.next_id
        self.__body = body
        self.__tag = tag
        Entity.next_id += 1

        self.image = None
        self.rect = None

    def get_id(self) -> int:
        return self.__id

    def get_body(self) -> Body:
        return self.__body

    def set_body(self, new_body: Body) -> None:
        self.__body = new_body

    def get_tag(self) -> str:
        return self.__tag

    @abstractmethod
    def on_collision(self, entity: Entity) -> None: ...

    def update(self, dt: float) -> None:
        if self.image is None:
            return
        self.rect = self.image.get_rect()
        self.rect.center = self.get_body().get_position()

    @abstractmethod
    def destroy(self) -> None: ...

    @abstractmethod
    def move(self, dt: float) -> None: ...
