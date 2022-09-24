import pygame
from models.player import Player

class InputHandler:
    
    def __init__(self, player: Player) -> None:
        self.__player = player
    
    def handle_input(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            print("XL")
            print(f"mag {self.__player.get_velocity().magnitude()}")
            self.__player.accelerate()
        
        else:
            print("DXL")
            print(f"mag {self.__player.get_velocity().magnitude()}")
            self.__player.slowdown()
            

    