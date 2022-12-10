from utility.singleton.singleton import Singleton


class ShooterConstants(Singleton):

    def __init__(self) -> None:
        self.radius_multiplier = 1.2
