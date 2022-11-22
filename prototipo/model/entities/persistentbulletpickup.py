

from controller.entitiescontroller import EntitiesController

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickup import PickUp
from model.entities.player import Player
from model.factory.persistentbulletfactory import PersistentBulletFactory


class PersistentBulletPickUp(PickUp):

    def __init__(self, body: Body) -> None:
        super().__init__(body)

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.get_weapon().set_bullet_factory(PersistentBulletFactory())
            EntitiesController.instance().register_deletion(self)
