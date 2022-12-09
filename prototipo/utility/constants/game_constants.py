from utility.singleton.singleton import Singleton

import pygame

from tkinter import Tk
root = Tk() 
height = root.winfo_screenheight() 
width = root.winfo_screenwidth()


class GameConstants(Singleton):

    def __init__(self) -> None:
        self.screen_size = pygame.math.Vector2(width, height)
        self.fps = 55

        self.state_menu = "inmenu"
        self.state_end_game = "endgame"
        self.state_default_mode = "statedefaultmode"
        self.state_dodge_mode = "statedodgemode"
        self.state_alien_mode = "statealienmode"
        self.state_asteroid_mode = "stateasteroidmode"
        self.state_pickup_mode = "statepickupmode"
        self.state_score_board = "statescoreboard"

        self.music_1_path = './sounds/music/music_1.wav'
        self.music_2_path = './sounds/music/music_2.wav'
        self.music_3_path = './sounds/music/music_3.wav'
        self.music_4_path = './sounds/music/music_4.wav'
        self.game_over_music_path = './sounds/music/game_over.wav'
