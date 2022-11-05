from cgitb import text
from controller.gamecontroller import GameController
from controller.scoremanager import ScoreManager
from utility.textinput import TextInput
from utility.states.state import State

import utility.constants as CONSTANT
import pygame


# Implementação do estado no fim do jogo
# Nele estará a lógica persistência do score
# do player
class StateInEndGame(State):

    def __init__(self, owner):
        super().__init__(owner)

        self.__text_input = TextInput(" ")

    def entry(self) -> None:
        self.__text_input = TextInput(" ")

    def exit(self) -> None:
        score_log = ScoreManager.instance().generate_score_log(self.__text_input.text)
        ScoreManager.instance().write_to_disk(score_log)
        ScoreManager.instance().reset_score()
        for s in ScoreManager.instance().get_score_dao().get_all():
            print(f"{s.get_name()}, {s.get_score()}")

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()
            self.__text_input.handle_event(event)

    def handle_update(self, dt: float) -> None:
        ...

    def handle_rendering(self) -> None:

        # Temporário
        font = pygame.font.get_default_font()
        screen = self.get_owner().get_screen()
        white = (255, 255, 255)

        message = f"STATE IN END GAME"
        message2 = f"Aperte ENTER para transitar para STATE IN MENU (ENTER também salva o score)"
        message_img = pygame.font.SysFont(
            font, 50).render(message, True, white)
        message2_img = pygame.font.SysFont(
            font, 20).render(message2, True, white)

        nome_img = self.__text_input.get_text_as_image(32, white)

        digite_aqui_img = pygame.font.SysFont(
            font, 32).render("Nome: ", True, white)
        screen.blit(message_img, (CONSTANT.SCREEN_SIZE.x /
                    2 - 200, CONSTANT.SCREEN_SIZE.y/2 - 40))
        screen.blit(message2_img, (CONSTANT.SCREEN_SIZE.x /
                    2 - 200, CONSTANT.SCREEN_SIZE.y/2 + 60))
        screen.blit(digite_aqui_img, (CONSTANT.SCREEN_SIZE.x /
                    2 - 96, CONSTANT.SCREEN_SIZE.y/2))
        screen.blit(nome_img, (CONSTANT.SCREEN_SIZE.x /
                    2, CONSTANT.SCREEN_SIZE.y/2))

    def handle_transition(self) -> None:
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            next_state = CONSTANT.STATE_MENU
            GameController.instance().change_state(next_state)
