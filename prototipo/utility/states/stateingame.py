
# Model imports
from math import ceil
from model.body import Body
from model.factory.playerfactory import PlayerFactory
from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner
from model.entities.player import Player
from model.entities.asteroid import Asteroid

# Controller imports
from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager
from controller.scoremanager import ScoreManager
from controller.levelcontroller import LevelController

# Utility imports
import utility.constants as CONSTANT
from utility.states.state import State
from utility.debug import Debug

# Pygame
from pygame.math import Vector2
import pygame


# Implementação do no jogo
# Nele estará a lógica de cada frame para o jogo
class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)
        self.__alien_spawner = AlienSpawner()
        self.__asteroid_spawner = AsteroidSpawner()
        self.__level_controller = LevelController()

        self.__debug = None

    def entry(self) -> None:
        # Criando player
        player_body = Body(Vector2(ceil(CONSTANT.SCREEN_SIZE.x/2),
                           ceil(CONSTANT.SCREEN_SIZE.y/2)),
                           Vector2(0, 0), CONSTANT.PLAYER_SIZE)
        player_lives = CONSTANT.MAX_LIVES
        player = PlayerFactory().create(player_body, player_lives)

        self.__debug = Debug(player)
        self.__level_controller.set_player(player)
        EntitiesController.instance().add_entity(player)

    def exit(self) -> None:
        EntitiesController.instance().clear_entities()  # limpar tudo

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
        self.__alien_spawner.generate(dt)

        # Gerando asteroids
        self.__asteroid_spawner.generate()

        # Detecta as colisões a cada frame
        collisions = CollisionDetector().detect_collisions(entities)

        # Trata as colisões
        CollisionManager().handle_collisions(collisions)

        # Atualiza o score do jogador baseado nas destruições e no tempo
        deletion_buffer = EntitiesController.instance().get_deletion_buffer()
        ScoreManager.instance().update_score(dt, deletion_buffer)

        # Gerencia as destruições de cada entidade
        EntitiesController.instance().handle_deletion()

        self.__debug.update(self.get_owner().get_clock())

    def handle_rendering(self) -> None:
        screen = self.get_owner().get_screen()

        for entity in EntitiesController.instance().get_entities()[::-1]:
            if isinstance(entity, Player):
                pygame.draw.line(screen, (255, 0, 0), entity.get_body().get_position(),
                                 entity.get_body().get_position() + entity.get_direction()*100, 1)
                pygame.draw.line(screen, (255, 255, 255), entity.get_body().get_position(),
                                 entity.get_body().get_position() + entity.get_body().get_velocity(), 1)
            if entity.image is None:
                continue
            screen.blit(entity.get_image(), entity.get_rect())
            
        self.__debug.render(screen)

    def handle_transition(self) -> None:
        self.__level_controller.update()
