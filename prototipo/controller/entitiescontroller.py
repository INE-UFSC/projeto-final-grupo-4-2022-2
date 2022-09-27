

class EntitiesController:

    _instance = None

    def __init__(self):
        self.__entities = []
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_entities(self):
        return self.__entities

    def add_entity(self, new_entity):
        self.__entities.append(new_entity)

    def add_entities(self, new_entities):
        self.__entities.extend(new_entities)

    def del_entity(self, entity):
        self.__entities.remove(entity)
