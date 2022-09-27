from utility.state.state import State
import pygame

class StateInEndGame(State):

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
        pass

    def handle_rendering(self):
        pass

