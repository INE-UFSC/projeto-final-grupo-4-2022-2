
import pygame

class MusicLoader:
    def __init__(self) -> None:
        pygame.mixer.init()


    def load(self, path: str, volume: float) -> pygame.surface.Surface:
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play()
        except pygame.error as e:
            print(e)


#MusicLoader().load("./../../sounds/weapon/shotv2.mp3", 1000.0)