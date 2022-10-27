
from model.entities.abstractentity import Entity
from model.factory.alienfactory import AlienFactory

from controller.entitiescontroller import EntitiesController

import utility.constants as CONSTANTS


class AlienSpawner:
    def __init__(self) -> None:
        self.__cooldown = 20
        self.__factory = AlienFactory()

    def set_cooldown(self, cooldown: float):
        self.__cooldown = cooldown

    def get_cooldown(self) -> float:
        return self.__cooldown

    def get_factory(self) -> AlienFactory:
        return self.__factory

    def decrease(self, dt: float):
        self.set_cooldown(self.get_cooldown() - dt)

    def generate(self, dt: float) -> Entity:
        self.decrease(dt)
        if self.get_cooldown() < 0:
            self.set_cooldown(CONSTANTS.ALIEN_SPAWN_COOLDOWN)
            alien = self.get_factory().create()
            EntitiesController.instance().add_entity(alien)
