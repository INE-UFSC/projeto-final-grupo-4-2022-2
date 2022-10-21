
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
        self.set_lives(self.get_lives() - 1)

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
            self.get_weapon().set_bullet_factory(DefaultBulletFactory())
        
        if pygame.key.get_pressed()[pygame.K_2]:
            self.get_weapon().set_bullet_factory(PersistentBulletFactory())

        if pygame.key.get_pressed()[pygame.K_3]:
            self.get_weapon().set_bullet_factory(PiercingBulletFactory())
        
        if pygame.key.get_pressed()[pygame.K_4]:
            self.get_weapon().set_bullet_factory(RubberBulletFactory())

        if pygame.key.get_pressed()[pygame.K_q]:
            self.set_weapon(BulletlessWeapon(self, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, self.get_weapon().get_bullet_factory()))
        
        if pygame.key.get_pressed()[pygame.K_w]:
            self.set_weapon(DefaultWeapon(self, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, self.get_weapon().get_bullet_factory()))
        
        if pygame.key.get_pressed()[pygame.K_e]:
            self.set_weapon(InfinityWeapon(self, CONSTANT.WEAPON_COOLDOWN, self.get_weapon().get_bullet_factory()))
        
        if pygame.key.get_pressed()[pygame.K_r]:
            self.set_weapon(Shotgun(self, CONSTANT.WEAPON_COOLDOWN, CONSTANT.MAX_AMMUNITION, self.get_weapon().get_bullet_factory()))

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
        print(f"Score: {ScoreManager.instance().get_score()}")
        print(f"Vidas: {self.get_lives()}")

        barrel_position = self.get_direction()*self.get_body().get_radius()*CONSTANT.MULTIPLIER + self.get_body().get_position()
        aiming_direction = self.get_direction()
        self.set_barrel_position(barrel_position)
        self.set_aiming_direction(aiming_direction)

        self.handle_input(dt)
        self.move(dt)

    def destroy(self) -> None:
        pass
