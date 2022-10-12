from model.entities.bullet import Bullet
from model.entities.abstractentity import AbstractEntity

class PersistentBullet(Bullet):

    def on_collision(self, entity: AbstractEntity) -> None:
        pass

    def move(self, dt: float) -> None:
        pass

    def update(self, dt: float) -> None:
        pass
