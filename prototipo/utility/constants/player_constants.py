
from utility.singleton.singleton import Singleton


class PlayerConstants(Singleton):

    def __init__(self) -> None:
        self.tag = "player"
        self.size = 10
        self.max_velocity_mag = 300
        self.max_lives = 3
        self.acceleration_mag = 350
        self.slowdown_coefficient = -50
        self.angular_velocity = 250
        self.image_path = './images/player/player_inertial.png'
