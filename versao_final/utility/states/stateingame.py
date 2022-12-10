
# Managers imports
from managers.entitiesmanager import EntitiesManager
from managers.collisiondetectormanager import CollisionDetectorManager
from managers.collisionmanager import CollisionManager
from managers.gameovermanager import GameOverManager
from managers.gfxmanager import GFXManager

# Utility imports
from utility.states.state import State
from utility.constants.game_constants import GameConstants

# Pygame
import pygame


class Game:
    ...

# Implementação do no jogo
# Nele estará a lógica de cada frame para o jogo


class StateInGame(State):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        self._score_manager = None
        #self._debug = None
        self._player = None
        self._status_reporter = None

    def entry(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def handle_event(self) -> None:
        super().handle_event()

    def handle_update(self, dt: float) -> None:
        super().handle_update(dt)

        # Atualiza cada entidade do jogo
        EntitiesManager.instance().update_entities(dt)

        # Atualiza as GFX do jogo
        GFXManager.instance().gfx_update(dt)

        # Detecta as colisões a cada frame
        entities = EntitiesManager.instance().get_entities()
        collisions = CollisionDetectorManager().detect_collisions(entities)

        # Trata as colisões
        CollisionManager().handle_collisions(collisions)

        # Atualiza o score do jogador baseado nas destruições e no tempo
        deletion_buffer = EntitiesManager.instance().get_deletion_buffer()
        self._score_manager.update_score(dt, deletion_buffer)

        # Gerencia as destruições de cada entidade
        EntitiesManager.instance().handle_deletion()
        self._status_reporter.update()

        #self._debug.update(self.get_owner().get_clock())

    def handle_rendering(self) -> None:
        super().handle_rendering()
        screen = self.get_owner().get_screen()

        # GFX (deve ser desenhado antes das entities)
        GFXManager.instance().gfx_draw(screen)

        for entity in EntitiesManager.instance().get_entities()[::-1]:
            entity.draw(screen)

        self._status_reporter.render(screen)

    def handle_transition(self) -> None:
        if GameOverManager().check(self._player):
            next_state = GameConstants().state_end_game
            self.get_owner().change_state(next_state)
