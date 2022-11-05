
from controller.gamecontroller import GameController
from utility.states.state import State
import utility.constants as CONSTANTE

import pygame

# Implementação do Menu
# Mostrará as opções de ações que
# o usuário pode fazer, como acessar
# scoreboard, sair do jogo ou jogar
class StateInMenu(State):

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
        message = f"STATE IN MENU!"
        message2 = f"Aperte G para transitar para STATE IN GAME"
        font = pygame.font.get_default_font() 
        message_img = pygame.font.SysFont(font, 50).render(message, True, (255,255,255))
        message2_img = pygame.font.SysFont(font, 20).render(message2, True, (255, 255, 255))
        self.get_owner().get_screen().blit(message_img, (CONSTANTE.SCREEN_SIZE.x/2 - 100, CONSTANTE.SCREEN_SIZE.y/2 - 20))
        self.get_owner().get_screen().blit(message2_img, (CONSTANTE.SCREEN_SIZE.x/2 - 100, CONSTANTE.SCREEN_SIZE.y/2 + 30))

    def handle_transition(self) -> None:
        if pygame.key.get_pressed()[pygame.K_g]:
            next_state = CONSTANTE.STATE_IN_GAME
            GameController.instance().change_state(next_state)
