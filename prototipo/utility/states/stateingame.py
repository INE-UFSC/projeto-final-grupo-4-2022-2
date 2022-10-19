
from model.entities.player import Player
from model.body import Body
from model.factory.asteroidfactory import AsteroidFactory
from model.factory.rubberbulletfactory import RubberBulletFactory
from model.weapon.shotgun import Shotgun
from model.factory.playerfactory import PlayerFactory

from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager

from utility.states.state import State
import utility.constants as CONSTANT

from pygame.math import Vector2
import pygame


class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def entry(self) -> None:

        player_body = Body(Vector2(0, 0), Vector2(0, 0), CONSTANT.PLAYER_SIZE)
        player_lives = CONSTANT.MAX_LIVES
        player_weapon = Shotgun(
            None, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, RubberBulletFactory())

        player = PlayerFactory().create(player_body, player_lives, player_weapon)
        player.get_weapon().set_owner(player)

        asteroids = AsteroidFactory().create(10)

        EntitiesController.instance().add_entity(player)
        EntitiesController.instance().add_entities(asteroids)

    def exit(self) -> None:
        pass

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    def handle_update(self, dt: float) -> None:
        entities = EntitiesController.instance().get_entities()
        for entity in entities:
            entity.update(dt)

        CollisionDetector.instance().detect_collisions(entities)
        CollisionManager.instance().handle_collisions()

        #print(f"Numero de entidades: {len(EntitiesController.instance().get_entities())}")
        EntitiesController.instance().handle_deletion()
        EntitiesController.instance().flush_deletion_buffer()

    def handle_rendering(self) -> None:
        for entity in EntitiesController.instance().get_entities()[::-1]:
            body = entity.get_body()

            # Uma lógica só para visualizar quem é quem
            color = (0, 0, 255)
            if entity.get_tag() == "player":
                color = (255, 0, 0)
            elif entity.get_tag() == "bullet":
                color = (0, 255, 0)
            pygame.draw.circle(self.get_owner().get_screen(), color,
                               body.get_position(), body.get_radius())
