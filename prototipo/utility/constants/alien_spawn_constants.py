from utility.singleton.singleton import Singleton


class AlienSpawnConstants(Singleton):

    def __init__(self) -> None:
        self.cooldown = 5
