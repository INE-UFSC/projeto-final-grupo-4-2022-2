
from managers.entitiesmanager import EntitiesManager

from model.factory.defaultbulletfactory import DefaultBulletFactory
from model.factory.persistentbulletfactory import PersistentBulletFactory
from model.factory.piercingbulletfactory import PiercingBulletFactory
from model.factory.rubberbulletfactory import RubberBulletFactory
from model.weapon.bulletless import BulletlessWeapon
from model.weapon.default import DefaultWeapon
from model.weapon.infinity import InfinityWeapon
from model.weapon.shotgun import Shotgun
from model.entities.player import Player

from utility.constants.weapon_constants import WeaponConstants

import pygame


# Classe para debugar mais facilmente
# Estará presente apenas para teste
class Debug:

    def __init__(self, player: Player) -> None:

        self.__num_entities = 0
        self.__fps = 0
        self.__lives = 0
        self.__ammo = 0
        self.__score = 0
        self.__bullet_factory = ""
        self.__weapon = ""
        self.__player = player

        self.__font = pygame.font.SysFont(None, 20)

    def get_font(self) -> pygame.font.Font:
        return self.__font

    def update(self, clock: pygame.time.Clock) -> None:

        self.__num_entities = len(EntitiesManager.instance().get_entities())
        self.__fps = int(clock.get_fps())
        self.__lives = self.__player.get_lives()
        self.__ammo = self.__player.get_weapon().get_ammunition()
        self.__score = self.__player.get_score().get_points()
        self.__bullet_factory = self.__player.get_weapon().get_bullet_factory()
        self.__weapon = self.__player.get_weapon()

        if pygame.key.get_pressed()[pygame.K_1]:
            self.__player.get_weapon().set_bullet_factory(DefaultBulletFactory())

        if pygame.key.get_pressed()[pygame.K_2]:
            self.__player.get_weapon().set_bullet_factory(PersistentBulletFactory())

        if pygame.key.get_pressed()[pygame.K_3]:
            self.__player.get_weapon().set_bullet_factory(PiercingBulletFactory())

        if pygame.key.get_pressed()[pygame.K_4]:
            self.__player.get_weapon().set_bullet_factory(RubberBulletFactory())

        if pygame.key.get_pressed()[pygame.K_q]:
            self.__player.set_weapon(BulletlessWeapon(self.__player))

        if pygame.key.get_pressed()[pygame.K_w]:
            self.__player.set_weapon(DefaultWeapon(self.__player, WeaponConstants(
            ).cooldown, WeaponConstants().max_ammunition, self.__player.get_weapon().get_bullet_factory()))

        if pygame.key.get_pressed()[pygame.K_e]:
            self.__player.set_weapon(InfinityWeapon(self.__player, WeaponConstants(
            ).cooldown, self.__player.get_weapon().get_bullet_factory()))

        if pygame.key.get_pressed()[pygame.K_r]:
            self.__player.set_weapon(Shotgun(self.__player, WeaponConstants().cooldown, WeaponConstants(
            ).max_ammunition, self.__player.get_weapon().get_bullet_factory()))

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
