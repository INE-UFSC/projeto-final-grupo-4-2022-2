
from model.collision import Collision


class CollisionDetectorManager:

    # NOTE: Deve haver algum jeito mais otimizado
    def detect_collisions(self, entities: list) -> list:
        collisions = list()
        entities_len = len(entities)

        for index, target in enumerate(entities):
            target_id = target.get_id()
            target_body = target.get_body()
            target_tag = target.get_tag()
            target_position = target_body.get_position()
            target_radius = target_body.get_radius()

            for entity_index in range(index + 1, entities_len):
                entity = entities[entity_index]

                entity_id = entity.get_id()
                entity_body = entity.get_body()
                entity_tag = entity.get_tag()
                entity_position = entity_body.get_position()
                entity_radius = entity_body.get_radius()

                # If´s para diminur processamento
                if target_id == entity_id:
                    continue
                if target_tag == entity_tag:
                    continue

                # If para identificar a colisão
                if target_radius + entity_radius < target_position.distance_to(entity_position):
                    continue

                # Registrando a colisão
                collisions.append(Collision(target, entity))

        return collisions

    # NOTE: Deixei este código aqui para caso algum bug louco de colisão apareça, daí não precisa re-escrever
    def detect_collisions_old(self, entities: list) -> list:
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

                # Verificando se a colisão já não existe
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
