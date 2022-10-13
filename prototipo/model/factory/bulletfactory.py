

from abc import abstractmethod

from abc import ABC, abstractclassmethod

class BulletFactory(ABC):

  @abstractmethod
  def create(self): ...
