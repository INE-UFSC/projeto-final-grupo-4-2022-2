

from controller.entitiescontroller import EntitiesController
from model.body import Body
from model.entities.abstractentity import Entity
from model.entities.pickup import PickUp
from model.entities.player import Player
from utility.constants.weapon_constants import WeaponConstants


class AmmoPickUp(PickUp):

    def __init__(self, body: Body):
        super().__init__(body)

    def on_collision(self, entity: Entity):
        if isinstance(entity, Player):
            entity.get_weapon().set_ammunition(WeaponConstants().max_ammunition)
        EntitiesController.instance().register_deletion(self)
