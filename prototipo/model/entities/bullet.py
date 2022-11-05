
from model.entities.abstractentity import Entity
from model.body import Body
import utility.constants as CONSTANT


# Bala abstrata
class Bullet(Entity):

    def __init__(self, body: Body, lifetime: int) -> None:
        super().__init__(body, CONSTANT.BULLET_TAG)
        self.__lifetime = lifetime

    def get_lifetime(self) -> int:
        return self.__lifetime

    def set_lifetime(self, new_lifetime: int) -> int:
        self.__lifetime = new_lifetime

    def destroy(self) -> None:
        pass
    
