
from managers.entitiesmanager import EntitiesManager

from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory

from utility.constants.bullet_constants import BulletConstants
from utility.data.soundplayer import SoundPlayer

# Arma padrão, atira quando aperta espaço,
# tem cooldown e munição


class DefaultWeapon(Weapon):

    def __init__(self, owner: Shooter, cooldown: float, ammunition: int, bullet_factory: BulletFactory) -> None:
        super().__init__(owner, cooldown, ammunition, bullet_factory)

    def shoot(self, dt: float) -> None:
        if self.get_time_since_last_shot() < self.get_cooldown():
            self.set_time_since_last_shot(self.get_time_since_last_shot() + dt)
            return
        if self.get_ammunition() <= 0:
            Weapon._noammo_sound.play()
            return

        owner_position = self.get_owner().get_barrel_position()
        owner_aiming_direction = self.get_owner().get_aiming_direction()
        velocity = owner_aiming_direction * BulletConstants().velocity_mag

        bullet_factory = self.get_bullet_factory()
        bullet = bullet_factory.create(owner_position, velocity)
        EntitiesManager.instance().add_entity(bullet)

        self.set_time_since_last_shot(0)
        self.set_ammunition(self.get_ammunition() - 1)

        SoundPlayer().play(Weapon._default_weapon_sound)

    def __str__(self) -> str:
        return f"Default Weapon"
