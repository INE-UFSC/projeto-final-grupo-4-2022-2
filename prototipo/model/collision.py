
from model.entities.abstractentity import Entity


class Collision:

    def __init__(self, first: Entity, second: Entity):
        self.__first = first
        self.__second = second

    def get_first(self) -> Entity:
        return self.__first

    def get_second(self) -> Entity:
        return self.__second

    def __eq__(self, other: Entity) -> bool:
        if ((other.get_first() == self.get_first() and other.get_second() == self.get_second()) or 
            (other.get_second() == self.get_first() and other.get_first() == self.get_second())):
            return True
        return False

