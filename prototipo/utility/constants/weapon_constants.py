from utility.singleton.singleton import Singleton

class WeaponConstants(Singleton):

    def __init__(self) -> None:
        self.cooldown = 0.5
        self.max_ammunition = 1000
