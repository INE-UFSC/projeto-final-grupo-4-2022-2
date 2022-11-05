from model.entities.abstractentity import Entity
from utility.constants import VELOCITY_MULTIPLIER, TIME_TO_SCORE


# Singleton que controla a criação e a destruição das entidades 
class EntitiesController:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__entities = []
        self.__deletion_buffer = set()

    def get_entities(self) -> list:
        return self.__entities

    def get_deletion_buffer(self):
        return list(self.__deletion_buffer)

    def add_entity(self, new_entity: Entity) -> None:
        self.__entities.append(new_entity)

    def add_entities(self, new_entity: Entity) -> None:
        self.__entities.extend(new_entity)

    def register_deletion(self, entity: Entity) -> None:
        self.__deletion_buffer.add(entity)

    def flush_deletion_buffer(self) -> None:
        self.__deletion_buffer.clear()

    def handle_deletion(self) -> None:
        for entity in self.__deletion_buffer:
            entity.destroy()
            self.del_entity(entity)
        self.flush_deletion_buffer()

    def del_entity(self, entity: Entity) -> None:
        try:
            self.__entities.remove(entity)
        except ValueError as ve:
            print(ve)

    def clear_entities(self):
        self.__entities.clear()
