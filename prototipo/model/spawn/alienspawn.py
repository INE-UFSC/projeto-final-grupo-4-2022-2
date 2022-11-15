
from model.entities.abstractentity import Entity
from model.factory.alienfactory import AlienFactory

from controller.entitiescontroller import EntitiesController

from utility.constants.alien_spawn_constants import AlienSpawnConstants

# Um spawn de Alien. Muito parecido com os spawns
# do Minecraft. A cada tantos segundos nasce um
# novo Alien randômicamente
class AlienSpawner:

    def __init__(self) -> None:
        self.__cooldown = AlienSpawnConstants().cooldown
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
        # Caso já passo o tempo de cooldown,
        # então cria-se um novo Alien randomicamente
        self.decrease(dt)
        if self.get_cooldown() < 0:
            self.set_cooldown(AlienSpawnConstants().cooldown)
            alien = self.get_factory().create()
            EntitiesController.instance().add_entity(alien)
