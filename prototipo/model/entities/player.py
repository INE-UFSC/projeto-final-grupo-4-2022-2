
from controller.scoremanager import ScoreManager

from model.entities.abstractentity import Entity
from model.entities.shooter import Shooter
from model.body import Body

# factory imports
from model.factory.defaultbulletfactory import DefaultBulletFactory
from model.factory.persistentbulletfactory import PersistentBulletFactory
from model.factory.piercingbulletfactory import PiercingBulletFactory
from model.factory.rubberbulletfactory import RubberBulletFactory

# weapon imports
from model.weapon.bulletless import BulletlessWeapon
from model.weapon.default import DefaultWeapon
from model.weapon.infinity import InfinityWeapon
from model.weapon.shotgun import Shotgun

import utility.constants as CONSTANT

import pygame
from pygame.math import Vector2

class Weapon: ...

class Player(Entity, Shooter):

    def __init__(self, body: Body, lives: int):
        Entity.__init__(self, body, CONSTANT.PLAYER_TAG)
        Shooter.__init__(self, DefaultWeapon(self, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, DefaultBulletFactory()),
                           Vector2(1, 1).normalize(), Vector2(0, 0))
        self.__lives = lives
        self.__direction = Vector2(1, 1).normalize()

        self.__score_atual = ScoreManager.instance().get_score()
        self.__ammo = CONSTANT.MAX_AMMUNITION
        self.__weapon = self.get_weapon()
        self.__bullet_factory = self.get_weapon().get_bullet_factory()

        # FIXME: Jogar as coisas abaixo (e outras linhas relevantes) numa classe debug
        self.DefaultBulletFactory = DefaultBulletFactory()
        self.PersistentBulletFactory = PersistentBulletFactory()
        self.PiercingBullerFactory = PiercingBulletFactory()
        self.RubberBulletFactory = RubberBulletFactory()

        self.DefaultWeapon = DefaultWeapon(self, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, self.__bullet_factory)
        self.BulletLessWeapon = BulletlessWeapon(self, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, self.__bullet_factory)
        self.InfinityWeapon = InfinityWeapon(self, CONSTANT.WEAPON_COOLDOWN, self.__bullet_factory)
        self.Shotgun = Shotgun(self, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, self.__bullet_factory)


    def get_lives(self) -> int:
        return self.__lives

    def set_lives(self, lives: int):
        self.__lives = lives

    def get_direction(self) -> Vector2:
        return self.__direction

    def set_direction(self, new_direction: Vector2):
        self.__direction = new_direction.normalize()

    def rotate_clockwise(self, angle: float) -> None:
        self.get_direction().rotate_ip(angle)

    def rotate_anticlockwise(self, angle: float) -> None:
        self.get_direction().rotate_ip(-angle)

    def on_collision(self, entity: Entity) -> None:
        if (self.get_lives() >= 1):
            self.set_lives(self.get_lives() - 1)
            print(f"Vidas: {self.get_lives()}")

    def handle_input(self, dt: float) -> None:
        body = self.get_body()
        if pygame.key.get_pressed()[pygame.K_UP]:
            body.accelerate(self.get_direction()*dt*100)
        else:
            body.accelerate(-0.7*body.get_velocity()*dt)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rotate_clockwise(5)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rotate_anticlockwise(5)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.shoot(dt)

        if pygame.key.get_pressed()[pygame.K_1]:
            self.get_weapon().set_bullet_factory(self.DefaultBulletFactory)
        
        if pygame.key.get_pressed()[pygame.K_2]:
            self.get_weapon().set_bullet_factory(self.PersistentBulletFactory)

        if pygame.key.get_pressed()[pygame.K_3]:
            self.get_weapon().set_bullet_factory(self.PiercingBullerFactory)
        
        if pygame.key.get_pressed()[pygame.K_4]:
            self.get_weapon().set_bullet_factory(self.RubberBulletFactory)

        if pygame.key.get_pressed()[pygame.K_q]:
            self.set_weapon(self.BulletLessWeapon)
            
        if pygame.key.get_pressed()[pygame.K_w]:
            self.set_weapon(self.DefaultWeapon)

        if pygame.key.get_pressed()[pygame.K_e]:
            self.set_weapon(self.InfinityWeapon)

        if pygame.key.get_pressed()[pygame.K_r]:
            self.set_weapon(self.Shotgun)

    def move(self, dt: float) -> None:
        body = self.get_body()
        velocity = body.get_velocity()
        if velocity.magnitude() >= CONSTANT.MAX_VELOCITY_OF_PLAYER:
            velocity.scale_to_length(CONSTANT.MAX_VELOCITY_OF_PLAYER)

        position = body.get_position()
        if position.x < 0:
            position.x = CONSTANT.SCREEN_SIZE.x
        elif CONSTANT.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONSTANT.SCREEN_SIZE.y
        elif CONSTANT.SCREEN_SIZE.y < position.y:
            position.y = 0

        body.move(velocity*dt)
        body.set_velocity(self.get_direction()*velocity.magnitude())

    def update(self, dt: float) -> None:

        score = ScoreManager.instance().get_score()
        if score != self.__score_atual: 
            print(f"Score: {score}")
            self.__score_atual = score

        ammo = self.get_weapon().get_ammunition()
        if ammo != self.__ammo:
            print(f"Ammo: {ammo}")
            self.__ammo = ammo

        weapon = self.get_weapon()
        if weapon != self.__weapon:
            print(f"Weapon: {weapon}")
            self.__weapon = weapon
        
        bullet_factory = self.get_weapon().get_bullet_factory()
        if bullet_factory != self.__bullet_factory:
            print(f"Bullet Factory: {bullet_factory}")
            self.__bullet_factory = bullet_factory
        

        barrel_position = self.get_direction()*self.get_body().get_radius()*CONSTANT.RADIUS_MULTIPLIER + self.get_body().get_position()
        aiming_direction = self.get_direction()
        self.set_barrel_position(barrel_position)
        self.set_aiming_direction(aiming_direction)

        self.handle_input(dt)
        self.move(dt)

    def destroy(self) -> None:
        pass
