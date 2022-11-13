
import pygame

class ImageLoader:

    def load(self, path, scale):
        try:
            return pygame.transform.scale(pygame.image.load(path), scale)
        except FileNotFoundError as e:
            s = pygame.Surface((10, 10))
            s.fill((255,255,255))
            return pygame.transform.scale(s, scale)