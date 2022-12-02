from utility.singleton.singleton import Singleton

import pygame

pygame.mixer.init()

default_shot_sound = pygame.mixer.Sound('./sounds/weapon/infinityshot.wav')
explosion_sound = pygame.mixer.Sound('./sounds/asteroid/explosion.wav')
shotgun_sound = pygame.mixer.Sound('./sounds/weapon/shotgun.wav')
game_music = pygame.mixer.Sound('./sounds/music/gamemusic.wav')
endgame_music = pygame.mixer.Sound('./sounds/music/endgamemusic.wav')
menu_music = pygame.mixer.Sound('./sounds/music/menumusic.wav')
noammo_sound = pygame.mixer.Sound('./sounds/weapon/noammo.wav')
