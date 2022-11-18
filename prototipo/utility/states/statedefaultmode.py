
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from model.body import Body
from model.entities.ammopickup import AmmoPickUp
from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner
from model.factory.limitedbulletplayerfactory import LimitedBulletPlayerFactory

from utility.states.stateingame import StateInGame
from utility.debug import Debug
from utility.constants.pickup_constants import PickUpConstants

from pygame.math import Vector2

class StateDefaultMode(StateInGame):

    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.__alien_spawner = None
        self.__asteroid_spawner = None

    def entry(self) -> None:
        self.__alien_spawner = AlienSpawner()
        self.__asteroid_spawner = AsteroidSpawner()

        player = LimitedBulletPlayerFactory().create()
        self._player = player
        self._debug = Debug(player)
        self._score_manager = ScoreManager(player)

        pickup = AmmoPickUp(Body(Vector2(100,100),Vector2(0,0), PickUpConstants().size))
        EntitiesController.instance().add_entity(pickup)
        EntitiesController.instance().add_entity(player)

    def handle_update(self, dt: float) -> None:
        self.__alien_spawner.generate(dt)
        self.__asteroid_spawner.generate()
        super().handle_update(dt)
