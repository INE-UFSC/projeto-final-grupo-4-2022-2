import pygame
from models.player import Player

class InputHandler:
    
    def __init__(self, player: Player) -> None:
        self.__player = player
    
    def handle_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.__player.accelerate()
        else:
            self.__player.slowdown()

        if key[pygame.K_RIGHT]:
            self.__player.rotate_clockwise()
        if key[pygame.K_LEFT]:
            self.__player.rotate_anticlockwise()

        
            

    