
from abc import ABC, abstractmethod

class Game: ...

class State(ABC):

    def __init__(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def set_owner(self, new_owner: Game) -> None:
        self.__owner = new_owner

    @abstractmethod
    def entry(self) -> None: ...

    @abstractmethod
    def exit(self) -> None: ...

    @abstractmethod
    def handle_event(self) -> None: ...

    @abstractmethod
    def handle_update(self, dt: float) -> None: ...

    @abstractmethod
    def handle_rendering(self) -> None: ...

    @abstractmethod
    def handle_transition(self) -> None: ...
