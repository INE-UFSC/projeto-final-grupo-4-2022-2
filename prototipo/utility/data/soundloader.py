
import pygame



class SoundLoader:

    def load(self, path: str, volume: float) -> pygame.mixer.Sound:
        try:
            sound = pygame.mixer.Sound(path)
            sound.set_volume(volume)
            return sound
        except FileNotFoundError as e:
            print(e)

pygame.mixer.init()

"""
s = SoundLoader().load("./../../sounds/weapon/noammo.wav", 1)
s.play(-1)

while True:
    s = input("")
    break
"""
