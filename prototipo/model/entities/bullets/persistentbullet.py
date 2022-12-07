
from managers.entitiesmanager import EntitiesManager

from model.entities.abstractentity import Entity
from model.entities.bullets.bullet import Bullet
from model.body import Body

from utility.constants.game_constants import GameConstants
from utility.constants.pickup_constants import PickUpConstants

# Bala com o comportamento de persistencia
# Apena desaparece depois que atinge um objeto,
# exclusos outras balas


class PersistentBullet(Bullet):

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
        self.move(dt)
