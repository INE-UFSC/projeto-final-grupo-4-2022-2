import utility.constants as CONST

from utility.state.stateingame import StateInGame
from model.entities.player import Player
from model.body import Body
from model.entities.asteroid import Asteroid

from controller.entitiescontroller import EntitiesController
from controller.collisioncontroller import CollisionController

import pygame
from pygame.math import Vector2

class Game:

    def __init__(self, name="Game"):
        pygame.init()
        pygame.display.set_caption(name)

        self.__running = True
        self.__current_state = StateInGame(self)
        self.__screen = pygame.display.set_mode(tuple(CONST.SCREEN_SIZE))
        self.__clock = pygame.time.Clock()

        player_body = Body(Vector2(10, 10), Vector2(0.1, 0.1), 10)
        player = Player(player_body, 5)

        asteroid_body = Body(Vector2(100, 100), Vector2(15, 315), Asteroid.BIG)
        asteroids = [Asteroid(asteroid_body, Asteroid.BIG) for _ in range(10)]

        EntitiesController.instance().add_entity(player)
        EntitiesController.instance().add_entities(asteroids)

        self.__collision_controller = CollisionController(EntitiesController.instance().get_entities())

    def is_running(self):
        return self.__running

    def close(self):
        self.__running = False

    def get_current_state(self):
        return self.__current_state

    def set_current_state(self, new_state):
        self.__current_state = new_state
        
    def change_state(self, new_state):
        self.get_current_state().exit()
        self.set_current_state(new_state)
        self.get_current_state().entry()

    def get_screen(self):
        return self.__screen

    def set_screen(self, new_screen):
        self.__screen = new_screen

    def get_clock(self):
        return self.__clock

    def set_clock(self, new_clock):
        self.__clock = new_clock

    def handle_event(self):
        self.__current_state.handle_event()

    def handle_update(self, dt):
        self.__current_state.handle_update(dt)
        self.__collision_controller.handle_collision()

    def clean_window(self):
        self.get_screen().fill((0, 0, 0))

    def update_screen(self):
        pygame.display.flip()

    def handle_rendering(self):
        self.clean_window()
        self.__current_state.handle_rendering()
        self.update_screen()

    def run(self):
        self.get_current_state().entry()
        while self.is_running():
            dt = self.get_clock().tick(60)
            dt = 1.0/dt
            self.handle_event()
            self.handle_update(dt)
            self.handle_rendering()
        self.get_current_state().exit()
        pygame.quit()