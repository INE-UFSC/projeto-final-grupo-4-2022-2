
import random

# UTILITY
from utility.constants.pickup_constants import PickUpConstants

# MODEL
from model.factory.pickupfactory import PickUpFactory
from model.entities.bulletlesspickup import BulletlessPickUp
from model.entities.defaultpickup import DefaultWeaponPickUp
from model.entities.defaultbulletpickup import DefaultBulletPickUp
from model.entities.infinitypickup import InfinityPickUp
from model.entities.lifepickup import LifePickUp
from model.entities.persistentbulletpickup import PersistentBulletPickUp
from model.entities.rubberbulletpickup import RubberBulletPickUp
from model.entities.ammopickup import AmmoPickUp
from model.entities.shotgunpickup import ShotGunPickUp
from model.entities.bulletlesspickup import BulletlessPickUp

# CONTROL
from controller.entitiescontroller import EntitiesController

# Mesma lógica que o Spawn do Alien, porém
# ele só cria novos pickups (10 Asteroids) depois que não há
# mais Asteroids em campo
class PikcUpSpawner:

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

            max = len(self.get_pickups()) -1
            index = random.randint(0, max)
            type = self.get_pickups()[index]

            pickup = PickUpFactory().create(type)

            EntitiesController.instance().add_entity(pickup)
