from utility.constants.game_constants import GameConstants


class ParticleDestroyer:

    def destroy(self, particles: list) -> None:
        aux = []
        for p in particles:
            if p.get_position().x > GameConstants().screen_size.x:
                aux.append(p)
        for p in aux:
            particles.remove(p)

        return particles[:]
