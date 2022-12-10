
from abc import ABC, abstractmethod

from model.factory.bulletfactory import BulletFactory

from utility.constants.weapon_constants import WeaponConstants
from utility.data.soundloader import SoundLoader


class Shooter:
    ...

# Classe abstrata para as armas


class Weapon(ABC):

    _noammo_sound = SoundLoader().load(WeaponConstants().noammo_sound_path, 0.3)
    _default_weapon_sound = SoundLoader().load(
        WeaponConstants().default_weapon_sound_path, 0.3)
    _shotgun_sound = SoundLoader().load(WeaponConstants().shotgun_sound_path, 0.1)

    def __init__(self, owner: Shooter, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        self.__owner = owner
        self.__cooldown = cooldown
        self.__ammunition = ammunition
        self.__bullet_factory = bullet_factory
        self.__time_since_last_shot = cooldown

    def get_owner(self) -> Shooter:
        return self.__owner

    def set_owner(self, new_owner: Shooter) -> None:
        self.__owner = new_owner

    def get_cooldown(self) -> float:
        return self.__cooldown

    def set_cooldown(self, new_cooldown: float) -> None:
        self.__cooldown = new_cooldown

    def get_ammunition(self) -> int:
        return self.__ammunition

    def set_ammunition(self, new_ammunition: int) -> None:
        self.__ammunition = new_ammunition

    def get_bullet_factory(self) -> BulletFactory:
        return self.__bullet_factory

    def set_bullet_factory(self, new_bullet_factory: BulletFactory) -> None:
        self.__bullet_factory = new_bullet_factory

    def get_time_since_last_shot(self) -> float:
        return self.__time_since_last_shot

    def set_time_since_last_shot(self, new_value: float) -> None:
        self.__time_since_last_shot = new_value

    # Método que vai ser implementado de acordo com a classe de arma
    # Por exemplo, a arma shotgun ao invés de atirar um único tiro atira vários
    @abstractmethod
    def shoot(self, dt: float) -> None:
        pass

    def __str__(self) -> str:
        return f"Weapon (ABC) (!)"
