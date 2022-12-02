from utility.singleton.singleton import Singleton

import pygame


class SoundsConstants(Singleton):

    def __init__(self) -> None:
        self.shot_channel = 0
        self.explosion_channel = 1
        self.shotgun_channel = 2
        self.infinity_channel = 3
        self.music_channel = 4
        self.noammo_channel = 5
        self.channel_6 = 6
        self.channel_7 = 7
        self.channel_8 = 8

        self.explosion_sound = pygame.mixer.Sound('./sounds/asteroid/explosion.wav')
        self.shotgun_sound = pygame.mixer.Sound('./sounds/weapon/shotgun.wav')
        self.default_shot_sound = pygame.mixer.Sound('./sounds/weapon/infinityshot.wav')
        self.game_music = pygame.mixer.Sound('./sounds/music/gamemusic.wav')
        self.endgame_music = pygame.mixer.Sound('./sounds/music/endgamemusic.wav')
        self.menu_music = pygame.mixer.Sound('./sounds/music/menumusic.wav')
        self.noammo_sound = pygame.mixer.Sound('./sounds/weapon/noammo.wav')

        pygame.mixer.Channel(self.music_channel).set_volume(0.3)