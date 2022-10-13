from abc import ABC, abstractmethod
from model.body import Body

class Entity(ABC):

    next_id = 0

    def __init__(self, body: Body, tag: str):
        self.__id = Entity.next_id
        self.__body = body
        self.__tag = tag
        Entity.next_id += 1

    def get_id(self) -> int:
        return self.__id

    def get_body(self) -> Body:
        return self.__body

    def set_body(self, new_body: Body) -> None:
        self.__body = new_body

    def get_tag(self) -> str:
        return self.__tag

    @abstractmethod
    def on_collision(self) -> None: ...

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def destroy(self) -> None: ...
