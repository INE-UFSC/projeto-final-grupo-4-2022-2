
from model.entities.abstractentity import Entity
from controller.entitiescontroller import EntitiesController
from model.body import Body


class Bullet(Entity):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, "bullet")
        self.__lifetime = lifetime

    def get_lifetime(self) -> int:
        return self.__lifetime

    def set_lifetime(self, new_lifetime: int) -> int:
        self.__lifetime = new_lifetime

    def destroy(self) -> None:
        #EntitiesController.instance().del_entity(self)
        EntitiesController.instance().register_deletion(self)
    
