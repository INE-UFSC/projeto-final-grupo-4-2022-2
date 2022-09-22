
from model.asteroid import Asteroid
import pygame


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroid")
        self.__running = True
        self.__screen = pygame.display.set_mode((500, 500))
        self.__clock = pygame.time.Clock()
        self.dummy = Asteroid(position=pygame.math.Vector2(250,250),
                              velocity=pygame.math.Vector2(15,15))
    
    def is_running(self):
        return self.__running

    def close(self):
        self.__running = False

    def quit(self):
        pygame.quit()

    def get_screen(self):
        return self.__screen

    def set_screen(self, new_screen):
        self.__screen = new_screen

    def get_clock(self):
        return self.__clock

    def set_clock(self, new_clock):
        self.__clock = new_clock

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()

    def handle_update(self, fps):
        dt = 1.0/float(fps)
        coefficient = 30
        self.dummy.update(dt*coefficient)

    def handle_rendering(self):
        self.get_screen().fill((255, 255, 255))
        pygame.draw.circle(self.get_screen(), (0, 0, 255), self.dummy.get_position(), self.dummy.get_radius())
        pygame.display.flip()

    def run(self):

        while self.is_running():
            self.handle_rendering()
            self.handle_event()
            self.handle_update(self.get_clock().tick(16))
        self.quit()