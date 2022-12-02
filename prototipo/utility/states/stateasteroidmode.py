
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from model.spawn.asteroidspawntertime import AsteroidSpawnerTime
from model.factory.defaultplayerfactory import DefaultPlayerFactory

from utility.states.stateingame import StateInGame
from utility.debug import Debug
from utility.statusreporter import StatusReporter
from utility.constants.sounds_constants import game_music

import pygame

class Game: ...

class StateAsteroidMode(StateInGame):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        self.__asteroid_spawner = None

    def entry(self) -> None:
        self.__asteroid_spawner = AsteroidSpawnerTime()

        player = DefaultPlayerFactory().create()
        self._player = player
        self._debug = Debug(player)
        self._score_manager = ScoreManager(player)
        self._status_reporter = StatusReporter(player)

        EntitiesController.instance().add_entity(player)
        
        game_music.play()

    def exit(self) -> None:
        game_music.stop()

    def handle_update(self, dt: float) -> None:
        self.__asteroid_spawner.generate(dt)
        super().handle_update(dt)
