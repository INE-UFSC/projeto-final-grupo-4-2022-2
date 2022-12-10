
from model.factory.asteroidfactory import AsteroidFactory

from managers.entitiesmanager import EntitiesManager

from utility.constants.asteroid_constants import AsteroidConstants
from utility.constants.asteroid_spawn_constants import AsteroidSpawnConstants

# Mesma lógica que o Spawn do Alien, porém
# ele só cria novos Asteroid (10 Asteroids) depois que não há
# mais Asteroids em campo


class AsteroidSpawner:

    def __init__(self) -> None:
        self.__factory = AsteroidFactory()

    def get_factory(self) -> AsteroidFactory:
        return self.__factory

    def _has_asteroids(self) -> bool:
        for entity in EntitiesManager.instance().get_entities():
            if entity.get_tag() == AsteroidConstants().tag:
                return True
        return False

    def generate(self) -> None:
        if not(self._has_asteroids()):
            asteroids = AsteroidFactory().create(AsteroidSpawnConstants().number_of_asteroids)
            EntitiesManager.instance().add_entities(asteroids)
