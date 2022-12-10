
from model.entities.abstractentity import Entity
from model.entities.bullets.bullet import Bullet
from model.body import Body
from managers.entitiesmanager import EntitiesManager

from utility.constants.game_constants import GameConstants


# Bala que apenas é destruida após
# não ter mais tempo de vida


class PiercingBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: Entity) -> None:
        pass

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
        self.set_lifetime(self.get_lifetime() - dt)
        if self.get_lifetime() < 0:
            EntitiesManager.instance().register_deletion(self)
        self.move(dt)
