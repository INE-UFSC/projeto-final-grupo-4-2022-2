from utility.singleton.singleton import Singleton

import pygame


class GameConstants(Singleton):

    def __init__(self) -> None:
        self.screen_size = pygame.math.Vector2(960, 500)
        self.fps = 60
        
        self.state_menu = "inmenu"
        self.state_end_game = "endgame"
        self.state_default_mode = "statedefaultmode"
        self.state_dodge_mode = "statedodgemode"
        self.state_alien_mode = "statealienmode"
        self.state_asteroid_mode = "stateasteroidmode"
        self.state_pickup_mode = "statepickupmode"
        self.state_score_board = "statescoreboard"

        self.game_music_path = './sounds/music/gamemusic.wav'
        self.endgame_music_path = './sounds/music/endgamemusic.wav'
        self.menu_music_path = './sounds/music/menumusic.wav'
