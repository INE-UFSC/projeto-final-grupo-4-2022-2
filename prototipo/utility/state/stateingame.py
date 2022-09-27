
from controller.entitiescontroller import EntitiesController
from utility.state.state import State
import pygame
from pygame.math import Vector2

class StateInGame(State):

    def __init__(self, owner):
        super().__init__(owner)

    def entry(self):
        pass

    def exit(self):
        pass

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.get_owner().close()

    def handle_update(self, dt):
        for entity in EntitiesController.instance().get_entities():
            entity.update(dt, Vector2(self.get_owner().get_screen().get_size()))
        print(f"Numero de entidades: {len(EntitiesController.instance().get_entities())}")

    def handle_rendering(self):
        for entity in EntitiesController.instance().get_entities():
            body = entity.get_body()

            pygame.draw.circle(self.get_owner().get_screen(), (0, 0, 255),
                            body.get_position(), body.get_radius())

