from utility.states.state import State
import pygame

class Game: ...

class StateInMenu(State):

    def __init__(self, owner: Game):
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

