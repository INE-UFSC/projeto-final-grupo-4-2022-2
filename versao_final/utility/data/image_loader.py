
import pygame


class ImageLoader:

    def load(self, path: str, scale: float) -> pygame.surface.Surface:
        try:
            return pygame.transform.scale(pygame.image.load(path), scale)
        except FileNotFoundError as e:
            print(e)
            s = pygame.Surface((10, 10))
            s.fill((255, 255, 255))
            return pygame.transform.scale(s, scale)
