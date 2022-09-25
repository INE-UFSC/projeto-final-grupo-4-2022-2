
from pygame.math import Vector2
from models.entity import Entity

class Player(Entity):

    MAX_VELOCITY = 30.0

    def __init__(self, position: Vector2, lifes: int, radius: float, sprite=None):
        super().__init__(position, Vector2(0.1, 0.1), sprite, radius)
        self.__direction = Vector2(0.1, 0.1).normalize()
        self.__lifes = lifes

    def get_type(self) -> str:
        return "player"

    def get_direction(self) -> Vector2:
        return self.__direction

    def get_lifes(self) -> int:
        return self.__lifes

    def set_lifes(self, new_lifes: int):
        self.__lifes = new_lifes

    def has_lifes(self):
        return self.get_lifes()

    def lose_life(self):
        self.__lifes -= 1
        
    def set_direction(self, new_direction) -> None:
        self.__direction = new_direction

    def rotate_clockwise(self) -> None:
        self.__direction.rotate_ip(8)

    def rotate_anticlockwise(self) -> None:
        self.__direction.rotate_ip(-8)
    
    def accelerate(self) -> None:
        if (self.get_velocity().magnitude() == 0):
            self.set_velocity(Vector2(1, 1))
        elif (self.get_velocity().magnitude() < Player.MAX_VELOCITY):
            self.set_velocity(self.get_velocity() * (1.10))
        elif (Player.MAX_VELOCITY < self.get_velocity().magnitude()):
            self.get_velocity().scale_to_length(Player.MAX_VELOCITY)
    
    def slowdown(self) -> None:
        if self.get_velocity().magnitude() < 0.2:
            self.set_velocity(Vector2(0,0))
        else:
            self.set_velocity(self.get_velocity() * 0.96)

    def on_colision(self):
        self.lose_life()

    def update(self, dt, screen_size) -> None:
        super().update(dt, screen_size)
        self.set_velocity(self.get_direction().normalize()*self.get_velocity().magnitude())
        
