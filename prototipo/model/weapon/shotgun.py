
import math

from controller.entitiescontroller import EntitiesController

from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory

from pygame.math import Vector2


class Shotgun(Weapon):

    def __init__(self, direction: Vector2, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(direction, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float, player_position: Vector2) -> None:
        if self.get_time_since_last_shot() < self.get_cooldown():
            self.set_time_since_last_shot(self.get_time_since_last_shot() + dt)
            return
        if self.get_ammunition() <= 0:
            return

        bullet_factory = self.get_bullet_factory()
        bullets = [bullet_factory.create(player_position, self.get_direction()*10)]
        for i in range(2,6):
            bullets.append(bullet_factory.create(player_position, (self.get_direction()*10).rotate(-i*math.pi/6)))
            bullets.append(bullet_factory.create(player_position, (self.get_direction()*10).rotate(i*math.pi/6)))
        EntitiesController.instance().add_entities(bullets[:])

        self.set_time_since_last_shot(0)
        self.set_ammunition(self.get_ammunition() - 9)