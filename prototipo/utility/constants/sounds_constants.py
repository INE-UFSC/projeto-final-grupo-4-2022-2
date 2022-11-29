from utility.singleton.singleton import Singleton

import pygame


class SoundsConstants(Singleton):

    def __init__(self) -> None:
        self.shot_channel = 0
        self.explosion_channel = 1
        self.channel_2 = 2
        self.channel_3 = 3
        self.channel_4 = 4
        self.channel_5 = 5
        self.channel_6 = 6
        self.channel_7 = 7
        self.channel_8 = 8
        self.shot_sound = pygame.mixer.Sound('./sounds/weapon/shot.mp3')
        self.explosion_sound = pygame.mixer.Sound('./sounds/asteroid/explosionv2.mp3')
