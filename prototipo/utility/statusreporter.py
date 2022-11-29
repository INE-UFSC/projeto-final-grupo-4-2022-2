from model.entities.player import Player

from utility.constants.game_constants import GameConstants

import pygame

class StatusReporter:


    def __init__(self, player: Player) -> None:
        self.__player = player

        self.__small_font = pygame.font.SysFont(None, 20)
        self.__medium_font = pygame.font.SysFont(None, 30)
        self.__big_font = pygame.font.SysFont(None, 40)

    def get_player(self) -> Player:
        return self.__player

    def set_player(self, new_player: Player) -> Player:
        self.__player = new_player

    def get_small_font(self) -> pygame.font.Font:
        return self.__small_font

    def get_medium_font(self) -> pygame.font.Font:
        return self.__medium_font

    def get_big_font(self) -> pygame.font.Font:
        return self.__big_font

    def update(self) -> None:
        self.__lives = self.get_player().get_lives()
        self.__ammo = self.get_player().get_weapon().get_ammunition()
        self.__score = self.get_player().get_score().get_points()
        self.__bullet_factory = self.get_player().get_weapon().get_bullet_factory()
        self.__weapon = self.get_player().get_weapon()

    def render(self, screen: pygame.Surface) -> None:

        gray = pygame.Color(180, 180, 180)

        lives_str = f"Vidas: {self.__lives}"
        ammo_str = f"Ammo: {self.__ammo}"
        score_str = f"Score: {self.__score}"
        weapon_str = f"Arma: {self.__weapon}"
        bullet_str = f"Bullet: {self.__bullet_factory}"

        small_font = self.get_small_font()
        medium_font = self.get_medium_font()
        big_font = self.get_big_font()

        lives_img = big_font.render(lives_str, True, gray)
        score_img = big_font.render(score_str, True, gray)
        ammo_img = medium_font.render(ammo_str, True, gray)
        weapon_img = small_font.render(weapon_str, True, gray)
        bullet_img = small_font.render(bullet_str, True, gray)

        r_l = lives_img.get_rect()
        r_s = score_img.get_rect()
        r_a = ammo_img.get_rect()
        r_w = weapon_img.get_rect()
        r_b = bullet_img.get_rect()

        r_l.center = (GameConstants().screen_size.x/2, 50)
        r_s.center = (GameConstants().screen_size.x/2, 100)
        r_a.bottomleft = (10, GameConstants().screen_size.y - 60)
        r_w.bottomleft = (10, GameConstants().screen_size.y - 40)
        r_b.bottomleft = (10, GameConstants().screen_size.y - 10)

        screen.blit(lives_img, (r_l.x, r_l.y))
        screen.blit(ammo_img, (r_a.x, r_a.y))
        screen.blit(score_img, (r_s.x, r_s.y))
        screen.blit(weapon_img, (r_w.x, r_w.y))
        screen.blit(bullet_img, (r_b.x, r_b.y))
