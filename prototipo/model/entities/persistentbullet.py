
from model.entities.abstractentity import AbstractEntity
from model.entities.bullet import Bullet
from model.body import Body

class PersistentBullet(Bullet):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, lifetime)

    def on_collision(self, entity: AbstractEntity) -> None:
        pass

    def move(self, dt: float) -> None:
        pass

    def update(self, dt: float) -> None:
        pass
