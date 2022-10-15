
import math

from controller.entitiescontroller import EntitiesController

from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory


class Player: ...


class Shotgun(Weapon):

    def __init__(self, owner: Player, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(owner, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float) -> None:
        if self.get_time_since_last_shot() < self.get_cooldown():
            self.set_time_since_last_shot(self.get_time_since_last_shot() + dt)
            return
        if self.get_ammunition() <= 0:
            return

        player_position = self.get_owner().get_body().get_position()
        player_radius = self.get_owner().get_body().get_radius()
        player_direction = self.get_owner().get_direction()

        bullet_factory = self.get_bullet_factory()
        bullets = [bullet_factory.create(player_position + player_direction*player_radius*1.05, player_direction*10)]
        for i in range(2,6):
            bullets.append(bullet_factory.create(player_position + player_direction*player_radius*1.05, (player_direction*10).rotate(-i*math.pi)))
            bullets.append(bullet_factory.create(player_position + player_direction*player_radius*1.05, (player_direction*10).rotate(i*math.pi)))
        EntitiesController.instance().add_entities(bullets[:])

        self.set_time_since_last_shot(0)
        self.set_ammunition(self.get_ammunition() - 9)