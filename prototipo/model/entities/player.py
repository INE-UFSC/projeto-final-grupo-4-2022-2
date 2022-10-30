from model.entities.abstractentity import Entity
from model.entities.shooter import Shooter
from model.body import Body

# factory imports
from model.factory.defaultbulletfactory import DefaultBulletFactory

# weapon imports
from model.weapon.default import DefaultWeapon

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
        if (self.get_lives() >= 0):
            self.set_lives(self.get_lives() - 1)

    def alive(self) -> bool:
        return self.__lives > -1

    def handle_input(self, dt: float) -> None:
        body = self.get_body()
        
        # Forward
        if pygame.key.get_pressed()[pygame.K_UP]:
            body.accelerate(self.get_direction() * CONSTANT.ACCELERATION_MAGNITUDE*dt)

        # Slowing down
        elif (body.get_velocity().magnitude() > 1):
            body.accelerate(body.get_velocity().normalize() * CONSTANT.SLOWDOWN_COEFFICIENT*dt)
        else:
            body.set_velocity(Vector2(0,0))

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rotate_clockwise(5)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rotate_anticlockwise(5)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.shoot(dt)

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

        body.move(velocity * dt)

    def update(self, dt: float) -> None:

        barrel_position = self.get_direction()*self.get_body().get_radius()*CONSTANT.RADIUS_MULTIPLIER + self.get_body().get_position()
        aiming_direction = self.get_direction()
        self.set_barrel_position(barrel_position)
        self.set_aiming_direction(aiming_direction)

        self.handle_input(dt)
        self.move(dt)

    def destroy(self) -> None:
        pass