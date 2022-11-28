
from pygame.math import Vector2
from pygame.font import get_default_font
from pygame.font import SysFont
from pygame import Surface


class Button:

    def __init__(self,
                 key: str,
                 position: Vector2 = Vector2(0, 0),
                 text: str = "",
                 font: str = "",
                 font_size: int = 20,
                 font_color: tuple = (255, 255, 255),
                 background_color: tuple = (255, 0, 0)) -> None:
        self.__key = key
        self.__position = position
        self.__text = text
        self.__font = font
        if font == "":
            self.__font = get_default_font()
        self.__font_size = font_size
        self.__font_color = font_color
        self.__background_color = background_color
        self.__color_when_marked = (255, 255, 0)
        self.__marked = False

    def get_key(self) -> str:
        return self.__key

    def get_position(self) -> Vector2:
        return self.__position

    def set_position(self, new_position: Vector2) -> None:
        self.__position = new_position

    def get_text(self) -> str:
        return self.__text

    def set_text(self, new_text: str) -> None:
        self.__text = new_text

    def get_font(self) -> str:
        return self.__font

    def set_font(self, new_font: str) -> None:
        self.__font = new_font

    def get_font_size(self) -> int:
        return self.__font_size

    def set_font_size(self, new_font_size: int) -> None:
        self.__font_size = new_font_size

    def get_font_color(self) -> tuple:
        return self.__font_color

    def set_font_color(self, new_font_color: tuple) -> None:
        self.__font_color = new_font_color

    def get_background_color(self) -> tuple:
        return self.__background_color

    def set_background_color(self, new_background_color: tuple) -> None:
        self.__background_color = new_background_color

    def get_marked(self) -> bool:
        return self.__marked

    def mark(self) -> None:
        self.__marked = True
    
    def mark_off(self) -> None:
        self.__marked = False

    def draw(self, screen: Surface) -> None:
        img = SysFont(self.get_font(),
                      self.get_font_size()).render(self.get_text(),
                                                   True, self.get_font_color() if not self.get_marked() else self.__color_when_marked)
        r = img.get_rect()
        r.center = (self.get_position().x, self.get_position().y)
        screen.blit(img, (r.x, r.y))
