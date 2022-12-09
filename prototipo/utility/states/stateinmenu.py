
from utility.states.state import State
from utility.constants.game_constants import GameConstants
from utility.widgets.button import Button
from utility.data.soundplayer import SoundPlayer

import pygame


class Game:
    ...

# Implementação do Menu
# Mostrará as opções de ações que
# o usuário pode fazer, como acessar
# scoreboard, sair do jogo ou jogar


class StateInMenu(State):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        b_play = Button("play_button", text="Play", font_size=30)
        b_default_mode = Button(
            GameConstants().state_default_mode, text="Default", font_size=30)
        b_dodge_mode = Button(
            GameConstants().state_dodge_mode, text="Dodge", font_size=30)
        b_asteroid_mode = Button(
            GameConstants().state_asteroid_mode, text="Asteroid", font_size=30)
        b_alien_mode = Button(
            GameConstants().state_alien_mode, text="Alien", font_size=30)
        b_pickup_mode = Button(
            GameConstants().state_pickup_mode, text="PickUp", font_size=30)
        b_score_board = Button(
            GameConstants().state_score_board, text="ScoreBoard", font_size=30)
        b_back = Button("back_button", text="Back", font_size=30)
        b_exit = Button("exit_button", text="Exit", font_size=30)

        self.__modes_buttons = [b_default_mode, b_dodge_mode,
                                b_asteroid_mode, b_alien_mode,
                                b_pickup_mode, b_back]
        self.__action_buttons = [b_play, b_score_board, b_exit]

        self.__keys_current_state = {pygame.K_UP: False,
                                     pygame.K_DOWN: False,
                                     pygame.K_SPACE: False}
        self.__keys_previous_state = {pygame.K_UP: False,
                                      pygame.K_DOWN: False,
                                      pygame.K_SPACE: False}
        self.__selected_button = 0

    def __update_buttons_position(self) -> None:
        for i, w in enumerate(self.__current_buttons):
            pos = pygame.math.Vector2(GameConstants(
            ).screen_size.x/2, GameConstants().screen_size.y/2 + w.get_font_size() * 1.1 * (i - 1))
            w.set_position(pos)

    def __reset_keys(self) -> None:
        for k in self.__keys_current_state.keys():
            self.__keys_current_state[k] = False
            self.__keys_previous_state[k] = False

    def entry(self) -> None:
        self.__reset_keys()
        self.__current_buttons = self.__action_buttons
        self.__update_buttons_position()

    def exit(self) -> None:
        # SoundPlayer().stop(self.get_owner().get_menu_music_sound())
        pass

    def handle_event(self) -> None:
        super().handle_event()

    def handle_update(self, dt: float) -> None:
        super().handle_update(dt)

        for k in self.__keys_current_state.keys():
            self.__keys_previous_state[k] = self.__keys_current_state[k]
        for k in self.__keys_current_state.keys():
            self.__keys_current_state[k] = pygame.key.get_pressed()[k]

        if self.__keys_current_state[pygame.K_UP] == True and self.__keys_previous_state[pygame.K_UP] == False:
            self.__selected_button -= 1
        if self.__keys_current_state[pygame.K_DOWN] == True and self.__keys_previous_state[pygame.K_DOWN] == False:
            self.__selected_button += 1

        if self.__selected_button < 0:
            self.__selected_button = len(self.__current_buttons) - 1
        elif self.__selected_button > len(self.__current_buttons) - 1:
            self.__selected_button = 0

        for w in self.__current_buttons:
            w.mark_off()
        self.__current_buttons[self.__selected_button].mark()

    def handle_rendering(self) -> None:
        super().handle_rendering()

        # Temporário
        title = f"Asteroid"
        font = pygame.font.get_default_font()
        message_img = pygame.font.SysFont(
            font, 50).render(title, True, (255, 255, 255))
        r = message_img.get_rect()
        r.center = (GameConstants().screen_size.x/2,
                    GameConstants().screen_size.y/2 - 100)
        self.get_owner().get_screen().blit(message_img, (r.x, r.y))

        for widget in self.__current_buttons:
            widget.draw(self.get_owner().get_screen())

    def handle_transition(self) -> None:
        if self.__keys_current_state[pygame.K_SPACE] == True and self.__keys_previous_state[pygame.K_SPACE] == False:
            widget = self.__current_buttons[self.__selected_button]
            if widget.get_key() == "play_button":
                self.__current_buttons = self.__modes_buttons
                self.__update_buttons_position()
            elif widget.get_key() == "back_button":
                self.__current_buttons = self.__action_buttons
                self.__update_buttons_position()
            elif widget.get_key() == "exit_button":
                self.get_owner().close()
            else:
                self.get_owner().change_state(widget.get_key())
