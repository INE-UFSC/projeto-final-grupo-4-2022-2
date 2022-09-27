
from model.entities.abstractentity import AbstractEntity
from model.entities.body import Body
from model.entities.bullet import Bullet
from controller.entitiescontroller import EntitiesController

import pygame
from pygame.math import Vector2


class Player(AbstractEntity):

    def __init__(self, body, lifes):
        super().__init__(body)
        self.__direction = Vector2(1,1).normalize()
        self.__lifes = lifes
        self.__cooldown = 1

    def get_direction(self):
        return self.__direction

    def set_direction(self, new_direction):
        self.__direction = new_direction

    def get_lifes(self):
        return self.__lifes

    def set_lifes(self, new_lifes):
        self.__lifes = new_lifes

    def get_cooldown(self):
        return self.__cooldown

    def set_cooldown(self, new_cooldown):
        self.__cooldown = new_cooldown

    def rotate_clockwise(self, angle):
        self.get_direction().rotate_ip(angle)

    def rotate_anticlockwise(self, angle):
        self.get_direction().rotate_ip(-angle)
    
    def on_collision(self, entity):
        if entity.get_type() == self.get_type():
            return
        entity.destroy()
        self.destroy()

    def handle_input(self, dt):
        body = self.get_body()
        if pygame.key.get_pressed()[pygame.K_UP]:
            body.accelerate(1000*self.get_direction()*dt)
        else:
            body.accelerate(-0.7*body.get_velocity()*dt)

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rotate_clockwise(60*dt)

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rotate_anticlockwise(60*dt)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.get_cooldown() <= 0:
                EntitiesController.instance().add_entity(Bullet(Body(self.get_body().get_position() + 1.01*self.get_body().get_radius()*self.get_direction(),
                                                                     150*self.get_direction(), 2), 7))
                self.set_cooldown(1)

    def move(self, dt, screen_size):
        body = self.get_body()
        velocity = body.get_velocity()
        if velocity.magnitude() >= 100:
            velocity.scale_to_length(100)

        position = body.get_position()
        if position.x < 0:
            position.x = screen_size.x
        elif screen_size.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = screen_size.y
        elif screen_size.y < position.y:
            position.y = 0

        body.set_position(body.get_position() + body.get_velocity()*dt)

    def update(self, dt, screen_size):
        self.__cooldown -= dt
        if self.__cooldown < 0:
            self.__cooldown = 0
        self.handle_input(dt)
        self.move(dt, screen_size)
        print(f"Vidas: {self.get_lifes()}")

    def get_type(self):
        return "player"

    def destroy(self):
        self.__lifes -= 1
