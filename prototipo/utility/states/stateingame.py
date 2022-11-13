
from abc import abstractmethod

# Controller imports
from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager
from controller.levelcontroller import LevelController

# Utility imports
from utility.states.state import State

# Pygame
import pygame


# Implementação do no jogo
# Nele estará a lógica de cada frame para o jogo
class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)
        self._level_controller = LevelController()
        self._score_manager = None
        self._debug = None

    @abstractmethod
    def entry(self) -> None: pass

    def exit(self) -> None:
        pass

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    def handle_update(self, dt: float) -> None:

        # Atualiza cada entidade do jogo
        EntitiesController.instance().update_entities(dt)

        # Detecta as colisões a cada frame
        entities = EntitiesController.instance().get_entities()
        collisions = CollisionDetector().detect_collisions(entities)

        # Trata as colisões
        CollisionManager().handle_collisions(collisions)

        # Atualiza o score do jogador baseado nas destruições e no tempo
        deletion_buffer = EntitiesController.instance().get_deletion_buffer()
        self._score_manager.update_score(dt, deletion_buffer)

        # Gerencia as destruições de cada entidade
        EntitiesController.instance().handle_deletion()

        self._debug.update(self.get_owner().get_clock())

    def handle_rendering(self) -> None:
        screen = self.get_owner().get_screen()

        for entity in EntitiesController.instance().get_entities()[::-1]:
            if entity.get_image() is None:
                continue
            screen.blit(entity.get_image(), entity.get_rect())
            
        self._debug.render(screen)

    def handle_transition(self) -> None:
        self._level_controller.update()
