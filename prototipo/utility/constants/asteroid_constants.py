
from utility.singleton.singleton import Singleton

class AsteroidConstants(Singleton):

    def __init__(self):
        self.tag = "asteroid"
        self.small_size = 8
        self.medium_size = 16
        self.big_size = 32

        self.correction_constant = 800
        self.small_velocity_mag = self.correction_constant / self.small_size
        self.medium_velocity_mag = self.correction_constant / self.medium_size
        self.big_velocity_mag = self.correction_constant / self.big_size
        

