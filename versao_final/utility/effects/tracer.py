
import pygame

from utility.effects.gfx import GFX


class Tracer:
    ...


class Tracer(GFX):

    def __init__(self, position: pygame.Vector2, radius: float) -> None:
        super().__init__(1, position, radius)

    def update(self, dt) -> None:

        self.update_duration(dt)
        old_radius = self.get_radius()
        
        ratio = self._duration/self.get_lifetime()
        radius_factor = 1 - ratio
        new_radius = old_radius * radius_factor
        self.set_radius(new_radius)

    def draw(self, screen: pygame.surface.Surface) -> None:
        COLOR = (180, 180, 180)
        pygame.draw.circle(screen, COLOR, self.get_position(), self.get_radius())

    def update_duration(self, dt: float) -> None:
        self._duration += dt
