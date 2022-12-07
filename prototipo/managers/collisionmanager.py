

# Singleton que tratará as colisões
class CollisionManager:

    def handle_collisions(self, collisions: list) -> None:
        # Tratando as colisões
        # Cada entidade irá reagir de uma forma à colisão
        for collision in collisions:
            entity_1 = collision.get_first()
            entity_2 = collision.get_second()

            entity_1.on_collision(entity_2)
            entity_2.on_collision(entity_1)
