
from weapon import Weapon

class BulletlessWeapon(Weapon):

    def __init__(self) -> None:
        super().__init__()

    def shoot(self) -> None:
        pass
