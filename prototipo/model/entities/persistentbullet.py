
from model.entities.abstractentity import Entity
from model.entities.bullet import Bullet
from model.body import Body
from controller.entitiescontroller import EntitiesController
import utility.constants as CONSTANTE

class PersistentBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: Entity) -> None:
        EntitiesController.instance().register_deletion(self)

    def move(self, dt: float) -> None:
        body = self.get_body()

        position = body.get_position()
        if position.x < 0:
            position.x = CONSTANTE.SCREEN_SIZE.x
        elif CONSTANTE.SCREEN_SIZE.x < position.x:
            position.x = 0

        if position.y < 0:
            position.y = CONSTANTE.SCREEN_SIZE.y
        elif CONSTANTE.SCREEN_SIZE.y < position.y:
            position.y = 0

        body.move(body.get_velocity()*dt*10)

    def update(self, dt: float) -> None:
        self.move(dt)
