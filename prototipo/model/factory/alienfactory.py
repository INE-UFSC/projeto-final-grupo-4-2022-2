import random
import utility.constants as CONSTANTE

from pygame import Vector2

from model.body import Body
from model.entities.alien import Alien

# Fábrica de alien, cuida de contruir as propriedades de cada alien
class AlienFactory:

    def create(self) -> Alien:

        direction = self.make_direction()
        position = self.make_position(direction)
        velocity = self.make_velocity(direction)

        alien_body = Body(position, velocity, CONSTANTE.ALIEN_SIZE)
        alien = Alien(alien_body, direction)
        return alien

    def make_velocity(self, direction: int) -> Vector2:
        # Define a velocidade com base na direção de movimentação
        return direction*Vector2(1, 0)*CONSTANTE.ALIEN_VELOCITY


    def make_position(self, direction: int) -> Vector2:

        position = Vector2(0, random.randint(0, CONSTANTE.SCREEN_SIZE.y))

        # Se o Alien vai da direita para esquerda, então ele nasce no lado direito
        # Caso contrário, o Alien nasce no lado esquerdo
        if (direction == -1):
            position.x = CONSTANTE.SCREEN_SIZE.x - 10
        else:
            position.x = 10

        return position

    def make_direction(self) -> int:
        # O Alien pode ir da esquerda para direita (1) ou da direita para esquerda (-1)
        directions = (-1, 1)

        return random.choice(directions)
