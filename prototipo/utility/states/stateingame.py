
# Model imports
from model.body import Body
from model.factory.playerfactory import PlayerFactory
from model.spawn.alienspawn import AlienSpawner
from model.spawn.asteroidspawner import AsteroidSpawner

# Controller imports
from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager
from controller.scoremanager import ScoreManager

# Utility imports
from utility.states.state import State
import utility.constants as CONSTANT
from utility.debug import Debug

# Pygame
from pygame.math import Vector2
import pygame

class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)
        self.__alien_spawner = AlienSpawner()
        self.__asteroid_spawner = AsteroidSpawner()

        self.__debug = Debug()

    def entry(self) -> None:

        # Criando player
        player_body = Body(Vector2(0, 0), Vector2(0, 0), CONSTANT.PLAYER_SIZE)
        player_lives = CONSTANT.MAX_LIVES
        player = PlayerFactory().create(player_body, player_lives)

        EntitiesController.instance().add_entity(player)

    def exit(self) -> None:
        pass

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    def handle_update(self, dt: float) -> None:

        #print(f"Numero de entidades: {len(EntitiesController.instance().get_entities())}")

        # Atualiza cada entidade do jogo
        entities = EntitiesController.instance().get_entities()
        for entity in entities:
            entity.update(dt)

        # Gerando alien
        self.__alien_spawner.generate(dt)

        # Gerando asteroids
        self.__asteroid_spawner.generate()

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
        for entity in EntitiesController.instance().get_entities()[::-1]:
            body = entity.get_body()
            pygame.draw.circle(self.get_owner().get_screen(), CONSTANT.COLORS_DIC[entity.get_tag()],
                               body.get_position(), body.get_radius())

        screen = self.get_owner().get_screen()
        self.__debug.blit_strings(screen)
