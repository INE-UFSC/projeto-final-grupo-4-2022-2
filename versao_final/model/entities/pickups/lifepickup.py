

from managers.entitiesmanager import EntitiesManager

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickups.pickup import PickUp
from model.entities.player import Player

from utility.constants.player_constants import PlayerConstants
from utility.data.image_loader import ImageLoader
from utility.constants.pickup_constants import PickUpConstants


class LifePickUp(PickUp):

    __original_image = ImageLoader().load(PickUpConstants().path_cura,
                                          (PickUpConstants().size, PickUpConstants().size))

    def __init__(self, body: Body) -> None:
        super().__init__(body)

        self.set_image(LifePickUp.__original_image)
        self.set_rect(self.get_image().get_rect())

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.set_lives(entity.get_lives() + 1)
            EntitiesManager.instance().register_deletion(self)
