from model.entities.player import Player
import pygame

class StatusReporter:


    def __init__(self, player: Player) -> None:
        self.__player = player

        self.__font = pygame.font.SysFont(None, 20)

    def get_player(self) -> Player:
        return self.__player

    def set_player(self, new_player: Player) -> Player:
        self.__player = new_player

    def get_font(self) -> pygame.font.Font:
        return self.__font

    def render(self, screen: pygame.Surface) -> None:

        gray = pygame.Color(180, 180, 180)
        lives = self.get_player().get_lives()
        ammo = self.get_player().get_weapon().get_ammunition()
        score = self.get_player().get_score().get_points()
        bullet_factory = self.get_player().get_weapon().get_bullet_factory()
        weapon = self.get_player().get_weapon()

        lives_str = f"Vidas: {lives}"
        ammo_str = f"Ammo: {ammo}"
        score_str = f"Score: {score}"
        weapon_str = f"Arma: {weapon}"
        bullet_str = f"Bullet: {bullet_factory}"

        lives_img = self.get_font().render(lives_str, True, gray)
        ammo_img = self.get_font().render(ammo_str, True, gray)
        score_img = self.get_font().render(score_str, True, gray)
        weapon_img = self.get_font().render(weapon_str, True, gray)
        bullet_img = self.get_font().render(bullet_str, True, gray)

        screen.blit(lives_img, (20, 80))
        screen.blit(ammo_img, (20, 110))
        screen.blit(score_img, (20, 140))
        screen.blit(weapon_img, (20, 170))
        screen.blit(bullet_img, (20, 200))
