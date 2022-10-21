
from controller.entitiescontroller import EntitiesController

from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory

import utility.constants as CONSTANT

class InfinityWeapon(Weapon):

    def __init__(self, owner: Shooter, cooldown: float, bullet_factory: BulletFactory) -> None:
        super().__init__(owner, cooldown, None, bullet_factory)

    def shoot(self, dt: float) -> None:
        if self.get_time_since_last_shot() < self.get_cooldown():
            self.set_time_since_last_shot(self.get_time_since_last_shot() + dt)
            return

        owner_position = self.get_owner().get_barrel_position()
        owner_aiming_direction = self.get_owner().get_aiming_direction()
        velocity = owner_aiming_direction*CONSTANT.VELOCITY_OF_BULLET

        bullet_factory = self.get_bullet_factory()
        bullet = bullet_factory.create(owner_position, velocity)
        EntitiesController.instance().add_entity(bullet)

        self.set_time_since_last_shot(0)
