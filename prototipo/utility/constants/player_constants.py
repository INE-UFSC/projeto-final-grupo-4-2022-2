
from utility.singleton.singleton import Singleton


class PlayerConstants(Singleton):

    def __init__(self) -> None:
        self.tag = "player"
        self.size = 10
        self.max_velocity_mag = 90
        self.max_lives = 5
        self.acceleration_mag = 90
        self.slowdown_coefficient = -10
        self.angular_velocity = 80
        self.image_path = './images/player/player_inertial.png'
