
from utility.singleton.singleton import Singleton


class BulletConstants(Singleton):

    def __init__(self) -> None:
        self.tag = "bullet"
        self.size = 3
        self.velocity_mag = 300
        self.life_time = 3
        self.image_path = './images/bullet/bullet.png'
