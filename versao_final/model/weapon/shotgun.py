
import math

from managers.entitiesmanager import EntitiesManager

from model.entities.shooter import Shooter
from model.weapon.weapon import Weapon
from model.factory.bulletfactory import BulletFactory

from utility.constants.bullet_constants import BulletConstants
from utility.data.soundplayer import SoundPlayer


# Shotgun, atira múltiplas balas
class Shotgun(Weapon):

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

        # Criando os tiros variando a angulação
        bullet_factory = self.get_bullet_factory()
        bullets = [bullet_factory.create(owner_position, velocity)]
        for i in range(2, 6):
            bullets.append(bullet_factory.create(
                owner_position, (velocity).rotate(-i*math.pi)))
            bullets.append(bullet_factory.create(
                owner_position, (velocity).rotate(i*math.pi)))
        EntitiesManager.instance().add_entities(bullets[:])

        self.set_time_since_last_shot(0)
        self.set_ammunition(self.get_ammunition() - 9)

        SoundPlayer().play(Weapon._shotgun_sound)

    def __str__(self) -> str:
        return f"Shotgun"
