
from controller.entitiescontroller import EntitiesController

from model.weapon.weapon import Weapon
from model.entities.player import Player
from model.factory.bulletfactory import BulletFactory

from pygame.math import Vector2


class InfinityWeapon(Weapon):

    def __init__(self, owner: Player, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(owner, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float, player_position: Vector2) -> None:
        if self.get_time_since_last_shot() < self.get_cooldown():
            self.set_time_since_last_shot(self.get_time_since_last_shot() + dt)
            return
        if self.get_ammunition() <= 0:
            return

        bullet_factory = self.get_bullet_factory()
        bullet = bullet_factory.create(player_position, self.get_direction()*10)
        EntitiesController.instance().add_entity(bullet)

        self.set_time_since_last_shot(0)
