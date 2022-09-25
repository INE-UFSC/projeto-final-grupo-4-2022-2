
from typing import List
from models.entity import Entity


class CollisionHandler:

    def __init__(self, entities: List[Entity]):
        self.__entities = entities

    def handle_collision(self):
        for target in self.__entities:
            t_position = target.get_position()
            t_radius = target.get_radius()
            t_type = target.get_type()

            for e in self.__entities:
                e_position = e.get_position()
                e_radius = e.get_radius()
                e_type = e.get_type()

                if t_type == e_type:
                    continue
                if t_radius + e_radius < t_position.distance_to(e_position):
                    continue

                if t_type == "player" and e_type == "asteroid":
                    target.on_colision()
                    e.on_colision()
                    self.__entities.remove(e)
