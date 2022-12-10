from abc import ABC, abstractmethod
from model.body import Body

import pygame


class Entity:
    ...

# Classe abstrata para aplicar polimorfismo
# Ela será a base de todas as entidades do jogo


class Entity(ABC):

    next_id = 0

    def __init__(self, body: Body, tag: str) -> None:
        self.__id = Entity.next_id
        self.__body = body
        self.__tag = tag
        Entity.next_id += 1

        self.__image = None
        self.__rect = None

    def get_id(self) -> int:
        return self.__id

    def get_body(self) -> Body:
        return self.__body

    def set_body(self, new_body: Body) -> None:
        self.__body = new_body

    def get_tag(self) -> str:
        return self.__tag

    def get_image(self) -> pygame.surface.Surface:
        return self.__image

    def set_image(self, image: pygame.surface.Surface) -> None:
        self.__image = image

    def get_rect(self) -> pygame.rect.Rect:
        return self.__rect

    def set_rect(self, rect: pygame.rect.Rect) -> None:
        self.__rect = rect

    # Método abstrato para lidar com colisão entre entidades
    # Cada entidade implementa sua lógica de colisão
    @abstractmethod
    def on_collision(self, entity: Entity) -> None: ...

    # Método que vai ser reutilizado e sobrescrito por cada entidade
    # Atualiza a posição, a velocidade, e tudo que deve ser atualizado para cada entidade
    def update(self, dt: float) -> None:
        image = self.get_image()

        if image is None:
            return
        self.set_rect(image.get_rect())
        self.get_rect().center = self.get_body().get_position()

    # Método chamado sempre que uma entidade é destruida
    @abstractmethod
    def destroy(self) -> None: ...

    # Método chamado para atualizar a posição da entidade
    @abstractmethod
    def move(self, dt: float) -> None: ...

    def draw(self, screen: pygame.Surface) -> None:
        #pygame.draw.circle(screen, (255, 0, 0), self.get_body().get_position(), self.get_body().get_radius())
        if self.get_image() is None:
            return
        screen.blit(self.get_image(), self.get_rect())
