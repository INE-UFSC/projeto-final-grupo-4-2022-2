
from abc import abstractmethod

# Controller imports
from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager
from controller.gameoverchecker import GameOverChecker


# Utility imports
from utility.states.state import State
from utility.constants.game_constants import GameConstants

# Pygame
import pygame

class Game: ...

# Implementação do no jogo
# Nele estará a lógica de cada frame para o jogo
class StateInGame(State):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        self._score_manager = None
        self._debug = None
        self._player = None
        self._status_reporter = None
        
    def entry(self) -> None:
        self.get_owner().get_game_music_sound().play(-1)

    def exit(self) -> None:
        self.get_owner().get_game_music_sound().stop()

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
        self._status_reporter.update()
        self._debug.update(self.get_owner().get_clock())

    def handle_rendering(self) -> None:
        screen = self.get_owner().get_screen()

        for entity in EntitiesController.instance().get_entities()[::-1]:
            entity.draw(screen)
            
        #self._debug.render(screen)
        self._status_reporter.render(screen)

    def handle_transition(self) -> None:
        if GameOverChecker().check(self._player):
            next_state = GameConstants().state_end_game
            self.get_owner().change_state(next_state)
