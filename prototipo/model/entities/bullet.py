
from model.entities.abstractentity import Entity
from controller.entitiescontroller import EntitiesController
from model.body import Body
import utility.constants as CONST


class Bullet(Entity):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, CONST.BULLET_TAG)
        self.__lifetime = lifetime

    def get_lifetime(self) -> int:
        return self.__lifetime

    def set_lifetime(self, new_lifetime: int) -> int:
        self.__lifetime = new_lifetime
    
    def bullet_tag_check(self, tag: str) -> bool:
        return tag == CONST.BULLET_TAG or tag == CONST.PLAYER_TAG

    def destroy(self) -> None:
        EntitiesController.instance().register_deletion(self)
    
