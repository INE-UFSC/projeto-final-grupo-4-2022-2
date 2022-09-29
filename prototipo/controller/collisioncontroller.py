

class CollisionController:

    def __init__(self, entities):
        self.__entities = entities

    def handle_collision(self) -> None:
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
                target.on_collision(e)
