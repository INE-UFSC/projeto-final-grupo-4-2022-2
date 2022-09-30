from model.entities.bullet import Bullet
from model.entities.abstractentity import AbstractEntity

class PiercingBullet(Bullet):

    def on_collision(self, entity: AbstractEntity) -> None:
        pass
