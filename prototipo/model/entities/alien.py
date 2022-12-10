
import random

from managers.entitiesmanager import EntitiesManager
from managers.gfxmanager import GFXManager

from model.entities.abstractentity import Entity
from model.entities.shooter import Shooter
from model.body import Body
from model.weapon.infinity import InfinityWeapon
from model.factory.defaultbulletfactory import DefaultBulletFactory

from utility.effects.explosion import Explosion
from utility.effects.debris import Debris
from utility.constants.alien_constants import AlienConstants
from utility.constants.game_constants import GameConstants
from utility.constants.shooter_constants import ShooterConstants
from utility.constants.pickup_constants import PickUpConstants
from utility.data.image_loader import ImageLoader
from utility.data.soundloader import SoundLoader
from utility.data.soundplayer import SoundPlayer

from pygame import Vector2


class Alien(Entity, Shooter):

    __original_alien = ImageLoader().load(AlienConstants().image_path,
                                          (4*AlienConstants().size, 3*AlienConstants().size))
    __explosion_sound = SoundLoader().load(
        AlienConstants().explosion_sound_path, 0.3)

    def __init__(self, body: Body, direction: int) -> None:
        Entity.__init__(self, body, AlienConstants().tag)
        Shooter.__init__(self, InfinityWeapon(self, AlienConstants().shoot_cooldown, DefaultBulletFactory()),
                         Vector2(1, 1).normalize(), Vector2(0, 0))
        self.__move_cooldown = 0
        self.__direction = direction

        self.set_image(self.__original_alien)
        self.set_rect(self.get_image().get_rect())

    def get_move_cooldown(self) -> float:
        return self.__move_cooldown

    def set_move_cooldown(self, new_value: float) -> None:
        self.__move_cooldown = new_value

    def get_direction(self) -> int:
        return self.__direction

    def set_direction(self, direction: int) -> None:
        self.__direction = direction

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == PickUpConstants().tag:
            return
        
        # GFX
        explosion = Explosion(self.get_body().get_position(), 25)
        GFXManager.instance().add(explosion)
        debris = self.gerenare_debris(5)
        for d in debris:
            GFXManager.instance().add(d)

        # Manager
        EntitiesManager.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        velocity = body.get_velocity()
        position = body.get_position()

        # Trecho que cuida da mudança de direção do Alien
        # Espera um tempo e só depois muda randomicamente,
        # podendo assim permanecer na mesma direção
        self.set_move_cooldown(self.get_move_cooldown() - dt)
        if self.get_move_cooldown() < 0:
            self.set_move_cooldown(AlienConstants().move_cooldown)
            body.set_velocity(AlienConstants().directions[random.randint(
                0, len(AlienConstants().directions) - 1)] * AlienConstants().velocity_mag)
            body.set_velocity(Vector2(body.get_velocity().x *
                              self.get_direction(), body.get_velocity().y))

        # Verifica se o Alien chegou ao fim da tela
        #  e, se chegou, morre
        if position.x < 0:
            EntitiesManager.instance().register_deletion(self)
        elif GameConstants().screen_size.x < position.x:
            EntitiesManager.instance().register_deletion(self)

        if position.y < 0:
            position.y = GameConstants().screen_size.y
        elif GameConstants().screen_size.y < position.y:
            position.y = 0

        # Movimenta
        body.move(velocity*dt)

    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        # Determina a direção da mira randomicamente
        aiming_direction = Vector2(
            self.get_direction(), 0).rotate(random.uniform(0, 360))
        # Evita que a bala nasça dentro do Alien
        barrel_position = Vector2(aiming_direction*self.get_body().get_radius(
        ) * ShooterConstants().radius_multiplier + self.get_body().get_position())

        self.set_barrel_position(barrel_position)
        self.set_aiming_direction(aiming_direction)

        # Atualiza o comportamento de tiro e de movimentação
        self.shoot(dt)
        self.move(dt)

    def destroy(self) -> None:
        SoundPlayer().play(Alien.__explosion_sound)

    def gerenare_debris(self, amount: int) -> list:
        debris = list()
        pos = self.get_body().get_position()
        for _ in range(1, amount):
            debris.append(Debris(pos))
        
        return debris
