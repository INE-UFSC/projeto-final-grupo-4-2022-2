
import pygame


class SoundPlayer:

    def play(self, sound: pygame.mixer.Sound, loops: int = 0) -> None:
        if isinstance(sound, pygame.mixer.Sound):
            sound.play(loops=loops)

    def stop(self, sound: pygame.mixer.Sound) -> None:
        if isinstance(sound, pygame.mixer.Sound):
            sound.stop()
