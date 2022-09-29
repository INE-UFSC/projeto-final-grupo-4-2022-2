from abc import ABC, abstractmethod
from model.body import Body

class AbstractEntity(ABC):

    next_id = 0

    def __init__(self, body: Body):
        self.__id = AbstractEntity.next_id
        self.__body = body
        AbstractEntity.next_id += 1

    def get_id(self) -> int:
        return self.__id

    def get_body(self) -> Body:
        return self.__body

    def set_body(self, new_body: Body) -> None:
        self.__body = new_body

    @abstractmethod
    # Colocar os types em constantes.py?
    def get_type(self) -> str: ...

    @abstractmethod
    def on_collision(self, entity) -> None: ...

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def destroy(self) -> None: ...
