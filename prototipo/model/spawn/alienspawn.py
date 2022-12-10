
from model.entities.abstractentity import Entity
from model.factory.alienfactory import AlienFactory

from managers.entitiesmanager import EntitiesManager

from utility.constants.alien_spawn_constants import AlienSpawnConstants

# Um spawn de Alien. Muito parecido com os spawns
# do Minecraft. A cada tantos segundos nasce um
# novo Alien randômicamente


class AlienSpawner:

    def __init__(self) -> None:
        self.__cooldown = AlienSpawnConstants().cooldown
        self.__factory = AlienFactory()
        self.__cooldown_decrement = 0
        self.__created_aliens = 0

    def set_cooldown(self, cooldown: float) -> None:
        self.__cooldown = cooldown

    def get_cooldown(self) -> float:
        return self.__cooldown

    def get_factory(self) -> AlienFactory:
        return self.__factory

    def set_cooldown_decrement(self, cooldown_decrement: float) -> None:
        self.__cooldown_decrement = cooldown_decrement

    def get_cooldown_decrement(self) -> float:
        return self.__cooldown_decrement

    def set_created_aliens(self, created_aliens: int) -> None:
        self.__created_aliens = created_aliens

    def get_created_aliens(self) -> int:
        return self.__created_aliens

    def decrease(self, dt: float) -> None:
        self.set_cooldown(self.get_cooldown() - dt)

    def update(self, dt: float) -> Entity:
        # Caso já passo o tempo de cooldown,
        # então cria-se um novo Alien randomicamente
        self.decrease(dt)
        if self.get_cooldown() - self.get_cooldown_decrement() > 0:
            return

        self.set_cooldown(AlienSpawnConstants().cooldown)
        alien = self.get_factory().create()
        EntitiesManager.instance().add_entity(alien)
        self.set_created_aliens(self.get_created_aliens() + 1)

        if self.get_created_aliens() % 10 == 0 and self.get_cooldown_decrement() < 4:
            self.set_cooldown_decrement(self.get_cooldown_decrement() + 0.2)
            self.set_created_aliens(0)
