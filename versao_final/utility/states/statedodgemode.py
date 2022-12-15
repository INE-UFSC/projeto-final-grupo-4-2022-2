
from managers.entitiesmanager import EntitiesManager
from managers.gfxmanager import GFXManager
from managers.scoremanager import ScoreManager

from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner
from model.factory.bulletlessplayerfactory import BulletLessPlayerFactory

from utility.statusreporter import StatusReporter
from utility.states.stateingame import StateInGame
from utility.debug import Debug


class Game:
    ...


class StateDodgeMode(StateInGame):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        self.__alien_spawner = None
        self.__asteroid_spawner = None

    def entry(self) -> None:
        super().entry()
        self.__alien_spawner = AlienSpawner()
        self.__asteroid_spawner = AsteroidSpawner()

        player = BulletLessPlayerFactory().create()
        self._player = player
        #self._debug = Debug(player)
        self._score_manager = ScoreManager(player)
        self._status_reporter = StatusReporter(player)
        EntitiesManager.instance().add_entity(player)

    def exit(self) -> None:
        super().exit()
        GFXManager().instance().clear()

    def handle_update(self, dt: float) -> None:
        super().handle_update(dt)
        self.__alien_spawner.update(dt)
        self.__asteroid_spawner.generate()
