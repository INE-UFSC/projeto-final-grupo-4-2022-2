
from utility.singleton.singleton import Singleton


class PickUpConstants(Singleton):

    def __init__(self):
        self.tag = "pickup"
        self.size = 10
        self.image_path = ""
