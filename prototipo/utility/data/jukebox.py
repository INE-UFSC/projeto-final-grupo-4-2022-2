
from utility.data.soundplayer import SoundPlayer

import random

class JukeBox:

    def __init__(self, musics: list=[]) -> None:
        self.__musics = musics
        self.__time_elapsed = 0
        self.__current_music = random.choice(musics)
        SoundPlayer().play(self.__current_music)

    def update(self, dt: float) -> None:
        self.__time_elapsed += dt
        if self.__time_elapsed > self.__current_music.get_length():
            SoundPlayer().stop(self.__current_music)
            musics_copy = self.__musics[:]
            musics_copy.remove(self.__current_music)
            self.__current_music = random.choice(musics_copy)
            SoundPlayer().play(self.__current_music)
            self.__time_elapsed = 0
