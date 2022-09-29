
from controller.entitiescontroller import EntitiesController
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
        for entity in EntitiesController.instance().get_entities():
            entity.update(dt)
        print(f"Numero de entidades: {len(EntitiesController.instance().get_entities())}")

    def handle_rendering(self) -> None:
        for entity in EntitiesController.instance().get_entities():
            body = entity.get_body()

            pygame.draw.circle(self.get_owner().get_screen(), (0, 0, 255),
                            body.get_position(), body.get_radius())

