
from model.entities.abstractentity import Entity
from model.entities.shooter import Shooter
from model.body import Body
from model.factory.defaultbulletfactory import DefaultBulletFactory
from model.weapon.default import DefaultWeapon

from utility.constants.player_constants import PlayerConstants
from utility.constants.weapon_constants import WeaponConstants
from utility.constants.shooter_constants import ShooterConstants
from utility.constants.game_constants import GameConstants
from utility.data.image_loader import ImageLoader
from utility.data.score import Score

import pygame
from pygame.math import Vector2

class Weapon: ...


class Player(Entity, Shooter):

    __original_image = ImageLoader().load(PlayerConstants().image_path, (40,30))

    def __init__(self, body: Body, lives: int):
        Entity.__init__(self, body, PlayerConstants().tag)
        Shooter.__init__(self, DefaultWeapon(self, WeaponConstants().cooldown, WeaponConstants().max_ammunition, DefaultBulletFactory()),
                           Vector2(1, 0).normalize(), Vector2(0, 0))
        
        self.__angle = 0

        self.set_image(Player.__original_image)
        self.set_rect(self.get_image().get_rect())

        self.__lives = lives
        self.__direction = Vector2(1, 0).normalize()

        self.__score = Score(0, "None")

    def get_angle(self):
        return self.__angle
    
    def set_angle(self, new_angle):
        self.__angle = new_angle

    def get_lives(self) -> int:
        return self.__lives

    def set_lives(self, lives: int):
        self.__lives = lives

    def get_direction(self) -> Vector2:
        return self.__direction

    def set_direction(self, new_direction: Vector2):
        self.__direction = new_direction.normalize()

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        self.__score = new_score

    def rotate_clockwise(self, angle: float) -> None:
        self.set_angle(self.get_angle() - angle % 360)
        self.set_image(pygame.transform.rotate(Player.__original_image, self.get_angle()))
        self.get_direction().rotate_ip(angle)

    def rotate_anticlockwise(self, angle: float) -> None:
        self.set_angle(self.get_angle() + angle % 360)
        self.set_image(pygame.transform.rotate(Player.__original_image, self.get_angle()))
        self.get_direction().rotate_ip(-angle)

    def on_collision(self, entity: Entity) -> None:
        if (self.get_lives() >= 0):
            self.set_lives(self.get_lives() - 1)
            self.reset()

    def alive(self) -> bool:
        return self.__lives > -1

    def reset(self):
        self.get_body().set_position(GameConstants().screen_size/2)
        self.get_body().set_velocity(Vector2(0,0))
        self.set_direction(Vector2(1, 0).normalize())
        self.set_angle(0)


    def handle_input(self, dt: float) -> None:
        body = self.get_body()
        
        # Acelerando
        if pygame.key.get_pressed()[pygame.K_UP]:
            body.accelerate(self.get_direction() * PlayerConstants().acceleration_mag * dt)

        # Desacelerando
        elif (body.get_velocity().magnitude() > 1):
            body.accelerate(body.get_velocity().normalize() * PlayerConstants().slowdown_coefficient * dt)
        else:
            body.set_velocity(Vector2(0,0))

        # Lidando com o comportamento de mudança de direção
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rotate_clockwise(PlayerConstants().angular_velocity * dt)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rotate_anticlockwise(PlayerConstants().angular_velocity * dt)

        # Ação de atirar
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt: float) -> None:
        body = self.get_body()
        velocity = body.get_velocity()
        position = body.get_position()

        # Truncando a velocidade para não passar da máxima
        if velocity.magnitude() >= PlayerConstants().max_velocity_mag:
            velocity.scale_to_length(PlayerConstants().max_velocity_mag)

        # Condicionais para evitar que o player saia da tela
        if position.x < 0:
            position.x = GameConstants().screen_size.x
        elif GameConstants().screen_size.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = GameConstants().screen_size.y
        elif GameConstants().screen_size.y < position.y:
            position.y = 0

        # Atualizando a posição
        body.move(velocity * dt)

    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        # Definindo a direção da mira do player
        aiming_direction = self.get_direction()
        # Evitando que a bala seja criada dentro do player
        barrel_position = self.get_direction()*self.get_body().get_radius() * ShooterConstants().radius_multiplier + self.get_body().get_position()
        
        self.set_barrel_position(barrel_position)
        self.set_aiming_direction(aiming_direction)

        self.handle_input(dt)
        self.move(dt)

    def destroy(self) -> None:
        pass