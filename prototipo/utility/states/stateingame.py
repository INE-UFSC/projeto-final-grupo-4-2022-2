
# Model imports
from model.body import Body
from model.factory.asteroidfactory import AsteroidFactory
from model.factory.playerfactory import PlayerFactory
from model.factory.alienfactory import AlienFactory
from model.spawn.alienspawn import AlienSpawn

# Controller imports
from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager
from controller.scoremanager import ScoreManager


# Utility imports
from utility.states.state import State
import utility.constants as CONSTANT

# Pygame
from pygame.math import Vector2
import pygame


class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)
        self.__alien_spawn = AlienSpawn()

    def entry(self) -> None:

        # Criando player
        player_body = Body(Vector2(0, 0), Vector2(0, 0), CONSTANT.PLAYER_SIZE)
        player_lives = CONSTANT.MAX_LIVES
        player = PlayerFactory().create(player_body, player_lives)

        # Asteroides
        asteroids = AsteroidFactory().create(0)

        # Alien
        alien = AlienFactory().create()

        EntitiesController.instance().add_entity(player)
        EntitiesController.instance().add_entities(asteroids)
        EntitiesController.instance().add_entity(alien)

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
        self.__alien_spawn.generate(dt)

        # Detecta as colisões a cada frame e as registram
        CollisionDetector.instance().detect_collisions(entities)

        # Trata as colisões
        CollisionManager.instance().handle_collisions()

        # Atualiza o score do jogador baseado nas destruições e no tempo
        ScoreManager.instance().update_score(dt)

        # Gerencia as destruições de cada entidade
        EntitiesController.instance().handle_deletion()

    def handle_rendering(self) -> None:
        for entity in EntitiesController.instance().get_entities()[::-1]:
            body = entity.get_body()
            pygame.draw.circle(self.get_owner().get_screen(), CONSTANT.COLORS[entity.get_tag()],
                               body.get_position(), body.get_radius())
