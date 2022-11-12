from utility.singleton.singleton import Singleton

import pygame


class GameConstants(Singleton):

    def __init__(self):
        self.screen_size = pygame.math.Vector2(960, 500)
        self.fps = 60
        
        self.state_menu = "inmenu"
        self.state_end_game = "endgame"
        self.state_in_game = "ingame"
