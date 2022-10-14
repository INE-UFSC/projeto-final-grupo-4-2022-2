
from controller.entitiescontroller import EntitiesController
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager

from utility.states.state import State
import utility.constants as CONST

import pygame

class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def entry(self) -> None:
        pass

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

