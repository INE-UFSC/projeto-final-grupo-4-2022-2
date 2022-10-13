from model.entities.abstractentity import AbstractEntity

class EntitiesController:

    _instance = None

    def __init__(self):
        self.__entities = []
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_entities(self) -> list[AbstractEntity]:
        return self.__entities

    def add_entity(self, new_entity: AbstractEntity) -> None:
        self.__entities.append(new_entity)

    def add_entities(self, new_entity: AbstractEntity) -> None:
        self.__entities.extend(new_entity)

    def del_entity(self, entity: AbstractEntity) -> None:
        try:
            self.__entities.remove(entity)
        except ValueError as ve:
            print(ve)
