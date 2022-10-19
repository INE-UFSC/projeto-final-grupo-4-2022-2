
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
        first_tag = collision.get_first().get_tag()
        second_tag = collision.get_second().get_tag()
        if first_tag == second_tag:
            return
        for c in self.__collisions:
            if c == collision:
                return
        # print(f"appended {collision}")
        self.__collisions.append(collision)
        # print('Registrando colisão: ', collision)

    def handle_collisions(self):
        for collision in self.__collisions:
            entity_1 = collision.get_first()
            entity_2 = collision.get_second()

            entity_1.on_collision(entity_2)
            entity_2.on_collision(entity_1)
            # print('Handelando colisão: ', collision)

        self.__collisions.clear()
