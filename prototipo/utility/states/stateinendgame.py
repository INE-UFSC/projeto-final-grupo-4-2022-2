

from utility.states.state import State

import utility.constants as CONSTANT

import pygame

class StateInMenu: ...

class StateInEndGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def entry(self) -> None:
        pass

    def exit(self) -> None:
        pass

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    def handle_update(self, dt: float) -> None:
        pass

    def handle_rendering(self) -> None:
        # Temporário
        message = f"Game over!"
        font = pygame.font.get_default_font() 
        message = pygame.font.SysFont(font, 50).render(message, True, (255,255,255))
        self.get_owner().get_screen().blit(message, (CONSTANT.SCREEN_SIZE.x/2 - 100, CONSTANT.SCREEN_SIZE.y/2 - 20))

    def handle_transition(self) -> None:
        pass
