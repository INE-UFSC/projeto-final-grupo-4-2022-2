
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from model.spawn.alienspawn import AlienSpawner
from model.factory.defaultplayerfactory import DefaultPlayerFactory

from utility.states.stateingame import StateInGame
from utility.debug import Debug

class StateAlienMode(StateInGame):

    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.__alien_spawner = None

    def entry(self):
        self.__alien_spawner = AlienSpawner()

        player = DefaultPlayerFactory().create()
        self._player = player
        self._debug = Debug(player)
        self._score_manager = ScoreManager(player)
        EntitiesController.instance().add_entity(player)

    def handle_update(self, dt: float) -> None:
        self.__alien_spawner.generate(dt)
        super().handle_update(dt)