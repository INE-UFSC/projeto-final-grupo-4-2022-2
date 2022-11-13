
from utility.singleton.singleton import Singleton

import math
import pygame


class AlienConstants(Singleton):

    def __init__(self):
        self.tag = "alien"
        self.size = 10
        self.velocity_mag = 40
        self.move_cooldown = 3
        self.shoot_cooldown = 5
        self.directions = (pygame.math.Vector2(math.sqrt(2)/2, math.sqrt(2)/2),
                           pygame.math.Vector2(1, 0),
                           pygame.math.Vector2(math.sqrt(2)/2, -math.sqrt(2)/2))
        self.image_path = './images/alien/alien.png'
