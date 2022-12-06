# UTILITY
from utility.states.statedefaultmode import StateDefaultMode
from utility.states.stateinendgame import StateInEndGame
from utility.states.stateinmenu import StateInMenu
from utility.states.state import State
from utility.states.statedodgemode import StateDodgeMode
from utility.states.statealienmode import StateAlienMode
from utility.states.stateasteroidmode import StateAsteroidMode
from utility.states.statepickupmode import StatePickUpMode
from utility.states.statescoreboard import StateScoreBoard
from utility.data.soundloader import SoundLoader
from utility.data.soundplayer import SoundPlayer

# CONSTANTS
from utility.constants.game_constants import GameConstants

# MISC
import random
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

        # Música
        self.__sound_loader = SoundLoader()
        self.__sound_player = SoundPlayer()
        music_1 = self.__sound_loader.load(GameConstants().music_1_path, 0.2)
        music_2 = self.__sound_loader.load(GameConstants().music_2_path, 0.2)
        music_3 = self.__sound_loader.load(GameConstants().music_3_path, 0.2)
        music_4 = self.__sound_loader.load(GameConstants().music_4_path, 0.2)
        self.__music_library = [music_1, music_2, music_3, music_4]
        self.__game_over_music = self.__sound_loader.load(GameConstants().game_over_music_path, 0.5)

        self.__current_music = None

    # ATRIBUTOS
    def get_current_state(self) -> State:
        return self.__current_state

    def set_current_state(self, new_state: State) -> None:
        self.__current_state = new_state

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
    
    def get_sound_loader(self) -> SoundLoader:
        return self.__sound_loader
    
    def get_sound_player(self) -> SoundPlayer:
        return self.__sound_player

    def get_music_library(self) -> list:
        return self.__music_library

    def get_game_over_music(self) -> pygame.mixer.Sound:
        return self.__game_over_music

    def get_current_music(self) -> pygame.mixer.Sound:
        return self.__current_music

    def set_current_music(self, current_music: pygame.mixer.Sound):
        self.__current_music = current_music

    # LÓGICA
    def is_running(self) -> bool:
        return self.__running

    def close(self) -> None:
        self.__running = False
        
    def change_state(self, new_state_str: str) -> None:

        # Game fazendo o papel do contexto
        next_state = self.get_states_dictionary()[new_state_str]        

        # Troca de estado
        self.get_current_state().exit()
        particle_set = self.get_current_state().snapshot_particles()
        self.set_current_state(next_state)
        self.get_current_state().load_particle_snapshot(particle_set)
        self.get_current_state().entry()

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

    def pick_random_music(self) -> pygame.mixer.Sound:
        index = random.randint(0, 3)
        return self.get_music_library()[index]

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
