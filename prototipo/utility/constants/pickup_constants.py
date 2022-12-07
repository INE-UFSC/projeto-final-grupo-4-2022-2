
from utility.singleton.singleton import Singleton


class PickUpConstants(Singleton):

    def __init__(self) -> None:
        self.tag = "pickup"
        self.size = 30
        self.image_path = ""
        self.cooldown = 5
        self.path_shotgun = "./images/weapon/shotgun.png"
        self.path_pistola = "./images/weapon/pistola.png"
        self.path_cura = "./images/weapon/cura.png"
        self.path_infinito = "./images/weapon/infinito.png"
        self.path_block = "./images/weapon/block.png"
        self.path_ammo = "./images/weapon/ammo.png"
        self.path_defaultbullet = "./images/weapon/red_ball.png"
        self.path_persistentbullet = "./images/weapon/yellow_ball.png"
        self.path_piercingbullet = "./images/weapon/green_ball.png"
        self.path_rubberbullet = "./images/weapon/purple_ball.png"
