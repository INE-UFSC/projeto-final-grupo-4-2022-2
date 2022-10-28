from cgitb import text
import pygame as pg

class TextInput:

    def __init__(self, default_text: str) -> None:
        self.__text = default_text
    
    @property
    def text(self) -> str:
        return self.__text
    
    @text.setter
    def text(self, new_text):
        self.__text = new_text

    def get_text(self) -> str:
        return self.__text

    def set_text(self, text):
        self.__text = text

    def handle_event(self, event: pg.event.Event) -> None:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                new_text = self.text[:-1]
                self.text = new_text
            else:
                print(f"{event.unicode}")
                self.text += event.unicode
                print(f"{self.text}")
    
    def get_text_as_image(self, size: int, color: pg.Color) -> pg.Surface:

        font = pg.font.get_default_font()
        text_as_img = pg.font.SysFont(font, size).render(self.text, True, color)

        return text_as_img
        