
from abc import ABC, abstractmethod

class Game: ...

# Classe asbtrata do State
class State(ABC):

    def __init__(self, owner: Game):
        self.__owner = owner

    def get_owner(self) -> Game:
        return self.__owner

    def set_owner(self, new_owner: Game) -> None:
        self.__owner = new_owner

    # Método chamado quando um estado inicia
    @abstractmethod
    def entry(self) -> None: ...

    # Método chamado quando um estado termina
    @abstractmethod
    def exit(self) -> None: ...

    # Método que vai lidar com os métodos do pygame
    @abstractmethod
    def handle_event(self) -> None: ...

    # Método onde é atualizado os componentes do estado
    @abstractmethod
    def handle_update(self, dt: float) -> None: ...

    # Método que renderiza os componentes
    @abstractmethod
    def handle_rendering(self) -> None: ...

    # Método que lidará com a transição de estados
    @abstractmethod
    def handle_transition(self) -> None: ...
