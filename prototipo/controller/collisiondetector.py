

from controller.collisionmanager import CollisionManager

from model.entities.abstractentity import Entity
from model.collision import Collision


class CollisionDetector:

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def detect_collisions(self, entities: list) -> None:
        cont = 0
        for target in entities:
            t_tag = target.get_tag()
            t_id = target.get_id()
            t_body = target.get_body()
            t_position = t_body.get_position()
            t_radius = t_body.get_radius()

            for entity in entities:
                e_id = entity.get_id()
                e_tag = entity.get_tag()
                e_body = entity.get_body()
                e_position = e_body.get_position()
                e_radius = e_body.get_radius()

                if t_id == e_id:
                    continue
                if t_radius + e_radius < t_position.distance_to(e_position):
                    continue
                if t_tag == e_tag:
                    continue

                collided = Collision(target, entity)
                CollisionManager.instance().register_collision(collided)
                cont += 1
                print('Contador: ', cont)
