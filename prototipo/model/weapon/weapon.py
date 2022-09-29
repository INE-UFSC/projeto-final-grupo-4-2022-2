from abc import ABC, abstractmethod

class Weapon(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def shoot(self):
        pass
    
    