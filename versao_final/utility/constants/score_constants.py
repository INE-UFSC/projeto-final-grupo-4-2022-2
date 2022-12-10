
from utility.singleton.singleton import Singleton


class ScoreConstants(Singleton):

    def __init__(self) -> None:
        self.destroy = 10
        self.time = 5
        self.time_to_score = 20
