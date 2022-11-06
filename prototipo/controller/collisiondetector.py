
from model.collision import Collision

# Singleton, identifica as colisões e registra no
# gerenciador de colisões onde serão tratadas
class CollisionDetector:

    def detect_collisions(self, entities: list) -> None:
        collisions = list()
        for target in entities:
            t_id = target.get_id()
            t_body = target.get_body()
            t_position = t_body.get_position()
            t_radius = t_body.get_radius()
            t_tag = target.get_tag()

            for entity in entities:
                e_id = entity.get_id()
                e_body = entity.get_body()
                e_position = e_body.get_position()
                e_radius = e_body.get_radius()
                e_tag = entity.get_tag()

                # If´s para diminur processamento
                if t_id == e_id:
                    continue
                if t_tag == e_tag:
                    continue

                # If para identificar a colisão
                if t_radius + e_radius < t_position.distance_to(e_position):
                    continue

                # Verificnado se a colisão já não existe
                collision = Collision(target, entity)
                eq = False
                for c in collisions:
                    if c == collision:
                        eq = True
                        break
                if eq:
                    continue

                # Registrando a colisão
                collisions.append(collision)
            
        return collisions[:]
