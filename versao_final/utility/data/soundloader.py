
import pygame
pygame.mixer.init()


class SoundLoader:

    def load(self, path: str, volume: float) -> pygame.mixer.Sound:
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(volume)
            return sound
        except FileNotFoundError as e:
            print(e)
        except pygame.error as e:
            print(e)
