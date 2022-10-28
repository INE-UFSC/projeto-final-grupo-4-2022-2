
# Model imports
from math import ceil
from model.body import Body
from model.factory.playerfactory import PlayerFactory
from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner
from model.entities.player import Player

# Controller imports
from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager
from controller.scoremanager import ScoreManager
from controller.levelcontroller import LevelController

# Utility imports
import utility.constants as CONSTANTE
from utility.states.state import State
from utility.debug import Debug

# Pygame
from pygame.math import Vector2
import pygame

class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)
        self.__alien_spawner = AlienSpawner()
        self.__asteroid_spawner = AsteroidSpawner()
        self.__level_controller = LevelController()

        self.__debug = Debug()

    def entry(self) -> None:
        # Criando player
        player_body = Body(Vector2(ceil(CONSTANTE.SCREEN_SIZE.x/2), ceil(CONSTANTE.SCREEN_SIZE.y/2)), Vector2(0, 0), CONSTANTE.PLAYER_SIZE)
        player_lives = CONSTANTE.MAX_LIVES
        player = PlayerFactory().create(player_body, player_lives)
        player.set_direction(Vector2(0, -CONSTANTE.SCREEN_SIZE.y/2).normalize())

        self.__level_controller.set_player(player)
        EntitiesController.instance().add_entity(player)


    def exit(self) -> None:
        EntitiesController.instance().clear_entities() # limpar tudo

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    def handle_update(self, dt: float) -> None:

        # Atualiza cada entidade do jogo
        entities = EntitiesController.instance().get_entities()
        for entity in entities:
            entity.update(dt)

        # Gerando alien
        #self.__alien_spawner.generate(dt)

        # Gerando asteroids
        #self.__asteroid_spawner.generate()

        # Detecta as colisões a cada frame e as registram
        CollisionDetector.instance().detect_collisions(entities)

        # Trata as colisões
        CollisionManager.instance().handle_collisions()

        # Atualiza o score do jogador baseado nas destruições e no tempo
        ScoreManager.instance().update_score(dt)

        # Gerencia as destruições de cada entidade
        EntitiesController.instance().handle_deletion()

        self.__debug.update(self.get_owner().get_clock(), EntitiesController.instance().get_entities()[0])

    def handle_rendering(self) -> None:
        screen = self.get_owner().get_screen()
        for entity in EntitiesController.instance().get_entities()[::-1]:
            body = entity.get_body()
            pygame.draw.circle(screen, CONSTANTE.COLORS_DIC[entity.get_tag()],
                               body.get_position(), body.get_radius())
            if isinstance(entity, Player):
                pygame.draw.line(screen, (255,0,0), entity.get_body().get_position(), entity.get_body().get_position() + entity.get_direction()*100, 1)
                pygame.draw.line(screen, (255,255,255), entity.get_body().get_position(), entity.get_body().get_position() + entity.get_body().get_velocity(), 1)
        self.__debug.render(screen)

    def handle_transition(self) -> None:
        self.__level_controller.update()
