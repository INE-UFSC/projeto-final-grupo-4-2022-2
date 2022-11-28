
from utility.states.state import State
from utility.constants.game_constants import GameConstants
from utility.widgets.button import Button

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
        b_default_mode = Button("default_mode", text="Default", font_size=30)
        b_dodge_mode = Button("dodge_mode", text="Dodge", font_size=30)
        b_asteroid_mode = Button("asteroid_mode", text="Asteroid", font_size=30)
        b_alien_mode = Button("alien_mode", text="Alien", font_size=30)
        b_pickup_mode = Button("pickup_mode", text="PickUp", font_size=30)
        b_exit = Button("exit_button", text="Exit", font_size=30)
        self.__widgets = [b_default_mode, b_dodge_mode,
                          b_asteroid_mode, b_alien_mode,
                          b_pickup_mode, b_exit]

        for i, w in enumerate(self.__widgets):
            pos = pygame.math.Vector2(GameConstants().screen_size.x/2, GameConstants().screen_size.y/2 + w.get_font_size() * 1.1 * (i - 1))
            w.set_position(pos)

        self.__keys_current_state = {pygame.K_UP: False,
                                     pygame.K_DOWN: False,
                                     pygame.K_SPACE: False}
        self.__keys_previous_state = {pygame.K_UP: False,
                                      pygame.K_DOWN: False,
                                      pygame.K_SPACE: False}
        self.__selected_button = 0


    def entry(self) -> None:
        pass

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

        if self.__keys_current_state[pygame.K_UP] == True and self.__keys_previous_state[pygame.K_UP] == False:
            self.__selected_button -= 1
        if self.__keys_current_state[pygame.K_DOWN] == True and self.__keys_previous_state[pygame.K_DOWN] == False:
            self.__selected_button += 1

        if self.__selected_button < 0:
            self.__selected_button = len(self.__widgets) - 1
        elif self.__selected_button > len(self.__widgets) - 1:
            self.__selected_button = 0

        for w in self.__widgets:
            w.mark_off()
        self.__widgets[self.__selected_button].mark()
        

    def handle_rendering(self) -> None:
        # Temporário
        title = f"Asteroid"
        font = pygame.font.get_default_font()
        message_img = pygame.font.SysFont(font, 50).render(title, True, (255, 255, 255))
        r = message_img.get_rect()
        r.center = (GameConstants().screen_size.x/2, GameConstants().screen_size.y/2 - 100)
        self.get_owner().get_screen().blit(message_img, (r.x, r.y))

        for widget in self.__widgets:
            widget.draw(self.get_owner().get_screen())

    def handle_transition(self) -> None:
        if self.__keys_current_state[pygame.K_SPACE] == True and self.__keys_previous_state[pygame.K_SPACE] == False:
            widget = self.__widgets[self.__selected_button]
            if widget.get_key() == "default_mode":
                next_state = GameConstants().state_default_mode
                self.get_owner().change_state(next_state)
            elif widget.get_key() == "dodge_mode":
                next_state = GameConstants().state_dodge_mode
                self.get_owner().change_state(next_state)
            elif widget.get_key() == "asteroid_mode":
                next_state = GameConstants().state_asteroid_mode
                self.get_owner().change_state(next_state)
            elif widget.get_key() == "alien_mode":
                next_state = GameConstants().state_alien_mode
                self.get_owner().change_state(next_state)
            elif widget.get_key() == "pickup_mode":
                next_state = GameConstants().state_pickup_mode
                self.get_owner().change_state(next_state)
            else:
                self.get_owner().close()

