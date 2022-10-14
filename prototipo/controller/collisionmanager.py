
from model.collision import Collision

class CollisionManager:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.__collisions = list()

    def register_collision(self, collision: Collision):
        for c in self.__collisions:
            e1_c = c.get_first().get_id()
            e2_c = c.get_second().get_id()
            e1_co = collision.get_first().get_id()
            e2_co = collision.get_second().get_id()
            if ((e1_c == e1_co) and (e2_c == e2_co)) or ((e1_c == e2_co) and (e2_c == e1_co)):
                return
        self.__collisions.append(collision)

    def handle_collisions(self):
        for collision in self.__collisions:
            entity_1 = collision.get_first()
            entity_2 = collision.get_second()

            entity_1.on_collision(entity_2)
            entity_2.on_collision(entity_1)

        self.__collisions.clear()