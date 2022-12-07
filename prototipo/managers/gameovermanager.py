from model.entities.player import Player

# O gerenciador de level determinará quando o jogo acaba.


class GameOverManager:

    def check(self, player: Player) -> bool:
        # Se o player morreu, então o jogo acaba
        if player is not None and not player.alive():
            return True
        return False
