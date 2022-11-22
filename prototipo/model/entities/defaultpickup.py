

from controller.entitiescontroller import EntitiesController

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickup import PickUp
from model.entities.player import Player
from model.weapon.default import DefaultWeapon

from utility.constants.weapon_constants import WeaponConstants


class DefaultPickUp(PickUp):

    def __init__(self, body: Body) -> None:
        super().__init__(body)

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.set_weapon(DefaultWeapon(entity, WeaponConstants().cooldown, WeaponConstants().max_ammunition, entity.get_weapon().get_bullet_factory()))
            EntitiesController.instance().register_deletion(self)
