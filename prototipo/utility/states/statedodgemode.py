
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner
from model.factory.bulletlessplayerfactory import BulletLessPlayerFactory 

from utility.states.stateingame import StateInGame
from utility.debug import Debug

class StateDodgeMode(StateInGame):

    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.__alien_spawner = None
        self.__asteroid_spawner = None

    def entry(self):
        self.__alien_spawner = AlienSpawner()
        self.__asteroid_spawner = AsteroidSpawner()

        player = BulletLessPlayerFactory().create()
        self._debug = Debug(player)
        self._level_controller.set_player(player)
        self._score_manager = ScoreManager(player)
        EntitiesController.instance().add_entity(player)

    def handle_update(self, dt: float) -> None:
        self.__alien_spawner.generate(dt)
        self.__asteroid_spawner.generate()
        super().handle_update(dt)
