
from managers.entitiesmanager import EntitiesManager
from managers.gfxmanager import GFXManager
from managers.scoremanager import ScoreManager

from utility.textinput import TextInput
from utility.states.state import State
from utility.constants.game_constants import GameConstants
from utility.data.soundplayer import SoundPlayer

import pygame


class Game:
    ...

# Implementação do estado no fim do jogo
# Nele estará a lógica persistência do score
# do player

class StateInEndGame(State):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)

        self.__text_input = None
        self.__player = None

    def entry(self) -> None:
        self.get_owner().get_juke_box().stop()
        SoundPlayer().play(self.get_owner().get_game_over_music())
        self.__text_input = TextInput("")
        self.__player = EntitiesManager.instance().get_entities()[0]

    def exit(self) -> None:
        SoundPlayer().stop(self.get_owner().get_game_over_music())
        self.get_owner().get_juke_box().new_music()

        ScoreManager(self.__player).write_to_disk(self.__text_input.get_text())
        EntitiesManager.instance().clear_entities()
        GFXManager().instance().clear()

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_owner().close()
            self.__text_input.handle_event(event)

    def handle_update(self, dt: float) -> None:
        super().handle_update(dt)

    def handle_rendering(self) -> None:
        super().handle_rendering()

        # Temporário
        font = pygame.font.get_default_font()
        screen = self.get_owner().get_screen()
        white = (255, 255, 255)
        screen_size_x = GameConstants().screen_size.x
        screen_size_y = GameConstants().screen_size.y

        msg_actions = f"""Enter: Salvar; TAB: Menu"""
        actions_img = pygame.font.SysFont(
            font, 20).render(msg_actions, True, white)
        rect_actions = actions_img.get_rect()
        rect_actions.center = (screen_size_x/2, screen_size_y/2 - 160)

        msg_score = f"Score: {self.__player.get_score().get_points()}"
        score_img = pygame.font.SysFont(
            font, 50).render(msg_score, True, white)
        r_score = score_img.get_rect()
        r_score.center = (screen_size_x/2, screen_size_y/2 - 100)

        msg_type_here = f"Nome: {self.__text_input.get_text()}"
        type_here_img = pygame.font.SysFont(
            font, 32).render(msg_type_here, True, white)
        r_type_here = type_here_img.get_rect()
        r_type_here.center = (screen_size_x/2, screen_size_y/2 - 40)

        screen.blit(actions_img, (rect_actions.x, rect_actions.y))
        screen.blit(score_img, (r_score.x, r_score.y))
        screen.blit(type_here_img, (r_type_here.x, r_type_here.y))

    def handle_transition(self) -> None:
        if pygame.key.get_pressed()[pygame.K_RETURN] or pygame.key.get_pressed()[pygame.K_TAB]:
            next_state = GameConstants().state_menu
            self.get_owner().change_state(next_state)
