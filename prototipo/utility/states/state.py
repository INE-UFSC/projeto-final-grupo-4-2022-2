
from abc import ABC, abstractmethod

from utility.effects.particlegenerator import ParticleGenerator
from utility.effects.particledestroyer import ParticleDestroyer

import pygame

class Game: ...

# Classe asbtrata do State
class State(ABC):

    def __init__(self, owner: Game):
        self.__owner = owner
        self.__particles = []
        self.__particle_generator = ParticleGenerator()
        self.__particle_destroyer = ParticleDestroyer()

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
        pass
        p = self.__particle_generator.generate(dt)
        if p is not None:
            self.__particles.append(p)
        
        for p in self.__particles:
            p.update(dt)

        self.__particles = self.__particle_destroyer.destroy(self.__particles)

    # Método que renderiza os componentes
    def handle_rendering(self) -> None:
        pass
        for p in self.__particles:
            pygame.draw.circle(self.get_owner().get_screen(), (255,255,255), p.get_position(), p.get_radius())

    # Método que lidará com a transição de estados
    @abstractmethod
    def handle_transition(self) -> None: ...
