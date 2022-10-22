
from controller.collisiondetector import CollisionDetector
from controller.collisionmanager import CollisionManager
from controller.entitiescontroller import EntitiesController
from controller.scoremanager import ScoreManager

import utility.constants as CONSTANTES

import pygame

class Debug:

    def __init__(self) -> None:

        self.__num_entities = 0
        self.__fps = 0
        self.__lives = 0
        self.__ammo = 0
        self.__score = 0

        self.__font = pygame.font.SysFont(None, 20)

    @property
    def font(self):
        return self.__font

    def update(self, dt: float) -> None:

        self.__num_entities = len(EntitiesController.instance().get_entities())
        self.__fps = 1/dt
        #self.__lives = self.gambiarra_lives()
        #self.__ammo = 


    def blit_strings(self, screen: pygame.Surface) -> None:

        black = pygame.Color(180, 180, 180)

        entities_str = f"Número de entidades: {self.__num_entities}"
        fps_str = f"FPS: {self.__fps}"


        entities_img = self.font.render(entities_str, True, black)
        fps_img = self.font.render(fps_str, True, black)

        screen.blit(entities_img, (20, 20))
        screen.blit(fps_img, (20, 50))
        #screen.blit()

    def gambiarra_lives() -> int:

        for e in EntitiesController.instance().get_entities():
            if e.get_tag() == CONSTANTES.PLAYER_TAG:
                return e.get_lives()
