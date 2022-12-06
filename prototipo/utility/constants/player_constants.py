
from utility.singleton.singleton import Singleton


class PlayerConstants(Singleton):

    def __init__(self) -> None:
        self.tag = "player"
        self.size = 10
        self.max_velocity_mag = 100
        self.max_lives = 5
        self.acceleration_mag = 125
        self.slowdown_coefficient = -15
        self.angular_velocity = 100
        self.image_path = './images/player/player_inertial.png'
