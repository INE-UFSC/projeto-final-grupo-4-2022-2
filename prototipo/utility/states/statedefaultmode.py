
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from model.body import Body
from model.entities.ammopickup import AmmoPickUp
from model.entities.lifepickup import LifePickUp
from model.entities.shotgunpickup import ShotGunPickUp
from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner
from model.factory.limitedbulletplayerfactory import LimitedBulletPlayerFactory

from utility.states.stateingame import StateInGame
from utility.debug import Debug
from utility.constants.pickup_constants import PickUpConstants

from pygame.math import Vector2

class Game: ...

class StateDefaultMode(StateInGame):

    def __init__(self, owner: Game) -> None:
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

        pickup1 = AmmoPickUp(Body(Vector2(150,100),Vector2(0,0), PickUpConstants().size))
        pickup2 = LifePickUp(Body(Vector2(100,100),Vector2(0,0), PickUpConstants().size))
        pickup3 = ShotGunPickUp(Body(Vector2(200,100),Vector2(0,0), PickUpConstants().size))
        EntitiesController.instance().add_entity(pickup1)
        EntitiesController.instance().add_entity(pickup2)
        EntitiesController.instance().add_entity(pickup3)
        EntitiesController.instance().add_entity(player)

    def handle_update(self, dt: float) -> None:
        self.__alien_spawner.generate(dt)
        self.__asteroid_spawner.generate()
        super().handle_update(dt)
