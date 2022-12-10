
from model.entities.abstractentity import Entity
from model.factory.asteroidfactory import AsteroidFactory


from managers.entitiesmanager import EntitiesManager

from utility.constants.asteroid_spawn_constants import AsteroidSpawnConstants

# Classe que spawna asteroids aleatoriamente
# Utilizado para a implementação do AsteroidMode


class AsteroidSpawnerTime:

    def __init__(self) -> None:
        self.__cooldown = AsteroidSpawnConstants().cooldown
        self.__factory = AsteroidFactory()

    def set_cooldown(self, cooldown: float) -> None:
        self.__cooldown = cooldown

    def get_cooldown(self) -> float:
        return self.__cooldown

    def get_factory(self) -> AsteroidFactory:
        return self.__factory

    def decrease(self, dt: float) -> None:
        self.set_cooldown(self.get_cooldown() - dt)

    def update(self, dt: float) -> Entity:
        # Caso já passo o tempo de cooldown,
        # então cria-se novos asteroids randomicamente
        self.decrease(dt)
        if self.get_cooldown() < 0:
            self.set_cooldown(AsteroidSpawnConstants().cooldown)
            asteroid = self.get_factory().create(1)
            EntitiesManager.instance().add_entities(asteroid)
