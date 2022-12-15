

from managers.entitiesmanager import EntitiesManager

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickups.pickup import PickUp
from model.entities.player import Player
from model.weapon.shotgun import Shotgun

from utility.constants.weapon_constants import WeaponConstants
from utility.data.image_loader import ImageLoader
from utility.constants.pickup_constants import PickUpConstants


class ShotGunPickUp(PickUp):

    __original_image = ImageLoader().load(PickUpConstants().path_shotgun,
                                          (1.5*PickUpConstants().size, 1.5*PickUpConstants().size))

    def __init__(self, body: Body) -> None:
        super().__init__(body)

        self.set_image(ShotGunPickUp.__original_image)
        self.set_rect(self.get_image().get_rect())

        self.set_rect(self.get_image().get_rect())
        self.get_rect().center = self.get_body().get_position()

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.set_weapon(Shotgun(entity, WeaponConstants().cooldown, WeaponConstants(
            ).max_ammunition, entity.get_weapon().get_bullet_factory()))
            EntitiesManager.instance().register_deletion(self)
