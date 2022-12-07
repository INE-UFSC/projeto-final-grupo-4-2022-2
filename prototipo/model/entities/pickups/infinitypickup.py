

from managers.entitiesmanager import EntitiesManager

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickups.pickup import PickUp
from model.entities.player import Player
from model.weapon.infinity import InfinityWeapon

from utility.constants.weapon_constants import WeaponConstants
from utility.data.image_loader import ImageLoader
from utility.constants.pickup_constants import PickUpConstants


class InfinityPickUp(PickUp):

    __original_image = ImageLoader().load(PickUpConstants().path_infinito,
                                          (0.5*PickUpConstants().size, 0.5*PickUpConstants().size))

    def __init__(self, body: Body) -> None:
        super().__init__(body)

        self.set_image(InfinityPickUp.__original_image)
        self.set_rect(self.get_image().get_rect())

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.set_weapon(InfinityWeapon(entity, WeaponConstants(
            ).cooldown, entity.get_weapon().get_bullet_factory()))
            EntitiesManager.instance().register_deletion(self)
