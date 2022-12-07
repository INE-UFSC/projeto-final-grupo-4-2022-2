
from managers.entitiesmanager import EntitiesManager

from model.entities.abstractentity import Entity
from model.entities.bullets.bullet import Bullet
from model.body import Body

from utility.constants.game_constants import GameConstants

from utility.constants.pickup_constants import PickUpConstants

# Bala com comportamento normal:
# vai sempre para a frente e
# desaparece depois de um certo tempo


class DefaultBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: Entity) -> None:
        if entity.get_tag() == PickUpConstants().tag:
            return
        EntitiesManager.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        position = body.get_position()

        # Condições para manter a bala sempre dentro da janela
        if position.x < 0:
            position.x = GameConstants().screen_size.x
        elif GameConstants().screen_size.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = GameConstants().screen_size.y
        elif GameConstants().screen_size.y < position.y:
            position.y = 0

        # Atualiza a posição
        body.move(body.get_velocity() * dt)

    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        # Decrementa o tempo de vida da bala.
        # Caso não tenha mais, a bala desaparece
        self.set_lifetime(self.get_lifetime() - dt)
        if self.get_lifetime() < 0:
            EntitiesManager.instance().register_deletion(self)

        self.move(dt)
