
from utility.states.statedefaultmode import StateDefaultMode
from utility.states.stateinendgame import StateInEndGame
from utility.states.stateinmenu import StateInMenu
from utility.states.state import State
from utility.states.statedodgemode import StateDodgeMode
from utility.states.statealienmode import StateAlienMode
from utility.states.stateasteroidmode import StateAsteroidMode
from utility.states.statepickupmode import StatePickUpMode
from utility.states.statescoreboard import StateScoreBoard
from utility.constants.game_constants import GameConstants
from utility.data.soundloader import SoundLoader

import pygame
from pygame import Surface
from pygame.time import Clock

# O Game determinará o fluxo do jogo
class Game:

    def __init__(self, name="Game") -> None:
        pygame.mixer.pre_init(44100, -16, 8, 2048)
        pygame.mixer.init()
        pygame.init()
        pygame.display.set_caption(name)

        self.__running = True
        self.__current_state = StateInMenu(self)
        self.__screen = pygame.display.set_mode(tuple(GameConstants().screen_size))
        self.__clock = pygame.time.Clock()

        self.__states_dictionary = {
            GameConstants().state_menu: StateInMenu(self),
            GameConstants().state_default_mode: StateDefaultMode(self), 
            GameConstants().state_end_game: StateInEndGame(self),
            GameConstants().state_dodge_mode: StateDodgeMode(self),
            GameConstants().state_alien_mode: StateAlienMode(self),
            GameConstants().state_pickup_mode: StatePickUpMode(self),
            GameConstants().state_asteroid_mode: StateAsteroidMode(self),
            GameConstants().state_score_board: StateScoreBoard(self)
         }

        self.__game_music_sound = SoundLoader().load(GameConstants().game_music_path, 0.1)
        self.__menu_music_sound = SoundLoader().load(GameConstants().menu_music_path, 0.1)
        self.__endgame_music_sound = SoundLoader().load(GameConstants().endgame_music_path, 0.1)

    def is_running(self) -> bool:
        return self.__running

    def close(self) -> None:
        self.__running = False

    def get_current_state(self) -> State:
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

    def get_game_music_sound(self) -> pygame.mixer.Sound:
        return self.__game_music_sound

    def get_menu_music_sound(self) -> pygame.mixer.Sound:
        return self.__menu_music_sound

    def get_endgame_music_sound(self) -> pygame.mixer.Sound:
        return self.__endgame_music_sound

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

    def handle_transition(self) -> None:
        self.__current_state.handle_transition()

    # Método que vai definir o fluxo do jogo
    def run(self) -> None:
        self.get_current_state().entry()
        while self.is_running():
            self.get_clock().tick(GameConstants().fps)
            try:
                dt = 1.0/self.get_clock().get_fps()
            except ZeroDivisionError as e:
                dt = 1.0/60.0
            self.handle_event()
            self.handle_update(dt)
            self.handle_rendering()
            self.handle_transition()
        self.get_current_state().exit()
        pygame.quit()
