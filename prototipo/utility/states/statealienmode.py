
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

from model.spawn.alienspawn import AlienSpawner
from model.factory.defaultplayerfactory import DefaultPlayerFactory

from utility.states.stateingame import StateInGame
from utility.debug import Debug
from utility.statusreporter import StatusReporter
from utility.constants.sounds_constants import SoundsConstants

import pygame

class Game: ...

class StateAlienMode(StateInGame):

    def __init__(self, owner: Game) -> None:
        super().__init__(owner)
        self.__alien_spawner = None

    def entry(self) -> None:
        self.__alien_spawner = AlienSpawner()

        player = DefaultPlayerFactory().create()
        self._player = player
        self._debug = Debug(player)
        self._score_manager = ScoreManager(player)
        self._status_reporter = StatusReporter(player)
        EntitiesController.instance().add_entity(player)

        canal = SoundsConstants().music_channel
        som = SoundsConstants().game_music
        pygame.mixer.Channel(canal).play(som)

    def exit(self) -> None:
        canal = SoundsConstants().music_channel
        pygame.mixer.Channel(canal).stop()

    def handle_update(self, dt: float) -> None:
        self.__alien_spawner.generate(dt)
        super().handle_update(dt)
