
import utility.constants as CONST

from model.entities.abstractentity import AbstractEntity
from model.body import Body


import pygame
from pygame.math import Vector2


class Player(AbstractEntity):

    def __init__(self, body: Body, lifes: int):
        super().__init__(body, "player")
        self.__lifes = lifes
        self.__direction = Vector2(1, 1).normalize()

    def get_lifes(self) -> int:
        return self.__lifes

    def set_lifes(self, lifes: int):
        self.__lifes = lifes

    def get_direction(self) -> Vector2:
        return self.__direction

    def set_direction(self, new_direction: Vector2):
        self.__direction = new_direction.normalize()

    def rotate_clockwise(self, angle: float) -> None:
        self.get_direction().rotate_ip(angle)

    def rotate_anticlockwise(self, angle: float) -> None:
        self.get_direction().rotate_ip(-angle)

    def on_collision(self, entity: AbstractEntity) -> None:
        pass

    def handle_input(self, dt: float) -> None:
        body = self.get_body()
        if pygame.key.get_pressed()[pygame.K_UP]:
            body.accelerate(self.get_direction() * dt*1000)
        else:
            body.accelerate(-0.7*body.get_velocity()*dt)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rotate_clockwise(5)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rotate_anticlockwise(5)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            pass  # weapon.shoot será chamado aqui

    def move(self, dt: float) -> None:
        body = self.get_body()
        velocity = body.get_velocity()
        if velocity.magnitude() >= 100:
            velocity.scale_to_length(100)

        position = body.get_position()
        if position.x < 0:
            position.x = CONST.SCREEN_SIZE.x
        elif CONST.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONST.SCREEN_SIZE.y
        elif CONST.SCREEN_SIZE.y < position.y:
            position.y = 0

        body.set_position(position + velocity*dt)
        body.set_velocity(self.get_direction()*velocity.magnitude())

    def update(self, dt: float) -> None:
        self.handle_input(dt)
        self.move(dt)
        print(f"posicao: {self.get_body().get_position()}")
        print(f"velocidade: {self.get_body().get_velocity()}")

    def destroy(self) -> None:
        self.__lifes -= 1
