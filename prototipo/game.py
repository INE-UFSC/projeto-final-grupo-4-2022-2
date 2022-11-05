
from utility.states.stateingame import StateInGame
from utility.states.stateinendgame import StateInEndGame
from utility.states.stateinmenu import StateInMenu
from utility.states.state import State
import utility.constants as CONSTANTE


import pygame
from pygame import Surface
from pygame.time import Clock

# O Game determinará o fluxo do jogo
class Game:

    def __init__(self, name="Game"):
        pygame.init()
        pygame.display.set_caption(name)

        self.__running = True
        self.__current_state = StateInGame(self)
        self.__screen = pygame.display.set_mode(tuple(CONSTANTE.SCREEN_SIZE))
        self.__clock = pygame.time.Clock()
        
        self.__states_dictionary = {
            CONSTANTE.STATE_MENU: StateInMenu(self),
            CONSTANTE.STATE_IN_GAME: StateInGame(self), 
            CONSTANTE.STATE_END_GAME: StateInEndGame(self)
        }

    def is_running(self) -> bool:
        return self.__running

    def close(self) -> None:
        self.__running = False

    def get_current_state(self):
        return self.__current_state

    def set_current_state(self, new_state: State) -> None:
        self.__current_state = new_state

    def change_state(self, new_state_str: str) -> None:

        # Game fazendo o papel do contexto
        next_state = self.get_states_dictionary()[new_state_str]        

        # Troca de estado
        self.get_current_state().exit()
        self.set_current_state(next_state)
        self.get_current_state().entry()

    def get_screen(self) -> Surface:
        return self.__screen

    def set_screen(self, new_screen: Surface) -> None:
        self.__screen = new_screen

    def get_clock(self) -> Clock:
        return self.__clock

    def set_clock(self, new_clock: Clock) -> None:
        self.__clock = new_clock

    def get_states_dictionary(self) -> dict:
        return self.__states_dictionary

    def set_states_dictionary(self, states_dic: dict) -> None:
        self.__states_dictionary = states_dic

    def handle_event(self) -> None:
        self.__current_state.handle_event()

    def handle_update(self, dt: float) -> None:
        self.__current_state.handle_update(dt)

    def clean_window(self) -> None:
        self.get_screen().fill((0, 0, 0))

    def update_screen(self) -> None:
        pygame.display.update()

    def handle_rendering(self) -> None:
        self.clean_window()
        self.__current_state.handle_rendering()
        self.update_screen()

    def handle_transition(self):
        self.__current_state.handle_transition()

    def run(self) -> None:
        self.get_current_state().entry()
        while self.is_running():
            dt = 1.0/self.get_clock().tick(CONSTANTE.FPS)
            self.handle_event()
            self.handle_update(dt)
            self.handle_rendering()
            self.handle_transition()
        self.get_current_state().exit()
        pygame.quit()
