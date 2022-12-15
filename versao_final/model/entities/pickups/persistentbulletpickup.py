

from managers.entitiesmanager import EntitiesManager

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickups.pickup import PickUp
from model.entities.player import Player
from model.factory.persistentbulletfactory import PersistentBulletFactory

from utility.data.image_loader import ImageLoader
from utility.constants.pickup_constants import PickUpConstants


class PersistentBulletPickUp(PickUp):

    __original_image = ImageLoader().load(PickUpConstants().path_persistentbullet,
                                          (0.75*PickUpConstants().size, 0.75*PickUpConstants().size))

    def __init__(self, body: Body) -> None:
        super().__init__(body)

        self.set_image(PersistentBulletPickUp.__original_image)
        self.set_rect(self.get_image().get_rect())

        self.set_rect(self.get_image().get_rect())
        self.get_rect().center = self.get_body().get_position()

    def on_collision(self, entity: Entity):
        if entity.get_tag() == PickUpConstants():
            return
        if isinstance(entity, Player):
            entity.get_weapon().set_bullet_factory(PersistentBulletFactory())
            EntitiesManager.instance().register_deletion(self)
