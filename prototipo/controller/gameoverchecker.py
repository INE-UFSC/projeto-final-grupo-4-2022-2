

# O gerenciador de level determinará quando o jogo acaba.
class GameOverChecker:

    def check(self, player):
        # Se o player morreu, então o jogo acaba
        if player is not None and not player.alive():
            return True
        return False


