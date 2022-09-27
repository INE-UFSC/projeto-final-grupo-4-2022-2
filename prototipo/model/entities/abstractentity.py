
from abc import ABC, abstractmethod


class AbstractEntity(ABC):

    next_id = 0

    def __init__(self, body) -> None:
        self.__id = AbstractEntity.next_id
        self.__body = body
        AbstractEntity.next_id += 1

    def get_id(self):
        return self.__id

    def get_body(self):
        return self.__body

    def set_body(self, new_body):
        self.__body = new_body

    @abstractmethod
    def get_type(self): ...

    @abstractmethod
    def on_collision(self, entity): ...

    @abstractmethod
    def update(self, dt, screen_size): ...

    @abstractmethod
    def destroy(self): ...
