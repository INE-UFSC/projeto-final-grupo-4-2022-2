

from controller.entitiescontroller import EntitiesController

from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickup import PickUp
from model.entities.player import Player
from model.weapon.bulletless import BulletlessWeapon

from utility.constants.weapon_constants import WeaponConstants


class BulletlessPickUp(PickUp):

    def __init__(self, body: Body) -> None:
        super().__init__(body)

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.set_weapon(BulletlessWeapon(entity))
            EntitiesController.instance().register_deletion(self)
