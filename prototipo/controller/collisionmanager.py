
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
            if c == collision:
                return
        # print(f"appended {collision}")
        self.__collisions.append(collision)

    def handle_collisions(self):
        for collision in self.__collisions:
            entity_1 = collision.get_first()
            entity_2 = collision.get_second()

            entity_1.on_collision(entity_2)
            entity_2.on_collision(entity_1)

        self.__collisions.clear()