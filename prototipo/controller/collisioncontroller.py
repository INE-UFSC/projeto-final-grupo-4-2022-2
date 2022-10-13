

from model.entities.abstractentity import Entity


class CollisionController:

    def __init__(self, entities: list[Entity]):
        self.__entities = entities
        self.__collision_buffer = set() # poderia ser uma lista
    
    def register_collision(self, entity: Entity) -> None:
        self.__collision_buffer.add(entity) # no caso se fosse uma lista haveria uma logica para evitar registros duplicados
    
    def flush_collision_register(self) -> None:
        self.__collision_buffer.clear()
        
    def handle_collision(self) -> None:
        for bc in self.__collision_buffer:
            bc.on_collision()

    def detect_collisions(self) -> None:
        for target in self.__entities:
            t_id = target.get_id()
            t_body = target.get_body()
            t_position = t_body.get_position()
            t_radius = t_body.get_radius()

            for e in self.__entities:
                e_id = e.get_id()
                e_body = e.get_body()
                e_position = e_body.get_position()
                e_radius = e_body.get_radius()

                if t_id == e_id:
                    continue
                if t_radius + e_radius < t_position.distance_to(e_position):
                    continue
                if target.get_tag() == e.get_tag():
                    continue
                if target.get_tag() == "bullet" and e.get_tag() == "player":
                    continue
                if target.get_tag() == "player" and e.get_tag() == "bullet":
                    continue

                self.register_collision(target)
                self.register_collision(e)
