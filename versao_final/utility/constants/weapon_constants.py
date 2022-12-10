from utility.singleton.singleton import Singleton


class WeaponConstants(Singleton):

    def __init__(self) -> None:
        self.cooldown = 0.2
        self.max_ammunition = 10000

        self.default_weapon_sound_path = './sounds/weapon/infinityshot.wav'
        self.shotgun_sound_path = './sounds/weapon/shotgun.wav'
        self.noammo_sound_path = './sounds/weapon/noammo.wav'
