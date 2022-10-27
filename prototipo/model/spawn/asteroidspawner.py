
from model.factory.asteroidfactory import AsteroidFactory

from controller.entitiescontroller import EntitiesController

import utility.constants as CONSTANTS


class AsteroidSpawner:
    def __init__(self) -> None:
        self.__factory = AsteroidFactory()

    def get_factory(self) -> AsteroidFactory:
        return self.__factory

    def has_asteroids(self) -> bool:
        for entity in EntitiesController.instance().get_entities():
            if entity.get_tag() == CONSTANTS.ASTEROID_TAG:
                return True
        return False

    def generate(self) -> None:
        if not(self.has_asteroids()):
            asteroids = AsteroidFactory().create(10)
            EntitiesController.instance().add_entities(asteroids)
