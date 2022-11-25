
from utility.singleton.singleton import Singleton


class PickUpConstants(Singleton):

    def __init__(self) -> None:
        self.tag = "pickup"
        self.size = 30
        self.image_path = ""
        self.cooldown = 5
