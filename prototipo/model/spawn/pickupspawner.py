
import random

# UTILITY
from utility.constants.pickup_constants import PickUpConstants

# MODEL
from model.factory.pickupfactory import PickUpFactory
from model.entities.pickups.bulletlesspickup import BulletlessPickUp
from model.entities.pickups.defaultpickup import DefaultWeaponPickUp
from model.entities.pickups.defaultbulletpickup import DefaultBulletPickUp
from model.entities.pickups.infinitypickup import InfinityPickUp
from model.entities.pickups.lifepickup import LifePickUp
from model.entities.pickups.persistentbulletpickup import PersistentBulletPickUp
from model.entities.pickups.rubberbulletpickup import RubberBulletPickUp
from model.entities.pickups.ammopickup import AmmoPickUp
from model.entities.pickups.shotgunpickup import ShotGunPickUp
from model.entities.pickups.bulletlesspickup import BulletlessPickUp

# MANAGER
from managers.entitiesmanager import EntitiesManager

# Mesma lógica que o Spawn do Alien, porém
# ele só cria novos pickups (10 Asteroids) depois que não há
# mais Asteroids em campo


class PickUpSpawner:

    def __init__(self) -> None:
        self.__cooldown = PickUpConstants().cooldown

        self.__pickups = [
            BulletlessPickUp,
            DefaultBulletPickUp,
            DefaultWeaponPickUp,
            InfinityPickUp,
            LifePickUp,
            PersistentBulletPickUp,
            RubberBulletPickUp,
            ShotGunPickUp,
            AmmoPickUp,
            BulletlessPickUp
        ]

    def get_cooldown(self) -> float:
        return self.__cooldown

    def set_cooldown(self, cooldown: float) -> None:
        self.__cooldown = cooldown

    def get_pickups(self) -> list:
        return self.__pickups

    def generate(self, dt: float) -> None:
        cd = self.get_cooldown()
        self.set_cooldown(cd - dt)

        if self.get_cooldown() <= 0:

            self.set_cooldown(PickUpConstants().cooldown)

            max = len(self.get_pickups()) - 1
            index = random.randint(0, max)
            type = self.get_pickups()[index]

            pickup = PickUpFactory().create(type)

            EntitiesManager.instance().add_entity(pickup)
