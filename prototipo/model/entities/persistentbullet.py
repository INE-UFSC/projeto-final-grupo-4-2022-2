
from model.entities.abstractentity import Entity
from model.entities.bullet import Bullet
from model.body import Body
from controller.entitiescontroller import EntitiesController
import utility.constants as CONSTANT


# Bala com o comportamento de persistencia
# Apena desaparece depois que atinge um objeto,
# exclusos outras balas
class PersistentBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: Entity) -> None:
        EntitiesController.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()
        position = body.get_position()

        # Condições para manter a bala sempre dentro da janela
        if position.x < 0:
            position.x = CONSTANT.SCREEN_SIZE.x
        elif CONSTANT.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONSTANT.SCREEN_SIZE.y
        elif CONSTANT.SCREEN_SIZE.y < position.y:
            position.y = 0

        # Atualiza a posição
        body.move(body.get_velocity() * dt)

    def update(self, dt: float) -> None:
        Entity.update(self, dt)
        self.move(dt)
