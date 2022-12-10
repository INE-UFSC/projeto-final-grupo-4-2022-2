

from managers.entitiesmanager import EntitiesManager

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickups.pickup import PickUp
from model.entities.player import Player
from model.factory.piercingbulletfactory import PiercingBulletFactory

from utility.data.image_loader import ImageLoader
from utility.constants.pickup_constants import PickUpConstants


class PiercingBulletPickUp(PickUp):

    __original_image = ImageLoader().load(PickUpConstants().path_piercingbullet,
                                          (0.75*PickUpConstants().size, 0.75*PickUpConstants().size))

    def __init__(self, body: Body) -> None:
        super().__init__(body)

        self.set_image(PiercingBulletPickUp.__original_image)
        self.set_rect(self.get_image().get_rect())

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.get_weapon().set_bullet_factory(PiercingBulletFactory())
            EntitiesManager.instance().register_deletion(self)
