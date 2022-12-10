from managers.entitiesmanager import EntitiesManager

from model.entities.abstractentity import Entity
from model.entities.bullets.bullet import Bullet
from model.body import Body

from utility.constants.game_constants import GameConstants
from utility.constants.pickup_constants import PickUpConstants

import pygame


# Bala com comportamento de ricochete
class RubberBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == PickUpConstants().tag:
            return
        EntitiesManager.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        position = body.get_position()

        # Condicionais que simulando uma colisão real com a parede
        if position.x < 0 or GameConstants().screen_size.x < position.x:

            new_x = -(self.get_body().get_velocity().x)
            y = self.get_body().get_velocity().y

            velocity_switch_x = pygame.Vector2(new_x, y)
            self.get_body().set_velocity(velocity_switch_x)

        if position.y < 0 or GameConstants().screen_size.y < position.y:

            x = self.get_body().get_velocity().x
            new_y = -(self.get_body().get_velocity().y)

            velocity_switch_x = pygame.Vector2(x, new_y)
            self.get_body().set_velocity(velocity_switch_x)

        # Atualiza a posição
        body.move(body.get_velocity() * dt)

    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        # Morre quando não tiver mais tempo de vida
        self.set_lifetime(self.get_lifetime() - dt)
        if self.get_lifetime() < 0:
            EntitiesManager.instance().register_deletion(self)
        self.move(dt)
