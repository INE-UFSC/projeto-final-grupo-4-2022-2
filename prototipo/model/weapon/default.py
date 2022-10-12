

from weapon import Weapon

class DefaultWeapon(Weapon):

    def __init__(self) -> None:
        super().__init__()

    def shoot(self) -> None:
        pass