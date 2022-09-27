
from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner):
        self.__owner = new_owner

    @abstractmethod
    def entry(self): ...

    @abstractmethod
    def exit(self): ...

    @abstractmethod
    def handle_event(self): ...

    @abstractmethod
    def handle_update(self, dt): ...

    @abstractmethod
    def handle_rendering(self): ...
