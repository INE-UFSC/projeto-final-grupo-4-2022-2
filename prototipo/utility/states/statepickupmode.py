
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner
from model.spawn.pickupspawner import PikcUpSpawner
from model.factory.limitedbulletplayerfactory import LimitedBulletPlayerFactory

from utility.states.stateingame import StateInGame
from utility.debug import Debug


class Game: ...

class StatePickUpMode(StateInGame):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        self.__alien_spawner = None
        self.__asteroid_spawner = None
        self.__pickup_spawner = None

    def entry(self) -> None:
        self.__alien_spawner = AlienSpawner()
        self.__asteroid_spawner = AsteroidSpawner()
        self.__pickup_spawner = PikcUpSpawner()

        player = LimitedBulletPlayerFactory().create()
        self._player = player
        self._debug = Debug(player)
        self._score_manager = ScoreManager(player)

        EntitiesController.instance().add_entity(player)

    def handle_update(self, dt: float) -> None:
        self.__alien_spawner.generate(dt)
        self.__pickup_spawner.generate(dt)
        self.__asteroid_spawner.generate()
        super().handle_update(dt)
