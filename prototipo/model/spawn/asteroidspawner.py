
from model.factory.asteroidfactory import AsteroidFactory

from controller.entitiescontroller import EntitiesController

import utility.constants as CONSTANT


# Mesma lógica que o Spawn do Alien, porém
# ele só cria novos Asteroid (10 Asteroids) depois que não há
# mais Asteroids em campo
class AsteroidSpawner:

    def __init__(self) -> None:
        self.__factory = AsteroidFactory()

    def get_factory(self) -> AsteroidFactory:
        return self.__factory

    def _has_asteroids(self) -> bool:
        for entity in EntitiesController.instance().get_entities():
            if entity.get_tag() == CONSTANT.ASTEROID_TAG:
                return True
        return False

    def generate(self) -> None:
        if not(self._has_asteroids()):
            asteroids = AsteroidFactory().create(3)
            EntitiesController.instance().add_entities(asteroids)
