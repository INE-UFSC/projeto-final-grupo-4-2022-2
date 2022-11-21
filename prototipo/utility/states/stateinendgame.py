
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from utility.textinput import TextInput
from utility.states.state import State
from utility.data.scoreDAO import ScoreDAO
from utility.constants.game_constants import GameConstants

import pygame

class Game: ...

# Implementação do estado no fim do jogo
# Nele estará a lógica persistência do score
# do player



class StateInEndGame(State):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)

        self.__text_input = TextInput(" ")

    def entry(self) -> None:
        self.__text_input = TextInput(" ")

    def exit(self) -> None:
        player = EntitiesController.instance().get_entities()[0]
        ScoreManager(player).write_to_disk(self.__text_input.get_text())
        EntitiesController.instance().clear_entities()
        [print(scorelog) for scorelog in ScoreDAO().get_all()]

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
        screen.blit(message_img, (GameConstants().screen_size.x /
                    2 - 200, GameConstants().screen_size.y/2 - 40))
        screen.blit(message2_img, (GameConstants().screen_size.x /
                    2 - 200, GameConstants().screen_size.y/2 + 60))
        screen.blit(digite_aqui_img, (GameConstants().screen_size.x /
                    2 - 96, GameConstants().screen_size.y/2))
        screen.blit(nome_img, (GameConstants().screen_size.x /
                    2, GameConstants().screen_size.y/2))

    def handle_transition(self) -> None:
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            next_state = GameConstants().state_menu
            self.get_owner().change_state(next_state)
