from utility.singleton.singleton import Singleton

class AsteroidSpawnConstants(Singleton):

    def __init__(self) -> None:
        self.cooldown = 5
        self.number_of_asteroids = 5
