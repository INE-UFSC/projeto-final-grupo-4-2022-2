from cgitb import text
from controller.gamecontroller import GameController
from controller.scoremanager import ScoreManager
from utility.textinput import TextInput
from utility.states.state import State

import utility.constants as CONSTANTE
import pygame

class StateInEndGame(State):

    def __init__(self, owner):
        super().__init__(owner)
        self.__can_transition = False

        self.__text_input = TextInput(" ")

    @property
    def text_input(self) -> TextInput:
        return self.__text_input

    def entry(self) -> None:
        pass

    def exit(self) -> None:
        score_log = ScoreManager.instance().generate_score_log(self.text_input.text)
        salvou = ScoreManager.instance().write_to_disk(score_log)
        print(salvou)
        ScoreManager.instance().reset_score()

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()
            
            self.text_input.handle_event(event)
            

    def handle_update(self, dt: float) -> None:
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            self.__can_transition = True


    def handle_rendering(self) -> None:

        # Temporário
        font = pygame.font.get_default_font() 
        screen = self.get_owner().get_screen()
        white = (255,255,255)

        message = f"STATE IN END GAME"
        message2 = f"Aperte ENTER para transitar para STATE IN MENU (ENTER também salva o score)"
        message_img = pygame.font.SysFont(font, 50).render(message, True, white)
        message2_img = pygame.font.SysFont(font, 20).render(message2, True, white)

        nome_img = self.text_input.get_text_as_image(32, white)

        digite_aqui_img = pygame.font.SysFont(font, 32).render("Nome: ", True, white)
        screen.blit(message_img, (CONSTANTE.SCREEN_SIZE.x/2 - 200, CONSTANTE.SCREEN_SIZE.y/2 - 40))
        screen.blit(message2_img, (CONSTANTE.SCREEN_SIZE.x/2 - 200, CONSTANTE.SCREEN_SIZE.y/2 + 60))
        screen.blit(digite_aqui_img, (CONSTANTE.SCREEN_SIZE.x/2 - 96, CONSTANTE.SCREEN_SIZE.y/2))
        screen.blit(nome_img, (CONSTANTE.SCREEN_SIZE.x/2, CONSTANTE.SCREEN_SIZE.y/2))

    def handle_transition(self) -> None:
        if self.__can_transition:
            next_state = CONSTANTE.STATE_MENU
            GameController.instance().change_state(next_state)
            self.__can_transition = False
