from utility.singleton.singleton import Singleton


class AsteroidSpawnConstants(Singleton):

    def __init__(self) -> None:
        self.cooldown = 2
        self.number_of_asteroids = 10
