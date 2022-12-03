
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

        self.__text_input = None
        self.__player = None

    def entry(self) -> None:
        self.get_owner().endgame_music_sound.play(-1)
        self.__text_input = TextInput("")
        self.__player = EntitiesController.instance().get_entities()[0]
        print(type(self.__player))

    def exit(self) -> None:
        ScoreManager(self.__player).write_to_disk(self.__text_input.get_text())
        EntitiesController.instance().clear_entities()
        [print(scorelog) for scorelog in ScoreDAO().get_all()]

        self.get_owner().endgame_music_sound.stop()

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

        msg_score = f"Score: {self.__player.get_score().get_points()}"
        score_img = pygame.font.SysFont(
            font, 50).render(msg_score, True, white)
        r_score = score_img.get_rect()
        r_score.center = (GameConstants().screen_size.x/2, GameConstants().screen_size.y/2 - 100)

        msg_type_here = f"Nome: {self.__text_input.get_text()}"
        type_here_img = pygame.font.SysFont(
            font, 32).render(msg_type_here, True, white)
        r_type_here = type_here_img.get_rect()
        r_type_here.center = (GameConstants().screen_size.x/2, GameConstants().screen_size.y/2 - 40)

        screen.blit(score_img, (r_score.x, r_score.y))
        screen.blit(type_here_img, (r_type_here.x, r_type_here.y))

    def handle_transition(self) -> None:
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            next_state = GameConstants().state_menu
            self.get_owner().change_state(next_state)
