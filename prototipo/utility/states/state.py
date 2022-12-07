
from abc import ABC, abstractmethod

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
    @abstractmethod
    def handle_event(self) -> None: ...

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
        for p in self.get_owner().get_background_particles():
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pygame.draw.circle(self.get_owner().get_screen(),
                               (r, g, b), p.get_position(), p.get_radius())

    # Método que lidará com a transição de estados
    @abstractmethod
    def handle_transition(self) -> None: ...
