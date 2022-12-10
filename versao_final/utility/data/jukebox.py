
from utility.data.soundplayer import SoundPlayer

import random

class JukeBox:

    def __init__(self, musics: list=[]) -> None:
        self.__musics = musics
        self.__time_elapsed = 0
        self.__current_music = random.choice(musics)
        SoundPlayer().play(self.__current_music)

    def update(self, dt: float) -> None:
        if self.__current_music is None:
            return
        self.__time_elapsed += dt
        if self.__time_elapsed > self.__current_music.get_length():
            self.change_music()

    def stop(self) -> None:
        SoundPlayer().stop(self.__current_music)

    def new_music(self) -> None:
        new_music = random.choice(self.__musics)
        self.__current_music = new_music
        SoundPlayer().play(new_music)

    def change_music(self) -> None:
        SoundPlayer().stop(self.__current_music)
        musics_copy = self.__musics[:]
        musics_copy.remove(self.__current_music)
        self.__current_music = random.choice(musics_copy)
        SoundPlayer().play(self.__current_music)
        self.__time_elapsed = 0