from utility.states.state import State 
import utility.constants as CONST

from utility.states.stateingame import StateInGame
from model.entities.player import Player
from model.body import Body
from model.entities.asteroid import Asteroid

from controller.entitiescontroller import EntitiesController
from controller.collisioncontroller import CollisionController

import pygame
from pygame.math import Vector2
from pygame import Surface
from pygame.time import Clock

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

        tmp_asteroid_list = list()
        for _ in range(10):
            new_body = Body(Vector2(100, 100), Vector2(10, 10), Asteroid.BIG)
            new_asteroid = Asteroid(new_body, Asteroid.BIG)
            tmp_asteroid_list.append(new_asteroid)
            
        asteroids = list(tmp_asteroid_list)

        EntitiesController.instance().add_entity(player)
        EntitiesController.instance().add_entities(asteroids)

        self.__collision_controller = CollisionController(EntitiesController.instance().get_entities())

    def is_running(self) -> bool:
        return self.__running

    def close(self) -> None:
        self.__running = False

    def get_current_state(self):
        return self.__current_state

    def set_current_state(self, new_state) -> None:
        self.__current_state = new_state
        
    def change_state(self, new_state) -> None:
        self.get_current_state().exit()
        self.set_current_state(new_state)
        self.get_current_state().entry()

    def get_screen(self) -> Surface:
        return self.__screen

    def set_screen(self, new_screen: Surface) -> None:
        self.__screen = new_screen

    def get_clock(self) -> Clock:
        return self.__clock

    def set_clock(self, new_clock: Clock) -> None:
        self.__clock = new_clock

    def handle_event(self) -> None:
        self.__current_state.handle_event()

    def handle_update(self, dt: float) -> None:
        self.__current_state.handle_update(dt)
        self.__collision_controller.handle_collision()

    def clean_window(self) -> None:
        self.get_screen().fill((0, 0, 0))

    def update_screen(self) -> None:
        pygame.display.flip()

    def handle_rendering(self) -> None:
        self.clean_window()
        self.__current_state.handle_rendering()
        self.update_screen()

    def run(self) -> None:
        self.get_current_state().entry()
        while self.is_running():
            dt = self.get_clock().tick(60)
            dt = 1.0/dt # se dt é o periodo do tick, 1/dt é a frequência do tick, talvez usar outro nome?
            self.handle_event()
            self.handle_update(dt)
            self.handle_rendering()
        self.get_current_state().exit()
        pygame.quit()