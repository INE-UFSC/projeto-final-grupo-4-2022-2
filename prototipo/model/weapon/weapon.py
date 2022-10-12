from abc import ABC, abstractmethod

class Weapon(ABC):

    def __init__(self, cooldown: float, ammunition: int) -> None:
        self.__cooldown = cooldown
        self.__ammunition = ammunition

    @abstractmethod
    def shoot(self) -> None:
        pass
    
    