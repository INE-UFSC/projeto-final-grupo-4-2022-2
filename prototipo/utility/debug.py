
from model.entities.player import Player

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
        self.__bullet_factory = ""
        self.__weapon = ""

        self.__font = pygame.font.SysFont(None, 20)

    def get_font(self):
        return self.__font

    def update(self, clock: pygame.time.Clock, player: Player) -> None:

        self.__num_entities = len(EntitiesController.instance().get_entities())
        self.__fps = int(clock.get_fps())
        self.__lives = player.get_lives()
        self.__ammo = player.get_weapon().get_ammunition()
        self.__score = ScoreManager.instance().get_score()
        self.__bullet_factory = player.get_weapon().get_bullet_factory()
        self.__weapon = player.get_weapon()


    def render(self, screen: pygame.Surface) -> None:

        gray = pygame.Color(180, 180, 180)

        entities_str = f"Número de entidades: {self.__num_entities}"
        fps_str = f"FPS: {self.__fps}"
        lives_str = f"Vidas: {self.__lives}"
        ammo_str = f"Ammo: {self.__ammo}"
        score_str = f"Score: {self.__score}"
        weapon_str = f"Arma: {self.__weapon}"
        bullet_str = f"Bullet: {self.__bullet_factory}"

        entities_img = self.get_font().render(entities_str, True, gray)
        fps_img = self.get_font().render(fps_str, True, gray)
        lives_img = self.get_font().render(lives_str, True, gray)
        ammo_img = self.get_font().render(ammo_str, True, gray)
        score_img = self.get_font().render(score_str, True, gray)
        weapon_img = self.get_font().render(weapon_str, True, gray)
        bullet_img = self.get_font().render(bullet_str, True, gray)

        screen.blit(entities_img, (20, 20))
        screen.blit(fps_img, (20, 50))
        screen.blit(lives_img, (20, 80))
        screen.blit(ammo_img, (20, 110))
        screen.blit(score_img, (20, 140))
        screen.blit(weapon_img, (20, 170))
        screen.blit(bullet_img, (20, 200))

    def gambiarra_lives() -> int:

        for e in EntitiesController.instance().get_entities():
            if e.get_tag() == CONSTANTES.PLAYER_TAG:
                return e.get_lives()
