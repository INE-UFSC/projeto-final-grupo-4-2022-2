
from utility.singleton.singleton import Singleton


class BulletConstants(Singleton):

    def __init__(self) -> None:
        self.tag = "bullet"
        self.size = 3
        self.velocity_mag = 450
        self.life_time = 2
        self.image_path = './images/bullet/bullet.png'
