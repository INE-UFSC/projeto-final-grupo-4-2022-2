
from model.entities.abstractentity import Entity


class Collision:
    ...


# Uma classe que guarda a lógica de uma colisão
# quando elas são iguais e quem colidiu com quem
class Collision:

    def __init__(self, first: Entity, second: Entity) -> None:
        self.__first = first
        self.__second = second

    def get_first(self) -> Entity:
        return self.__first

    def get_second(self) -> Entity:
        return self.__second

    def __eq__(self, other: Collision) -> bool:
        if ((other.get_first().get_id() == self.get_first().get_id() and other.get_second().get_id() == self.get_second().get_id()) or
                (other.get_second().get_id() == self.get_first().get_id() and other.get_first().get_id() == self.get_second().get_id())):
            return True
        return False

    def __str__(self) -> str:
        return f"(f:{self.get_first().get_tag()} {self.get_first().get_id()}, s:{self.get_second().get_tag()} {self.get_second().get_id()})"
