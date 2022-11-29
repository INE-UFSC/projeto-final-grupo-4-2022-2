
from utility.states.state import State
from utility.constants.game_constants import GameConstants
from utility.widgets.button import Button
from utility.data.scoreDAO import ScoreDAO

import pygame


class Game:
    ...

# Implementação do Menu
# Mostrará as opções de ações que
# o usuário pode fazer, como acessar
# scoreboard, sair do jogo ou jogar


class StateScoreBoard(State):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        button_right = Button("button_right", text=">>", font_size=15)
        button_left = Button("button_left", text="<<", font_size=15)

        self.__scoreDAO = ScoreDAO()

        self.__scores = None

        self.__nav_buttons = [button_left, button_right]

        self.__keys_current_state = {pygame.K_LEFT: False,
                                     pygame.K_RIGHT: False,
                                     pygame.K_ESCAPE: False}

        self.__keys_previous_state = {pygame.K_LEFT: False,
                                     pygame.K_RIGHT: False,
                                     pygame.K_ESCAPE: False}

        self.__page = 0

    def __reset_keys(self) -> None:
        for k in self.__keys_current_state.keys():
            self.__keys_current_state[k] = False
            self.__keys_previous_state[k] = False

    def entry(self) -> None:
        self.__reset_keys()
        self.__scores = self.__scoreDAO.get_all()

        score_matrix = list()
        list_to_append = list()
        for j, score in enumerate(self.__scores):
            list_to_append.append(score)
            if (j + 1) % 10 == 0:
                score_matrix.append(list_to_append[:])
                list_to_append = list()

        if 0 < len(list_to_append) <= 10:
            score_matrix.append(list_to_append)

        self.__scores = score_matrix[:]

    def exit(self) -> None:
        pass

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    def handle_update(self, dt: float) -> None:

        for k in self.__keys_current_state.keys():
            self.__keys_previous_state[k] = self.__keys_current_state[k]
        for k in self.__keys_current_state.keys():
            self.__keys_current_state[k] = pygame.key.get_pressed()[k]

        if self.__keys_current_state[pygame.K_LEFT] == True and self.__keys_previous_state[pygame.K_LEFT] == False:
            self.__page -= 1
        if self.__keys_current_state[pygame.K_RIGHT] == True and self.__keys_previous_state[pygame.K_RIGHT] == False:
            self.__page += 1

        if self.__page >= len(self.__scores):
            self.__page = 0
        if self.__page < 0:
            self.__page = len(self.__scores) - 1

    def handle_rendering(self) -> None:

        COLOR_WHITE = (255, 255, 255)
        # Temporário
        # vai ser temporário sim, confia
        title = f"Scoreboard"
        font = pygame.font.get_default_font()
        message_img = pygame.font.SysFont(font, 50).render(title, True, COLOR_WHITE)
        r = message_img.get_rect()
        r.center = (GameConstants().screen_size.x/2, 100)
        self.get_owner().get_screen().blit(message_img, (r.x, r.y))

        score_font = pygame.font.SysFont(font, 20)

        if len(self.__scores) > 0:

            for i, score in enumerate(self.__scores[self.__page]):
                # gerando texto
                score_string = str(self.__page * 10 + i + 1) + ": " + str(score)
                score_image = score_font.render(score_string, True, COLOR_WHITE)

                # centralizando texto
                score_rectangle = score_image.get_rect()
                score_pos = (GameConstants().screen_size.x/2, (120 + i * 20))
                score_rectangle.center = score_pos

                # printando
                self.get_owner().get_screen().blit(score_image, (score_rectangle.x, score_rectangle.y))

        for widget in self.__nav_buttons:
            widget.draw(self.get_owner().get_screen())

    def handle_transition(self) -> None:
        if self.__keys_current_state[pygame.K_ESCAPE] == True and self.__keys_previous_state[pygame.K_ESCAPE] == False:
            self.get_owner().change_state(GameConstants().state_menu)
