# from prototipo.game import Game # import circular, queria tipar owner do init
from utility.states.state import State
import pygame

class StateInEndGame(State):

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
        pass

    def handle_rendering(self) -> None:
        pass

