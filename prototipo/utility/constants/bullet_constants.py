
from utility.singleton.singleton import Singleton

class BulletConstants(Singleton):

    def __init__(self):
        self.tag = "bullet"
        self.size = 2
        self.velocity_mag = 150
        self.life_time = 3
