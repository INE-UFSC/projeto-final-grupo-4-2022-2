
from abc import ABC, abstractmethod

from utility.constants.game_constants import GameConstants

import random

import pygame


class Game:
    ...

# Classe asbtrata do State


class State(ABC):

    def __init__(self, owner: Game):
        self.__owner = owner

    def get_owner(self) -> Game:
        return self.__owner

    def set_owner(self, new_owner: Game) -> None:
        self.__owner = new_owner

    # Método chamado quando um estado inicia
    @abstractmethod
    def entry(self) -> None: ...

    # Método chamado quando um estado termina
    @abstractmethod
    def exit(self) -> None: ...

    # Método que vai lidar com os métodos do pygame
    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_owner().close()

    # Método onde é atualizado os componentes do estado
    def handle_update(self, dt: float) -> None:
        owner = self.get_owner()
        p = owner.get_particle_generator().generate(dt)
        if p is not None:
            owner.get_background_particles().append(p)

        for p in owner.get_background_particles():
            p.update(dt)

        owner.set_background_particles(owner.get_particle_destroyer().destroy(owner.get_background_particles()))

        owner.get_juke_box().update(dt)

    # Método que renderiza os componentes
    def handle_rendering(self) -> None:
        title = f"ESC to exit"
        font = pygame.font.get_default_font()
        message_img = pygame.font.SysFont(
            font, 25).render(title, True, (255, 255, 255))
        r = message_img.get_rect()
        r.bottomright = (GameConstants().screen_size.x - 10, GameConstants().screen_size.y - 10)
        self.get_owner().get_screen().blit(message_img, (r.x, r.y))
        screen = self.get_owner().get_screen()
        for p in self.get_owner().get_background_particles():
           p.draw(screen)

    # Método que lidará com a transição de estados
    @abstractmethod
    def handle_transition(self) -> None: ...
