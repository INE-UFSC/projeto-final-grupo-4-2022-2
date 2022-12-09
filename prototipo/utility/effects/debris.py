
import pygame
import random
from utility.effects.gfx import GFX

class Debris(GFX):

    def __init__(self, position: pygame.Vector2) -> None:
        super().__init__(0.25, position, 2)

    def update(self, dt) -> None:
        self._duration += dt
        if self._duration < self.get_lifetime():
            position = self.get_position()
            new_x = position.x + random.uniform(-10, 10)
            new_y = position.y + random.uniform(-10, 10)
            new_position = pygame.Vector2(new_x, new_y)
            self.set_position(new_position)
        else:
            self.set_radius(0.01)

    def draw(self, screen: pygame.surface.Surface) -> None:
        COLOR = (180, 180, 180)
        pygame.draw.circle(screen, COLOR, self.get_position(), self.get_radius())
