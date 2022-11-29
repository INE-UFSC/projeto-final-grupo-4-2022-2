
from model.entities.abstractentity import Entity
from model.body import Body
from controller.entitiescontroller import EntitiesController

from utility.constants.asteroid_constants import AsteroidConstants
from utility.constants.pickup_constants import PickUpConstants
from utility.constants.game_constants import GameConstants
from utility.data.image_loader import ImageLoader
from utility.data.music_loader import MusicLoader

from pygame.math import Vector2
import math
import pygame
from utility.constants.sounds_constants import SoundsConstants


class Asteroid(Entity):

    __original_big_asteroid = ImageLoader().load(AsteroidConstants().image_path, (3*AsteroidConstants().big_size, 3*AsteroidConstants().big_size))
    __original_medium_asteroid = ImageLoader().load(AsteroidConstants().image_path, (3*AsteroidConstants().medium_size, 3*AsteroidConstants().medium_size))
    __original_small_asteroid = ImageLoader().load(AsteroidConstants().image_path, (3*AsteroidConstants().small_size, 3*AsteroidConstants().small_size))
    

    def __init__(self, body: Body) -> None:
        super().__init__(body, AsteroidConstants().tag)
        
        if body.get_radius() == AsteroidConstants().big_size:
            self.set_image(Asteroid.__original_big_asteroid)
        elif body.get_radius() == AsteroidConstants().medium_size:
            self.set_image(Asteroid.__original_medium_asteroid)
        else:
            self.set_image(Asteroid.__original_small_asteroid)
            
        self.set_rect(self.get_image().get_rect())

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == AsteroidConstants().tag:
            return
        if entity.get_tag() == PickUpConstants().tag:
            return
        EntitiesController.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        position = body.get_position()

        # Verificações para fazer com que o
        # Asteroid sempre fique "dentro" da janela
        if position.x < 0:
            position.x = GameConstants().screen_size.x
        elif GameConstants().screen_size.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = GameConstants().screen_size.y
        elif GameConstants().screen_size.y < position.y:
            position.y = 0

        # Atuliza a posição
        body.move(body.get_velocity()*dt)

    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        self.move(dt)

    def destroy(self) -> None:

        body = self.get_body()
        position = body.get_position()
        velocity = body.get_velocity()

        # Cria os Asteroid pequenos quando um maior é destruido
        # Caso seja pequeno, não é criado novos
        if body.get_radius() == AsteroidConstants().big_size:
            velocity.scale_to_length(AsteroidConstants().medium_velocity_mag)
            radius = AsteroidConstants().medium_size
        elif body.get_radius() == AsteroidConstants().medium_size:
            velocity.scale_to_length(AsteroidConstants().small_velocity_mag)
            radius = AsteroidConstants().small_size
        elif body.get_radius() == AsteroidConstants().small_size:
            EntitiesController.instance().register_deletion(self)
            return

        position_a = Vector2(position + body.get_radius()
                             * velocity.normalize().rotate(math.pi/2))
        position_b = Vector2(position - body.get_radius()
                             * velocity.normalize().rotate(math.pi/2))

        # Rotação para simular a conservação de energia
        rotation = 30

        velocity_a = velocity.rotate(rotation)
        velocity_b = velocity.rotate(-rotation)

        body_a = Body(position_a, velocity_a, radius)
        body_b = Body(position_b, velocity_b, radius)

        asteroid_a = Asteroid(body_a)
        asteroid_b = Asteroid(body_b)

        # Adicionando a lista de entidades
        EntitiesController.instance().add_entity(asteroid_a)
        EntitiesController.instance().add_entity(asteroid_b)

        
        #canal = SoundsConstants().explosion_channel
        #som = SoundsConstants().explosion_sound
        #pygame.mixer.Channel(canal).play(som)