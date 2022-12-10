import pygame

from utility.effects.gfx import GFX

class GFXManager:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
            cls.__effects = list()

        return cls._instance

    def __init__(self) -> None:
        pass

    def add(self, fx: GFX) -> None:
        self.__effects.append(fx)

    def gfx_update(self, dt: float) -> None:
        for fx in self.__effects:
            fx.update(dt)

            if fx.get_radius() < 0.1:
                self.__effects.remove(fx)
                del fx

    def gfx_draw(self, screen: pygame.surface.Surface) -> None:
        for fx in self.__effects:
            fx.draw(screen)