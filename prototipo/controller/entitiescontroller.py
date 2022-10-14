from model.entities.abstractentity import Entity

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

    def add_entity(self, new_entity: Entity) -> None:
        self.__entities.append(new_entity)

    def add_entities(self, new_entity: Entity) -> None:
        self.__entities.extend(new_entity)

    def register_deletion(self, entity: Entity) -> None:
        self.__deletion_buffer.add(entity)

    def flush_deletion_buffer(self) -> None:
        self.__deletion_buffer.clear()
    
    def handle_deletion(self) -> None:
        for bd in self.__deletion_buffer:
            self.del_entity(bd)

    def del_entity(self, entity: Entity) -> None:
        try:
            self.__entities.remove(entity)
        except ValueError as ve:
            print(ve)
